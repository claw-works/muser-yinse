# 添加一件乐器

[English](CONTRIBUTING.md) | 简体中文

下面用仓库里的三角钢琴（`instruments/strike/grand-piano/`）做例子。
要录多少个音、怎么检查够不够：[docs/sampling.zh-CN.md](docs/sampling.zh-CN.md)。

1. **先确认许可证**：录音必须允许再分发和衍生作品（见 README）。Salamander Grand Piano 是 CC BY 3.0，署名
   Alexander Holm 就可以收录。

2. **提取**：音色库是 SFZ 的，让 muser 自己演奏来提取（顺便量制音器）：

   ```bash
   mkdir -p instruments/strike/grand-piano
   muser yinse extract --from "sfz:/path/SalamanderGrandPiano-V3+20200602.sfz" \
     --pitches 21-108/3 --velocities 0.3,0.6,0.9 --hold 6 --notes-dir /tmp/piano-notes \
     -o instruments/strike/grand-piano/grand-piano.yinse.json --name "Grand Piano (Salamander, Yamaha C5)"
   muser yinse compare --between instruments/strike/grand-piano/grand-piano.yinse.json /tmp/piano-notes
   ```

   用录音的话，一条命令把一个文件夹变成乐器。录音要这样：

   - 一个文件一个音（wav、flac、aiff、ogg、mp3），只敲或拨一下。音前面有空白没关系；起音后至少要响 0.3 秒，
     有一个文件量不出来，整个提取就停下。
   - 每个音录到自己响完（最多用前 20 秒）。提前剪掉的，余音多长只能估。
   - 干、安静：话筒近、没有混响、上一个音的弦别还在响。一直不变的哼声会被去掉；混响会进到余音里。
   - 要演奏的音域里每 3 到 5 个半音一个（每根弦、每块音板都录更好，用 `--between` 检查），每个音高 2 到 3 种力度。
     立体声、单声道都行；所有的音用同样的话筒位置和增益，不要逐个文件拉满音量：轻重之间差多少就是力度响应。
   - 文件名里写音高（`A4`、`Eb3`、`C#5` 或 MIDI 号）、力度（`v80` 是 0 到 127，`v0.7`，`pp` … `ff`）、演奏法。
     没写音高就从声音里量；没写力度，同一个音高的几个文件按响度从轻到重排。
   - 可选：`mute`、`harmonic`、`back`、`pluck`、`staccato`、`rim`、`soft`、`hard` 或 `art-<名字>` 是别的音色（各录几个音高）；
     轮音（`tremolo`）、带揉音的音（`vibrato`）、用手止住的音（`damp`）各录一个。

   ```text
   A4_v80.wav  A4_v80_mute.wav  D5_tremolo.wav  A4_vibrato.wav  E4_damp.wav  A3_art-fanzhu_v90.wav
   ```

   ```bash
   muser yinse extract ~/recordings/piano -o instruments/strike/grand-piano/grand-piano.yinse.json --name "…"
   muser yinse compare --between instruments/strike/grand-piano/grand-piano.yinse.json ~/recordings/piano
   ```

   也可以把整个采样过程录成**一条音频**，让 muser 自己切（`--split`）：

   ```bash
   muser yinse extract take.wav --split --notes-dir take-notes -o instruments/pluck/guzheng/guzheng.yinse.json --name "…"
   muser yinse compare --between instruments/pluck/guzheng/guzheng.yinse.json take-notes
   ```

   这条音频要这样：

   - 是采样，不是一首曲子：一次只弹一个音，一个接一个，顺序随意。不弹和弦，不在上一个音还响着的时候弹下一个。
   - 每个音让它自己响完再弹下一个，不要用手把弦按住。上一个音落到比它低 20 dB 以下、到下一个音之前至少响了
     0.5 秒的音才会用。
   - 音高要清楚，在 C1 到 E7 之间（音高是量出来的）。钟、音板、鼓这类要一个文件一个音、文件名写音高。
   - 要力度分层，就每个音高弹轻、中、重各一遍，响度至少差 3 dB（差不到 3 dB 的算同一种力度）。
   - 音和音之间保持安静（咳嗽一声会被当成一个音，并把前一个音截短）；一直不变的哼声没关系。
   - 从头到尾话筒位置和增益不变；可以一次给好几条。

   muser 会把找到的每个音列出来，写明用了还是为什么没用。`--notes-dir` 把切出来的单音留下，文件名带音高：
   听几个，不对的删掉或改名，加上 `_mute`、`_v40` 或动作的录音，再对这个文件夹跑一遍 `extract`（不加 `--split`）重建。

   `compare` 逐个录音给出频谱差（2 到 3 dB 算接近）、响度差和衰减；加 `--between` 还给出没录的音高差多少。
   只在自己机器上用，到这里就够了：`muser yinse install <文件> --as strike/my-piano`，然后写
   `"instrument": "yinse:strike/my-piano"`。

3. **meta.json** 写在旁边（字段见 README）：录音来源、作者、SPDX 许可证，以及 `compare` 最后一行的平均频谱差（`compare_db`）。
   参考 [instruments/strike/grand-piano/meta.json](instruments/strike/grand-piano/meta.json)。

4. **README.md** 写在乐器的文件夹里：录音的署名、怎么演奏、哪些没有提取。

5. **试听**：在 muser 里用它演奏一段（`MUSER_YINSE_PATH=<这个仓库>`，`"instrument": "yinse:strike/grand-piano"`）。

6. `uv run python scripts/index.py` 检查每个 `meta.json` 并重新生成 `index.json`，然后提 pull request。
