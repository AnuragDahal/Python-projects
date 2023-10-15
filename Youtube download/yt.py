import youtube_dl as yt

url=input("Enter the url of the video: \n")

with yt.YoutubeDL() as ydl:
    ydl.download([url])
