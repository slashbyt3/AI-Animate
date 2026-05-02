# 🎬 AI Animate

**Cinematic zoom + audio‑synced slideshows** – turn any set of images and narrated audio into a polished documentary video with professional Ken Burns effect, crossfades, and color grading.

![Example output](output_preview.gif)  
*(Replace with an actual GIF or link to your video)*

## ✨ Features
- **Smart aspect‑ratio cropping** – automatically forces all images to 16:9 without stretching.
- **Smooth & glitch‑free zoom** – custom per‑frame Ken Burns zoom (1.0 → 1.05x).
- **Audio alignment** – distributes images evenly across the length of each commentary track.
- **Crossfade transitions** – 0.5s overlaps for seamless chapter flow.
- **Cinematic color filter** – contrast boost, slight desaturation preservation + vignette.
- **Multi‑chapter support** – combine several `.wav` / image groups into one final video.

## 📦 Requirements
- Python 3.8+
- FFmpeg (installed separately – see below)
- Python packages (install via `pip`):

```bash
pip install numpy pillow moviepy
