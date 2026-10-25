# English brief — autowarefoundation/auto_e2e

Upstream: https://github.com/autowarefoundation/auto_e2e
Fork: https://github.com/onnxscibroccoli/auto_e2e
License: Apache-2.0
Default branch: main
Upstream pushed: 2026-10-25T12:09:12Z
This file is an operator brief written for this account. It is not a substitute for the upstream license. Copyright stays with the upstream authors. Keep their notice if you copy their code.

## What it is

Camera-only driving model from the Autoware Foundation. The public checkpoint can run without an HD map. It is not a phone app.

## Plain English

Already English at the README. Treat it as a contract example: sensors in, a proposed path out, a person or a rule stack can reject the path.

## Why it belongs here

Grasshopper can record that shape of task (proposal, then veto) for any local model. The veto is the product. The network is not allowed to act alone.

## Do not

Do not claim this checkpoint runs in Termux. Do not connect it to a vehicle from this account. Respect the checkpoint's own notice on the model card.

## Integration

### Grasshopper

Model a task state machine: proposed, accepted, rejected. Store who accepted. A model task that skips accepted is a failed task.

## For someone else's agent stack

If you run your own camera model, publish the input size, the license, and the fact that a rule can override it. Do not hide the model behind a brand name.

## Values

- Economic: run the work on hardware the person already has. Do not meter a local action.
- Community: leave the license and the authors' names in place so the next person can fork too.
- Disability: prefer the accessibility tree and a local voice over a screenshot sent to a vendor.
- Everyday: a person should be able to tell which step ran on their machine.

Values named for this upstream: community, everyday.

## Translated passages

No non-English lines in the README checked this run.

## README checked

Characters read: 9713.
