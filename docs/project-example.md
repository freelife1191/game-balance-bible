# 프로젝트 사례

<a id="document-top"></a>

[문서 지도](index.md) · [README](../README.md)

> [!NOTE]
> **이 문서가 설명하는 검수 기록**
>
> 이 프로젝트는 《게임 밸런스 수치 기획 바이블》을 **실무 적용·학습·장별 참고**에 사용할 수 있는 한국어 스킬로 변환했습니다. 아래 내용은 2026-10-12 검수 기록을 설명하며, 다른 책에도 동일한 결과나 분량을 보장하는 기준은 아닙니다. 이후 원문 재검수로 스킬 자료가 보완됐으므로, 아래 호스트·표본 시험 결과는 보완 전 버전에 대한 기록입니다.

**이 문서에서 찾기**

- [무엇을 만들었는가](#무엇을-만들었는가)
- [완성된 스킬 사용하기](#use-skill)
- [검수 기록을 읽는 방법](#evidence)
- [장별로 실무에 적용할 때](#장별로-실무에-적용할-때)
- [스킬 근거를 보완할 때](#스킬-근거를-보완할-때)

---

## 무엇을 만들었는가

| 구성 | 위치 | 역할 |
|---|---|---|
| 책 지식 스킬 | `.agents/skills/game-balance-bible/` | 게임 수치 설계·학습·검증 지식 |
| Claude Code 연결 | `.claude/skills/game-balance-bible/` | 동일한 책 스킬 원본을 사용 |
| 검수 기록 | `output/skill-review/` | 원문 대조·수치 검산·사용 시험 근거 |

입력 PDF는 290쪽이며, 실제 본문은 8장입니다. 자동 탐지의 장 수를 그대로 사용하지 않고 실제 목차에 맞춰 구성했습니다. PDF 쪽수와 인쇄 쪽수의 차이, 중복 스캔과 빈 장 경계 페이지도 별도 기록했습니다.

텍스트 추출 후 원문 109쪽을 이미지로 재대조했습니다. 표 113개·그림 51개를 목록화하고 그림의 구조·축·라벨과 필요한 주요 표·산식·각주를 확인했습니다. 모든 표 셀과 그래프 좌표를 전수 검산하지는 않았습니다. 실제 파일 구성은 다음과 같습니다.

```text
game-balance-bible/
├── SKILL.md
├── agents/openai.yaml
├── chapters/
│   ├── ch01-process.md
│   ├── ch02-preparation.md
│   ├── ch03-combat.md
│   ├── ch04-economy.md
│   ├── ch05-validation.md
│   ├── ch06-monetization.md
│   ├── ch07-visualization.md
│   └── ch08-modularization.md
├── glossary.md
├── patterns.md
├── cheatsheet.md
└── references/
    ├── combat-formulas.md
    ├── economy-models.md
    ├── source-map.md
    └── task-map.md
```

`agents/openai.yaml`은 Codex의 표시·호출 메타데이터입니다. 공통 지식은 `SKILL.md`, 장 파일과 참고 자료에 있으며, 다른 호스트를 위해 계산 내용을 따로 복제하지 않았습니다.

---

<a id="use-skill"></a>

## 완성된 스킬 사용하기

**에이전트 대화창**에 입력합니다.

```text
# Codex: 실무 설계
$game-balance-bible 이 게임의 대미지 공식과 성장 비용을 분석해줘.
단위·가정·계산 근거와 검증 방법을 제시해줘.

# Codex: 학습
$game-balance-bible ch04의 자원 생산·소비 모델을 설명하고 예제를 풀어줘.

# Claude Code / Antigravity: 특정 주제 참고
/game-balance-bible 순차 판정과 원탁 판정의 실제 치명타 확률 차이를 설명해줘.
```

프로젝트 수치를 설계할 때는 장르, 목표 경험, 전투 단위, 성장 기간, 대상 유저, 실제 데이터를 함께 제공합니다. 값이 없으면 책 예시로 채우기보다 가정을 명시하게 요청합니다.

현재 프로젝트에는 책 스킬 `game-balance-bible`과 이를 가리키는 Claude Code 연결이 포함됩니다. 새 프로젝트에서 연결을 구성하려면 [설치와 호스트 연결](setup.md)을 참고합니다.

---

<a id="evidence"></a>

## 검수 기록을 읽는 방법

| 기록 | 확인할 내용 |
|---|---|
| `source-recheck-audit.json` | 원문 재확인: 표 113개·그림 51개, 시각 확인 109쪽, 보완 근거·재현 한계·스킬 파일 해시 |
| `game-balance-bible-numeric-audit.json` | 84개 주장 그룹의 대조, 수정 근거, 독립 사용 평가와 검수 한계 |
| `numeric-regression-results.json` | 산술 64개, 순차 확률 1,331개 조합, 피해식 24개 동치의 결과 |
| `multi-agent-compatibility.json` | 원본 공유, 호스트 인식과 실제 실행 검증 상태 |
| `codex-host-smoke.json` | 이전 검증의 Codex CLI 0.162.0 호출 1회(스킬 보완 전 버전): 스킬 탐색·레퍼런스 읽기·계산·적용 한계 확인 |
| `prompt-sample-validation.json` | README 2개·고급 예시 3개의 정확성/실행 증거, 후속 재검산, 스킬 보완 후 실행·미실행 2건과 해당 버전 해시 |
| `numeric_regression.py` | 산술·모델 불변식 검산을 다시 실행하는 코드 |

> [!IMPORTANT]
> **검수 숫자의 집계 단위**
>
> 숫자 후보 520행에는 장 번호·항목 번호·중복도 포함되어 있습니다. **84개 주장 그룹을 84개의 독립 숫자라고 읽지 않습니다.** 산술 검산과 확률 조합 검증 역시 다른 범주의 검사입니다.

**과거 수치 감사 기록**에서는 기존 예제의 추가 산술 오류를 발견하지 못했습니다. 다만 레벨 변수·계단식 경계·포화식 범위·LTV 가정을 보강했고, 원문 자체의 오기와 단가 차이를 기록했습니다. 이는 스킬에 포함된 내용을 검수한 결과이며, 책의 모든 표·이미지를 전면 교정했다는 의미는 아닙니다.

후속 원문 재확인에서는 성장 분배·NPC 템플릿, I/O 흐름, 피해 비율과 생존 비율 구분, 성유물 풀·성장식을 보완했습니다. 화폐 비율(아래 정정 참고), 레벨 예시, 그래프 범례, 상품 합계 등 원문 자체의 불일치도 확인했으며, [원문에 남아 있는 불일치](reference-review.md#원문에-남아-있는-불일치)에 적용 조건과 함께 남겼습니다.

> [!NOTE]
> **정정: 화폐 비율**
>
> 화폐 비율은 후속 원문 재검수에서 본문과 표 모두 `1:10:10`으로 확인되어 원문 불일치가 아닙니다(인쇄 165 / PDF 195). 같은 장에서 실제로 어긋나는 값은 코인 단가 `0.0001`(인쇄 163 / PDF 193의 예시, 인쇄 165 / PDF 195의 표 4.34)과 `0.001`(인쇄 140 / PDF 170의 임시값인 표 4.12와 인쇄 173 / PDF 203의 표 4.39)입니다.

> [!NOTE]
> **스킬 등록과 계산 시험의 차이**
>
> 과거 호스트 검증에서는 Antigravity의 계산 시험이 통과했습니다. Claude Code는 스킬 등록을 확인했지만 OAuth 인증 만료로 계산 시험이 중단되었습니다. 두 결과를 모두 실행 통과로 묶지 않습니다.

이전 검증의 Codex CLI 0.162.0 호출 1회에서는 이름으로 스킬과 관련 자료를 찾고 Python 검산을 실행했습니다. HP 변환, 이산 타격과 초당 피해(DPS) 근사의 구분, 과금 유저 내 가중 ARPPU·전체 활성 ARPU·근사 LTV 계산이 일치했으며 회수 월은 입력 부족으로 남겼습니다. 원시 세션 대신 [입력 조건·결과·읽은 파일 해시](../output/skill-review/codex-host-smoke.json)를 기록했습니다. 다른 호스트의 과거 결과를 이 검사로 갱신한 것은 아니며, 이 결과는 후속 원문 재검수로 스킬 자료를 보완하기 전 버전에 대한 것입니다.

### 산술 검산 재실행

**프로젝트 루트의 셸**에서 실행합니다.

```bash
python3 output/skill-review/numeric_regression.py
```

> [!IMPORTANT]
> **검산 명령이 갱신하는 파일**
>
> 같은 폴더의 `numeric-regression-results.json`이 갱신됩니다. 이 명령은 정해진 예제와 모델 불변식을 검사하며, 원문 판독과 실제 호스트 답변 시험을 대신하지 않습니다.

### 로컬 파일 바로가기

다음 링크는 이 프로젝트의 로컬 폴더 구성을 기준으로 합니다. 가이드만 다른 프로젝트로 복사하면 사례 파일은 함께 제공되지 않습니다.

- [책 스킬](../.agents/skills/game-balance-bible/SKILL.md)
- [원문 페이지 지도와 추출 범위](../.agents/skills/game-balance-bible/references/source-map.md)
- [원문 재확인 감사 기록](../output/skill-review/source-recheck-audit.json)
- [과거 수치 감사 보고서](../output/skill-review/game-balance-bible-numeric-audit.json)
- [산술 검산 결과](../output/skill-review/numeric-regression-results.json)
- [과거 호스트 호환성 기록](../output/skill-review/multi-agent-compatibility.json)
- [Codex 실제 호출 기록](../output/skill-review/codex-host-smoke.json)
- [산술 검산 재현기](../output/skill-review/numeric_regression.py)

---

## 장별로 실무에 적용할 때

[장별 고급 활용법](advanced-usage.md)에 1~8장의 준비 데이터, 사용 전략, 복사할 요청, 산출물과 검수 기준을 정리했습니다. 전투·성장·경제를 함께 설계한다면 3장→4장→5장의 흐름부터 적용하고, 리듬 점검은 7장, 변경 영향 분석은 8장으로 이어갑니다.

---

## 스킬 근거를 보완할 때

책의 새 판본, 기획 메모, 추가 자료를 반영한다면 근거가 바뀐 장과 공식, 관련 색인, 영향받는 계산을 함께 다시 검수합니다. 파일을 늘리는 것만으로 끝내지 않고, 새 자료와 기존 지식의 충돌 및 적용 범위를 기록합니다. 현재 반영 범위와 남은 원문 확인 항목은 [책 내용과 레퍼런스 재검토](reference-review.md)를 참고합니다.

[← 이전: 문제 해결](troubleshooting.md)

---

[↑ 맨 위로](#document-top)
