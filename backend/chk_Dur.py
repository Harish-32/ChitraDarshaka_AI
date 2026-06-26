from moviepy import VideoFileClip, AudioFileClip

video = VideoFileClip("trailer.mp4")
audio = AudioFileClip("story.mp3")

print("Video Duration:", video.duration)
print("Audio Duration:", audio.duration)