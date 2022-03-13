from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

video = askopenfilename()
clip = VideoFileClip(video)
save_path = asksaveasfilename()
clip.write_gif(save_path+".gif",fps=10)

