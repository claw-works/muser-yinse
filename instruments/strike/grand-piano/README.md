# Grand piano / 三角钢琴

`yinse:strike/grand-piano` · A0-C8 · 90 notes (every 3 semitones, 3 velocities) · about 430 KB

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
- Not extracted: the hammer and key release noises and the resonance of the whole string set under the pedal.
  没有提取：击弦与松键的机械声、踩踏板时整套弦的共鸣。

## How close / 和原采样差多少

`muser yinse compare` on the 90 notes: mean spectral difference 3.77 dB (third-octave bands, first 2 s, loudness matched);
2-3 dB in the bass and middle, the most at C8 (about 10 dB, where only one partial is measured).
