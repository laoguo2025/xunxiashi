# Xunxiashi

`Xunxiashi` means `训虾师`.

An OpenClaw skill package for novice IM-first users who want to turn a forgetful shrimp into a usable work partner.

Current version: `v0.1.0`

Repository: [github.com/laoguo2025/xunxiashi](https://github.com/laoguo2025/xunxiashi)

---

## 中文

### 你是不是正卡在这里

很多人装完 OpenClaw 之后，真实体验是这样的：

1. 接上飞书、微信、钉钉、企微、Telegram。
2. 开始聊天，觉得这只虾能聊，但不够会干活。
3. 你刚教过它，它嘴上说记住了，过一会儿又忘了。
4. 聊久了以后，越来越乱，越来越笨，越来越像在重复劳动。

`Xunxiashi` 就是为这个场景做的。

它不是一个普通 prompt，也不是只会聊天的“人设包”。
它的目标，是把你在真实使用中的习惯、纠错、流程和边界，逐步沉淀成 OpenClaw 真正会读取的 workspace 文件。

### 它怎么解决

`Xunxiashi` 不是一把梭地丢给你一长串问卷，而是三步走：

#### 第一步：建脑

作用：

- 先把这只虾的基础脑子装起来
- 明确它是谁、你是谁、什么事不能乱做
- 先得到一个“能用、能聊、能干活”的初版

结果：

- 有基础人格
- 有基本安全边界
- 有默认干活方式

#### 第二步：训脑

作用：

- 在真实使用里边聊边训
- 把“以后都按这个来”“记住这个”“别再这么说”这种反馈变成真实规则
- 不再只是口头承诺

结果：

- 你的习惯会慢慢沉淀进规则文件和记忆
- 重复纠错会越来越少
- 这只虾会越来越像你的工作搭子

#### 第三步：养脑

作用：

- 定期整理 workspace
- 合并重复规则
- 蒸馏 daily memory
- 修补“越养越乱、越养越失忆”的问题

结果：

- 更稳
- 更清晰
- 更容易跨会话恢复
- 不容易聊久了就跑偏

### 它适合谁

- 刚装完 OpenClaw 的小白用户
- 已经接好 IM，但感觉虾不够聪明的人
- 想把 OpenClaw 从“会聊天”养成“会干活”的人
- 想减少“说记住了，其实没写进去”的人
- 想让 agent 既有边界，又有个性的人

### 这个仓库里有什么

- [Xunxiashi/SKILL.md](Xunxiashi/SKILL.md)
  主 skill 规则
- [Xunxiashi/references/question-set.md](Xunxiashi/references/question-set.md)
  终版 30 题
- [Xunxiashi/references/file-mapping.md](Xunxiashi/references/file-mapping.md)
  问题到文件的映射速查
- [Xunxiashi/references/hooks-setup.md](Xunxiashi/references/hooks-setup.md)
  `/new` 恢复、重启恢复等 hook 接线说明
- [Xunxiashi/assets/templates/](Xunxiashi/assets/templates/)
  workspace 模板
- [docs/examples/xunxiashi-vertical-short-drama/](docs/examples/xunxiashi-vertical-short-drama/)
  一个“竖屏短剧编剧”的完整示例

### 推荐阅读顺序

1. [README.md](README.md)
2. [SKILL.md](Xunxiashi/SKILL.md)
3. [question-set.md](Xunxiashi/references/question-set.md)
4. [file-mapping.md](Xunxiashi/references/file-mapping.md)
5. [docs/examples/xunxiashi-vertical-short-drama/README.md](docs/examples/xunxiashi-vertical-short-drama/README.md)

### 技术说明

- `Xunxiashi` 是单 skill，不拆成多个 skill。
- 默认支持三阶段：建脑 / 训脑 / 养脑。
- `BOOTSTRAP.md` 不在时，不假装重跑官方首次 bootstrap，而是进入“重新建脑”。
- 重新建脑前必须先告知后果，再让用户选择 `叠加` 或 `覆盖`。
- `/new` 恢复、网关重启恢复、写入后再说“记住了”是默认产品行为。
- 其中恢复相关行为，仍然需要按 OpenClaw 官方机制接 `boot-md` 和 `session-memory` hook。
- skill 默认跟随用户语言，不限制中文；仓库文档至少保持中英双语。

### 当前状态

当前版本是 `v0.1.0`。

它已经是一个可安装、可阅读、可演示、可继续扩展的 skill 包。
但它仍然更接近“高质量设计包 + 首版实现”，还不是经过大规模真实生产验证的成熟成品。

---

## English

### The Pain This Tries To Fix

For many users, the real OpenClaw experience looks like this:

1. Connect Feishu, WeChat, DingTalk, WeCom, or Telegram.
2. Start chatting.
3. Realize the shrimp can talk, but cannot really work well.
4. Teach it something once, hear "I remembered that", then watch it forget.
5. Keep using it for a while, then feel the workspace getting noisier, dumber, and harder to trust.

`Xunxiashi` is built for exactly that situation.

It is not just a prompt pack and not just a personality wrapper.
Its job is to turn repeated feedback, habits, workflows, and boundaries into real OpenClaw workspace files.

### The Three-Step Solution

#### Step 1: Build the Brain

What it does:

- gives the shrimp a first usable brain
- defines who it is, who you are, and what it must never do casually
- creates a first version that is usable for real work

What you get:

- a basic personality
- basic safety boundaries
- a default working style

#### Step 2: Train the Brain

What it does:

- trains the shrimp during real usage
- turns feedback like "remember this", "do it like this next time", and "stop saying it that way" into real rules
- reduces empty verbal promises

What you get:

- repeated preferences becoming real structure
- fewer repeated corrections
- a shrimp that feels more like your actual work partner

#### Step 3: Maintain the Brain

What it does:

- cleans the workspace over time
- merges duplicate rules
- distills daily memory
- repairs the "more use, more drift" problem

What you get:

- better stability
- clearer memory
- better cross-session recovery
- less long-term drift

### Who This Is For

- novice OpenClaw users
- IM-first users who already connected channels but feel the shrimp is weak
- users who want to turn OpenClaw from "can chat" into "can work"
- users who want fewer fake memory claims
- users who want an agent that is both safe and interesting

### What Is In This Repository

- [Xunxiashi/SKILL.md](Xunxiashi/SKILL.md)
  Main skill rules
- [Xunxiashi/references/question-set.md](Xunxiashi/references/question-set.md)
  Final 30-question set
- [Xunxiashi/references/file-mapping.md](Xunxiashi/references/file-mapping.md)
  Fast mapping from answers to files
- [Xunxiashi/references/hooks-setup.md](Xunxiashi/references/hooks-setup.md)
  Hook wiring notes for startup recovery and `/new`
- [Xunxiashi/assets/templates/](Xunxiashi/assets/templates/)
  Workspace templates
- [docs/examples/xunxiashi-vertical-short-drama/](docs/examples/xunxiashi-vertical-short-drama/)
  A full vertical short drama writer example

### Recommended Reading Order

1. [README.md](README.md)
2. [SKILL.md](Xunxiashi/SKILL.md)
3. [question-set.md](Xunxiashi/references/question-set.md)
4. [file-mapping.md](Xunxiashi/references/file-mapping.md)
5. [docs/examples/xunxiashi-vertical-short-drama/README.md](docs/examples/xunxiashi-vertical-short-drama/README.md)

### Technical Notes

- `Xunxiashi` is one skill, not many separate skills.
- It is built around three stages: build / train / maintain.
- If `BOOTSTRAP.md` is gone, it does not pretend to replay official first-run bootstrap. It enters rebuild mode.
- Rebuild must warn first, then ask the user to choose `叠加` or `覆盖`.
- `/new` recovery, startup recovery, and write-before-remember are default product behaviors.
- Recovery-related behavior still needs official OpenClaw hook wiring through `boot-md` and `session-memory`.
- The skill follows the user's working language by default and the repository keeps bilingual documentation.

### Current Status

Current version: `v0.1.0`

This repository is already installable, reviewable, demoable, and extendable.
It is still closer to a strong design package plus first implementation than to a heavily battle-tested production release.
