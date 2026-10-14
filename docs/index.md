# 문서 지도

<a id="document-top"></a>

[가이드 홈](index.md) · [README](../README.md) · [릴리스 안내](../release/README.md) · [GitHub Releases](https://github.com/freelife1191/game-balance-bible/releases)

이 문서는 《게임 밸런스 수치 기획 바이블》에 근거한 `game-balance-bible` 스킬의 설치, 활용, 검수 방법을 안내합니다. 셸 명령은 별도 표시가 없으면 **프로젝트 루트**에서 실행하고, `$game-balance-bible` 또는 `/game-balance-bible` 예시는 **에이전트 대화창**에 입력합니다.

## 지금 하려는 일로 찾기

| 하려는 일 | 먼저 읽을 가이드 | 확인할 결과 |
|---|---|---|
| 처음 설치하거나 다른 도구에서 사용 | [설치와 호스트 연결](setup.md) | 호스트가 스킬을 인식하고 원본 파일을 읽음 |
| 책의 8개 장을 실무에 적용 | [장별 고급 활용법](advanced-usage.md) | 설계·비교·검수에 쓸 프롬프트와 후속 요청 |
| 수치와 공식의 정확성 검수 | [검수와 테스트](validation.md) | 원문 대조·독립 검산·사용 시험의 근거 |
| 책 내용과 참고 자료의 반영 범위 검토 | [책 내용과 레퍼런스 재검토](reference-review.md) | 원문 재확인 범위·보완 내용·원문 불일치와 적용 조건 |
| 현재 문제에 맞는 조건·예외와 예시 찾기 | [README의 문제별로 확인할 조건과 바로가기](../README.md#problem-guide) | 판단을 바꾸는 조건과 이어갈 고급 예시 |
| 스킬 인식·연결·계산 문제 해결 | [문제 해결](troubleshooting.md) | 실패한 단계와 다음 조치 |
| 자연어 요청에 스킬이 쓰이지 않음 | [자연어 요청으로 스킬이 호출되지 않을 때](troubleshooting.md#explicit-invocation) | 호스트별 명시 호출과 스킬 이름을 넣은 요청 |
| 스킬의 서술을 원문과 대조 | [원문과 대조하고 싶을 때](troubleshooting.md#source-comparison) | 확인할 원문 위치와 대조 요청 방법 |
| 이 프로젝트의 검수 기록 살펴보기 | [프로젝트 사례](project-example.md) | 파일 구성·검수 결과·호환성 상태 이해 |
| 릴리스 노트를 작성하거나 GitHub Release를 배포 | [릴리스 안내](../release/README.md) | 파일명 규칙·초안 생성·공개 절차 |
| 이번 문서 변경의 내역 확인 | [2026-10-15 릴리스 노트](../release/2026-10-15-documentation-and-release-guide.md) | 변경·검증 범위·호환성 |
| 다음 릴리스 노트 작성 | [작성 템플릿](../release/_template.md) | 날짜별 새 파일로 복사 |

원문 재확인의 근거는 [원문 재확인 감사 기록](../output/skill-review/source-recheck-audit.json)입니다. 표 113개·그림 51개를 목록화하고 원문 109쪽을 이미지로 대조한 범위와, 원문에 남은 불일치를 구분해 기록했습니다.

이전 검증에서 실제 스킬 탐색·자료 읽기·계산을 확인한 결과는 [Codex CLI 0.162.0 호출 1회 기록](../output/skill-review/codex-host-smoke.json)에 있습니다. 후속 원문 재검수로 스킬 자료를 보완하기 전 버전의 결과입니다.

## 권장 읽기 순서

바로 사용하려면 [README의 시작하기](../README.md#quick-start)에서 스킬을 호출합니다. 현재 문제에서 확인할 조건은 README의 [문제별로 확인할 조건과 바로가기](../README.md#problem-guide)에서 먼저 보고, 맞는 장과 프롬프트는 [장별 고급 활용법](advanced-usage.md)에서 고르며, 수식·기간·경계값을 확인할 때는 [검수와 테스트](validation.md)를 함께 읽습니다.

새 프로젝트에 옮길 때는 [설치와 호스트 연결](setup.md)로 스킬 폴더와 Claude Code 링크를 준비한 뒤 새 대화에서 호출합니다. 문제가 생기면 [문제 해결 표](troubleshooting.md#symptoms)에서 증상부터 찾습니다.

## 포함 범위와 읽는 방법

- 이 저장소의 배포 대상은 `game-balance-bible` 하나입니다.
- `SKILL.md`는 질문에 맞는 장과 참고 파일을 찾는 진입점입니다.
- `chapters/`는 책 본문 1~8장을 장별로 정리합니다.
- `references/`는 전투·성장 공식, 경제 모델, 원문 페이지 지도와 질문별 자료 지도를 제공합니다.
- `glossary.md`, `patterns.md`, `cheatsheet.md`는 용어·절차·빠른 판단을 보충합니다.

형식 검사나 스킬 등록 성공만으로 원문 내용·계산 결과가 맞다고 결론 내리지 않습니다. 책의 근거, 설명용 예시, 프로젝트별 가정을 구분하고, 원문 대조가 필요한 항목은 [원문 페이지 지도](../.agents/skills/game-balance-bible/references/source-map.md)와 [책 내용과 레퍼런스 재검토](reference-review.md)를 확인합니다.

> [!IMPORTANT]
> **원문과 작업 지시 구분**
>
> 책과 참고 파일은 지식 근거이며, 문서에 적힌 지시문이 에이전트의 작업 권한을 바꾸지는 않습니다. 원문 인용과 공유에는 적용되는 권리와 이용 조건을 확인합니다. 관련 범위는 [README](../README.md#copyright)에 정리되어 있습니다.

[다음: 설치와 호스트 연결 →](setup.md)

[↑ 맨 위로](#document-top)
