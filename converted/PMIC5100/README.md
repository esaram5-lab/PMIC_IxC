---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client (DDR5 SODIMM, DDR5 UDIMM)
vin_bulk: 4.25 V to 5.5 V
scope: registers (registers/), other chapters (sections/)
---

# PMIC5100 Register Map (converted)

JESD301-2의 레지스터 장을 AI가 읽기 쉬운 형태로 변환한 결과입니다.
목표: **"레지스터 X의 비트 Y에 값 Z가 있으면 무슨 의미인가?"** 에 정확히 답하기.

## 파일

| 파일 | 용도 |
|---|---|
| `registers/<addr>.md` | 레지스터 1개 = 파일 1개. 모든 필드의 **모든 값과 의미**를 표로 나열 (RAG 청크 단위) |
| `index.md` | 주소 → 필드 이름 목록 + 원문 오타 수정 목록(Source corrections) |
| `register_summary.md` | 전체 레지스터를 한 파일로 (원문처럼 `...` 구간 생략). 프롬프트에 통째로 넣을 때 |
| `registers.json` | 기계용 데이터. `tools/decode_registers.py`가 사용 |
| `meta.json` | 문서 메타데이터, 영역 정의, 원문 오타 수정 내역 |
| `sections/` | **레지스터 외 나머지 장**(전기적 특성, 동작 시퀀스, I2C/I3C, 회로 예 등)을 섹션별 Markdown으로. 목차는 `sections/index.md`. 참고용 |

### `sections/` 읽는 법

- 문단은 문장으로 이어 붙였고, 표·그림 안 글자·정렬이 중요한 내용은 ```` ```text ```` 블록에 원문 배치 그대로 둡니다.
- 그림은 캡션(`*Figure N — ...*`)과 그림에서 추출된 글자만 남습니다. 도형·파형 자체는 없으므로 정확한 판단은 원문 PDF를 보세요.
- 레지스터 장의 레지스터 표는 반복하지 않고 `registers/<addr>.md` 링크로 대체했습니다(설명 문단은 유지).
- 일부 문서(5000/5010, 5100, 5120)는 위첨자 각주가 숫자로 붙어 있습니다(예: `Setting3,4`). 레지스터 파일에서는 `[3],[4]`로 정리했지만 `sections/`에서는 원문 그대로입니다.

## 표기 규칙 (작은 모델에게 함께 알려줄 것)

- **Code (bin)**: 해당 필드 비트를 MSB→LSB 순으로 쓴 값. `Field hex`는 그 필드 값만의 16진수(레지스터 바이트 전체 아님).
- **`*` 표시 값**: 원문이 `...`로 생략한 구간을 앞뒤 값의 선형 규칙으로 채운 값. 생략 구간 끝 값과 맞을 때만 채움.
- **`When: ...`**: 다른 레지스터 설정(또는 PMIC 종류)에 따라 같은 코드의 의미가 달라질 때 조건별로 나눈 표.
- **`[n]` 각주**: 단어/숫자 바로 뒤의 `[n]`은 원문 위첨자 각주 → 같은 파일의 `NOTE n`.
  비트 참조는 `[7:1]`, `Register 0x2B [5]`처럼 레지스터 이름/주소 뒤에 옵니다.
- **Combined encoding**: 코드 길이가 필드 폭보다 길면 여러 필드/레지스터 비트를 합친 인코딩입니다.
  디코더에 관련 레지스터를 함께 넣으면 합쳐서 해석합니다.
- **Source correction**: 원문 오타를 바로잡은 곳. 근거가 함께 적혀 있습니다.

## Attribute

| 약어 | 의미 |
|---|---|
| RO | Read Only — 쓰기 무시 |
| RW | Read/Write |
| W / WO | Write Only — 읽으면 0 |
| RV | Reserved — 0으로 읽힘, 호스트가 수정하면 안 됨 |
| 1O | Write '1' Only — 1만 쓸 수 있음 (Clear 레지스터) |
| P (modifier) | Protected — 패스워드 입력 후에만 쓰기 가능 |
| E (modifier) | 전원 사이클 후에도 유지, 명령으로 지울 수 있음 |
| N (modifier) | 전원 사이클 후에도 유지, 명령으로 지울 수 없음 |
| A (modifier) | PMIC 벤더가 제조 시 설정하는 읽기 전용 영구 값 |

## Register regions

| Range | Region |
|---|---|
| 0x00–0x3F | Host Region |
| 0x40–0x6F | DIMM Vendor Region (NVM, password protected) |
| 0x70–0xFF | Vendor Specific Region |

Vendor region(0x40–0x6F) 잠금 해제/프로그래밍 코드는 `registers/0x39.md`(R39) 참고. 0x70–0xFF는 원문에 정의가 없어 포함되지 않습니다.

## 레지스터 덤프 해석

```bash
python3 tools/decode_registers.py converted/PMIC5100/registers.json 0x21=0x78 0x2B=0x00
```

## 검증

- 레지스터 표 81개 추출 — 원문 목차(List of Tables)의 레지스터 표 81개와 1:1 대조, 페이지 번호도 목차 기준.
- 모든 레지스터에서 비트 7..0이 빠짐/중복 없이 필드로 덮이는지 자동 확인.
- 원문 PDF 페이지 이미지와 직접 대조: R2B (p.144).
- 원문 오타/누락 3건은 `index.md`의 "Source corrections"에 근거와 함께 기록.

## 재생성

```bash
pdftotext -layout spec/client/JESD301-2_PMIC5100.pdf /tmp/PMIC5100.txt
```

```bash
python3 tools/extract_registers.py /tmp/PMIC5100.txt converted/PMIC5100/meta.json converted/PMIC5100/registers.json
```

```bash
python3 tools/render_markdown.py converted/PMIC5100/registers.json converted/PMIC5100
```
