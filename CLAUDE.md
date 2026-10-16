# CLAUDE.md

This file gives Claude Code the repo-specific context it should not have to rediscover.

## Project

- - An online platform that caters to multiple hospitals, enabling efficient tracking, monitoring, and sharing of patient health records between themselves. Patients can access information on various hospitals and doctors, book appointments online, purchase medicines from an online pharmacy, pay for laboratory tests via an integrated payment gateway, and even chat with their appointed doctors. - Software Engineering Project - B.Sc. in Computer Science and Engineering (CSE).

## Package manager

- Use `npm` for this workspace. The lockfile is `package-lock.json`.
- Run package scripts with `npm run <script>`.

## Commands

```bash
npm run test         # run tests
```

No linter, formatter, test runner is configured.

## Architecture

- Project: healthstack-system-main.
- Package main: `index.js`.

## Testing and launch

- Test with `npm run test` (echo "Error: no test specified" && exit 1).

## Comment style

- Never place comments on the first two lines of a source file; start with imports or declarations.
- Prefer concise section headings such as `// ── Constants ──` or a three-line banner for major sections so files remain easy to scan.
- Use JSDoc blocks only when an API, intent, edge case, or constraint needs explanation; do not restate the code.

## Caveats

- No linter detected — no `lint` script, no ESLint config.
- No formatter detected — no Prettier config or format script.
- `node_modules/` is not listed in `.gitignore`.

## Boundaries

- Prefer existing local patterns and helper APIs before adding new abstractions.
- Keep generated, packaged, and runtime asset boundaries intact; do not move files across host/webview ownership without updating build and packaging config.

## Claude Code workflow

- For broad or uncertain changes, explore first and propose a plan before editing.
- Prefer focused verification commands while iterating, then run the full gate before finishing.
- Keep this file concise; move shared agent instructions to `AGENTS.md` if that file is added later.
