# muser-yinse

[English](README.md) | 简体中文

[muser](https://github.com/claw-works/muser) 的音色库：从录音里提取出来的模态乐器（`*.yinse.json`）。
每件乐器只是一张张分音表（频率、两段衰减、一组弦之间的拍、左右声道、起音噪声、演奏法），没有音频，几十到一两百 KB。

## 用法

```bash
git clone https://github.com/claw-works/muser-yinse.git
export MUSER_YINSE_PATH=/path/to/muser-yinse        # 可以用路径分隔符写多个库
```

```json
{ "instrument": "yinse:strike/grand-piano" }
```

`yinse:<类>/<名>` 在 `MUSER_YINSE_PATH` 的每个库里找 `instruments/<类>/<名>/<名>.yinse.json`。也可以直接写文件路径。
`muser instruments yinse:strike/grand-piano` 看音域和有哪些演奏法。

## 乐器

| 写法 | 乐器 | 音域 | 录音来源 · 许可证 |
|---|---|---|---|
| `yinse:strike/grand-piano` | [三角钢琴](instruments/strike/grand-piano/)（雅马哈 C5，有制音器） | A0-C8 | Alexander Holm 的 Salamander Grand Piano · CC BY 3.0 |

带演奏法的完整清单在 [index.json](index.json)。

## 目录

```
instruments/
  strike/            敲击：扬琴、钢琴、钟、马林巴……
  pluck/             拨弦：古筝、琵琶、竖琴、吉他……
  <类>/<名>/
    <名>.yinse.json  muser yinse extract 的输出
    meta.json        名字、录音来源与许可证、提取信息（见下）
    README.md        （可选）录音说明、演奏法、对比结果
index.json           全部乐器的清单（scripts/index.py 生成）
```

只收敲一下、拨一下就自己衰减的乐器：提取方法不适合吹管、拉弦这类持续发声的声音。

## meta.json

```json
{
  "name": "grand-piano",
  "zh": "三角钢琴",
  "family": "strike",
  "description": "Yamaha C5 grand piano, two AKG C414 in AB about 12 cm above the strings; dampers",
  "source": {
    "title": "Salamander Grand Piano V3 (FreePats SFZ+FLAC 20200602)",
    "url": "https://freepats.zenvoid.org/Piano/acoustic-grand-piano.html",
    "author": "Alexander Holm",
    "license": "CC-BY-3.0"
  },
  "extracted": { "muser": "0.6.0", "date": "2026-11-11", "recordings": 90, "compare_db": 3.77, "command": "muser yinse extract --from sfz:… --pitches 21-108/3 …" }
}
```

`source.license` 用 [SPDX](https://spdx.org/licenses/) 写法。`compare_db` 是 `muser yinse compare` 最后一行的平均频谱差。

## 收录规则

- **录音的许可证必须允许再分发和衍生作品**（CC0、CC-BY、CC-BY-SA、公有领域，或你自己录的）。分音表是录音的衍生数据：
  商业音源（Kontakt 等）即使免费下载，也不能拿来提取后放进这里。
- CC-BY / CC-BY-SA 的录音，在 `meta.json` 和 README 里写清署名；CC-BY-SA 的乐器同样以 CC-BY-SA 发布。
- 不放录音本身（`.gitignore` 挡掉了常见的音频格式）。
- 提交前跑一遍 `muser yinse compare`，把平均频谱差写进 `meta.json`。

添加乐器的步骤见 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。

## 许可证

仓库里的脚本和文档：MIT 或 Apache-2.0（任选）。每件乐器的许可证跟随它的录音，写在各自的 `meta.json` 里。
