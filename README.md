# PMIC_IxC — JEDEC PMIC Register Maps for AI

JEDEC PMIC 스펙(JESD301 계열)의 레지스터 맵과 본문을 AI가 읽기 쉬운 Markdown/JSON으로 변환한 공유용 저장소입니다.

- 원본 스펙 PDF는 포함하지 않습니다. 원본은 JEDEC(jedec.org)에서 직접 받으세요.
- 변환본은 각 문서의 표 번호·페이지를 함께 적어 두었습니다. 중요한 판단은 원본으로 확인하세요.

## 폴더 구조

| 폴더 | 내용 |
|---|---|
| `spec/server/` *(포함 안 됨)* | 재생성할 때 원본 PDF를 둘 위치 — `JESD301-1A.03_PMIC5000_5010.pdf`, `JESD301-5_PMIC5030.pdf` |
| `spec/client/` *(포함 안 됨)* | 〃 — `JESD301-2_PMIC5100.pdf`, `JESD301-6_PMIC5120.pdf`, `JESD301-3_PMIC5200_CAMM2.pdf` |
| `converted/<PMIC>/` | 레지스터 맵 변환본 (`registers/`, 값별 의미 포함) + 나머지 장 섹션별 Markdown (`sections/`) |
| `tools/` | 변환 스크립트, 레지스터 덤프 디코더 |

## 변환 현황

| PMIC | 문서 | 구분 | 레지스터 | 변환본 |
|---|---|---|---|---|
| PMIC5000/5010 | JESD301-1A.03 Rev 1.8.5 (2025.02) | server (RDIMM/LRDIMM) | 80 | [`converted/PMIC5000_5010`](converted/PMIC5000_5010/README.md) |
| PMIC5030 | JESD301-5 v1.00 (2026.01) | server (RDIMM/MRDIMM/CXL) | 168 | [`converted/PMIC5030`](converted/PMIC5030/README.md) |
| PMIC5100 | JESD301-2 Rev 1.03 (2022.10) | client (SODIMM/UDIMM) | 81 | [`converted/PMIC5100`](converted/PMIC5100/README.md) |
| PMIC5120 | JESD301-6 v1.0 (2025.02) | client (SODIMM/UDIMM/CSODIMM/CUDIMM) | 86 | [`converted/PMIC5120`](converted/PMIC5120/README.md) |
| PMIC5200 | JESD301-3 v1.0 (2025.10) | client (LPDDR5 CAMM2) | 104 | [`converted/PMIC5200`](converted/PMIC5200/README.md) |

같은 주소라도 PMIC마다 의미가 다릅니다. 질문할 때 항상 PMIC 이름을 함께 지정하세요.

## 도구

| 스크립트 | 역할 |
|---|---|
| `tools/extract_registers.py` | `pdftotext -layout` 출력 → `registers.json` (문서별 설정은 `converted/<PMIC>/meta.json`) |
| `tools/render_markdown.py` | `registers.json` → 레지스터별 Markdown, `index.md`, `register_summary.md` |
| `tools/render_readme.py` | 변환본 폴더의 `README.md` 생성 |
| `tools/extract_sections.py` | 레지스터 외 장을 섹션별 Markdown(`sections/`)으로 변환 |
| `tools/check_mirrors.py` | Host 레지스터와 전원 인가 시 복사 원본인 Vendor 레지스터 비교 |
| `tools/decode_registers.py` | 레지스터 덤프(`0x21=0x78 ...`)를 필드별 의미로 해석 |

## 빠른 사용법

자세한 사용법은 [USAGE.md](USAGE.md)를 보세요.

- 레지스터 값의 의미: `converted/<PMIC>/registers/<addr>.md` (예: `converted/PMIC5030/registers/0x21.md`)
- 주소/필드 찾기: `converted/<PMIC>/index.md`
- 레지스터 덤프 해석:

```bash
python3 tools/decode_registers.py converted/PMIC5030/registers.json 0x21=0x78 0x32=0x80
```

- 표기 규칙과 알려진 한계: 각 `converted/<PMIC>/README.md`
