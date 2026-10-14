# Systems intake

Daily fork-and-brief job for [onnxscibroccoli](https://github.com/onnxscibroccoli).

The digest explains the field. This repository does the work:

1. Read `intake/targets.json`. Every target has a permissive license that was checked (MIT, Apache-2.0, BSD, ISC, Unlicense, or CC0).
2. Fork it under this account if it is not already forked.
3. Write `intake/ENGLISH.md` on the fork: what the project is, what not to copy, and how it connects to the repositories this account already runs.
4. Keep the same brief in `mirrors/`.
5. Search public GitHub for accessibility, speech, and Shizuku-related tools. Record them in `catalog/latest.json`. Do not fork a search hit until a person adds it to the target list.
6. Publish the reading copy at the GitHub Pages site for this repo.

A second workflow, committed onto each fork, runs 30 minutes later and pulls the latest brief back onto the fork. Both workflows use the token of the repo they live in. No cloud desktop and no phone is required.

## Values

- **Economic.** Prefer a tool that runs on a phone or a browser the person already has over a metered API.
- **Community.** Leave the upstream copyright and license in place.
- **Disability.** Accessibility tree and local speech before a screenshot sent to a vendor. Do not disable a screen reader to make automation easier.
- **Everyday.** A person who does not work at a lab should be able to tell which step ran on their machine. Agent runtimes other than Grasshopper can use the same contracts. They are written in each brief under "For someone else's agent stack."

## What is not forked

AGPL tools, repos with no license file, surveillance-style globes, and exploit tools. Reasons are in `intake/targets.json` under `not_forked`.

## Secrets

The scheduled job runs without extra secrets. Two optional secrets make it stronger:

| Secret | Effect |
|---|---|
| `INTAKE_TOKEN` | A personal access token with `repo` and `workflow` scope, if the default token cannot create forks or push workflow files. |
| `XAI_API_KEY` | Translates non-English README lines. English upstreams do not need it. |

Do not put either secret in the repository.

## Run it once

GitHub Actions → daily-intake → Run workflow.

Or locally, with `gh` already logged in:

```bash
export GITHUB_TOKEN="$(gh auth token)"
export OWNER=onnxscibroccoli
python3 scripts/intake.py --fork --push-forks
```
