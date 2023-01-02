from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("Er is fout met de link")
  print("Download is gelukt")

link = input("Geef de de download link op")
Download(link)