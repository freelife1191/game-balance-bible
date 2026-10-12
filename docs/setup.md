# 설치와 도구별 호출

<a id="document-top"></a>

[문서 지도](index.md) · [README](../README.md)

> [!TIP]
> **가장 빠른 시작**
>
> 이 저장소에는 `game-balance-bible` 스킬 하나만 포함됩니다. 저장소를 설치한 뒤 새 대화에서 스킬을 호출하면, 기본적인 학습·설계·계산 질문에는 원문 PDF나 Python이 필요하지 않습니다.

**이 문서에서 찾기**

| 필요한 내용 | 바로가기 |
|---|---|
| 포함된 스킬과 파일 | [이동](#current-state) |
| 기존 프로젝트에 설치하기 | [이동](#install-game-balance-skill) |
| 설치 대상 고르기 | [이동](#choose-target) |
| Codex에서 호출하기 | [이동](#codex) |
| Claude Code와 Antigravity에서 호출하기 | [이동](#claude-antigravity) |
| Claude Code 연결 만들기 | [이동](#claude-link) |
| 설치·호출 성공 조건 | [이동](#success) |
| 자주 묻는 질문 | [이동](#faq) |

---

<a id="current-state"></a>

## 포함된 스킬과 파일

프로젝트 루트의 배포 대상은 다음 한 스킬입니다.

```text
<project-root>/
├── .agents/skills/game-balance-bible/  # 스킬 본문과 지식 파일 17개
└── .claude/skills/game-balance-bible/  # Claude Code용 상대 심볼릭 링크
```

`.agents/skills/game-balance-bible/`에는 `SKILL.md`, 8개 장 파일, 용어·패턴·요약 파일과 전투·경제·출처·질문별 자료 참고 파일이 들어 있습니다. 이 폴더 전체를 복사해야 장별 답변과 수식 근거를 함께 사용할 수 있습니다.

아래 셸 명령은 **설치할 프로젝트의 루트**에서 실행합니다. 대화창에 입력하는 스킬 호출 예시와 구별해 사용합니다.

---

<a id="install-game-balance-skill"></a>

## 기존 프로젝트에 설치하기

먼저 이 저장소를 내려받거나 복제합니다. 전체 프로젝트를 사용하려면 [README의 설치 안내](../README.md#installation)를 따릅니다. 기존 프로젝트에는 아래처럼 스킬 폴더 하나만 복사할 수 있습니다.

`GAME_BALANCE_SKILL_SOURCE`를 내려받은 이 저장소의 실제 절대 경로로 바꿉니다. 대상에 기존 파일이나 링크가 있으면 **아무것도 덮어쓰지 않고 중단**합니다.

```bash
GAME_BALANCE_SKILL_SOURCE='/절대/경로/game-balance-bible' python3 - <<'PY'
import os
from pathlib import Path
import shutil

source = Path(os.environ['GAME_BALANCE_SKILL_SOURCE']).expanduser().resolve()
original = source / '.agents/skills/game-balance-bible'
target = Path('.agents/skills/game-balance-bible')
claude_link = Path('.claude/skills/game-balance-bible')

if not (original / 'SKILL.md').is_file():
    raise SystemExit(f'스킬 원본을 찾을 수 없습니다: {original}')
for path in (target, claude_link):
    if path.exists() or path.is_symlink():
        raise SystemExit(f'기존 설치가 있습니다. 덮어쓰지 않습니다: {path}')

target.parent.mkdir(parents=True, exist_ok=True)
claude_link.parent.mkdir(parents=True, exist_ok=True)
shutil.copytree(original, target, ignore=shutil.ignore_patterns('.git'))
claude_link.symlink_to('../../.agents/skills/game-balance-bible', target_is_directory=True)

if not (target / 'SKILL.md').is_file():
    raise SystemExit('복사 후 SKILL.md를 읽을 수 없습니다.')
if claude_link.resolve() != target.resolve():
    raise SystemExit('Claude Code 링크 대상이 스킬 원본과 다릅니다.')
print('설치 및 Claude Code 링크 확인 완료')
PY
```

> [!IMPORTANT]
> **복사 대상은 스킬 폴더 전체입니다**
>
> `SKILL.md`만 복사하면 장별 지식 파일과 수식 참고가 빠집니다. 위 명령은 `.git`을 제외하고 스킬 폴더 전체를 복사하므로, 설치하는 프로젝트에 중첩 Git 저장소가 생기지 않습니다.

Python을 쓰지 않으려면 파일 탐색기나 셸의 복사 기능으로 `.agents/skills/game-balance-bible/` 전체를 같은 경로에 복사한 다음, [Claude Code 연결](#claude-link)만 별도로 만듭니다.

---

<a id="choose-target"></a>

## 설치 대상 고르기

| 목적 | 필요한 경로 | 호출 위치 |
|---|---|---|
| Codex와 Antigravity에서 사용 | `.agents/skills/game-balance-bible/` | 프로젝트 루트 |
| Claude Code에서도 함께 사용 | 위 경로 + `.claude/skills/game-balance-bible` 링크 | 프로젝트 루트 |

세 도구를 같은 프로젝트에서 쓴다면 두 경로를 함께 준비합니다. Claude Code 링크는 원본을 복제하지 않고 `.agents/skills`의 스킬을 가리키므로, 내용이 한 곳에서 일관되게 유지됩니다.

---

<a id="codex"></a>

## Codex에서 호출하기

Codex 대화에서 다음처럼 명시적으로 호출합니다.

```text
$game-balance-bible 전투력 1,000인 두 직업의 승률이 다른 이유를 점검해줘.
가정, 비교 지표, 검증 순서도 함께 제시해줘.
```

장별 학습에는 장 번호를 함께 지정하면 됩니다.

```text
$game-balance-bible ch04의 I/O 구조로 강화석의 생산·소비 구조를 설계해줘.
필요한 입력값과 검증할 잔여 자원 지표를 표로 정리해줘.
```

---

<a id="claude-antigravity"></a>

## Claude Code와 Antigravity에서 호출하기

Claude Code와 Antigravity 대화에서는 슬래시 호출을 사용합니다.

```text
/game-balance-bible HP 1,000, 실제 피해 50, 공격 속도 초당 2회일 때
처치 횟수와 첫 타격 시점 0초 기준 처치 시간을 계산하고 가정을 밝혀줘.
```

장별 참고도 같은 이름으로 호출합니다.

```text
/game-balance-bible ch06 기준으로 결제율, ARPPU, ARPU를 함께 볼 때의
검증 질문과 해석상 주의점을 정리해줘.
```

Antigravity는 `.agents/skills/game-balance-bible/`을 사용합니다. Claude Code는 `.claude/skills/game-balance-bible/` 링크를 사용합니다. 설치 후에는 새 대화에서 호출해 인식을 확인합니다.

---

<a id="claude-link"></a>

## Claude Code 연결 만들기

다음은 프로젝트 루트에서 실행하는 명령입니다. 기존 파일이나 링크가 있으면 중단하므로 실재 디렉터리를 덮어쓰지 않습니다.

```bash
LINK='.claude/skills/game-balance-bible'
TARGET='../../.agents/skills/game-balance-bible'

mkdir -p .claude/skills
if [ -e "$LINK" ] || [ -L "$LINK" ]; then
  printf '중단: 기존 파일 또는 링크가 있습니다: %s\n' "$LINK" >&2
  exit 1
fi

ln -s "$TARGET" "$LINK"
test -L "$LINK" \
  && test "$(readlink "$LINK")" = "$TARGET" \
  && test -r "$LINK/SKILL.md"
```

> [!WARNING]
> **기존 디렉터리는 먼저 검토합니다**
>
> `.claude/skills/game-balance-bible`가 실재 디렉터리라면 자동으로 바꾸지 않습니다. 기존 내용과 소유자를 확인한 뒤, 필요한 경우 별도 이관 절차를 정합니다.

---

<a id="success"></a>

## 설치·호출 성공 조건

다음 체크를 순서대로 통과하면 설치를 확인할 수 있습니다.

- [ ] `.agents/skills/game-balance-bible/SKILL.md`를 읽을 수 있다.
- [ ] Claude Code를 쓴다면 `.claude/skills/game-balance-bible/SKILL.md`도 읽을 수 있다.
- [ ] 새 대화에서 해당 도구의 호출 문법으로 `game-balance-bible`을 인식한다.
- [ ] 기본 질문에 장별 개념, 가정, 계산 절차가 포함된 답을 받는다.

> [!NOTE]
> **기본 사용에 필요한 것**
>
> 포함된 스킬을 쓰는 데는 원문 PDF나 Python 환경이 필요하지 않습니다. Python은 위의 안전한 폴더 복사 명령을 사용할 때만 선택적으로 필요합니다.

---

<a id="faq"></a>

## 자주 묻는 질문

### 설치 뒤 스킬이 보이지 않아요

현재 대화의 작업 위치가 설치한 프로젝트인지, `SKILL.md`가 위 경로에 있는지 확인한 후 새 대화를 엽니다. 계속 보이지 않으면 [문제 해결](troubleshooting.md#symptoms)의 인식 점검을 따릅니다.

### 원문 PDF나 Python이 있어야 하나요

아니요. 포함된 장·참고 파일을 바탕으로 질문하고 계산을 검토하는 기본 사용에는 필요하지 않습니다. Python은 설치 폴더를 안전하게 복사하는 방법 중 하나입니다.

### 새 프로젝트에 어떤 파일을 올려야 하나요

`.agents/skills/game-balance-bible/`의 17개 파일 전체와, Claude Code 지원이 필요하면 `.claude/skills/game-balance-bible` 상대 링크를 함께 올립니다.

[← README](../README.md) · [다음: 고급 활용법](advanced-usage.md) →

---

[↑ 맨 위로](#document-top)
