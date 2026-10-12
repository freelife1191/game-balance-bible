# 문제 해결

<a id="document-top"></a>

[문서 지도](index.md) · [README](../README.md)

> [!TIP]
> **문제가 난 단계를 먼저 구분합니다**
>
> 이 스킬의 문제는 보통 **인식**, **Claude Code 연결**, **파일 누락**, **장별 근거·계산**, **호스트 인증** 중 하나입니다. 해당 단계만 확인하면 원인을 빠르게 좁힐 수 있습니다.

**이 문서에서 찾기**

| 필요한 내용 | 바로가기 |
|---|---|
| 증상으로 찾기 | [이동](#symptoms) |
| 스킬 인식 확인 | [이동](#skill-discovery) |
| Claude Code 링크 확인 | [이동](#claude-link-check) |
| 파일 누락 확인 | [이동](#missing-files) |
| 장별 근거와 계산 검토 | [이동](#evidence-and-calculation) |
| 인증 문제 구분 | [이동](#authentication) |
| 문제 보고에 남길 정보 | [이동](#reporting) |

---

<a id="symptoms"></a>

## 증상으로 찾기

| 증상 | 먼저 확인할 것 | 이동 |
|---|---|---|
| 스킬이 목록에 없거나 호출되지 않음 | 프로젝트 위치·`SKILL.md` | [인식 확인](#skill-discovery) |
| Claude Code에서 이전 내용이 나옴 | 링크 대상·복사본 여부 | [Claude Code 링크](#claude-link-check) |
| 장별 답변이 지나치게 일반적임 | 8개 장 파일·관련 장 지정 | [파일 누락](#missing-files) |
| 수식이나 계산 결과가 기대와 다름 | 단위·조건·반올림·모델 | [근거와 계산](#evidence-and-calculation) |
| 도구 실행이 인증 오류로 멈춤 | 해당 호스트의 로그인 상태 | [인증](#authentication) |

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

명령이 실패했다면 기존 링크나 실재 디렉터리를 바로 덮어쓰지 않습니다. 먼저 그 위치의 내용과 소유자를 확인하고, 설치가 아직 없다면 [설치 가이드](setup.md#claude-link)의 안전한 링크 생성 명령을 사용합니다.

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
| 피해·방어·확률·성장 | ch03 | 속성 정의, 판정 순서, 반올림 위치 |
| 자원 생산·소비·가치 | ch04 | 기간, 초기 보유량, 공급·소비 루트 |
| 잔여 자원·전투·성장 검증 | ch05 | 비교 집단, 목표 지표, 측정 기간 |
| 결제 지표·충전·소비 | ch06 | 모집단, 집계 기간, 지표 정의 |
| 곡선과 단계 목표 | ch07 | 목표 경험, 구간, 달성 주기 |
| 시스템 연결과 영향 범위 | ch08 | 입력·출력, 바뀐 매개변수, 연결 모듈 |

읽을 파일이 불분명하면 [질문별 자료 지도](../.agents/skills/game-balance-bible/references/task-map.md)에서 관련 장·공식·입력 조건을 찾습니다.

계산 결과가 다르면 다음 순서로 다시 확인합니다.

1. `피해`, `초당 피해`, `턴 피해`처럼 단위가 섞이지 않았는지 확인합니다.
2. 공격력·방어력·확률 보정이 어느 순서로 적용되는지 고정합니다.
3. 치명·관통·회피처럼 여러 판정이 있을 때 순차 판정인지 확인합니다.
4. 표시값과 내부값의 반올림 위치, 처치 횟수의 올림 처리를 분리합니다.
5. 책의 예시 값과 현재 프로젝트 입력값을 구분하고, 불확실한 값은 가정으로 표시합니다.

원문 표와 재계산값이 다를 때는 [확인된 원문 불일치](../.agents/skills/game-balance-bible/references/source-map.md#추가로-확인한-원문-불일치와-적용-조건)를 먼저 봅니다. 화폐 단가, 현재/다음 레벨, 당일/누적량, 피해비율/생존비율을 같은 의미로 취급하지 않습니다. 산출식·선택 가중치·반올림이 원문에 없으면 임의로 채우지 않고 프로젝트 입력으로 정합니다.

> [!WARNING]
> **한 식을 모든 전투에 적용하지 않습니다**
>
> 스킬의 공식과 예시는 책의 모델과 전제를 따릅니다. 회복·보호막·행동 횟수·AI가 들어간 실제 전투에는 해당 조건을 추가로 모델링해야 합니다. 답변에는 사용한 가정과 검증 방법을 함께 요청합니다.

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

[← 설치와 호출](setup.md) · [다음: 고급 활용법](advanced-usage.md) →

---

[↑ 맨 위로](#document-top)
