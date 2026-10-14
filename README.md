<a id="게임-밸런스-수치-기획-스킬"></a>

<a id="document-top"></a>

<p align="center">
  <a href="https://github.com/freelife1191/game-balance-bible">
    <img src="docs/assets/banner.svg" alt="Game Balance Bible — Combat, Growth, Economy, Monetization" width="900">
  </a>
</p>

<h1 align="center">게임 밸런스 수치 기획 스킬</h1>

<p align="center">《게임 밸런스 수치 기획 바이블》의 지식을 전투·성장·경제·수익화 설계와 학습에 연결하는 <code>game-balance-bible</code> 스킬</p>

<p align="center">
  <a href="https://github.com/freelife1191/game-balance-bible"><img src="https://img.shields.io/github/stars/freelife1191/game-balance-bible?style=flat-square&amp;label=GitHub" alt="GitHub stars"></a>
  <a href="https://github.com/freelife1191/game-balance-bible/releases"><img src="https://img.shields.io/badge/GitHub-Releases-243f7a?style=flat-square" alt="GitHub release"></a>
  <a href="docs/index.md"><img src="https://img.shields.io/badge/docs-guide-2f5f9f?style=flat-square" alt="Documentation"></a>
</p>

<p align="center">
  <a href="#quick-start">시작하기</a> ·
  <a href="#usage">사용 예시</a> ·
  <a href="#documentation">문서</a> ·
  <a href="release/README.md">릴리스</a>
</p>

<a id="toc"></a>

## 목차(TOC)

- [설치하기](#installation)
- [시작하기](#quick-start)
- [간단한 사용법과 예시](#usage)
  - [문제별로 확인할 조건과 바로가기](#problem-guide)
- [포함된 스킬](#what-it-does)
- [책의 8개 장이 스킬에 포함된 방식](#book-chapters)
- [스킬과 파일 구성](#skill-structure)
- [필요한 경우 상세 가이드 보기](#documentation)
- [릴리스 노트와 GitHub Release](#releases)
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

복제한 폴더를 Codex·Claude Code·Antigravity에서 열면 포함된 스킬과 Claude Code 상대 링크를 사용합니다. ZIP으로 받았다면 압축을 푼 폴더를 설치 소스로 사용합니다. **기존 프로젝트에 스킬을 복사하고 Claude Code 연결을 생성**하는 명령은 [기존 프로젝트에 설치하기](docs/setup.md#install-game-balance-skill)에 있습니다. 기본 책 질문에는 Python이나 원문 PDF가 필요하지 않습니다.

---

<a id="quick-start"></a>

## 시작하기

### 1. 프로젝트 폴더 열기

**설치·로그인된 Codex·Claude Code·Antigravity에서 이 프로젝트 폴더를 엽니다.** 책 스킬과 Claude Code용 상대 링크가 함께 제공됩니다.

> [!TIP]
> **기본 질문에는 원문 PDF가 필요하지 않습니다**
>
> 기본 질문은 포함된 책 지식 파일을 사용합니다. Python은 산술 검산을 재현할 때, 원문 PDF는 추가 원문 대조가 필요할 때 준비합니다. 대조를 요청하는 방법은 [원문과 대조하고 싶을 때](docs/troubleshooting.md#source-comparison)에 있습니다.

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
플레이어 공격력 100, 몬스터 방어력 100·체력 1,000, 초당 공격 2회다.
목표 처치 시간은 8~12초다. 책의 나눗셈 피해 예시 모델을 사용하고,
첫 타격은 0초, 피해는 고정이며 치명·회복·다른 피해원은 없다고 가정해줘.
타격당 피해·필요 타격 수·정확한 처치 시각과 초당 피해(DPS) 근사를 구분해 계산해줘.
목표를 만족하는지 판단하고, 벗어날 때만 최소 조정안을 제안해줘.
```

스킬이 보이지 않으면 프로젝트 폴더와 `SKILL.md` 경로를 확인한 뒤 새 대화에서 다시 확인합니다. 호출 기호 없이 자연어로 요청했을 때 스킬이 쓰이지 않으면 [자연어 요청으로 스킬이 호출되지 않을 때](docs/troubleshooting.md#explicit-invocation)를, 연결·인증 문제는 [문제 해결](docs/troubleshooting.md#symptoms)을 참고합니다.

---

<a id="usage"></a>

## 간단한 사용법과 예시

기본형은 **`$game-balance-bible <요청>`** 또는 **`/game-balance-bible <요청>`**입니다. 질문에 맞는 장·공식·참고 자료를 찾아 답합니다.

| 목적 | Codex 대화 예시 |
|---|---|
| 실무 적용 | `$game-balance-bible RPG의 30일 강화 목표를 설계해줘. 목표 단계·누적 비용·일일 공급은 아직 미정이다. 필요한 입력과 모델을 먼저 정리하고 미정값은 가정으로 구분해줘.` |
| 계산 검토 | `$game-balance-bible 명중 70%→관통 30%→치명 5% 순서로 판정한다. 관통 성공 시 치명 판정은 하지 않는다. 관통·치명·일반·빗나감의 실제 확률과 합계를 검산해줘.` |
| 개념 학습 | `$game-balance-bible 잔여 자원과 잔여 비율을 설명하고 작은 예제를 풀어줘.` |
| 장별 참고 | `$game-balance-bible ch04의 생산·소비 모델을 설명해줘.` |
| 내용 탐색 | `$game-balance-bible 장별 목차와 각 장의 주요 주제를 보여줘.` |

설계 요청에는 **장르·목표 경험·기간·대상 유저·수치 데이터**를 함께 제공합니다. 계산 요청에는 **단위·적용 순서·집계 기준**도 붙입니다. 실제 값이 없으면 미정으로 남기거나 설명용 가정을 따로 표시하고, 책의 사례와 프로젝트 값을 구별합니다.

<a id="problem-guide"></a>

### 문제별로 확인할 조건과 바로가기

같은 공식이라도 분모·대상·기간이나 적용 범위가 다르면 결론이 바뀝니다. 현재 문제에 해당하는 조건을 요청에 함께 적고, 바로가기의 예시로 이어갑니다. 아래 조건은 스킬 자료에 정리된 내용이며, 원문 위치는 연결된 장 파일에서 확인합니다.

| 현재 문제 | 확인할 조건·예외 | 바로가기 |
|---|---|---|
| 재화가 부족하거나 남을 때 | 잔여 비율은 `(생산−소비)÷소비`로 소비가 분모이며, 소비가 0이면 정의되지 않습니다. 초기 보유량을 넣은 실제 잔고와 구분합니다. 엥겔 계수 R1 구간은 잔여 비율 값으로 환산하지 않고, −50%는 모든 재화의 임곗값이 아니라 설계 출발점으로 봅니다. | [재화 부족을 검토할 때](#재화-부족을-검토할-때)<br>[5장 A. 잔여 압력과 실제 지갑을 분리하는 30일 검증](docs/advanced-usage.md#ch05-a) |
| 결제 지표를 비교하거나 LTV를 추정할 때 | 활성 유저 결제율(PR)·ARPPU·ARPU는 같은 모집단·같은 기간으로 맞춥니다. 이탈률의 분모는 원문 식대로 ‘총 유저 수’이며 책의 예시는 월초 유저 수를 씁니다. 근사 LTV `ARPU÷주기 이탈률`은 표 6.1의 계산과 단위를 맞춘 스킬의 해석이며, 원문 본문 식은 ‘활성 유저의 평균 결제율 × (1 ÷ 주기 이탈률)’입니다. 근사 LTV는 참고치이며 상한이나 하한으로 단정하지 않습니다. DAU·MAU는 책에 정의가 없는 지표이므로 쓰면 책 밖 지식으로 표시합니다. | [결제 지표를 검토할 때](#결제-지표를-검토할-때)<br>[6장 A. KPI 분모·기간을 고정한 ARPU와 근사 LTV 검증](docs/advanced-usage.md#ch06-a) |
| 성장 예산을 여러 루트에 나눌 때 | 비율의 합이 반드시 100%여야 하는 것은 글로벌 분할뿐이며, 벤치마크 분할은 100%가 아니어도 됩니다. 두 방식 모두 1단계 공격·방어·체력의 총 분할 비율은 서로 같게 둡니다. 수집형 루트는 새 항목을 위한 여지를 남길 수 있습니다(원문 표 3.23은 합 70%). | [3장 C. 총 성장 예산을 육성 루트에 분할하기](docs/advanced-usage.md#ch03-c) |
| 속성 비율을 고정했으니 레벨별 전투 사이클도 같다고 볼 때 | 1단계 비율(예: 공격:방어:체력 `1:1:10`)을 고정해도 사이클은 고정되지 않습니다. 원문 표 3.5는 사이클이 레벨 1의 10.03턴에서 레벨 100의 13턴으로 늘고, 표 3.6은 치명·관통을 더하면 사이클이 9.95턴에서 6.93턴으로 줄어듭니다. 성장식·피해식·2단계 속성 효과를 함께 넣어 레벨별로 다시 계산합니다. | [3장 C. 총 성장 예산을 육성 루트에 분할하기](docs/advanced-usage.md#ch03-c) |
| 계획경제에서 유저 거래를 허용할 때 | 거래 허용 여부만 정하지 않고 거래 방식·품목·한도를 함께 정합니다. 책의 사례는 상회처럼 시스템이 중간 저장소인 거래에서 귀속 화폐만 주고 재판매를 막습니다. 또 가격 민감형 자원은 익명 거래로, 가격 협의형 자원은 실명 거래로 나누고, 부캐 전달에는 거래 한도를 둡니다. 저장 거래 시스템의 재고·가격·세금 설계는 저자가 개인 의견이라고 밝힌 부분입니다. 생산 모델에서는 시스템 생산과 거래로 얻는 양을 따로 계산합니다. | [4장 A. I/O와 거래 제약을 포함한 재화 흐름 설계](docs/advanced-usage.md#ch04-a) |
| 성장 비용을 확정하거나 가치 체계의 가격을 매길 때 | 구축 단계의 소비 모델은 완전하지 않아 그 소비 수치는 생산 모델 설계용이며, 가치 체계를 만든 뒤 소비 모델을 다시 조정합니다. 기준점이 되는 가격은 감성으로 정할 수 있고, 화폐와 전투력에 가격을 먼저 매긴 뒤 소비 모델을 참고해 자원 가격을 정합니다. 소비 가치는 대부분 전투력 가치와 달라, 소비 모델을 전투력 가치에 맞춰 피팅합니다. 가격의 비용 차원은 가장 놓치기 쉬우므로 사회적 비용과 게임 난이도까지 봅니다. | [4장 B. 목표 주기에서 보상을 역산하는 생산 모델](docs/advanced-usage.md#ch04-b)<br>[4장 D. 성장 가치와 가격을 같은 기준으로 비교하기](docs/advanced-usage.md#ch04-d) |
| 성장·플레이의 가성비를 비교할 때 | 플레이 가성비의 분모는 그 플레이에 쓴 **시간** 가치입니다. 재료·사회적 비용을 분모에 넣는 것은 책의 식이 아닌 프로젝트 확장이며, 넣는다면 시간과 이중 계산하지 않습니다. 가성비는 참조 데이터로만 씁니다. | [4장 D. 성장 가치와 가격을 같은 기준으로 비교하기](docs/advanced-usage.md#ch04-d) |
| 원문 표의 화폐 단가로 재현한 값이 맞지 않을 때 | 화폐 비율 `1:10:10`은 본문과 표가 일치합니다. 어긋나는 것은 코인 단가로, 인쇄 163쪽 예시와 인쇄 165쪽 표 4.34는 `0.0001`, 변환 관계를 임시로 정한 표 4.12와 표 4.39는 `0.001`입니다. 표마다 그 표의 단가를 쓰고 섞지 않습니다. | [추가로 확인한 원문 불일치와 적용 조건](.agents/skills/game-balance-bible/references/source-map.md#추가로-확인한-원문-불일치와-적용-조건)<br>[4장 E. 책 예시의 화폐 비율과 표별 코인 단가를 섞지 않고 재현하기](docs/advanced-usage.md#ch04-e) |
| 월간 패스나 보상 패키지를 설계할 때 | 월간 패스의 가장 큰 목적은 그 기간의 리텐션입니다. 일반·프리미엄의 가격 차별에는 두 가지 방식이 있습니다. 하나는 일반 월간 패스의 수익을 프리미엄보다 높여 일반을 맛보기 상품으로 두는 방식이고, 다른 하나는 프리미엄의 수익·가성비를 훨씬 높이는 방식입니다(여기서 ‘수익’을 유저가 받는 보상 비율로 읽는 것은 스킬의 해석입니다). 매일 로그인할 때마다 초과 보상이나 차별 서비스를 넣을 수 있습니다. 보상 패키지는 구매 간격에 따라 일일/주간/월간 패키지, 평생 패키지, 조건 패키지로 나뉘고, 그 기간에 유저가 필요로 할 자원을 미리 예측해야 합니다. 소과금 유저가 구매를 망설이면 가성비·실용성·가격 중 무엇을 바꿀지 정합니다. | [6장 후속. D의 부족량 가설로 두 개선 시나리오 비교](docs/advanced-usage.md#ch06-followup) |
| 성장 곡선의 형태를 고를 때 | 책이 구분하는 추세는 선형·지수·로그·다항식 4종입니다. 저자는 선형은 특정 성장 모듈에만 쓰이고, 대부분의 성장은 로그 추이를 보이며, 다항식이 게임 경험상 가장 좋다고 평가합니다. 다항식이라는 이름만으로 주기성이 보장되지는 않습니다. | [7장 C. 질문별 그래프 선택과 동일 기준 비교](docs/advanced-usage.md#ch07-c) |
| 장르에 맞는 수치 우선순위를 정할 때 | 저자가 수치 설계의 중점을 직접 밝힌 장르는 RPG(육성 모듈)와 전략(전투·경제 모듈)뿐입니다. 다른 장르의 우선순위는 스킬의 추론이므로 책의 주장으로 인용하지 않습니다. | [2장 A. 장르와 테마를 수치 설계 조건으로 번역하기](docs/advanced-usage.md#ch02-a) |
| 수치 모델을 연결하거나 변경 영향을 볼 때 | 8장의 수치 모델 10단계와 8.3절의 10개 모듈은 1:1로 대응하는 목록이 아닙니다. 성장 검증(모델 8)은 경제 검증(모델 7)의 생산 검증 자원 데이터로 계산하며, 번호를 일방향 실행 순서로 고정하지 않습니다. | [8장 A. 10개 모델의 책임과 연결을 한 장에 매핑](docs/advanced-usage.md#ch08-a) |
| 답의 근거가 책인지 스킬 정리인지 구분하고 싶을 때 | `(인쇄 N / PDF M)`이 붙은 문장은 책의 서술이고, ‘스킬 정리’로 표시된 내용은 스킬이 정리한 것입니다. 스킬은 기본적으로 원문을 열지 않고 확인할 위치를 안내합니다. | [원문과 대조하고 싶을 때](docs/troubleshooting.md#source-comparison) |

### 재화 부족을 검토할 때

```text
$game-balance-bible
일반 유저의 7일 재화를 검토해줘. 초기 재고 100, 일일 공급 80,
7일 동안 한 번 받는 이벤트 보상 200, 같은 기간 계획 소비 900이다.
거래·다른 공급은 없다. 모두 같은 재화 단위다.
생산−계획 소비의 잔여량·잔여 비율과 초기 재고를 포함한 예상 잔고를 구분해줘.
예상 잔고가 음수면 계획 완수에 부족한 양으로 표시해줘.
계획 소비가 실제 지출과 다를 수 있음을 밝히고, 진행 가능성 판단에 필요한 자료를 적어줘.
```

### 결제 지표를 검토할 때

```text
$game-balance-bible
한 달 활성 유저 1,000명, 과금 유저 100명, 총 결제액 20,000 RMB다.
동일 모집단의 PR·ARPPU·ARPU를 계산하고 ARPU=PR×ARPPU를 검산해줘.
이 값만으로 LTV나 투자 회수 월을 확정하지 말고 추가 입력을 알려줘.
읽은 장·공식의 근거와 이 가상 데이터의 가정을 구분해줘.
```

표·CSV를 제공할 때는 열 이름, 단위, 일일/누적 구분, 현재/다음 레벨의 의미를 붙입니다. 여러 모듈이 같은 지갑을 쓰면 소비 우선순위도 제공합니다. 장별 입력 서식과 더 복잡한 예시는 [장별 고급 활용법](docs/advanced-usage.md)에 있습니다.

실행 검산이 필요하면 ‘핵심 수치를 계산 도구로 실제 실행하고 입력·식·실행 결과를 보여줘. 실행하지 못하면 미실행이라고 밝혀줘.’를 덧붙이고 도구 출력도 확인합니다.

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

책의 **본문 1~8장 모두**를 `chapters/`의 장별 지식 파일로 구성했습니다. 각 파일은 핵심 개념·프레임워크·적용 절차·예시·주의점·다른 장과의 연결을 정리합니다. 머리말 등 앞부분·후기·색인은 별도 장으로 세지 않습니다.

저자는 머리말에서 수치 기획을 막 시작했거나 이직을 앞둔 독자에게 1~6장을, 수치 기획 경험이 있는 독자에게 7장을 권하고, 8장은 게임 수치에 대한 개인적인 생각과 경험을 설명한 장이라고 밝힙니다(머리말, 인쇄 xxv / PDF 27). 또 읽으면서 익숙한 게임을 하나 골라 책의 방법으로 수치 시스템을 직접 만들어 보기를 권합니다(머리말, 인쇄 xxv / PDF 27).

| 책의 장 | 포함된 스킬 파일 | 담긴 내용과 활용 |
|---|---|---|
| 1장 · 수치 프로세스화 | [ch01-process.md](.agents/skills/game-balance-bible/chapters/ch01-process.md) | 준비→전투→경제→검증→수익화의 흐름, 작업 순서와 반복 검증 |
| 2장 · 수치 구축 준비 작업 | [ch02-preparation.md](.agents/skills/game-balance-bible/chapters/ch02-preparation.md) | 장르·테마·게임의 3요소·타깃 게임 분석, 설계 목표 설정 |
| 3장 · 게임의 전투 수치 | [ch03-combat.md](.agents/skills/game-balance-bible/chapters/ch03-combat.md) | 속성·대미지·확률 판정, 계층별 성장 분배, NPC·밸런스 계산 |
| 4장 · 게임의 경제 수치 | [ch04-economy.md](.agents/skills/game-balance-bible/chapters/ch04-economy.md) | 경제모델·화폐·자원·I/O·생산·소비·가치 체계 |
| 5장 · 게임 수치 검증 | [ch05-validation.md](.agents/skills/game-balance-bible/chapters/ch05-validation.md) | 잔여 자원·레벨 조회, 피해 비율과 생존 비율 구분, 유저군별 검증 |
| 6장 · 게임의 수익화 | [ch06-monetization.md](.agents/skills/game-balance-bible/chapters/ch06-monetization.md) | 결제 유형·운영 지표·운영 단계·충전과 소비 검증 |
| 7장 · 수치 시각화 | [ch07-visualization.md](.agents/skills/game-balance-bible/chapters/ch07-visualization.md) | 성장·전투 리듬, 의례감·몰입감, 단계 목표와 곡선 분석 |
| 8장 · 수치 모듈화 | [ch08-modularization.md](.agents/skills/game-balance-bible/chapters/ch08-modularization.md) | 10개 모델의 연결, 설계 아이디어 정리 뒤 매개변수→데이터 호출→계산, 성유물 풀·성장 예시 |

> [!NOTE]
> **책의 포함 범위와 근거**
>
> `SKILL.md`가 질문에 맞는 장을 찾고, 상세 산식은 `references/`, 공통 용어·절차는 용어집·패턴·치트시트에서 보충합니다. **장 전체의 주제를 다루지만 원문 전체·모든 표·이미지를 복제하거나 완전히 보존한 자료는 아닙니다.** [원문 페이지 지도와 추출 범위](.agents/skills/game-balance-bible/references/source-map.md)에 근거와 한계를 기록했습니다.

```text
$game-balance-bible ch03을 사용해 전투 모델을 검토하고,
ch04에서 성장 비용과 보상을 연결한 뒤 ch05의 기준으로 검증해줘.
각 단계의 입력·계산·산출물을 나눠서 정리해줘.
```

장별 준비 데이터, **공통 고급 예시 4개, 장별 고급 예시 32개와 보완 예시 1개, 후속 요청 8개, 장 연결 통합 요청 3개**는 [장별 고급 활용법](docs/advanced-usage.md)에 있습니다. 공통 프로젝트 맥락을 먼저 제공하고 상황별 예시를 골라 설계→비교→검증→수정으로 이어갈 수 있습니다.

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
output/skill-review/                # 검수 요약·산술 검산 재현기
```

Claude Code의 연결은 `.agents/skills/game-balance-bible` 폴더를 가리키는 상대 링크입니다. 원본과 링크를 Git에서 함께 관리합니다.

스킬 묶음은 Markdown 지식 파일 16개와 호스트 메타데이터 `agents/openai.yaml` 1개, 총 17개 파일입니다. `references/`에는 4개 참고 파일이 있습니다.

---

<a id="documentation"></a>
<a id="verification"></a>
<a id="troubleshooting"></a>

## 필요한 경우 상세 가이드 보기

| 필요한 내용 | 문서 |
|---|---|
| 전체 안내와 읽기 순서 | [문서 지도](docs/index.md) |
| 새 프로젝트 설치·호스트 연결 | [설치와 호스트 연결](docs/setup.md) |
| 책의 8개 장별 사용 전략·실무 프롬프트·장 연결 | [장별 고급 활용법](docs/advanced-usage.md) |
| 수치·원문·경계값·사용 시험 | [검수와 테스트](docs/validation.md) |
| 책 내용과 참고 자료의 반영 범위 | [책 내용과 레퍼런스 재검토](docs/reference-review.md) |
| 인식·연결·근거·인증 오류 | [문제 해결](docs/troubleshooting.md) |
| 실제 생성 결과와 검수 기록 | [프로젝트 사례](docs/project-example.md) |
| 릴리스 노트 규칙과 GitHub Release 배포 | [릴리스 안내](release/README.md) · [현재 노트](release/2026-10-15-documentation-and-release-guide.md) · [GitHub Releases](https://github.com/freelife1191/game-balance-bible/releases) |

---

<a id="releases"></a>

## 릴리스 노트와 GitHub Release

릴리스 노트는 [release/](release/README.md)에 KST 작성일과 영문 kebab-case 제목을 사용해 보관합니다. 원고 파일을 저장소에 추가하는 것만으로 공개 릴리스가 생성되지는 않으며, 검토 후 [`gh release create`](release/README.md#배포-절차)의 `--notes-file`로 지정했을 때 GitHub Release 설명에 게시됩니다.

현재 문서 변경의 원고는 [2026-10-15 documentation and release guide](release/2026-10-15-documentation-and-release-guide.md)입니다. 새 원고는 [템플릿](release/_template.md)에서 시작합니다.

---

<a id="development"></a>

## 검수 결과와 재현

[원문 재확인 감사 기록](output/skill-review/source-recheck-audit.json) · [산술 검산 결과](output/skill-review/numeric-regression-results.json) · [Codex 실제 호출 기록](output/skill-review/codex-host-smoke.json) · [과거 수치 감사 보고서](output/skill-review/game-balance-bible-numeric-audit.json) · [과거 호스트 호환성 기록](output/skill-review/multi-agent-compatibility.json)

원문 재확인에서는 표 **113개**·그림 **51개**를 목록화하고 **109쪽**을 이미지로 대조했습니다. 그림 전체의 구조·축·라벨과 필요한 주요 표·산식·각주를 확인했습니다. 모든 표 셀·그래프 좌표를 전수 검산한 결과는 아닙니다. 보완 내용과 원문의 불일치는 [검토 결과](docs/reference-review.md#원문-재확인-결과)에 정리했습니다.

산술 **64개**, 확률 **1,331개 조합**, 피해식 **24개 동치** 검사를 통과했습니다. 프로젝트 루트에서 `python3 output/skill-review/numeric_regression.py`를 실행하면 예제 산술과 모델 불변식을 검산하고 결과 JSON을 갱신합니다. 각 보고서의 통과는 기록된 검사 범위에 대한 결과입니다. `<project-root>`·`<temporary-workdir>`는 당시 로컬 경로를 대신하는 표기이며, 과거 호스트 기록은 현재 인증 상태를 보장하지 않습니다.

이전 검증(2026-10-12)에서는 Codex CLI 0.162.0의 실제 호출 **1회**에서 이름으로 스킬을 찾고 관련 레퍼런스를 읽고 Python으로 계산한 것을 확인했습니다([Codex 실제 호출 기록](output/skill-review/codex-host-smoke.json)). HP 변환·이산 처치 시간·결제 지표와 입력 부족 시 회수 월을 미확정으로 남기는 응답이 검산과 일치했습니다. 다른 호스트와 전체 고급 프롬프트를 실행한 결과는 아닙니다.

후속 [프롬프트 표본 검증](docs/validation.md#prompt-samples)에서는 README 2개·고급 예시 3개의 응답이 독립 검산과 일치했습니다. 그중 3개 응답은 계산 도구 실행 증거가 확인되지 않아 후속 요청을 보완했고, 추가 세션에서 실제 Python 검산을 확인했습니다. [입력·응답·판정 기록](output/skill-review/prompt-sample-validation.json)에 정확성과 실행 증거를 구분했습니다.

검증 기록을 바탕으로 스킬의 실행 검산 절차와 조회·조합 검증을 보완했습니다. 새 입력의 실제 실행·미실행 사례 2건도 독립 호출과 검수에서 통과했습니다. 해당 버전의 결과와 파일 해시는 같은 기록의 `post_validation_refinement`에 있으며, 과거 원문 대조나 초기 실행 증거를 소급해 갱신한 것은 아닙니다.

> [!NOTE]
> 위 호스트 호출과 프롬프트 표본의 결과는 모두 후속 원문 재검수로 스킬 자료를 보완하기 전 버전에 대한 기록입니다.

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
