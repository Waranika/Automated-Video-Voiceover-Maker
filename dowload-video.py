from pytube import YouTube

#pip show <package name>

YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()
#Create a YouTube object
yt = YouTube(r"https://www.youtube.com/watch?v=x22TJMv2RYo")

# Get the highest resolution stream available
video_stream = yt.streams.get_highest_resolution()

# Download the video
video_stream.download(output_path=r"C:\Users\kizer\Downloads")

print("Download complete!")
