# Grand piano / 三角钢琴

`yinse:strike/grand-piano` · A0-C8 · 90 notes (every 3 semitones, 3 velocities) · about 600 KB

Extracted from the **Salamander Grand Piano** by **Alexander Holm** (a Yamaha C5), published under
[CC BY 3.0](https://creativecommons.org/licenses/by/3.0/), in the FreePats SFZ+FLAC edition
(<https://freepats.zenvoid.org/Piano/acoustic-grand-piano.html>). This instrument is a derivative of those recordings and is
shared under the same license: credit Alexander Holm (Salamander Grand Piano) when you use it.

从 Alexander Holm 录制的 Salamander Grand Piano（雅马哈 C5，CC BY 3.0）提取。这件乐器是这些录音的衍生作品，以同样的许可证分享；使用时请署名 Alexander Holm（Salamander Grand Piano）。

## Playing / 演奏

```json
{ "instrument": "yinse:strike/grand-piano", "clips": [{ "start": 0, "length": 8, "pedal": [[0, 3.9], [4, 7.9]], "notes": [ … ] }] }
```

- Notes stop when released (dampers, about 0.3 s); the clip's `pedal` holds them. 松键止音（约 0.3 秒），clip 的 `pedal` 踩住就继续响。
- Velocity 0-1 blends the three recorded layers; below the softest and above the loudest the level follows the velocity.
  力度在三层录音之间插值。
- The hammer's knock is in it (attack noise in ten octave bands). Not extracted: the key release noise and the resonance
  of the whole string set under the pedal. 击弦那一下的声音有（分十个频段的起音噪声）；没有提取：松键的机械声、踩踏板时整套弦的共鸣。

## How close / 和原采样差多少

`muser yinse compare --between` on the 90 notes: mean spectral difference 2.66 dB (third-octave bands, first 2 s, loudness
matched): 1.5 dB in the bass, about 3 dB in the middle, 3.6 dB above A6. Level within about 1 dB of the samples below
C6; 2-3 dB quieter from C6 up and 6 dB quieter at F#7 (over the first 2 s): the first 10 ms of the top notes are louder
in the samples than the partial tables can follow. Pitches blended from their neighbours (not recorded ones): 4.0 dB.
The steady low rumble in the samples is left out on purpose.
