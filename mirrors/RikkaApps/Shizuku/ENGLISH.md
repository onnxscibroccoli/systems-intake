# English brief — RikkaApps/Shizuku

Upstream: https://github.com/RikkaApps/Shizuku
Fork: https://github.com/onnxscibroccoli/Shizuku
License: Apache-2.0
Default branch: master
Upstream pushed: 2025-06-18T04:21:02Z
This file is an operator brief written for this account. It is not a substitute for the upstream license. Copyright stays with the upstream authors. Keep their notice if you copy their code.

## What it is

Shizuku lets an ordinary Android app use ADB-level APIs through a small service the person starts themselves, instead of requiring root.

## Plain English

The upstream README is already English. This brief is the operator version: what to pin, what not to fork away from, and where broccoli-rish already depends on it.

## Why it belongs here

broccoli-rish is the transport. Shizuku is the privilege boundary. Keep them separate. The phone runs the command. A cloud agent only sends the text of the request.

## Do not

Do not hide the Shizuku start step. Do not ship a private fork that drifts from upstream security fixes. Do not use the API to click through another app's purchase screen.

## Integration

### broccoli-rish

Keep lib/rish_run.sh as the only wrapper. Record the upstream Shizuku release it was tested against in the brief's commit, not in a screenshot.

### broccoli-core

The kernel tick may call rish. It must not shell out to su. If Shizuku is not running, the tick returns a spoken and written 'not ready' instead of a fake success.

### dectalk-live

Speak that 'not ready' locally. Do not send the failure text to a paid voice API.

## For someone else's agent stack

Any agent runtime can use the same split. The agent emits a request. A local executor holding Shizuku permission runs it. The agent never receives a shell on the phone.

## Values

- Economic: run the work on hardware the person already has. Do not meter a local action.
- Community: leave the license and the authors' names in place so the next person can fork too.
- Disability: prefer the accessibility tree and a local voice over a screenshot sent to a vendor.
- Everyday: a person should be able to tell which step ran on their machine.

Values named for this upstream: everyday, disability, economic.

## Translated passages

No non-English lines in the README checked this run.

## README checked

Characters read: 5244.
