# importing editor from movie py
from moviepy.editor import *

# file name
pic = "image.jpeg"

# Screen size
screensize = (720, 460)

# Create a clip from the video
image_clip = ImageClip(pic, duration=5).set_start(0)

# Create a text clip
txt_clip = TextClip('It Works', color='white', font="Amiri-Bold", kerning=5, fontsize=100)

# Center the text in the video
text_center = CompositeVideoClip([txt_clip.set_position('center')], size=screensize)

# Combine the video and the text
video = [CompositeVideoClip([image_clip, text_center]).subclip(0, 5)]

# Try to add a slide effect
# slided_clips = CompositeVideoClip([frames.fx(transfx.slide_out, duration=1, side='left')])

# Actually it's useless
final_clip = concatenate_videoclips(video, padding=-1)

# Export the video
final_clip.write_videofile('output.webm', fps=25, codec='libvpx')
