# English brief — HorizonRobotics/HoloAgent

Upstream: https://github.com/HorizonRobotics/HoloAgent
Fork: https://github.com/onnxscibroccoli/HoloAgent
License: Apache-2.0
Default branch: main
Upstream pushed: 2026-07-17T06:26:17Z
This file is an operator brief written for this account. It is not a substitute for the upstream license. Copyright stays with the upstream authors. Keep their notice if you copy their code.

## What it is

An embodied-agent loop from Horizon Robotics: observe, retrieve, plan, act, verify, with a memory of the place. The project as a whole is Apache-2.0. Some bundled third-party SLAM pieces are not cleared for commercial use.

## Plain English

The README checked for this intake is English. Any Chinese comment or doc the daily job finds is translated below under Translated passages. The loop is the part worth copying. The weights and the restricted SLAM trees are not.

## Why it belongs here

Grasshopper's tick already has execute and confirm. Add a verify step that checks the world, not the model's own claim of success. Broccoli's confirm step is the phone version of the same idea.

## Do not

Do not import FAST-LIVO2 or HOVSG into a product. Their default licenses restrict commercial use. Do not download robot checkpoints into the phone repo.

## Integration

### Grasshopper

Name the task states observe, plan, act, verify. verify reads a local sensor or a test, not the model's summary of itself.

### broccoli-core

After a tick changes a setting, read the setting back through the accessibility tree or a local API. That read is verify.

## For someone else's agent stack

Publish the loop. Let another runtime implement verify however it can measure the world. Do not require their users to buy a particular robot.

## Values

- Economic: run the work on hardware the person already has. Do not meter a local action.
- Community: leave the license and the authors' names in place so the next person can fork too.
- Disability: prefer the accessibility tree and a local voice over a screenshot sent to a vendor.
- Everyday: a person should be able to tell which step ran on their machine.

Values named for this upstream: everyday, community.

## Translated passages

Chinese introduction. The source line is a badge linking to a WeChat article. The original characters stay in the image address so the link still works.

Source line:

[![中文介绍](https://img.shields.io/badge/中文介绍-07C160?logo=wechat&logoColor=white)](https://mp.weixin.qq.com/s/HqnBlTNqOL3Z4Kg8tLHCSw)

## README checked

Characters read: 6711.
