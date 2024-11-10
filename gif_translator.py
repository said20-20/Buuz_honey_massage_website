import os
from moviepy.editor import VideoFileClip

# Use raw strings for file paths
input_file = r"D:\Guac\Python_translation\dev_site\Buuz_honey_massage_website\assets\videos\signature-treatment.mp4"
output_file = r"D:\Guac\Python_translation\dev_site\Buuz_honey_massage_website\assets\videos\signature-treatment.gif"

# Check if the input file exists
if not os.path.isfile(input_file):
    raise FileNotFoundError(f"The input file was not found: {input_file}")

# Load the video clip
clip = VideoFileClip(input_file)

# Set high FPS and resolution for high quality
clip = clip.set_fps(60)  # Higher FPS for smoothness
clip = clip.resize(height=600)  # Higher resolution, adjust as needed

# Convert to high-quality GIF with color optimization
clip.write_gif(output_file, program='ffmpeg', opt='kmeans', fps=60)

print(f"Successfully created GIF: {output_file}")
