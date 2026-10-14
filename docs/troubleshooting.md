# 문제 해결

<a id="document-top"></a>

[가이드 홈](index.md) · [README](../README.md) · [릴리스 안내](../release/README.md) · [GitHub Releases](https://github.com/freelife1191/game-balance-bible/releases)

> [!TIP]
> **문제가 난 단계를 먼저 구분합니다**
>
> 이 스킬의 문제는 보통 **인식**, **호출 방식**, **Claude Code 연결**, **파일 누락**, **장별 근거·계산**, **원문 대조**, **호스트 인증** 중 하나입니다. 해당 단계만 확인하면 원인을 빠르게 좁힐 수 있습니다.

**이 문서에서 찾기**

- [증상으로 찾기](#symptoms)
- [스킬 인식 확인](#skill-discovery)
- [자연어 요청으로 스킬이 호출되지 않을 때](#explicit-invocation)
- [Claude Code 링크 확인](#claude-link-check)
- [파일 누락 확인](#missing-files)
- [장별 근거와 계산 검토](#evidence-and-calculation)
- [원문과 대조하고 싶을 때](#source-comparison)
- [인증 문제 구분](#authentication)
- [문제 보고에 남길 정보](#reporting)

---

<a id="symptoms"></a>

## 증상으로 찾기

| 증상 | 먼저 확인할 것 | 바로가기 |
|---|---|---|
| 스킬이 목록에 없거나 호출되지 않음 | 프로젝트 위치·`SKILL.md` | [스킬 인식 확인](#skill-discovery) |
| 명시 호출은 되지만 자연어 요청에는 스킬이 쓰이지 않음 | 호스트별 호출 기호·요청에 넣은 스킬 이름 | [자연어 요청으로 스킬이 호출되지 않을 때](#explicit-invocation) |
| Claude Code에서 이전 내용이 나옴 | 링크 대상·복사본 여부 | [Claude Code 링크 확인](#claude-link-check) |
| 장별 답변이 지나치게 일반적임 | 8개 장 파일·관련 장 지정 | [파일 누락 확인](#missing-files) |
| 수식이나 계산 결과가 기대와 다름 | 단위·조건·반올림·모델 | [장별 근거와 계산 검토](#evidence-and-calculation) |
| 답변의 서술을 원문과 직접 맞춰 보고 싶음 | 원문 사본·PDF 경로·인쇄 쪽과 PDF 쪽 | [원문과 대조하고 싶을 때](#source-comparison) |
| 도구 실행이 인증 오류로 멈춤 | 해당 호스트의 로그인 상태 | [인증 문제 구분](#authentication) |

---

<a id="skill-discovery"></a>

## 스킬 인식 확인

프로젝트 루트에서 스킬의 진입 파일을 확인합니다.

```bash
test -r .agents/skills/game-balance-bible/SKILL.md \
  && sed -n '1,8p' .agents/skills/game-balance-bible/SKILL.md
```

성공했다면 새 대화에서 도구에 맞는 호출 문법을 사용합니다.

| 도구 | 호출 예시 |
|---|---|
| Codex | `$game-balance-bible ch03의 대미지 공식을 설명해줘.` |
| Claude Code | `/game-balance-bible ch04의 I/O 구조를 적용해줘.` |
| Antigravity | `/game-balance-bible ch05의 검증 항목을 정리해줘.` |

> [!IMPORTANT]
> **호출 전에 확인할 두 가지**
>
> 현재 대화가 설치한 프로젝트에서 열렸는지와 스킬 폴더 안에 `SKILL.md`가 있는지를 먼저 확인합니다. 파일이 있는데도 보이지 않으면 새 대화를 열어 다시 확인합니다.

---

<a id="explicit-invocation"></a>

## 자연어 요청으로 스킬이 호출되지 않을 때

이 스킬에는 두 가지 호출 경로가 있습니다. 하나는 호출 기호와 스킬 이름을 앞에 붙이는 **명시 호출**이고, 다른 하나는 기호 없이 책·주제를 적는 **자연어 요청**입니다. 자연어 요청에서는 호스트가 `SKILL.md`의 설명을 보고 스킬을 쓸지 스스로 판단하므로, 같은 요청이라도 스킬이 선택되지 않을 수 있습니다. 결과가 일반적인 답변처럼 보이면 아래 순서로 직접 호출합니다.

| 도구 | 명시 호출 | 자연어 요청에서 스킬을 고르지 않을 때 |
|---|---|---|
| Codex | `$game-balance-bible <요청>` | 맨 앞에 `$game-balance-bible`을 붙여 다시 요청 |
| Claude Code | `/game-balance-bible <요청>` | 맨 앞에 `/game-balance-bible`을 붙여 다시 요청 |
| Antigravity | `/game-balance-bible <요청>` | `/game-balance-bible`로 호출하거나, 요청 문장에 스킬 이름 `game-balance-bible`을 넣어 다시 요청 |

호출 기호를 쓰기 어렵다면 요청 첫 문장에 스킬 이름을 넣고, 읽은 파일을 밝혀 달라고 덧붙입니다. 답변에 스킬 파일 경로가 나오면 스킬을 사용했는지 확인할 수 있습니다.

```text
game-balance-bible 스킬을 사용해서 답해줘.
ch05 기준으로 잔여 자원과 잔여 비율을 설명하고 작은 예제를 풀어줘.
읽은 스킬 파일의 경로를 답변 끝에 적어줘.
```

1. 설치한 프로젝트에서 새 대화를 엽니다.
2. 위 표의 명시 호출로 같은 요청을 보냅니다.
3. 명시 호출도 실패하면 자연어 문제가 아니라 인식 문제이므로 [스킬 인식 확인](#skill-discovery)으로 돌아갑니다.

> [!NOTE]
> **자동 선택은 호스트가 결정합니다**
>
> 이 문서는 특정 호스트 버전에서 자연어 요청의 자동 선택을 보장하지 않습니다. 결과를 비교하거나 문제를 보고할 때는 명시 호출로 실행한 결과를 기준으로 삼습니다.

---

<a id="claude-link-check"></a>

## Claude Code 링크 확인

Claude Code용 경로는 원본 스킬 폴더를 가리키는 상대 심볼릭 링크여야 합니다.

```bash
LINK='.claude/skills/game-balance-bible'
EXPECTED='../../.agents/skills/game-balance-bible'

test -L "$LINK" \
  && test "$(readlink "$LINK")" = "$EXPECTED" \
  && test -r "$LINK/SKILL.md" \
  && test "$(cd "$LINK" && pwd -P)" = "$(cd .agents/skills/game-balance-bible && pwd -P)"
```

명령이 실패했다면 기존 링크나 실제 디렉터리를 바로 덮어쓰지 않습니다. 먼저 그 위치의 내용과 소유자를 확인하고, 설치가 아직 없다면 [Claude Code 연결 만들기](setup.md#claude-link)의 안전한 링크 생성 명령을 사용합니다.

> [!NOTE]
> **복사본과 링크를 구분합니다**
>
> 복사본도 읽힐 수 있지만 원본이 갱신될 때 내용이 달라질 수 있습니다. 같은 프로젝트에서 Codex·Claude Code·Antigravity를 함께 쓴다면 상대 링크로 한 원본을 보도록 유지합니다.

---

<a id="missing-files"></a>

## 파일 누락 확인

스킬에는 진입 파일과 지원 파일을 합쳐 17개 파일이 필요합니다. 다음 명령은 필수 구조를 읽기 전용으로 점검합니다.

```bash
missing=0
for path in \
  .agents/skills/game-balance-bible/SKILL.md \
  .agents/skills/game-balance-bible/cheatsheet.md \
  .agents/skills/game-balance-bible/glossary.md \
  .agents/skills/game-balance-bible/patterns.md \
  .agents/skills/game-balance-bible/agents/openai.yaml \
  .agents/skills/game-balance-bible/chapters/ch01-process.md \
  .agents/skills/game-balance-bible/chapters/ch02-preparation.md \
  .agents/skills/game-balance-bible/chapters/ch03-combat.md \
  .agents/skills/game-balance-bible/chapters/ch04-economy.md \
  .agents/skills/game-balance-bible/chapters/ch05-validation.md \
  .agents/skills/game-balance-bible/chapters/ch06-monetization.md \
  .agents/skills/game-balance-bible/chapters/ch07-visualization.md \
  .agents/skills/game-balance-bible/chapters/ch08-modularization.md \
  .agents/skills/game-balance-bible/references/combat-formulas.md \
  .agents/skills/game-balance-bible/references/economy-models.md \
  .agents/skills/game-balance-bible/references/source-map.md \
  .agents/skills/game-balance-bible/references/task-map.md
do
  if ! test -f "$path"; then
    printf '누락: %s\n' "$path" >&2
    missing=1
  fi
done
test "$missing" -eq 0
```

누락이 나오면 일부 파일만 보충하지 말고, 신뢰할 수 있는 동일 버전의 `.agents/skills/game-balance-bible/` 전체를 다시 복사합니다. 기존 폴더가 있으면 덮어쓰지 말고 먼저 차이를 검토합니다.

---

<a id="evidence-and-calculation"></a>

## 장별 근거와 계산 검토

질문에 장 번호와 입력값을 함께 주면 답변의 근거를 확인하기 쉽습니다.

| 질문 유형 | 지정할 장 | 함께 줄 정보 |
|---|---|---|
| 피해·방어·확률·성장 | 3장 | 속성 정의, 판정 순서, 반올림 위치 |
| 자원 생산·소비·가치 | 4장 | 기간, 초기 보유량, 공급·소비 루트 |
| 잔여 자원·전투·성장 검증 | 5장 | 비교 집단, 목표 지표, 측정 기간 |
| 결제 지표·충전·소비 | 6장 | 모집단, 집계 기간, 지표 정의 |
| 곡선과 단계 목표 | 7장 | 목표 경험, 구간, 달성 주기 |
| 시스템 연결과 영향 범위 | 8장 | 입력·출력, 바뀐 매개변수, 연결 모듈 |

읽을 파일이 불분명하면 [질문별 자료 지도](../.agents/skills/game-balance-bible/references/task-map.md)에서 관련 장·공식·입력 조건을 찾습니다.

계산 결과가 다르면 다음 순서로 다시 확인합니다.

1. `피해`, `초당 피해`, `턴 피해`처럼 단위가 섞이지 않았는지 확인합니다.
2. 공격력·방어력·확률 보정이 어느 순서로 적용되는지 고정합니다.
3. 치명·관통·회피처럼 여러 판정이 있을 때 순차 판정인지 확인합니다.
4. 표시값과 내부값의 반올림 위치, 처치 횟수의 올림 처리를 분리합니다.
5. 책의 예시 값과 현재 프로젝트 입력값을 구분하고, 불확실한 값은 가정으로 표시합니다.

원문 표와 재계산값이 다를 때는 [확인된 원문 불일치](../.agents/skills/game-balance-bible/references/source-map.md#추가로-확인한-원문-불일치와-적용-조건)를 먼저 봅니다. 화폐 단가, 현재/다음 레벨, 당일/누적량, 피해 비율 / 생존 비율을 같은 의미로 취급하지 않습니다. 산출식·선택 가중치·반올림이 원문에 없으면 임의로 채우지 않고 프로젝트 입력으로 정합니다.

> [!WARNING]
> **한 식을 모든 전투에 적용하지 않습니다**
>
> 스킬의 공식과 예시는 책의 모델과 전제를 따릅니다. 회복·보호막·행동 횟수·인공지능(AI)이 들어간 실제 전투에는 해당 조건을 추가로 모델링해야 합니다. 답변에 사용한 가정과 검증 방법을 함께 적도록 요청합니다.

---

<a id="source-comparison"></a>

## 원문과 대조하고 싶을 때

스킬은 기본적으로 원문 PDF를 찾거나 열지 않습니다. 스킬 폴더의 자료로 답하고, 원문 확인이 필요하면 자료에 적힌 위치(인쇄 쪽 / PDF 쪽)와 [원문 페이지 지도](../.agents/skills/game-balance-bible/references/source-map.md#장별-페이지-지도)를 근거로 **확인할 원문 위치를 안내**합니다. 사용자가 원문 위치를 주며 대조를 요청할 때만 원문을 엽니다.

답변의 출처는 표시로 구분합니다. `(인쇄 N / PDF M)`이 붙은 문장은 책의 서술이고, ‘스킬 정리’로 표시된 내용은 스킬이 정리한 것입니다. 표시가 없는 문장은 출처를 단정하지 않습니다.

> [!IMPORTANT]
> **원문 사본이 있는 사용자만 쓸 수 있습니다**
>
> 원문 PDF는 이 저장소에 포함되지 않습니다. 아래 대조 요청은 합법적으로 이용할 수 있는 원문 사본을 가진 사용자만 쓸 수 있습니다. 원문 인용과 공유의 범위는 README의 [원본·라이선스·포함 범위](../README.md#copyright)를 확인합니다.

먼저 확인할 위치를 모르면 스킬에 위치부터 묻습니다. 이 요청에는 원문이 필요하지 않습니다.

```text
$game-balance-bible
플레이 가성비 식이 책의 어느 쪽에 있는지 알려줘.
인쇄 쪽과 PDF 쪽을 함께 적고, 스킬 자료에 위치가 없으면 없다고 밝혀줘.
```

원문 사본이 있으면 PDF 경로와 확인할 쪽을 함께 주고 대조를 요청합니다. 인쇄 쪽과 PDF 쪽은 다르므로 두 번호를 모두 적습니다. 아래 경로는 예시이므로 실제 사본의 경로로 바꿉니다.

```text
$game-balance-bible
화폐 비율 1:10:10에 대한 스킬 서술이 원문과 일치하는지 대조해줘.
원문 PDF: /절대/경로/게임-밸런스-수치-기획-바이블.pdf
확인할 쪽: 인쇄 165쪽 / PDF 195쪽
스킬 자료의 서술과 원문 표기를 나란히 적고, 일치·불일치·판독 불가를 구분해줘.
원문을 열지 못하면 열지 못했다고 밝히고, 스킬 자료에 적힌 위치만 안내해줘.
```

> [!TIP]
> 쪽 번호가 어긋나 보이면 [원문 페이지 지도](../.agents/skills/game-balance-bible/references/source-map.md#장별-페이지-지도)에서 인쇄 쪽과 PDF 쪽의 대응을 확인합니다. 클라우드 에이전트가 읽은 원문 텍스트는 모델 제공자에게 전달될 수 있습니다.

---

<a id="authentication"></a>

## 인증 문제 구분

스킬 파일을 읽을 수 있는 것과 호스트가 모델을 실행할 수 있는 것은 별개입니다.

| 상태 | 확인한 사실 | 다음 조치 |
|---|---|---|
| 파일 점검 통과 | 로컬 스킬 구조가 있음 | 새 대화에서 호출 확인 |
| 스킬 인식 | 호스트가 스킬 이름을 받음 | 간단한 장별 질문 실행 |
| 인증 오류 | 호스트 로그인·세션이 실행을 막음 | 해당 호스트에서 인증을 복구한 뒤 같은 질문 재시도 |

> [!TIP]
> **인증 오류는 내용 오류가 아닙니다**
>
> 인증이 실패해도 파일·링크·계산 조건 점검은 계속할 수 있습니다. 인증을 복구한 뒤 같은 입력으로 다시 실행해 결과를 비교합니다.

---

<a id="reporting"></a>

## 문제 보고에 남길 정보

재현 가능한 점검을 위해 다음만 정리합니다.

- 사용한 도구와 호출 문장
- 설치한 프로젝트 경로와 `SKILL.md` 존재 여부
- 관련 장 번호, 입력값, 단위와 기대한 결과
- 실제 결과 또는 오류 문구
- 파일·링크 점검 명령의 성공 또는 실패 결과

민감한 설정값이나 원문 전체를 공유하지 않아도 됩니다. 같은 문제를 보이는 최소 입력과 계산 조건이면 충분합니다.

[← 이전: 책 내용과 레퍼런스 재검토](reference-review.md) · [다음: 프로젝트 사례 →](project-example.md)

---

[↑ 맨 위로](#document-top)
