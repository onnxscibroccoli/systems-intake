# English brief — autowarefoundation/agnocast

Upstream: https://github.com/autowarefoundation/agnocast
Fork: https://github.com/onnxscibroccoli/agnocast
License: Apache-2.0
Default branch: main
Upstream pushed: 2026-10-22T10:21:44Z
This file is an operator brief written for this account. It is not a substitute for the upstream license. Copyright stays with the upstream authors. Keep their notice if you copy their code.

## What it is

ROS 2 middleware that moves large messages between processes without copying them. Includes a Linux kernel module. Apache-2.0.

## Plain English

Already English. Do not build the kernel module for this account. Copy the rule: agents pass a handle to bytes, they do not paste the bytes through a chat model.

## Why it belongs here

Grasshopper tasks that move logs, images, or desktop frames should pass a path or an id. The model sees a description and a size, not the payload.

## Do not

Do not load agnocast-kmod on a phone, a shared desktop, or a CI runner. Do not vendor the C++ into broccoli.

## Integration

### Grasshopper

Task inputs over a size limit become a resource id in the control plane. The executing environment opens the resource. The model is given the id and a one-line description.

### helix

A desktop stream already should not be base64'd into an agent prompt. Keep the RFB session in the browser. The agent gets a screenshot only when a person asks for one frame.

## For someone else's agent stack

Same rule on any runtime. Tool results carry ids. A separate local reader opens the bytes. This is how a person avoids paying a model to reread a log they already have on disk.

## Values

- Economic: run the work on hardware the person already has. Do not meter a local action.
- Community: leave the license and the authors' names in place so the next person can fork too.
- Disability: prefer the accessibility tree and a local voice over a screenshot sent to a vendor.
- Everyday: a person should be able to tell which step ran on their machine.

Values named for this upstream: economic, everyday.

## Translated passages

- ROSCon JP 2025, Nagoya: "CallbackIsolatedExecutor: a new executor and a scheduling theory that removes the need to schedule the same work twice" by Takahiro Ishikawa-Aso ([video](https://vimeo.com/1122709186), in Japanese; an English summary is available on the [TIER IV tech blog](https://medium.com/tier-iv-tech-blog/callbackisolatedexecutor-a-novel-executor-that-eliminates-nested-scheduling-in-scheduling-theory-400b0131ed75))

Source line:

- ROSCon JP 2025, Nagoya: "CallbackIsolatedExecutor: 二重スケジューリングを不要にする新しいExecutorとスケジューリング理論" by Takahiro Ishikawa-Aso ([video](https://vimeo.com/1122709186), in Japanese; an English summary is available on the [TIER IV tech blog](https://medium.com/tier-iv-tech-blog/callbackisolatedexecutor-a-novel-executor-that-eliminates-nested-scheduling-in-scheduling-theory-400b0131ed75))

## README checked

Characters read: 8713.
