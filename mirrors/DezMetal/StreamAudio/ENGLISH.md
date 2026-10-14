# English brief — DezMetal/StreamAudio

Upstream: https://github.com/DezMetal/StreamAudio
Fork: https://github.com/onnxscibroccoli/StreamAudio
License: Apache-2.0
Default branch: main
Upstream pushed: 2026-09-21T14:59:44Z
This file is an operator brief written for this account. It is not a substitute for the upstream license. Copyright stays with the upstream authors. Keep their notice if you copy their code.

## What it is

A long-lived local text-to-speech daemon using Piper, so the first word is not waiting on a process start. Apache-2.0.

## Plain English

Already English. DECtalk is the in-browser voice with no install. StreamAudio is the desktop voice when someone wants a different speaker and can run a daemon.

## Why it belongs here

Grasshopper confirmations on a workstation can go to the daemon. Phone confirmations stay on DECtalk. Same sentence, two speakers, neither billed per character.

## Do not

Do not add a network listener on 0.0.0.0. The daemon binds to localhost.

## Integration

### Grasshopper

A notifier calls http://127.0.0.1 only. If the daemon is down, write the sentence to the task log and, on a phone path, hand it to DECtalk.

### dectalk-live

Do not replace the WASM voice. Offer StreamAudio as the workstation option in the docs, not as a hard dependency.

## For someone else's agent stack

A speak tool with a required host of 127.0.0.1. Other stacks can point that tool at Piper, DECtalk, or Kokoro. The model only passes text.

## Values

- Economic: run the work on hardware the person already has. Do not meter a local action.
- Community: leave the license and the authors' names in place so the next person can fork too.
- Disability: prefer the accessibility tree and a local voice over a screenshot sent to a vendor.
- Everyday: a person should be able to tell which step ran on their machine.

Values named for this upstream: disability, everyday, economic.

## Translated passages

No non-English lines in the README checked this run.

## README checked

Characters read: 9622.
