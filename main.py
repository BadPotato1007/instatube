from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import random

clips = []
i = 1
path="./toprocess/"
for filename in os.listdir(path):
    my_dest = "./processed/" + str(i) + ".mp4"
    my_source =path + filename
    # rename() function will
    # rename all the files
    os.rename(my_source, my_dest)
    i += 1


# filenames = os.listdir("./processed/")  # You could generate this from os.listdir or similar
# clips = []

# for file in filenames:
#     clips.append(VideoFileClip(file, target_resolution=(1080, 1920)))

# final_clip = concatenate_videoclips(clips)  # method="chain" by default. This is fine because all clips are the same size
# final_clip.write_videofile("out.mp4")

N = 1
F = 1
# Load the four video clips
clip1 = VideoFileClip("./processed/" + str(N) + ".mp4", target_resolution=(720, 1280))  # can be 1080, 1920 for full hd
N = N+1
clip2 = VideoFileClip("./processed/" + str(N) + ".mp4", target_resolution=(720, 1280))
N = N+1
clip3 = VideoFileClip("./processed/" + str(N) + ".mp4", target_resolution=(720, 1280))
N = N+1
clip4 = VideoFileClip("./processed/" + str(N) + ".mp4", target_resolution=(720, 1280))
N = N+1
# Concatenate the four video clips
final_clip = concatenate_videoclips([clip1, clip2, clip3, clip4])

# Write the final clip to a file
final_clip.write_videofile("Final " + str(F) + ".mp4", threads = 4, fps=30)
