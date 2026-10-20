# English brief — AtsushiSakai/PythonRobotics

Upstream: https://github.com/AtsushiSakai/PythonRobotics
Fork: https://github.com/onnxscibroccoli/PythonRobotics
License: MIT
Default branch: master
Upstream pushed: 2026-10-19T20:03:09Z
This file is an operator brief written for this account. It is not a substitute for the upstream license. Copyright stays with the upstream authors. Keep their notice if you copy their code.

## What it is

One-file Python references for localization, SLAM, path planning, and obstacle avoidance. A textbook, not a vehicle stack.

## Plain English

Already English. The value is that a person can run a planner on a laptop they own and read every line.

## Why it belongs here

A Grasshopper task can shell out to one example script for a local plan. The result is a path, not a subscription.

## Do not

Do not put this code on a car. Do not wrap it in a paid API and strip the MIT notice.

## Integration

### Grasshopper

Register a task type local-python. The task record stores the script path, the inputs, and the stdout. Recovery replays the same command. No network in the task.

### broccoli-core

Only if the phone image actually has the script. Otherwise the tick says the planner is not installed. Do not pretend.

## For someone else's agent stack

Call the script as a tool with a working directory and a timeout. Return the path geometry. Keep the MIT copyright in the tool's about text.

## Values

- Economic: run the work on hardware the person already has. Do not meter a local action.
- Community: leave the license and the authors' names in place so the next person can fork too.
- Disability: prefer the accessibility tree and a local voice over a screenshot sent to a vendor.
- Everyday: a person should be able to tell which step ran on their machine.

Values named for this upstream: community, economic, everyday.

## Translated passages

No non-English lines in the README checked this run.

## README checked

Characters read: 25652.
