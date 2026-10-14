# English brief — Magi-Labs/mobilemcp

Upstream: https://github.com/Magi-Labs/mobilemcp
Fork: https://github.com/onnxscibroccoli/mobilemcp
License: MIT
Default branch: main
Upstream pushed: 2026-10-12T16:17:56Z
This file is an operator brief written for this account. It is not a substitute for the upstream license. Copyright stays with the upstream authors. Keep their notice if you copy their code.

## What it is

An MCP server and Android app that exposes the accessibility tree, with stable node refs, to an agent. Taps and typing go through that tree. MIT. Found by the intake search, then added by hand.

## Plain English

Already English. This is the closest public match to broccoli's job: the phone describes itself in words a screen reader would also use, and the agent asks for a labeled action.

## Why it belongs here

Grasshopper can call it as an external tool. broccoli-core remains the on-device kernel. Do not run both as competing clickers. Pick one executor per request.

## Do not

Do not point it at a banking app and let a remote model drive it. Do not turn off TalkBack to make the refs easier.

## Integration

### Grasshopper

Register mobilemcp as a tool with a device id. Task inputs are a node ref and an action. The task log stores the ref and the result, not a screenshot, unless a person asked for one frame.

### broccoli-core

If both can see the tree, broccoli stays the executor for requests that already go through rish. mobilemcp is the path for an agent that only speaks MCP.

## For someone else's agent stack

Any MCP client can use the same server. The contract is node-ref in, result out. The phone does the click. The model does not get a video stream by default.

## Values

- Economic: run the work on hardware the person already has. Do not meter a local action.
- Community: leave the license and the authors' names in place so the next person can fork too.
- Disability: prefer the accessibility tree and a local voice over a screenshot sent to a vendor.
- Everyday: a person should be able to tell which step ran on their machine.

Values named for this upstream: everyday, disability, economic.

## Translated passages

No non-English lines in the README checked this run.

## README checked

Characters read: 21213.
