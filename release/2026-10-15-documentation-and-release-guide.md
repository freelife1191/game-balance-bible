# 문서 구성과 릴리스 노트 가이드

| 항목 | 값 |
|---|---|
| 작성일 (KST) | `2026-10-15` |
| 대상 | 스킬 사용자와 저장소 관리자 |

## 변경 사항

- README에 스킬의 범위, 설치·사용·문서·릴리스로 이어지는 빠른 탐색을 정리했습니다.
- 사용자 문서에 공통 탐색 링크를 추가하고, 긴 가이드의 기존 목차·접기 블록·앵커를 유지했습니다.
- GitHub Release에 넣을 노트 파일 규칙과 `gh release create` 절차를 추가했습니다.

## 검증

- Markdown 링크와 앵커를 로컬에서 검사했습니다.
- `git diff --check`로 공백 오류를 검사했습니다.

## 범위와 한계

- 이번 변경은 문서와 릴리스 노트 구조만 다룹니다.
- 런타임 동작, 호스트 통합, 전체 수식·원문 재검증은 이번 노트의 검증 범위가 아닙니다.

## 사용자 조치와 관련 문서

설치 경로·호출 방식·기존 지식 자료는 그대로 사용할 수 있습니다. 관리자는 다음 변경부터 날짜별 노트 파일을 작성하고, 배포할 태그와 커밋은 GitHub Release 설정에서 지정합니다.

- [프로젝트 소개](https://github.com/freelife1191/game-balance-bible/blob/main/README.md)
- [사용 가이드](https://github.com/freelife1191/game-balance-bible/blob/main/docs/index.md)
- [릴리스 가이드](https://github.com/freelife1191/game-balance-bible/blob/main/release/README.md)

노트 파일을 커밋·푸시해도 공개 GitHub Release나 새 태그는 자동 생성되지 않습니다.
