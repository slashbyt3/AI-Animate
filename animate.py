import os
import numpy as np
from PIL import Image
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def ken_burns_zoom(get_frame, t, duration, initial_size=(1920, 1080)):
    """
    Manually processes every frame to ensure smooth zoom and zero glitches.
    """
    frame = get_frame(t)
    # Slow, high-end zoom (1.0 to 1.05)
    zoom_factor = 1 + (0.05 * (t / duration))
    
    img = Image.fromarray(frame)
    new_w = int(initial_size[0] * zoom_factor)
    new_h = int(initial_size[1] * zoom_factor)
    
    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Center crop back to 1080p
    left = (new_w - 1920) / 2
    top = (new_h - 1080) / 2
    right = (new_w + 1920) / 2
    bottom = (new_h + 1080) / 2
    
    return np.array(img.crop((left, top, right, bottom)))

def create_cinematic_clip(image_path, duration):
    """
    Pre-processes images for perfect 16:9 aspect ratio and applies manual zoom.
    """
    img = Image.open(image_path).convert("RGB")
    target_ratio = 1920 / 1080
    w, h = img.size
    
    # Aspect Ratio Correction (Prevents 'Broadened' look)
    if (w / h) > target_ratio:
        new_w = int(target_ratio * h)
        offset = (w - new_w) / 2
        img = img.crop((offset, 0, w - offset, h))
    else:
        new_h = int(w / target_ratio)
        offset = (h - new_h) / 2
        img = img.crop((0, offset, w, h - offset))

    img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
    clip = ImageClip(np.array(img)).set_duration(duration).set_fps(24)
    
    # Apply manual zoom engine
    return clip.fl(lambda gf, t: ken_burns_zoom(gf, t, duration))

def build_documentary():
    final_clips = []
    chapters = [
        ("01_the_fortress.wav", "ch1"),
        ("02_the_recon.wav", "ch2"),
        ("03_the_heist.wav", "ch3"),
        ("04_the_fatigue.wav", "ch4"),
        ("05_the_ashes.wav", "ch5")
    ]
    
    print("🎬 Starting Master Polish Render...")

    for audio_file, prefix in chapters:
        if not os.path.exists(audio_file):
            print(f"⚠️ Skipping {audio_file}: File not found.")
            continue
            
        audio = AudioFileClip(audio_file)
        imgs = sorted([f for f in os.listdir() if f.startswith(prefix) and f.endswith(".png")])
        
        if not imgs:
            continue
            
        img_dur = audio.duration / len(imgs)
        
        # Create clips with 0.5s Crossfade for smooth AI transitions
        chapter_clips = []
        for i, img_path in enumerate(imgs):
            print(f"🎞️ Processing: {img_path}")
            clip = create_cinematic_clip(img_path, img_dur)
            
            if i > 0:
                # Overlap clips by 0.5s for the crossfade effect
                clip = clip.crossfadein(0.5)
            chapter_clips.append(clip)
            
        # Combine with 'compose' method to handle the crossfade overlaps
        chapter_video = concatenate_videoclips(chapter_clips, method="compose", padding=-0.5).set_audio(audio)
        final_clips.append(chapter_video)

    print("\n🚀 Exporting Final Polished Documentary...")
    full_movie = concatenate_videoclips(final_clips)
    
    # MASTER POLISH FILTERS:
    # 1. Boost contrast (1.1)
    # 2. Lower brightness (-0.02)
    # 3. Increase saturation (1.2) for that 'Cyber' look
    # 4. Apply Vignette to draw eyes to the center
    color_filter = "eq=contrast=1.1:brightness=-0.02:saturation=1.2, vignette=PI/4"

    full_movie.write_videofile(
        "Scattered_Spider_POLISHED.mp4", 
        fps=24, 
        codec="libx264", 
        audio_codec="aac",
        ffmpeg_params=[
            "-pix_fmt", "yuv420p", 
            "-vf", color_filter
        ],
        threads=4
    )
    
    print("\n🏁 Polished Render Complete: Scattered_Spider_POLISHED.mp4")

if __name__ == "__main__":
    build_documentary()