# 淡彩细线知识图文 Skill

把一个知识主题，做成小白看得懂、信息充分、风格统一的小红书图文。

由 **Summer聊AI** 在实际图文制作中逐轮打磨：先讲清知识，再设计图片，最后逐张检查。覆盖科普文案、生图提示词、图片生成与验收。

**[下载完整 ZIP](https://github.com/sweetparty331/xiaohongshu-pastel-carousel/archive/refs/heads/main.zip)** · **[使用指南](docs/usage.md)** · **[常见问题](docs/faq.md)** · **[核心指令](SKILL.md)**

## 效果预览

<img src="examples/fde.png" alt="什么是FDE：淡彩细线科普图" width="420">

更多风格参考：[提示词页](references/approved-prompt.png) · [Skills页](references/approved-skills.png)。这些图片由AI生成并经过人工方向确认和逐页检查；它们是风格参考，不是可任意套用的事实来源。

## 固定下来的制作标准

- **内容**：先说明是什么，语言简洁但不删关键知识；按主题选择流程、优势、类型等模块，不强加例子。
- **画幅**：整套严格统一3:4竖图，默认1086×1448；最终读取实际像素验收。
- **视觉**：白底、深蓝黑文字、浅蓝／薄荷绿／少量浅黄、轻量二维细线。
- **强调**：重点字背后用浅色块，不用点状着重号。
- **排版**：四周留白、模块对齐、中文不单字孤行，正文适合手机阅读。
- **迭代**：先讨论文案和提示词；明确要求生图后再生成。微调保留已确认内容。
- **验收**：核对错字、漏字、流程箭头、知识边界、署名、留白及尺寸。

## 快速开始

需要支持本地Skill的AI工具。实际生成图片还需要该环境提供图片生成和图片查看能力；这个仓库本身不包含模型、账号、API额度或图片生成服务。

### 安装到 Codex

推荐直接把仓库地址交给你环境中的skill安装器，并在安装后确认能找到 `xiaohongshu-pastel-carousel`。

也可以手动安装。macOS / Linux，目标目录尚不存在时：

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/sweetparty331/xiaohongshu-pastel-carousel.git "$HOME/.agents/skills/xiaohongshu-pastel-carousel"
```

不用Git时，点击上方下载ZIP，解压后把文件夹重命名为 `xiaohongshu-pastel-carousel`，放入本机支持的技能目录。保留整个文件夹，不要只复制 `SKILL.md`。

当前官方文档列出的用户级目录为 `~/.agents/skills`；本项目原始制作环境使用 `~/.codex/skills`。请按自己的客户端支持位置安装，避免在多个目录重复安装同名skill。[官方说明](https://learn.chatgpt.com/docs/build-skills)

### 发出任务

先看文字与提示词：

```text
使用 $xiaohongshu-pastel-carousel，做一张“什么是FDE”的科普图。
面向小白，先给我上图文案和完整生图提示词，暂时不要生图。
```

确认后生成：

```text
文案可以，按这个版本生成图片，并检查文字、留白和3:4比例。
```

需要直接生成时：

```text
使用 $xiaohongshu-pastel-carousel，直接生成一张“什么是上下文”的科普图。
署名用“我的账号”，保持淡彩细线风，生成后完成逐项检查。
```

默认署名为 `Summer聊AI`；为自己的账号创作时，在任务中明确提供新署名。更多用法见[使用指南](docs/usage.md)。

## 仓库内容

```text
xiaohongshu-pastel-carousel/
├── SKILL.md                        核心流程与制作标准
├── agents/openai.yaml              显示名称和默认调用提示
├── references/
│   ├── prompt-template.md          单页及局部修正提示词模板
│   ├── accepted-standard.md        内容取舍与准确性案例
│   ├── approved-prompt.png         提示词页风格样张
│   └── approved-skills.png         Skills页风格样张
├── scripts/check_png_dimensions.py PNG比例与同尺寸检查
├── examples/fde.png                FDE完整成图示例
└── docs/                           使用指南、FAQ及版本说明
```

## 尺寸检查

需要Python 3，无第三方依赖。在仓库根目录运行：

```bash
python3 scripts/check_png_dimensions.py examples/fde.png references/approved-prompt.png references/approved-skills.png
```

退出码0表示这些PNG都为严格3:4且尺寸一致；退出码1表示存在问题。只检查PNG文件头尺寸，不验证文件完整解码，也不检查错字、排版或知识正确性。图片仍需逐张查看。

## 版本与许可

初始发布版：v1.0.0。参见[版本说明](docs/release-notes.md)。当前版本尚未添加许可证，后续授权以仓库明确发布的许可文件为准。

此仓库只提供图文制作skill；帖子配文skill不在本仓库中，也不是必需依赖。不会自动登录或发布到小红书。
