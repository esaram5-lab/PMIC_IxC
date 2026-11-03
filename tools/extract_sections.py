#!/usr/bin/env python3
"""Convert the prose chapters of a JEDEC PMIC spec into one Markdown file per section.

Usage:
    pdftotext -layout spec.pdf spec.txt
    python3 tools/extract_sections.py spec.txt converted/PMIC5030

Section numbers/titles come from the document's own table of contents. Large sections are split
one level deeper (see MAX_CHARS). Prose paragraphs are re-flowed; tables, figure text and other
column-aligned content are kept verbatim in ```text blocks. Register tables ("Table N — Register
0xXX") and register-map summary tables are replaced by links to the per-register files.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_registers import clean_lines  # noqa: E402  (same page/watermark cleaning)

MAX_CHARS = 20000
TOC_RE = re.compile(r"^\s*(\d+(?:\.\d+)*)\.?\s+(\S.*?)\s*\.{4,}\s*(\d+)\s*$")
CAPTION_RE = re.compile(r"^\s*(Table|Figure) (\d+) — (.+?)\s*$")
CONT_RE = re.compile(r"\(cont[’']d\)\s*$")


def parse_toc(raw):
    """Section entries in document order, keeping only a consistent numbering hierarchy."""
    entries, seen = [], set()
    chapter = 0
    for line in raw.split("\n")[:3000]:
        m = TOC_RE.match(line)
        if not m:
            continue
        num, title, page = m.group(1), m.group(2), int(m.group(3))
        parts = num.split(".")
        if title.startswith(("Table ", "Figure ")) or num in seen:
            continue
        if len(parts) == 1:
            if int(parts[0]) != chapter + 1:
                continue  # e.g. "1 Byte Address Mode" sub-items
            chapter = int(parts[0])
        elif int(parts[0]) != chapter:
            continue
        seen.add(num)
        entries.append({"num": num, "title": title, "page": page, "level": len(parts)})
    return entries


def locate_headings(lines, toc):
    """Find each TOC heading in the body (after the TOC), in order."""
    found, pos = [], 0
    # skip front matter: start searching after the last TOC-looking line
    for i, ln in enumerate(lines):
        if isinstance(ln, str) and TOC_RE.match(ln):
            pos = i + 1
    annex = {}
    for e in toc:
        words = re.escape(e["title"][:18]).replace(r"\ ", r"\s+")
        num = re.escape(e["num"])
        # annex chapters are numbered in the TOC (4, 4.1) but printed as "Annex A", "A.1" in the body
        if e["level"] == 1 and e["title"].startswith("Annex "):
            annex[e["num"]] = e["title"].split()[1]
        alt = None
        top = e["num"].split(".")[0]
        if top in annex:
            alt = annex[top] + e["num"][len(top):]
        pats = [rf"^\s{{0,6}}{num}\.?\s+{words}",                     # number + title
                rf"^\s{{0,6}}{words}" if e["level"] == 1 and top in annex else None,
                rf"^\s{{0,6}}{re.escape(alt)}\.?\s+[A-Z]" if alt and e["level"] > 1 else None,
                rf"^{num}\.?\s{{1,10}}[A-Z][A-Za-z]"]                      # number only (TOC title typo)
        for p in filter(None, pats):
            pat = re.compile(p)
            hit = next((i for i in range(pos, len(lines))
                        if isinstance(lines[i], str) and pat.match(lines[i]) and not CONT_RE.search(lines[i])
                        and not TOC_RE.match(lines[i])), None)
            if hit is not None:
                found.append(dict(e, line=hit))
                pos = hit + 1
                break
    return found


def is_pre(ln):
    """Column-aligned / indented content (tables, figure text) rather than running prose."""
    if not ln.strip():
        return False
    indent = len(ln) - len(ln.lstrip())
    return indent >= 4 or bool(re.search(r"\S\s{3,}\S", ln.strip()))


def render_body(lines, reg_links):
    """lines: cleaned strings (page markers removed). Returns Markdown."""
    out, para, pre = [], [], []

    def flush_para():
        if para:
            text = " ".join(x.strip() for x in para)
            text = re.sub(r"(\w)- (\w)", r"\1-\2", text)
            out.append(text)
            out.append("")
            para.clear()

    def flush_pre():
        while pre and not pre[-1].strip():
            pre.pop()
        if pre:
            ind = min(len(x) - len(x.lstrip()) for x in pre if x.strip())
            out.append("```text")
            out.extend(x[ind:].rstrip() for x in pre)
            out.append("```")
            out.append("")
            pre.clear()

    skip_table = False
    para_gap = [False]
    for ln in lines:
        s = ln.strip()
        if re.match(r"^\d+(\.\d+)*\s+\S.*\(cont[’']d\)\s*$", s):
            continue  # running section header on continuation pages
        cm = CAPTION_RE.match(ln)
        if cm:
            kind, num, title = cm.groups()
            if CONT_RE.search(title):
                continue  # repeated caption on the next page; content continues
            flush_para()
            flush_pre()
            rm = re.match(r"^Register (0x[0-9A-Fa-f]+)", title)
            if kind == "Table" and (rm or ("Register Map" in title and "Breakdown" not in title)):
                skip_table = True
                if rm:
                    addr = reg_links.get(int(num), rm.group(1))
                    out.append(f"**Table {num} — Register {addr}**: see [`registers/{addr}.md`](../registers/{addr}.md)")
                else:
                    out.append(f"**Table {num} — {title}**: see [`index.md`](../index.md)")
                out.append("")
                continue
            skip_table = False
            if kind == "Table":
                out.append(f"**Table {num} — {title}**")
            else:
                out.append(f"*Figure {num} — {title}* (figure; any text below/above was extracted from the drawing)")
            out.append("")
            continue
        if skip_table:
            # register tables run until the next caption or a prose line at column 0
            if s and not is_pre(ln) and not s.startswith("NOTE") and len(s) > 60:
                skip_table = False
            else:
                continue
        if not s:
            if para:
                para_gap[0] = True  # may be a page break inside the paragraph
            if pre:
                pre.append("")
            continue
        in_table = any(x.strip() for x in pre)
        if is_pre(ln) or s.startswith("NOTE") or (in_table and len(s) < 40 and not s.endswith(".")):
            flush_para()
            pre.append(ln)
            continue
        flush_pre()
        if para and para_gap[0] and not (s[0].islower() and not para[-1].rstrip().endswith((".", ":"))):
            flush_para()
        para_gap[0] = False
        if re.match(r"^([•▪●–-]|\d+\.|[a-z]\))\s", s):
            flush_para()
        para.append(ln)
    flush_para()
    flush_pre()
    text = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def slug(num, title):
    t = re.sub(r"[^A-Za-z0-9]+", "_", title).strip("_")[:50]
    return f"{num.replace('.', '_')}_{t}"


def main():
    txt, outdir = sys.argv[1:3]
    raw = open(txt, encoding="utf-8").read()
    meta = json.load(open(os.path.join(outdir, "meta.json"), encoding="utf-8"))
    regs = json.load(open(os.path.join(outdir, "registers.json"), encoding="utf-8"))["registers"]
    reg_links = {r["source_table"]: r["address"] for r in regs}
    doc = meta["document"]
    lines = clean_lines(raw)
    toc = parse_toc(raw)
    heads = locate_headings(lines, toc)
    missing = [e["num"] for e in toc if e["num"] not in {h["num"] for h in heads}]

    # build tree with each node's own text (up to the first child / next heading)
    for i, h in enumerate(heads):
        end = heads[i + 1]["line"] if i + 1 < len(heads) else len(lines)
        body = lines[h["line"] + 1:end]
        h["body"] = [x for x in body if isinstance(x, str)]
        pages = [x[1] for x in lines[h["line"]:end] if isinstance(x, tuple)]
        h["page_end"] = max(pages) if pages else h["page"]
        h["children"] = []
    roots, stack = [], []
    for h in heads:
        while stack and not h["num"].startswith(stack[-1]["num"] + "."):
            stack.pop()
        (stack[-1]["children"] if stack else roots).append(h)
        stack.append(h)

    def size(n):
        return sum(len(x) for x in n["body"]) + sum(size(c) for c in n["children"])

    def last_page(n):
        return max([n["page_end"]] + [last_page(c) for c in n["children"]])

    sdir = os.path.join(outdir, "sections")
    os.makedirs(sdir, exist_ok=True)
    for f in os.listdir(sdir):
        if f.endswith(".md"):
            os.remove(os.path.join(sdir, f))
    index = []

    def front(n):
        return "\n".join(["---", f"document: {doc['id']} ({doc['title']}, {doc['revision']}, {doc['date']})",
                          f"device: {doc['device']}", f"application: {doc['application']}",
                          f"section: {n['num']}", f"title: {n['title']}",
                          f"pages: {n['page']}-{last_page(n)}", "---", ""])

    def inline(n, depth):
        hdr = "#" * min(depth, 6)
        md = f"{hdr} {n['num']} {n['title']}\n\n" + render_body(n["body"], reg_links)
        for c in n["children"]:
            md += "\n" + inline(c, depth + 1)
        return md

    def emit(n):
        if size(n) <= MAX_CHARS or not n["children"]:
            name = slug(n["num"], n["title"]) + ".md"
            open(os.path.join(sdir, name), "w", encoding="utf-8").write(front(n) + inline(n, 1))
            index.append((n, name, True))
        else:
            name = slug(n["num"], n["title"]) + ".md"
            body = render_body(n["body"], reg_links)
            sub = "\n".join(f"- [{c['num']} {c['title']}]({slug(c['num'], c['title'])}.md)" for c in n["children"])
            open(os.path.join(sdir, name), "w", encoding="utf-8").write(
                front(n) + f"# {n['num']} {n['title']}\n\n{body}\n## Subsections\n\n{sub}\n")
            index.append((n, name, False))
            for c in n["children"]:
                emit(c)

    for r in roots:
        emit(r)
    lines_out = [f"# {doc['device']} — Sections", "",
                 f"Source: {doc['id']} {doc['revision']} ({doc['date']}). One file per section; "
                 "register tables are linked to `../registers/` instead of being repeated.", "",
                 "| Section | Pages | File |", "|---|---|---|"]
    for n, name, _ in index:
        lines_out.append(f"| {'&nbsp;' * 2 * (n['level'] - 1)}{n['num']} {n['title']} | {n['page']}–{last_page(n)} "
                         f"| [{name}]({name}) |")
    if missing:
        lines_out += ["", f"Headings listed in the TOC but not found in the body: {', '.join(missing)}"]
    open(os.path.join(sdir, "index.md"), "w", encoding="utf-8").write("\n".join(lines_out) + "\n")
    print(f"{len(toc)} TOC sections, {len(heads)} located, {len(index)} files; missing: {missing}", file=sys.stderr)


if __name__ == "__main__":
    main()
