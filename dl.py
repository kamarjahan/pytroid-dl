import youtube_dl
import os

video = {}
url = "https://www.youtube.com/watch?v=Wch3gJG2GJ4"
with youtube_dl.YoutubeDL(video) as ydl:
 ydl.download([url])
