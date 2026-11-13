# Sampling guide: what to record

English | [简体中文](sampling.zh-CN.md)

How many notes an instrument needs, how to record them, and how to tell whether it is enough.
The commands are in [CONTRIBUTING.md](../CONTRIBUTING.md).

## Short answer

You do not record every key at every velocity. muser blends between the nearest recorded pitches and velocities, so one
note is technically enough, but it only sounds right near that note. Record **a pitch every 3 semitones, each at 2-3
velocities**; on instruments with few strings or bars, record every one.

## How much is enough: measured

The grand piano in this library has 90 recordings (every 3 semitones, 3 velocities). Extracting from only some of them
and comparing against all 90 (`muser yinse compare`):

| recorded | notes | mean spectral difference | mean level difference | largest level difference |
|---|---|---|---|---|
| every 3 semitones × 3 velocities | 90 | 2.66 dB | 1.2 dB | -6.6 dB |
| every 3 semitones × 2 velocities | 60 | 2.87 dB | 2.0 dB | +7.6 dB |
| every 3 semitones × 1 velocity | 30 | 3.10 dB | 3.8 dB | -14.8 dB |
| every 6 semitones × 3 velocities | 45 | 3.46 dB | 2.1 dB | -13.7 dB |
| every 6 semitones × 2 velocities | 30 | 3.69 dB | 2.9 dB | -13.7 dB |
| every 12 semitones × 3 velocities | 24 | 3.83 dB | 2.1 dB | -8.1 dB |
| every 12 semitones × 1 velocity | 8 | 4.12 dB | 4.3 dB | -13.1 dB |

A spectral difference of 2-3 dB is close. Two things follow:

- **How many pitches decides how right the timbre is.** With 30 recordings, "every 3 semitones, one velocity" (3.10 dB)
  beats "every 6 semitones, two velocities" (3.69 dB).
- **How many velocities decides how right the loudness is.** With one velocity, soft and loud are the same sound turned
  down and up: 3.8 dB off on average and over 10 dB on some notes. Two layers bring it to 2 dB, three to 1.2 dB.

The source samples are themselves every 3 semitones, so whether recording more densely than that helps a piano was not
measured.

## What to record

- **Wide instruments whose timbre changes smoothly from key to key (piano)**: every 3 semitones (about 30 pitches on 88
  keys), each soft, medium and loud: about 90 notes. On a budget, soft and loud only: about 60.
- **Instruments with few strings or bars (guzheng 21 strings, guqin 7, yangqin, marimba)**: every string or bar.
  There are not many, and neighbouring strings do not differ smoothly, so a recording beats a blend.
- **Always the lowest and the highest note.** Outside the recorded range the nearest note is simply reused.
- **Both sides of a break in the timbre** (on a piano: wound to plain strings, one string to two to three). This is by
  reasoning, not measured.
- **Velocities really apart**: at least 3 dB between soft, medium and loud. Takes within 3 dB count as one velocity.
- **Other sounds** (mute, harmonic …): a few pitches each. Tremolo, vibrato and hand-damping: one recording each.

## How to record

- One strike or pluck per note; let it ring until it has died away (up to 20 s are used). Do not stop it by hand.
- Dry and quiet: close microphones, no reverb, nothing else still ringing. A steady hum is left out; reverb ends up in
  the decays.
- The same microphone position and gain for every note, and do not normalize files one by one: the level differences
  between soft and loud are the velocity response.
- Either one file per note with the pitch and velocity in the name (`A4_v80.wav`, `Eb3_pp.wav`), or one long take of
  notes played one after another (`muser yinse extract take.wav --split`). A take must be a sampling session, not a
  piece of music: one note at a time, each left to ring, quiet in between. In two solo performances tried, about one
  note in a hundred passed and the result was poor.
- Only struck or plucked sounds that ring away by themselves. Their partials need not be harmonics (bells, bars, drums),
  but those need one named file per note: `--split` measures the pitch and needs a clear one between C1 and E7.

## Is it enough?

```bash
muser yinse compare --between my.yinse.json recordings/
```

- **spectral**: how far the extracted note is from its recording. 2-3 dB is close.
- **level**: how much louder or softer it plays than the recording. More than a few dB on one velocity of a pitch means
  that layer is missing or the takes were too close in loudness.
- **between**: each recorded pitch is taken out, played blended from its neighbours and compared. If this is much worse
  than the spectral difference (the piano: 3.96 against 2.66 dB), the pitches are too far apart; record more next to the
  worst ones.

## What extraction cannot do

- Blown, bowed or sung sounds (anything held by the player).
- The first milliseconds of very high notes: the top piano notes come out 2-6 dB quieter over the first 2 s.
- Release noises (a piano key coming up) and the resonance of all strings under a sustain pedal.
- Timbre that follows a slide or a press: bends change the pitch, not the sound.
