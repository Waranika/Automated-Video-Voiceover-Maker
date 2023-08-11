# Automated Video Voiceover Maker
The Automated Video Voiceover Maker is a Python script that automates the process of creating video voiceovers by combining video clips and audio from YouTube videos. This project utilizes the moviepy library for video editing and the pytube library for downloading YouTube videos.

Table of Contents
Overview
Features
Requirements
Installation
Usage


## Overview
Creating video voiceovers manually can be time-consuming and labor-intensive. The Automated Video Voiceover Maker aims to simplify this process by providing a Python script that automatically downloads YouTube videos and combines them with other video clips, allowing you to focus on creating content rather than managing technical details.

## Features
Download YouTube videos using the pytube library.
Combine downloaded videos and other video clips using the moviepy library.
Easily customize the video and audio sources for your voiceover.
Automation of the voiceover creation process reduces manual effort.
## Requirements
Python 3.x
pytube library (for video downloading)
moviepy library (for video editing)
ffmpeg (for audio and video encoding, required by moviepy)
## Installation
Clone this repository:

'''
git clone https://github.com/your-username/automated-video-voiceover.git
'''
Navigate to the project directory:

'''
cd automated-video-voiceover
'''
Install the required Python packages:

'''
pip install -r requirements.txt
'''
Install ffmpeg if you haven't already (required by moviepy):


Download the ffmpeg executable from https://www.ffmpeg.org/download.html and add it to your system's PATH.

## Usage

Run the script:

'''
python make_voiceover.py
'''
The script will download the YouTube video, combine it with other video clips, and create the final voiceover video.




