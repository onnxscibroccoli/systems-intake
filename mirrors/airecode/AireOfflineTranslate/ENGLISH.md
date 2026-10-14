# English brief — airecode/AireOfflineTranslate

Upstream: https://github.com/airecode/AireOfflineTranslate
Fork: https://github.com/onnxscibroccoli/AireOfflineTranslate
License: Apache-2.0
Default branch: main
Upstream pushed: 2026-08-15T16:54:24Z
This file is an operator brief written for this account. It is not a substitute for the upstream license. Copyright stays with the upstream authors. Keep their notice if you copy their code.

## What it is

Face-to-face translation on an Android phone. Speech recognition, translation, and speech synthesis stay on the device after the model download. Apache-2.0.

## Plain English

Already English. The economic point is the same as DECtalk: once the model is local, a conversation is not a metered API call.

## Why it belongs here

DECtalk speaks English with a known voice and no download. AireOfflineTranslate covers the case where the other person speaks another language. They solve different sentences. Neither should upload the audio.

## Do not

Do not send the microphone stream to a cloud translator as a fallback without an on-screen switch the person can see.

## Integration

### dectalk-live

Keep DECtalk for short English prompts and confirmations. Link AireOfflineTranslate, do not embed its model, when the task is a two-language conversation.

### broccoli-core

A tick that needs a translation returns 'use the on-device translator' rather than calling a paid endpoint.

## For someone else's agent stack

Offer translate_local as a tool that fails closed when the model is not downloaded. Do not silently switch to a hosted model.

## Values

- Economic: run the work on hardware the person already has. Do not meter a local action.
- Community: leave the license and the authors' names in place so the next person can fork too.
- Disability: prefer the accessibility tree and a local voice over a screenshot sent to a vendor.
- Everyday: a person should be able to tell which step ran on their machine.

Values named for this upstream: disability, everyday, economic, community.

## Translated passages

No non-English lines in the README checked this run.

## README checked

Characters read: 15049.
