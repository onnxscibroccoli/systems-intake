# English brief — rwapp/A11y-Box-Android

Upstream: https://github.com/rwapp/A11y-Box-Android
Fork: https://github.com/onnxscibroccoli/A11y-Box-Android
License: MIT
Default branch: master
Upstream pushed: 2020-03-01T15:24:38Z
This file is an operator brief written for this account. It is not a substitute for the upstream license. Copyright stays with the upstream authors. Keep their notice if you copy their code.

## What it is

A small sample app of Android accessibility APIs: labels, focus, and the checks a developer is supposed to run.

## Plain English

Already English. Use it as a fixture, not as a product. It shows the node properties broccoli should require before it will click.

## Why it belongs here

A control is fair game for automation only when it has a name a person using a screen reader would also hear.

## Do not

Do not treat an unlabeled button as acceptable because a vision model can guess it.

## Integration

### broccoli-core

Add an offline fixture, copied under its MIT license with the copyright kept, that the kernel uses in smoke tests: refuse to activate a node with an empty content description.

### newsroom-desk

Cite the sample when explaining why a banking or chat app that hides the label fails both disabled users and any honest automation.

## For someone else's agent stack

Put the accessibility tree, not a screenshot, in the tool result. Screenshots are a fallback when the tree is empty, and they should stay on the device.

## Values

- Economic: run the work on hardware the person already has. Do not meter a local action.
- Community: leave the license and the authors' names in place so the next person can fork too.
- Disability: prefer the accessibility tree and a local voice over a screenshot sent to a vendor.
- Everyday: a person should be able to tell which step ran on their machine.

Values named for this upstream: disability, community, everyday.

## Translated passages

No non-English lines in the README checked this run.

## README checked

Characters read: 555.
