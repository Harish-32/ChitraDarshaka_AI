from moviepy import VideoFileClip, AudioFileClip

video = VideoFileClip(
"outputs/trailer.mp4"
)
audio = AudioFileClip(
"outputs/trailer_voice.mp3"
).subclipped(0, 15)

final = video.with_audio(15)
final.write_videofile(
"outputs/final_trailer.mp4",
codec="libx264",
audio_codec="aac"
)