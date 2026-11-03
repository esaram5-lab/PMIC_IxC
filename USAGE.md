# PMIC_IxC 사용법

JEDEC PMIC 스펙(JESD301 계열)의 레지스터 맵과 본문을 사람·AI·스크립트가 바로 쓸 수 있게 변환한 저장소입니다.

## 0. 준비

Python 3만 있으면 됩니다(표준 라이브러리만 사용, 추가 설치 없음).

```bash
git clone https://github.com/esaram5-lab/PMIC_IxC.git
```

```bash
cd PMIC_IxC
```

| 위치 | 내용 |
|---|---|
| `converted/<PMIC>/registers/0x21.md` | **레지스터 1개 = 파일 1개**: 필드별 비트·속성·기본값·모든 값의 의미 |
| `converted/<PMIC>/index.md` | 주소 ↔ 필드 이름 찾기, 원문 오타 수정 목록 |
| `converted/<PMIC>/sections/` | 레지스터 외 본문(전기 특성, 시퀀스, I2C/I3C 등). 목차는 `sections/index.md` |
| `converted/<PMIC>/register_summary.md` | PMIC 하나의 전체 레지스터를 한 파일로 |
| `converted/<PMIC>/registers.json` | 디코더·프로그램용 데이터 |
| `converted/<PMIC>/README.md` | 표기 규칙, 검증 내역, 알려진 한계 |
| `tools/decode_registers.py` | 레지스터 덤프 → 의미 해석 |

`<PMIC>` 폴더:

| 폴더 | 문서 | 구분 |
|---|---|---|
| `PMIC5000_5010` | JESD301-1A.03 | 서버 (RDIMM/LRDIMM) |
| `PMIC5030` | JESD301-5 | 서버 (RDIMM/MRDIMM/CXL) |
| `PMIC5100` | JESD301-2 | 클라이언트 (SODIMM/UDIMM) |
| `PMIC5120` | JESD301-6 | 클라이언트 (SODIMM/UDIMM/CSODIMM/CUDIMM) |
| `PMIC5200` | JESD301-3 | 클라이언트 (LPDDR5 CAMM2) |

**같은 주소라도 PMIC마다 의미가 다릅니다. 항상 폴더(PMIC)부터 고르세요.**

## 1. 직접 찾아보기

- **주소를 알 때**: `converted/PMIC5030/registers/0x32.md`를 엽니다.
- **이름만 알 때**(예: soft start): `index.md`에서 검색하거나

  ```bash
  grep -il "SOFT_START" converted/PMIC5030/registers/*.md
  ```

- **동작 설명이 필요할 때**(예: 파워온 순서): `sections/index.md`에서 해당 섹션을 찾습니다.
- 파일 맨 위에 **원문 표 번호와 페이지**가 있습니다. 중요한 값은 원문 PDF로 확인하세요.

### 레지스터 파일 읽는 법

- **Code (bin)**: 그 필드의 비트를 MSB→LSB로 쓴 값. `Field hex`는 필드 값만의 16진수(레지스터 바이트 전체가 아님).
- **`*` 표시**: 원문이 `...`로 생략한 구간을 앞뒤 값의 선형 규칙으로 채운 값.
- **`When: ...`**: 다른 레지스터 설정(또는 PMIC 종류)에 따라 의미가 달라질 때의 조건별 표.
- **`[n]`**: 단어·숫자 바로 뒤의 `[n]`은 원문 각주 → 같은 파일의 `NOTE n`. 비트 참조는 `[7:1]`, `Register 0x2B [5]` 형태.
- **Source correction**: 원문 오타·누락을 바로잡은 곳(근거 포함).

## 2. 레지스터 덤프 해석

보드에서 읽은 값을 넣으면 필드별 의미를 출력합니다.

```bash
python3 tools/decode_registers.py converted/PMIC5030/registers.json 0x21=0x78 0x32=0x80
```

```text
0x21 (R21) = 0x78 = 01111000b   [Host Region; Table 138, p.164]
  [7:1] SWA_VOLTAGE_SETTING = 0111100b  -> 1100 mV or 900 mV
  [0] SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING = 0b  -> -5% from the setting in ...
0x32 (R32) = 0x80 = 10000000b   [Host Region; Table 155, p.181]
  [7] VR_ENABLE = 1b  -> PMIC Enable
  ...
```

덤프 파일은 `--dump`로 넣습니다. 한 줄에 레지스터 하나씩, `0x21 0x78` / `0x21=0x78` / `21: 78` 형식 모두 됩니다.

```bash
python3 tools/decode_registers.py converted/PMIC5030/registers.json --dump dump.txt
```

정확한 해석을 위해 **관련 레지스터를 함께 넣으세요**.

- 조건으로 의미가 바뀌는 값: 조건 레지스터가 입력에 있으면 자동으로 해당 해석만 고릅니다.
  예) 측정값 0x0C는 0x1A·0x32와 함께.
- 여러 레지스터로 나뉜 값: 함께 넣으면 합쳐서 해석합니다. 예) 0x100+0x102, 0x36+0x22.
- `1100 mV or 900 mV`처럼 원문 각주로 갈리는 값은 자동 선택되지 않습니다. 파일의 NOTE를 보세요
  (R21의 경우 R2B[5]가 전압 범위를 정함).
- 0x70–0xFF(벤더 전용 영역)는 스펙에 정의가 없어 "not defined"로 표시됩니다.

## 3. 작은 AI에게 질문하기

### RAG에 넣기 (권장)

- `converted/*/registers/*.md`와 `converted/*/sections/*.md`를 **파일 하나 = 청크 하나**로 넣습니다.
- 파일 맨 위 `device:` 값으로 PMIC를 필터링하면 다른 PMIC와 섞이지 않습니다.
- 레지스터 질문에는 `registers/`를 우선 검색하도록 설정하는 것을 권장합니다.

### 프롬프트에 직접 붙이기

- 질문할 레지스터 파일 몇 개만 붙입니다.
- `register_summary.md`는 크기가 커서(PMIC5030 약 440 KB) 작은 모델에는 일부만 넣으세요.

### AI에게 같이 줄 지시문

```text
You answer questions about JEDEC PMIC registers using only the provided files.
- Always state which PMIC the answer is for; the same address differs between PMICs.
- "Code (bin)" is the field value MSB-first. Rows marked * were filled from the spec's linear pattern.
- "When: ..." tables apply only under that condition; name the condition in your answer.
- [n] right after a word or number is a footnote -> see "NOTE n" in the same file.
  Bit references look like [7:1] or "Register 0x2B [5]".
- Cite the document, Table and page from the file header.
- If the files do not contain the answer, say so instead of guessing.
```

### 질문 예시

- "PMIC5030 R21에 0x78이 있으면 SWA 출력 전압은?"
- "PMIC5120에서 DIMM Vendor 영역 잠금 해제 절차는?"
- "PMIC5100 R2B의 기본값은 무슨 의미야?"

**역할 분담 권장**: 값 해석은 디코더, "왜/언제 이렇게 동작하나" 같은 설명은 AI. 작은 모델은 비트 계산에서 자주 틀립니다.

## 4. 한계

- 각 `converted/<PMIC>/README.md`에 **알려진 한계**와 **원문 오타 수정 내역**이 있습니다.
  예) PMIC5200 R102–R105의 최댓값은 원문이 자기 모순이라 `...` 구간을 채우지 않았습니다.
- 원문의 `≥`(밑줄 친 `>`)는 텍스트 추출 시 `>`로 나올 수 있습니다.
- `sections/`의 그림은 글자만 남아 있습니다. 파형·도면은 원문을 보세요.
- 원문 PDF와의 직접 대조는 문서당 1–3쪽입니다. 나머지는 자동 검사(목차·표 번호 대조, 비트 7..0 커버리지,
  Host↔Vendor 레지스터 비교)만 거쳤습니다.

## 5. 새 스펙 revision 반영

원본 PDF는 이 저장소에 없습니다. JEDEC에서 받아 아래 이름으로 두세요.

| 경로 | 파일 |
|---|---|
| `spec/server/` | `JESD301-1A.03_PMIC5000_5010.pdf`, `JESD301-5_PMIC5030.pdf` |
| `spec/client/` | `JESD301-2_PMIC5100.pdf`, `JESD301-6_PMIC5120.pdf`, `JESD301-3_PMIC5200_CAMM2.pdf` |

그다음 해당 PMIC 폴더 `README.md` 맨 아래의 재생성 명령을 실행합니다(`pdftotext`, 즉 poppler-utils 필요).
`sections/`는 다음으로 재생성합니다.

```bash
python3 tools/extract_sections.py /tmp/PMIC5030.txt converted/PMIC5030
```

재생성 후 확인:

```bash
python3 tools/check_mirrors.py converted/PMIC5030/registers.json
```

표 형식이 바뀐 revision은 파서(`tools/extract_registers.py`)를 손봐야 할 수 있습니다.
