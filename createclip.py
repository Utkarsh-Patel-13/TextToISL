from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

from uuid import uuid4

def create_video(input_string: str):
    try:

        # input_string = "My account empty I am poor I want money"

        input_string = input_string.lower()

        input_str_list = input_string.split()

        output_clip_list = list()

        for file_name in input_str_list:
            file_name += ".mp4"
            try:
                clip = None
                clip = VideoFileClip(os.path.join('videos', 'processed-dataset-2', file_name))
                output_clip_list.append(clip)
            except Exception as e:
                print(e)
                print(f'{file_name} not found...')
            
        id = uuid4()

        f_name = str(id) + '.mp4'

        path = os.path.join('static', 'videos', f_name)

        final_video = concatenate_videoclips(output_clip_list)
        final_video.write_videofile(path)

        if os.path.exists(path):
            return f_name

        else:
            return None

    except Exception as e:
        print(e)
        return None