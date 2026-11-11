# Adding an instrument / 添加一件乐器

1. **Recordings / 录音**: one note per file, from the attack until it has rung away (2-3 s or more), dry. A pitch every
   3-5 semitones, 2-3 velocities. Name the files with pitch and velocity, and articulation if any:
   一个文件一个音，从起音录到响完，干声；每 3 到 5 个半音一个，2 到 3 种力度。文件名写音高、力度、演奏法：

   ```text
   A4_v80.wav  A4_v80_mute.wav  D5_tremolo.wav  A4_vibrato.wav  E4_damp.wav  A3_art-fanzhu_v90.wav
   ```

   Check the license first (see README) / 先确认许可证（见 README）。

2. **Extract / 提取**:

   ```bash
   mkdir -p instruments/strike/yangqin
   muser yinse extract ~/recordings/yangqin -o instruments/strike/yangqin/yangqin.yinse.json --name "扬琴 yangqin"
   muser yinse compare instruments/strike/yangqin/yangqin.yinse.json ~/recordings/yangqin
   ```

3. **meta.json** next to it (fields in the README), and a README.md for anything a player should know.
   在旁边写 `meta.json`（字段见 README），需要说明的写进 README.md。

4. **Listen / 试听**: play a phrase with it in muser before submitting.

5. `uv run python scripts/index.py` to check every `meta.json` and regenerate `index.json`, then open a pull request.
