from pytube import YouTube

VID_LINK = "https://www.youtube.com/watch?v=68-OouGkH4g"

yt_object = YouTube(VID_LINK)

info = yt_object
stream = info.streams[1]

stream.download("./outputs")
