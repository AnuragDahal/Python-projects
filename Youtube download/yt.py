from pytube import YouTube

path="C:/Users/freef/Videos"
link=input("Enter the link: ")
yt=YouTube(link)
ys=yt.streams.get_highest_resolution()
print("Downloading...")
ys.download(path)
print("Download completed!!")