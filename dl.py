import youtube_dl 


video = {}
url = "https://youtu.be/rruVLXierXU"
with youtube_dl.YoutubeDL(video) as ydl:
 ydl.download([url])
