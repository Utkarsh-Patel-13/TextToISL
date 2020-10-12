from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import os
from os.path import join, isfile

onlyfiles = [f for f in os.listdir('videos') if isfile(join('videos', f))]

for f in onlyfiles:
    try:
        clip = VideoFileClip(join('videos', f))
        video_length = clip.duration

        ffmpeg_extract_subclip(join('videos', f), 0, video_length/2, targetname=join('videos', 'edited', f).lower())
        print(f'Clipped file {f}')
    except Exception as e:
        print(str(e))
        print(f'Can not clip file {f}')