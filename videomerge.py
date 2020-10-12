from moviepy.editor import *

input_string = "above absent access"
input_string = input_string.lower()

input_str_list = input_string.split()

output_clip_list = list()

for file_name in input_str_list:
    file_name += ".mp4"

    clip = VideoFileClip(os.path.join('videos', 'processed-dataset', file_name))

    output_clip_list.append(clip)

final_video = concatenate_videoclips(output_clip_list)
final_video.write_videofile(os.path.join('videos', 'output-sentence', 'test.mp4'))