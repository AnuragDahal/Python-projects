import moviepy.editor as mp
import os

path=input("Enter the path of the video: ")

videoclip=mp.VideoFileClip(path)#path of the video
audioclip=videoclip.audio#extracting audio from the video
audioclip.write_audiofile("audio.mp3")
audioclip.close()
videoclip.close()
print("Audio extracted successfully!")


