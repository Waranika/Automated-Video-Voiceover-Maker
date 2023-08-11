from moviepy.editor import VideoFileClip, ImageClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Paths to your video and screenshot image
video_path = 'path/to/your/video.mp4'
screenshot_path = 'path/to/your/screenshot.png'

# Load the video clip
video_clip = VideoFileClip(video_path)

# Load the screenshot image as an ImageClip
screenshot = ImageClip(screenshot_path)

# Set the duration of the screenshot to match the video clip's duration
screenshot = screenshot.set_duration(video_clip.duration)

# Overlay the screenshot on the video
final_clip = video_clip.overlay(screenshot, position=(0, 0))

# Set the audio of the final clip to match the video clip's audio
final_clip = final_clip.set_audio(video_clip.audio)

# Export the final clip
output_path = 'path/to/output/final_video.mp4'
final_clip.write_videofile(output_path, codec='libx264')