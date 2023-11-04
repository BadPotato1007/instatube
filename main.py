from moviepy.editor import VideoFileClip, concatenate_videoclips
import os


i = 1
path="./vids/"
for filename in os.listdir(path):
    my_dest =str(i) + ".mp4"
    my_source =path + filename
    my_dest =path + my_dest
    # rename() function will
    # rename all the files
    os.rename(my_source, my_dest)
    i += 1
# N = 1
# F = 1

# # Load the four video clips
# clip1 = VideoFileClip(N + ".mp4")
# N = N+1
# clip2 = VideoFileClip(N + ".mp4")
# N = N+1
# clip3 = VideoFileClip(N + ".mp4")
# N = N+1
# clip4 = VideoFileClip(N + ".mp4")
# N = N+1

# # Concatenate the four video clips
# final_clip = concatenate_videoclips([clip1, clip2, clip3, clip4])

# # Write the final clip to a file
# final_clip.write_videofile("Final " + F + ".mp4")
