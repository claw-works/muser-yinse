# Adding an instrument

English | [简体中文](CONTRIBUTING.zh-CN.md)

The example below is the grand piano in this repository (`instruments/strike/grand-piano/`).

1. **Check the license.** The recordings must allow redistribution and derivatives (see the README). The Salamander Grand
   Piano is CC BY 3.0, so it can go in with credit to Alexander Holm.

2. **Extract.** From an SFZ library, let muser play the notes itself (it also measures the dampers):

   ```bash
   mkdir -p instruments/strike/grand-piano
   muser yinse extract --from "sfz:/path/SalamanderGrandPiano-V3+20200602.sfz" \
     --pitches 21-108/3 --velocities 0.3,0.6,0.9 --hold 6 --notes-dir /tmp/piano-notes \
     -o instruments/strike/grand-piano/grand-piano.yinse.json --name "Grand Piano (Salamander, Yamaha C5)"
   muser yinse compare instruments/strike/grand-piano/grand-piano.yinse.json /tmp/piano-notes
   ```

   From recordings instead: one note per file, from the attack until it has rung away (2-3 s or more), dry, a pitch every
   3-5 semitones and 2-3 velocities. Put pitch, velocity and articulation in the file names, then pass the folder:

   ```text
   A4_v80.wav  A4_v80_mute.wav  D5_tremolo.wav  A4_vibrato.wav  E4_damp.wav  A3_art-fanzhu_v90.wav
   ```

   ```bash
   muser yinse extract ~/recordings/piano -o instruments/strike/grand-piano/grand-piano.yinse.json --name "…"
   ```

3. **meta.json** next to it (fields in the README); put the source, author, SPDX license and the mean spectral difference
   from `compare` (`compare_db`) in it. See [instruments/strike/grand-piano/meta.json](instruments/strike/grand-piano/meta.json).

4. **README.md** in the instrument's folder: credit for the recordings, how to play it, what was not extracted.

5. **Listen**: play a phrase with it in muser (`MUSER_YINSE_PATH=<this repository>`, `"instrument": "yinse:strike/grand-piano"`).

6. `uv run python scripts/index.py` checks every `meta.json` and regenerates `index.json`; then open a pull request.
