import os
from moviepy.editor import VideoFileClip

input_video_path = r"D:\Guac\Python_translation\dev_site\Buuz_honey_massage_website\assets\videos\signature-treatment.mp4"
output_video_path = r"D:\Guac\Python_translation\dev_site\Buuz_honey_massage_website\assets\videos\signature-treatment-no-audio.mp4"

try:
    # Check if input video exists
    if not os.path.exists(input_video_path):
        raise FileNotFoundError(f"Input video file {input_video_path} not found.")

    # Load the video file
    video = VideoFileClip(input_video_path)

    # Remove the audio
    video_no_audio = video.without_audio()

    # Write the new video file
    video_no_audio.write_videofile(output_video_path, codec='libx264')

    print(f"Successfully created {output_video_path} without audio.")

except Exception as e:
    print(f"An error occurred: {e}")
