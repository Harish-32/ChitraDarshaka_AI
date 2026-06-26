from moviepy import ImageClip, concatenate_videoclips, AudioFileClip

images = [
    "outputs/scene1.png",
    "outputs/scene2.png",
    "outputs/scene3.png",
    "outputs/scene4.png",
    "outputs/scene5.png"
]

audio = AudioFileClip(
    "outputs/trailer_voice.mp3"
)

duration_per_image = 3

clips = []

for img in images:

    clip = (
        ImageClip(img)
        .with_duration(duration_per_image)
    )

    clips.append(clip)

video = concatenate_videoclips(clips)

video.write_videofile(
    "outputs/trailer.mp4",
    fps=24
)

print("✅ Trailer Created Successfully")