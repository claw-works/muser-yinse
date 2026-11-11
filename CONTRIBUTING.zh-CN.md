# 添加一件乐器

[English](CONTRIBUTING.md) | 简体中文

下面用仓库里的三角钢琴（`instruments/strike/grand-piano/`）做例子。

1. **先确认许可证**：录音必须允许再分发和衍生作品（见 README）。Salamander Grand Piano 是 CC BY 3.0，署名
   Alexander Holm 就可以收录。

2. **提取**：音色库是 SFZ 的，让 muser 自己演奏来提取（顺便量制音器）：

   ```bash
   mkdir -p instruments/strike/grand-piano
   muser yinse extract --from "sfz:/path/SalamanderGrandPiano-V3+20200602.sfz" \
     --pitches 21-108/3 --velocities 0.3,0.6,0.9 --hold 6 --notes-dir /tmp/piano-notes \
     -o instruments/strike/grand-piano/grand-piano.yinse.json --name "Grand Piano (Salamander, Yamaha C5)"
   muser yinse compare instruments/strike/grand-piano/grand-piano.yinse.json /tmp/piano-notes
   ```

   用录音的话：一个文件一个音，从起音录到响完（2 到 3 秒以上），干声，每 3 到 5 个半音一个、2 到 3 种力度。
   文件名写音高、力度、演奏法，再把文件夹交给它：

   ```text
   A4_v80.wav  A4_v80_mute.wav  D5_tremolo.wav  A4_vibrato.wav  E4_damp.wav  A3_art-fanzhu_v90.wav
   ```

   ```bash
   muser yinse extract ~/recordings/piano -o instruments/strike/grand-piano/grand-piano.yinse.json --name "…"
   ```

3. **meta.json** 写在旁边（字段见 README）：录音来源、作者、SPDX 许可证，以及 `compare` 最后一行的平均频谱差（`compare_db`）。
   参考 [instruments/strike/grand-piano/meta.json](instruments/strike/grand-piano/meta.json)。

4. **README.md** 写在乐器的文件夹里：录音的署名、怎么演奏、哪些没有提取。

5. **试听**：在 muser 里用它演奏一段（`MUSER_YINSE_PATH=<这个仓库>`，`"instrument": "yinse:strike/grand-piano"`）。

6. `uv run python scripts/index.py` 检查每个 `meta.json` 并重新生成 `index.json`，然后提 pull request。
