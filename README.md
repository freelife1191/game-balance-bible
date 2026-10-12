# 게임 밸런스 수치 기획 스킬

<a id="document-top"></a>

《게임 밸런스 수치 기획 바이블》의 지식을 전투·성장·경제·수익화 설계와 학습에 사용하는 **`game-balance-bible`** 스킬입니다.

<a id="toc"></a>

## 목차 (TOC)

- [설치하기](#installation)
- [시작하기](#quick-start)
- [간단한 사용법과 예시](#usage)
- [포함된 스킬](#what-it-does)
- [책의 8개 장이 스킬에 포함된 방식](#book-chapters)
- [스킬과 파일 구성](#skill-structure)
- [필요한 경우 상세 가이드 보기](#documentation)
- [검수 결과와 재현](#development)
- [원본·라이선스·포함 범위](#copyright)

---

<a id="installation"></a>

## 설치하기

> [!NOTE]
> **설치 대상과 기본 사용**
>
> Codex·Claude Code·Antigravity가 설치·로그인된 환경에서 사용합니다. 이 저장소에는 **`game-balance-bible` 스킬만** 포함됩니다. 이미 이 프로젝트를 열었다면 [시작하기](#quick-start)로 이동합니다.

### 프롬프트로 현재 프로젝트에 설치

사용 중인 에이전트 대화창에 다음 요청을 붙여 넣습니다. 로컬에서 설치하려면 `소스`를 다운로드한 폴더의 절대 경로로 바꿉니다. 설치 전에는 스킬 호출 기호를 붙이지 않습니다.

```text
다음 소스의 game-balance-bible을 현재 프로젝트 범위로 설치해줘.
소스: https://github.com/freelife1191/game-balance-bible.git
스킬 폴더 전체를 .agents/skills/에 복사하고 중첩 .git은 제외해줘.
Claude Code용 .claude/skills/에는 원본을 가리키는 상대 링크를 만들어줘.
기존 설치는 덮어쓰지 말고, 두 경로에서 SKILL.md를 읽을 수 있는지 확인해줘.
```

### CLI로 수동 설치

Git을 사용할 수 있는 터미널에서, 새 프로젝트 폴더를 만들 위치로 이동한 뒤 실행합니다. 대상 폴더가 이미 있으면 다른 이름을 사용합니다.

```bash
REPO_URL='https://github.com/freelife1191/game-balance-bible.git'
git clone --depth 1 "$REPO_URL" game-balance-bible
cd game-balance-bible
test -r .agents/skills/game-balance-bible/SKILL.md
test -r .claude/skills/game-balance-bible/SKILL.md
```

복제한 폴더를 Codex·Claude Code·Antigravity에서 열면 포함된 스킬과 Claude Code 상대 링크를 사용합니다. ZIP으로 받았다면 압축을 푼 폴더를 설치 소스로 사용합니다. **기존 프로젝트에 스킬을 복사하고 Claude 연결을 생성**하는 명령은 [설치 가이드](docs/setup.md#install-game-balance-skill)에 있습니다. 기본 책 질문에는 Python이나 원문 PDF가 필요하지 않습니다.

---

<a id="quick-start"></a>

## 시작하기

### 1. 프로젝트 폴더 열기

**설치·로그인된 Codex·Claude Code·Antigravity에서 이 프로젝트 폴더를 엽니다.** 책 스킬과 Claude Code용 상대 링크가 함께 제공됩니다.

> [!TIP]
> **기본 질문에는 원문 PDF가 필요하지 않습니다**
>
> 기본 질문은 포함된 책 지식 파일을 사용합니다. Python은 산술 검산을 재현할 때, 원문 PDF는 추가 원문 대조가 필요할 때 준비합니다.

### 2. 스킬 호출하기

**에이전트 대화창에 아래 요청을 입력합니다.** 셸 명령이 아닙니다.

| 도구 | 바로 사용할 요청 |
|---|---|
| Codex | `$game-balance-bible 대미지 공식과 성장 비용을 설계하는 순서를 설명해줘.` |
| Claude Code | `/game-balance-bible 대미지 공식과 성장 비용을 설계하는 순서를 설명해줘.` |
| Antigravity | `/game-balance-bible 대미지 공식과 성장 비용을 설계하는 순서를 설명해줘.` |

### 3. 목표와 데이터 추가하기

**목표와 데이터를 덧붙여 구체적으로 질문합니다.** 아래 예시를 복사하고 게임의 실제 값으로 바꿉니다. Claude Code·Antigravity에서는 맨 앞의 `$`를 `/`로 바꿉니다.

```text
$game-balance-bible
RPG 일반 몬스터의 전투 시간을 검토해줘.
플레이어 공격력 100, 몬스터 방어력 100·체력 1000, 초당 공격 2회다.
목표 처치 시간은 8~12초다. 책의 나눗셈 피해 예시 모델을 사용하고,
첫 타격은 0초, 피해는 고정이며 치명·회복·다른 피해원은 없다고 가정해줘.
타격당 피해·필요 타격 수·정확한 처치 시각과 DPS 근사를 구분해 계산해줘.
목표를 만족하는지 판단하고, 벗어날 때만 최소 조정안을 제안해줘.
```

스킬이 보이지 않으면 프로젝트 폴더와 `SKILL.md` 경로를 확인한 뒤 새 세션에서 다시 확인합니다. 연결·인증 문제는 [문제 해결](docs/troubleshooting.md#symptoms)을 참고합니다.

---

<a id="usage"></a>

## 간단한 사용법과 예시

기본형은 **`$game-balance-bible <요청>`** 또는 **`/game-balance-bible <요청>`**입니다. 질문에 맞는 장·공식·참고 자료를 찾아 답합니다.

| 목적 | Codex 대화 예시 |
|---|---|
| 실무 적용 | `$game-balance-bible RPG의 30일 강화 목표를 설계해줘. 목표 단계·누적 비용·일일 공급은 아직 미정이다. 필요한 입력과 모델을 먼저 정리하고 미정값은 가정으로 구분해줘.` |
| 계산 검토 | `$game-balance-bible 명중70%→관통30%→치명5% 순서로 판정한다. 관통 성공 시 치명 판정은 하지 않는다. 관통·치명·일반·빗나감의 실제 확률과 합계를 검산해줘.` |
| 개념 학습 | `$game-balance-bible 잔여 자원과 잔여 비율을 설명하고 작은 예제를 풀어줘.` |
| 장별 참고 | `$game-balance-bible ch04의 생산·소비 모델을 설명해줘.` |
| 내용 탐색 | `$game-balance-bible 장별 목차와 각 장의 주요 주제를 보여줘.` |

설계 요청에는 **장르·목표 경험·기간·대상 이용자·수치 데이터**를 함께 제공합니다. 계산 요청에는 **단위·적용 순서·집계 기준**도 붙입니다. 실제 값이 없으면 미정으로 남기거나 설명용 가정을 따로 표시하고, 책의 사례와 프로젝트 값을 구별합니다.

### 재화 부족을 검토할 때

```text
$game-balance-bible
같은 일반 유저의 7일 재화를 검토해줘. 초기 재고100, 일일 공급80,
7일 동안 한 번 받는 이벤트 보상200, 같은 기간 계획 소비900이다.
거래·다른 공급은 없다. 모두 같은 재화 단위다.
생산−계획 소비의 잔여량·잔여 비율과 초기 재고를 포함한 예상 잔고를 구분해줘.
예상 잔고가 음수면 계획 완수에 부족한 양으로 표시해줘.
계획 소비가 실제 지출과 다를 수 있음을 밝히고, 진행 가능성 판단에 필요한 자료를 적어줘.
```

### 결제 지표를 검토할 때

```text
$game-balance-bible
한 달 활성 유저1000명, 결제 유저100명, 총 결제액20000 RMB다.
동일 모집단의 PR·ARPPU·ARPU를 계산하고 ARPU=PR×ARPPU를 검산해줘.
이 값만으로 LTV나 투자 회수 월을 확정하지 말고 추가 입력을 알려줘.
읽은 장·공식의 근거와 이 가상 데이터의 가정을 구분해줘.
```

표·CSV를 제공할 때는 열 이름, 단위, 일일/누적 구분, 현재/다음 레벨의 의미를 붙입니다. 여러 모듈이 같은 지갑을 쓰면 소비 우선순위도 제공합니다. 장별 입력 서식과 더 복잡한 예시는 [고급 활용법](docs/advanced-usage.md)에 있습니다.

실행 검산이 필요하면 “핵심 수치를 계산 도구로 실제 실행하고 입력·식·실행 결과를 보여줘. 실행하지 못하면 미실행이라고 밝혀줘.”를 덧붙이고 도구 출력도 확인합니다.

---

<a id="what-it-does"></a>
<a id="this-project"></a>

## 포함된 스킬

| 스킬 | 하는 일 | 사용할 때 |
|---|---|---|
| [game-balance-bible](.agents/skills/game-balance-bible/SKILL.md) | 책의 개념·공식·판단 기준으로 설명, 계산, 설계 검토 | 이 책을 배우거나 게임 수치를 검토할 때 |

---

<a id="book-chapters"></a>

## 책의 8개 장이 스킬에 포함된 방식

책의 **본문 1~8장 모두**를 `chapters/`의 장별 지식 파일로 구성했습니다. 각 파일은 핵심 개념·프레임워크·적용 절차·예시·주의점·다른 장과의 연결을 정리합니다. 서문·후기·색인은 별도 장으로 세지 않습니다.

| 책의 장 | 포함된 스킬 파일 | 담긴 내용과 활용 |
|---|---|---|
| 1장 · 수치 프로세스화 | [ch01-process.md](.agents/skills/game-balance-bible/chapters/ch01-process.md) | 준비→전투→경제→검증→수익화의 흐름, 작업 순서와 반복 검증 |
| 2장 · 수치 구축 준비 작업 | [ch02-preparation.md](.agents/skills/game-balance-bible/chapters/ch02-preparation.md) | 장르·테마·게임의 3요소·타깃 게임 분석, 설계 목표 설정 |
| 3장 · 게임의 전투 수치 | [ch03-combat.md](.agents/skills/game-balance-bible/chapters/ch03-combat.md) | 속성·대미지·확률 판정, 계층별 성장 분배, NPC·밸런스 계산 |
| 4장 · 게임의 경제 수치 | [ch04-economy.md](.agents/skills/game-balance-bible/chapters/ch04-economy.md) | 경제모델·화폐·자원·I/O·생산·소비·가치 체계 |
| 5장 · 게임 수치 검증 | [ch05-validation.md](.agents/skills/game-balance-bible/chapters/ch05-validation.md) | 잔여 자원·레벨 조회, 피해비율과 생존비율 구분, 유저군별 검증 |
| 6장 · 게임의 수익화 | [ch06-monetization.md](.agents/skills/game-balance-bible/chapters/ch06-monetization.md) | 결제 유형·운영 지표·운영 단계·충전과 소비 검증 |
| 7장 · 수치 시각화 | [ch07-visualization.md](.agents/skills/game-balance-bible/chapters/ch07-visualization.md) | 성장·전투 리듬, 의례감·몰입감, 단계 목표와 곡선 분석 |
| 8장 · 수치 모듈화 | [ch08-modularization.md](.agents/skills/game-balance-bible/chapters/ch08-modularization.md) | 10개 모델의 연결, 매개변수→데이터 호출→계산, 성유물 풀·성장 예시 |

> [!NOTE]
> **책의 포함 범위와 근거**
>
> `SKILL.md`가 질문에 맞는 장을 찾고, 상세 산식은 `references/`, 공통 용어·절차는 용어집·패턴·치트시트에서 보충합니다. **장 전체의 주제를 다루지만 원문 전체·모든 표·이미지를 복제하거나 완전히 보존한 자료는 아닙니다.** [원문 페이지 지도와 추출 범위](.agents/skills/game-balance-bible/references/source-map.md)에 근거와 한계를 기록했습니다.

```text
$game-balance-bible ch03을 사용해 전투 모델을 검토하고,
ch04에서 성장 비용과 보상을 연결한 뒤 ch05의 기준으로 검증해줘.
각 단계의 입력·계산·산출물을 나눠서 정리해줘.
```

장별 준비 데이터·**고급 프롬프트 32개·후속 요청 8개·장 연결 통합 요청 3개**는 [장별 고급 활용법](docs/advanced-usage.md)에 있습니다. 공통 프로젝트 맥락을 먼저 제공하고 상황별 예시를 골라 설계→비교→검증→수정으로 이어갈 수 있습니다.

---

<a id="skill-structure"></a>

## 스킬과 파일 구성

| 책 스킬 파일 | 역할 |
|---|---|
| `SKILL.md` | 핵심 지침과 장별·주제별 색인 |
| `chapters/` | 8개 장의 개념, 적용 절차, 예시 |
| `references/` | 전투 공식, 경제 모델, 원문 페이지 지도, 질문별 자료 지도 |
| `glossary.md` | 용어와 해당 장의 참조 |
| `patterns.md` | 기법·적용 순서·절충점 |
| `cheatsheet.md` | 빠른 판단과 계산 규칙 |
| `agents/openai.yaml` | Codex 표시·호출 메타데이터 |

```text
README.md                          # 주 안내 문서
docs/                              # 상세 가이드 6개와 문서 지도
.agents/skills/
└── game-balance-bible/             # Codex·Antigravity가 읽는 책 스킬 원본
.claude/skills/
└── game-balance-bible              # 책 스킬 원본의 상대 링크
output/skill-review/                # 검수 요약·산술 재현 테스트
```

Claude Code의 연결은 개별 원본 폴더를 참조합니다. 원본과 링크를 Git에서 함께 관리합니다.

스킬 묶음은 Markdown 지식 파일 16개와 호스트 메타데이터 `agents/openai.yaml` 1개, 총 17개 파일입니다. `references/`에는 4개 참고 파일이 있습니다.

---

<a id="documentation"></a>
<a id="verification"></a>
<a id="troubleshooting"></a>

## 필요한 경우 상세 가이드 보기

| 필요한 내용 | 문서 |
|---|---|
| 전체 안내와 읽기 순서 | [문서 지도](docs/index.md) |
| 새 프로젝트 설치·호스트 연결 | [설치](docs/setup.md) |
| 책의 8개 장별 사용 전략·실무 프롬프트·장 연결 | [장별 고급 활용법](docs/advanced-usage.md) |
| 수치·원문·경계값·사용 테스트 | [검수와 테스트](docs/validation.md) |
| 책 내용과 참고 자료의 반영 범위 | [레퍼런스 검토](docs/reference-review.md) |
| 인식·연결·근거·인증 오류 | [문제 해결](docs/troubleshooting.md) |
| 실제 생성 결과와 검수 기록 | [프로젝트 사례](docs/project-example.md) |

---

<a id="development"></a>

## 검수 결과와 재현

[원문 재확인 감사 기록](output/skill-review/source-recheck-audit.json) · [산술 검산 결과](output/skill-review/numeric-regression-results.json) · [Codex 실제 호출 기록](output/skill-review/codex-host-smoke.json) · [과거 수치 검수 보고서](output/skill-review/game-balance-bible-numeric-audit.json) · [과거 호스트 호환성 기록](output/skill-review/multi-agent-compatibility.json)

원문 재확인에서는 표 **113개**·그림 **51개**를 목록화하고 **109쪽**을 이미지로 대조했습니다. 그림 전체의 구조·축·라벨과 필요한 주요 표·산식·각주를 확인했습니다. 모든 표 셀·그래프 좌표를 전수 검산한 결과는 아닙니다. 보완 내용과 원문의 불일치는 [검토 결과](docs/reference-review.md#원문-재확인-결과)에 정리했습니다.

산술 **64건**, 확률 **1,331개 조합**, 피해식 **24개 동치** 검사를 통과했습니다. 프로젝트 루트에서 `python3 output/skill-review/numeric_regression.py`를 실행하면 예제 산술과 모델 불변식을 검산하고 결과 JSON을 갱신합니다. 각 보고서의 통과는 기록된 검사 범위에 대한 결과입니다. `<project-root>`·`<temporary-workdir>`는 당시 로컬 경로를 대신하는 표기이며, 과거 호스트 기록은 현재 인증 상태를 보장하지 않습니다.

2026-10-12에는 Codex CLI에서 실제 호출 **1회**로 이름에 의한 스킬 탐색·관련 레퍼런스 읽기·Python 계산을 확인했습니다. HP 변환·이산 처치 시간·결제 지표와 입력 부족 시 회수 월을 미확정으로 남기는 응답이 검산과 일치했습니다. 다른 호스트와 전체 고급 프롬프트를 실행한 결과는 아닙니다.

후속 [프롬프트 표본 검증](docs/validation.md#prompt-samples)에서는 README2개·고급 예시3개의 응답이 독립 검산과 일치했습니다. 3개 응답의 계산 도구 실행 증거가 확인되지 않아 후속 요청을 보완했고, 추가 세션에서 실제 Python 검산을 확인했습니다. [입력·응답·판정 기록](output/skill-review/prompt-sample-validation.json)에 정확성과 실행 증거를 구분했습니다.

검증 기록을 바탕으로 스킬의 실행 검산 절차와 조회·조합 검증을 보완했습니다. 새 입력의 실제 실행·미실행 사례2건도 독립 호출과 검수에서 통과했습니다. 해당 버전의 결과와 파일 해시는 같은 기록의 `post_validation_refinement`에 있으며, 과거 원문 대조나 초기 실행 증거를 소급해 갱신한 것은 아닙니다.

---

<a id="copyright"></a>
<a id="️-copyright--fair-use"></a>

## 원본·라이선스·포함 범위

> [!WARNING]
> **원문과 스킬의 권리 구분**
>
> 이 스킬은 원문 전체를 대체하거나 복제하지 않습니다. 책과 책 기반 지식의 권리는 별도이며, 원문 인용과 공유에는 적용되는 권리와 이용 조건을 확인해야 합니다.

스킬·문서·호스트 연결·합성 테스트 자료·검수 요약은 Git에 포함합니다. 원문 도서·추출 원문·인증 정보·세션·캐시·임시 결과는 [.gitignore](.gitignore)에서 제외합니다. 클라우드 에이전트가 읽은 텍스트는 모델 제공자에게 전달될 수 있으므로 해당 데이터 처리 조건도 확인합니다.

---

[↑ 맨 위로](#document-top)
