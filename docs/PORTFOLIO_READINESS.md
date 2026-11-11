# Portfolio reviewer readiness — systems-intake

**Focus:** Scheduled attribution-aware licensed source research  
**Current evidence status:** `AUTOMATION_CI_EXECUTED` (2026-11-11 snapshot; **not** production approval).  
**Tracking:** [repository issue](https://github.com/onnxscibroccoli/systems-intake/issues/1) · [portfolio master ledger](https://github.com/onnxscibroccoli/broccoli-core/issues/102)  


## Inspect actual source
- [scripts/intake.py](https://github.com/onnxscibroccoli/systems-intake/blob/main/scripts/intake.py)
- [intake/targets.json](https://github.com/onnxscibroccoli/systems-intake/blob/main/intake/targets.json)
- [README.md](https://github.com/onnxscibroccoli/systems-intake/blob/main/README.md)

**Scoped reference workflow run:** [Inspect the historical GitHub Actions result](https://github.com/onnxscibroccoli/systems-intake/actions/runs/43080175863). Verify its SHA/branch before attributing it to current source; CI success is not live/production evidence.

## First reviewer command (check prerequisites before executing)

```sh
python3 scripts/intake.py --help
```

This is a proposed reproduction command, **not a claim of executed testing**. Confirm the command exists in the current repository; record missing scripts/dependencies as NOT_VERIFIED rather than masking failures.

## Ordered implementation queue

1. [ ] Publish a short evidence trail from scheduled run to fork brief and source license.
2. [ ] Explain the default token cannot create new forks without additional explicit credentials.
3. [ ] Add deterministic negative tests for missing permission and stale metadata.
4. [ ] Separate new original integration notes from attributed upstream source.

## Evidence promotion gate

A project is not ready for a public professional demonstration merely because it has a README, an Actions schedule, or a test result unrelated to its claimed behavior. Provide exact source SHA, real test scope, negative controls, and meaningful limitations. Production or hardware assertions require an authorized real environment and appropriately scoped acceptance.

## Safe resumption

Inspect this issue and the master ledger, refresh the repo's `main` head and relevant PRs, implement the first unchecked item on a draft PR, attach exact test evidence and update the tracker. Avoid mass merging, secret exposure, false human review, and speculative employment claims.
