import youtube_dl
import os
from sample_config import Config


video = {}
url = "https://www.youtube.com/watch?v=Bb8bnjnEM00"
with youtube_dl.YoutubeDL(video) as ydl:
 ydl.download([url])
