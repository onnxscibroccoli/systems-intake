# English brief — trypsynth/nvgt-bridge

Upstream: https://github.com/trypsynth/nvgt-bridge
Fork: https://github.com/onnxscibroccoli/nvgt-bridge
License: MIT
Default branch: master
Upstream pushed: 2026-10-06T16:47:22Z
This file is an operator brief written for this account. It is not a substitute for the upstream license. Copyright stays with the upstream authors. Keep their notice if you copy their code.

## What it is

A small Kotlin accessibility service that gives an audio game direct touch while TalkBack keeps menus, dialogs, and the keyboard.

## Plain English

Already English. The pattern matters more than the game: one channel for the screen reader, a different channel for the single gesture the person asked for.

## Why it belongs here

Broccoli should observe the accessibility tree and leave TalkBack in charge of system UI. Grabbing the whole screen is how automation breaks a blind user's phone.

## Do not

Do not disable TalkBack. Do not read notification text off the device to a remote model.

## Integration

### broccoli-core

Prefer accessibility-node actions (click a labeled node) over coordinates. If TalkBack is on, do not steal focus from it except for the node named in the request.

### dectalk-live

DECtalk is an extra voice for app results. It is not a replacement for the system screen reader.

### newsroom-desk

When a story is about background control of a phone, this bridge is the counter-example: the user can tell which layer has the gesture.

## For someone else's agent stack

Expose two tools to the model: speak_result and activate_labeled_node. Do not expose a raw swipe-anywhere tool when a screen reader is on.

## Values

- Economic: run the work on hardware the person already has. Do not meter a local action.
- Community: leave the license and the authors' names in place so the next person can fork too.
- Disability: prefer the accessibility tree and a local voice over a screenshot sent to a vendor.
- Everyday: a person should be able to tell which step ran on their machine.

Values named for this upstream: disability, everyday, community.

## Translated passages

No non-English lines in the README checked this run.

## README checked

Characters read: 4193.
