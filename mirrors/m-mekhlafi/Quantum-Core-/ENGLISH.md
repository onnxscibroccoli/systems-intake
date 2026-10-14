# English brief — m-mekhlafi/Quantum-Core-

Upstream: https://github.com/m-mekhlafi/Quantum-Core-
Fork: https://github.com/onnxscibroccoli/Quantum-Core-
License: Apache-2.0
Default branch: main
Upstream pushed: 2026-06-23T13:22:37Z
This file is an operator brief written for this account. It is not a substitute for the upstream license. Copyright stays with the upstream authors. Keep their notice if you copy their code.

## What it is

A small local assistant page: Whisper for speech-to-text, Ollama for the model, Kokoro for speech. Apache-2.0. The person runs all three on their own machine.

## Plain English

Already English. Useful as a reference wiring diagram, not as a dependency to vendor.

## Why it belongs here

Grasshopper tasks can call a local Ollama only when the machine has it. DECtalk remains the zero-download English voice. Kokoro is the higher-quality local voice when the person has installed it.

## Do not

Do not require a particular GPU. Do not hide a cloud key in the page.

## Integration

### Grasshopper

A task type local-model stores the endpoint as 127.0.0.1 and refuses any other host.

### dectalk-live

If Kokoro is absent, speak with DECtalk. Absence is a normal state, not an error to paper over.

### helix

The browser desktop can open this page on the local machine. It should not proxy the audio off the box.

## For someone else's agent stack

Bind the model, the recognizer, and the voice to localhost. Document the three ports. Another runtime can swap Ollama for a different local server if the contract stays host-local.

## Values

- Economic: run the work on hardware the person already has. Do not meter a local action.
- Community: leave the license and the authors' names in place so the next person can fork too.
- Disability: prefer the accessibility tree and a local voice over a screenshot sent to a vendor.
- Everyday: a person should be able to tell which step ran on their machine.

Values named for this upstream: everyday, economic, community.

## Translated passages

No non-English lines in the README checked this run.

## README checked

Characters read: 2502.
