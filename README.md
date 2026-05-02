# 🎬 AI Animate

**Cinematic zoom + audio‑synced slideshows** – turn any set of images and narrated audio into a polished documentary video with professional Ken Burns effect, crossfades, and color grading.

![Example output](output_preview.gif)  


## ✨ Features
- **Smart aspect‑ratio cropping** – automatically forces all images to 16:9 without stretching.
- **Smooth & glitch‑free zoom** – custom per‑frame Ken Burns zoom (1.0 → 1.05x).
- **Audio alignment** – distributes images evenly across the length of each commentary track.
- **Crossfade transitions** – 0.5s overlaps for seamless chapter flow.
- **Cinematic color filter** – contrast boost, slight desaturation preservation + vignette.
- **Multi‑chapter support** – combine several `.wav` / image groups into one final video.

## 📦 Requirements

- Python 3.8+
- FFmpeg (required by MoviePy for video encoding)

> **You might already have FFmpeg** – open a terminal and run `ffmpeg -version` to check. If you see version info, you're good to go.

### Installing FFmpeg (if not present)

Run the appropriate command for your operating system **in a terminal**:

| OS | Command |
|----|---------|
| **Windows** (with winget) | `winget install FFmpeg` |
| **Windows** (alternative) | Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH manually |
| **macOS** (with Homebrew) | `brew install ffmpeg` |
| **Linux (Ubuntu/Debian)** | `sudo apt install ffmpeg` |

After installation, restart your terminal and run `ffmpeg -version` to verify.

### Python packages

Install required Python libraries with:

```bash
pip install numpy pillow moviepy
