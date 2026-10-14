# 릴리스 노트 작성과 GitHub Release 배포

이 폴더는 GitHub Release에 넣을 **공개 릴리스 노트 원고**를 관리합니다. 파일 자체가 자동으로 공개 배포되지는 않으며, 검토한 원고를 `gh release create`의 `--notes-file`로 명시했을 때만 GitHub Release 설명으로 게시됩니다.

## 파일 규칙

| 항목 | 규칙 |
|---|---|
| 파일명 | `yyyy-mm-dd-title.md` |
| 날짜 | KST 기준 작성일 |
| 제목 | 영문 소문자·숫자·하이픈(`kebab-case`) |
| 버전 | 파일명 날짜와 분리해 노트 본문에 `릴리스: <TAG>`로 표기 |
| 기준 원본 | [템플릿](_template.md)을 복사해 작성 |

> [!IMPORTANT]
> **릴리스 노트가 증명하지 않는 것**
>
> 노트에는 실제로 확인한 변경과 검증 범위만 적습니다. 문서 변경 노트는 런타임, 호스트 통합, 전체 수식 재검증을 수행했다는 뜻이 아닙니다.

## 배포 절차

1. `release/_template.md`를 복사해 KST 날짜와 영문 kebab-case 제목으로 저장합니다.
2. 노트의 `릴리스: <TAG>`와 `대상 커밋: <FULL_COMMIT_SHA>`를 확정합니다. 태그와 날짜는 서로 대체하지 않습니다.
3. 새 태그를 만들 때는 노트와 대상 커밋을 검토한 뒤 초안을 만듭니다. `--target`은 **태그가 아직 없을 때** 그 태그가 가리킬 전체 커밋 SHA를 정합니다.

```bash
gh release create TAG \
  --repo freelife1191/game-balance-bible \
  --target FULL_COMMIT_SHA \
  --title "TITLE" \
  --notes-file release/FILE \
  --draft
```

4. 이미 만든 태그를 대상으로 할 때는 `--target` 대신 `--verify-tag`를 사용합니다.

```bash
gh release create TAG \
  --repo freelife1191/game-balance-bible \
  --verify-tag \
  --title "TITLE" \
  --notes-file release/FILE \
  --draft
```

5. GitHub Release 페이지에서 태그, 제목, 노트, 대상 커밋이 의도한 값인지 확인한 뒤 공개합니다.

```bash
gh release edit TAG --repo freelife1191/game-balance-bible --draft=false
```

자세한 옵션은 GitHub CLI의 [release create](https://cli.github.com/manual/gh_release_create), [release edit](https://cli.github.com/manual/gh_release_edit) 문서를 확인합니다.

## 기존 릴리스에 본문 적용

기존 본문과 노트 파일을 비교한 후 적용합니다. 이 명령은 기존 본문 전체를 교체하며 공개 상태는 바꾸지 않습니다.

```bash
gh release edit TAG \
  --repo freelife1191/game-balance-bible \
  --notes-file release/FILE
```

> [!TIP]
> GitHub Release 화면에 붙일 노트는 문서 링크를 전체 GitHub URL로 적습니다. 특정 배포본에 고정하려면 해당 태그나 커밋 URL을 사용합니다. 노트 파일에 인증 값·원문 PDF·실행 로그를 넣지 않습니다.

## 현재 원고

- [2026-10-15 — documentation and release guide](2026-10-15-documentation-and-release-guide.md)

## 연결

[문서 홈](../docs/index.md) · [README](../README.md) · [GitHub Releases](https://github.com/freelife1191/game-balance-bible/releases)
