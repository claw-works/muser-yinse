# Adding an instrument

English | [简体中文](CONTRIBUTING.zh-CN.md)

The example below is the grand piano in this repository (`instruments/strike/grand-piano/`).
How many notes to record and how to check it is enough: [docs/sampling.md](docs/sampling.md).

1. **Check the license.** The recordings must allow redistribution and derivatives (see the README). The Salamander Grand
   Piano is CC BY 3.0, so it can go in with credit to Alexander Holm.

2. **Extract.** From an SFZ library, let muser play the notes itself (it also measures the dampers):

   ```bash
   mkdir -p instruments/strike/grand-piano
   muser yinse extract --from "sfz:/path/SalamanderGrandPiano-V3+20200602.sfz" \
     --pitches 21-108/3 --velocities 0.3,0.6,0.9 --hold 6 --notes-dir /tmp/piano-notes \
     -o instruments/strike/grand-piano/grand-piano.yinse.json --name "Grand Piano (Salamander, Yamaha C5)"
   muser yinse compare --between instruments/strike/grand-piano/grand-piano.yinse.json /tmp/piano-notes
   ```

   From recordings instead, one command turns a folder into the instrument. What the recordings need:

   - One note per file (wav, flac, aiff, ogg, mp3), one strike or pluck only. Silence before the note is fine; it must
     ring for at least 0.3 s after the attack, and one file that cannot be measured stops the whole extraction.
   - Let every note ring until it has died away (up to 20 s are used). Cut off early, the decay is a guess.
   - Dry and quiet: close microphone, no reverb, no other strings left ringing from the note before. A steady hum is left
     out; reverb ends up in the decays.
   - A pitch every 3-5 semitones over the range you want to play (every string or bar is better: check with `--between`),
     and 2-3 velocities per pitch. Stereo or mono; keep the microphones and the gain the same for all notes, and do not
     normalize the files one by one: the level differences between soft and loud are the velocity response.
   - Names carry the pitch (`A4`, `Eb3`, `C#5`, or a MIDI number), the velocity (`v80` on 0-127, `v0.7`, `pp` … `ff`) and
     the articulation. No pitch in the name: it is measured. No velocity: the files of one pitch are ordered soft to loud.
   - Optional: `mute`, `harmonic`, `back`, `pluck`, `staccato`, `rim`, `soft`, `hard` or `art-<name>` for other sounds
     (a few pitches each), and one recording each of a `tremolo`, a note with `vibrato`, a note stopped by hand (`damp`).

   ```text
   A4_v80.wav  A4_v80_mute.wav  D5_tremolo.wav  A4_vibrato.wav  E4_damp.wav  A3_art-fanzhu_v90.wav
   ```

   ```bash
   muser yinse extract ~/recordings/piano -o instruments/strike/grand-piano/grand-piano.yinse.json --name "…"
   muser yinse compare --between instruments/strike/grand-piano/grand-piano.yinse.json ~/recordings/piano
   ```

   Or record the whole session as **one take** and let muser cut it (`--split`):

   ```bash
   muser yinse extract take.wav --split --notes-dir take-notes -o instruments/pluck/guzheng/guzheng.yinse.json --name "…"
   muser yinse compare --between instruments/pluck/guzheng/guzheng.yinse.json take-notes
   ```

   What the take needs:

   - A sampling take, not a piece of music: one note at a time, one after another, any order. No chords, nothing played
     over a note that is still ringing.
   - Let each note ring until it has died away before the next, and do not stop the strings by hand. A note is used only
     when the one before it has fallen 20 dB below it and it rings at least 0.5 s before the next.
   - A clear pitch between C1 and E7 (it is measured). Bells, bars and drums need one file per note, named.
   - For velocities play each pitch soft, medium and loud, at least 3 dB apart (takes within 3 dB count as one).
   - Quiet between the notes (a cough is taken for a note and cuts the one before it short); a steady hum is fine.
   - Same microphones and gain throughout; several takes can be given at once.

   muser prints every note it found and whether it was used or why not. `--notes-dir` keeps the cut notes, named by
   pitch: listen to a few, delete or rename what is wrong, add `_mute` / `_v40` or gesture recordings, and run
   `extract` on that folder (without `--split`) to rebuild.

   `compare` prints, per recording, the spectral difference (2-3 dB is close), the level difference and the decays; with
   `--between`, also how far off the pitches you did not record are. To use it only on your own machine, stop here:
   `muser yinse install <file> --as strike/my-piano`, then `"instrument": "yinse:strike/my-piano"`.

3. **meta.json** next to it (fields in the README); put the source, author, SPDX license and the mean spectral difference
   from `compare` (`compare_db`, its last line) in it. See [instruments/strike/grand-piano/meta.json](instruments/strike/grand-piano/meta.json).

4. **README.md** in the instrument's folder: credit for the recordings, how to play it, what was not extracted.

5. **Listen**: play a phrase with it in muser (`MUSER_YINSE_PATH=<this repository>`, `"instrument": "yinse:strike/grand-piano"`).

6. `uv run python scripts/index.py` checks every `meta.json` and regenerates `index.json`; then open a pull request.
