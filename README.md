# Xunxiashi

`Xunxiashi` means `训虾师`.

An OpenClaw skill for novice IM-first users who want a shrimp that is safer, more stable, and actually useful.

Current version: `v0.1.0`

Repository: [github.com/laoguo2025/xunxiashi](https://github.com/laoguo2025/xunxiashi)

---

## 中文

### 你是不是也遇到过这些问题

很多人装完 OpenClaw 之后，真实感受是：

- 能聊天，但不太会干活
- 刚教过，转头就忘
- 嘴上说“记住了”，其实没有真的写进去
- 用久了以后越来越乱，越来越笨
- skill 越装越多，但不知道哪些真的有用

`Xunxiashi` 就是专门解决这类问题的。

它不是普通 prompt，也不是单纯的人设包。  
它更像一个“训虾师”，帮你把这只虾从“能聊”养成“能干活、能记住、能长期稳定使用”。

### 它能帮你解决什么

#### 1. 先把脑子装好

它会先带你完成一次傻瓜式建脑，让这只虾先知道：

- 你是谁
- 它该怎么称呼你
- 它应该怎么说话
- 它该怎么干活
- 哪些事不能乱做

你不用懂 `json`、不用懂 hook、也不用懂 OpenClaw 内部结构。

#### 2. 再把习惯训进去

后面你正常使用、正常纠错、正常投喂资料就行。  
`Xunxiashi` 会把这些东西逐步变成真实规则，而不是只停留在聊天记录里。

#### 3. 最后让它越养越稳

它还会帮你把“越用越乱、越用越失忆”的问题压下去，比如：

- 记忆蒸馏
- 规则去重
- 跨会话恢复
- 定时体检和维护

### 为什么对小白友好

- 默认按聊天方式一步步引导，不需要你自己研究配置文件
- 安装后就能开始，不需要先搞懂一堆术语
- 会优先考虑安全边界，不让它乱碰关键内容
- 不要求你一上来就学会 OpenClaw 的各种内部机制

### 安全上做了什么

`Xunxiashi` 的默认思路是：

- 高风险操作优先确认
- 不能随便改关键文件
- 不能随便向外泄露敏感信息
- 不能口头承诺“记住了”却不落盘
- 如果要重建脑子，必须先告诉你后果，并让你选择 `叠加` 或 `覆盖`

也就是说，它追求的不是“更放飞”，而是“更稳、更可控”。

### 使用起来是什么感觉

你不需要一开始就懂很多。  
更像是：

1. 安装 skill
2. 跟着提示完成初始建脑
3. 后面正常聊天、正常使用、正常投喂资料
4. 让它边用边学，边用边养

如果中途被打断，它也应该知道从哪里继续，而不是每次都从头再来。

### 你大概会得到什么效果

- 回答方式更像你要的风格
- 干活流程更贴近你的习惯
- 重要偏好不容易反复重教
- skill 安装更克制，不容易乱装一堆没必要的东西
- 长期使用后，workspace 更稳定，不容易越养越笨

### 适合谁

- 刚装完 OpenClaw 的用户
- 已经接好飞书、微信、钉钉、企微、Telegram 等 IM 渠道的用户
- 想把 OpenClaw 从“会聊天”养成“会干活”的用户
- 想减少假记忆、乱安装、乱漂移问题的用户

### 简单技术说明

- `Xunxiashi` 是一个单 skill，不拆成多个 skill
- 它围绕三个方向工作：建脑、训脑、养脑
- 恢复相关能力会依赖 OpenClaw 官方机制，例如 `boot-md` 和 `session-memory`
- skill 默认支持多语言，会尽量跟随用户当前语言
- 当前仓库是 `v0.1.0`，已经可以安装、测试、继续演进

---

## English

### Common Pain After Installing OpenClaw

Many users end up with the same experience:

- the shrimp can chat, but cannot really work well
- you teach it something once, then it forgets
- it says "I remembered that" without really saving it
- the longer you use it, the noisier and less reliable it becomes
- you install more and more skills without knowing which ones are actually worth keeping

`Xunxiashi` is built for exactly this situation.

It is not just a prompt pack and not just a personality wrapper.  
It acts more like a shrimp trainer that helps turn OpenClaw from "can talk" into "can work, can remember, and can stay stable over time".

### What It Helps With

#### 1. Build a usable brain first

It guides the user through a beginner-friendly setup so the shrimp can first understand:

- who the user is
- how to address them
- how to talk
- how to work
- what not to do casually

The user does not need to understand `json`, hooks, or internal OpenClaw structure.

#### 2. Turn habits into real defaults

After that, the user can just work normally, correct normally, and feed materials normally.  
`Xunxiashi` is designed to turn those repeated signals into real rules instead of leaving them as chat-only promises.

#### 3. Keep the shrimp stable over time

It also helps control the "more use, more drift" problem through:

- memory distillation
- rule deduplication
- cross-session recovery
- scheduled maintenance and review

### Why It Is Beginner-Friendly

- it guides through chat instead of forcing users to study config files first
- it starts working right after installation
- it prioritizes safety boundaries
- it does not assume users understand OpenClaw internals

### Safety Philosophy

`Xunxiashi` defaults toward:

- confirmation for high-risk actions
- protection for critical files
- no casual leakage of sensitive information
- no fake "remembered" claims without a real write
- explicit warning plus `叠加` / `覆盖` choice before rebuild

It is designed to be more stable and more controllable, not more reckless.

### What The Experience Should Feel Like

The intended flow is simple:

1. install the skill
2. follow the initial brain-building guidance
3. use the shrimp normally
4. let it keep learning and stabilizing through real usage

If the process is interrupted, it should continue from where it left off instead of restarting blindly.

### Expected Outcome

- replies feel closer to the user's preferred style
- work behavior better matches real habits
- fewer repeated corrections
- more disciplined skill installation
- a more stable workspace over time

### Who This Is For

- new OpenClaw users
- IM-first users already connected to Feishu, WeChat, DingTalk, WeCom, Telegram, or similar channels
- users who want OpenClaw to become a real work partner
- users who want fewer fake memory, over-installation, and drift problems

### Short Technical Note

- `Xunxiashi` is one skill, not a bundle of separate skills
- it works around three directions: build, train, and maintain the brain
- recovery behavior relies on official OpenClaw mechanisms such as `boot-md` and `session-memory`
- it supports multilingual interaction by default
- current repository version is `v0.1.0`, ready for installation, testing, and iteration
