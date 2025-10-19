from pytubefix import YouTube # https://www.youtube.com/watch?v=dQw4w9WgXcQ
from pytubefix.cli import on_progress, Playlist

def pytube():

    playlist = False

    def escolha():
        print("1- Video"); print("2- Audio")
        escolha = int(input("Esolha usando os numeros: "))
        if escolha == 1:
            if playlist:
                for video in pl.videos:
                    stream = video.streams.get_highest_resolution()
                    stream.download(output_path="downloads pytube")
            else:
                stream = yt.streams.get_highest_resolution()
                stream.download(output_path="downloads pytube")


        elif escolha == 2:
            if playlist:
                for video in pl.videos:
                    stream = video.streams.get_audio_only()
                    stream.download(output_path="downloads pytube")
            else:
                stream = yt.streams.get_audio_only()
                stream.download(output_path="downloads pytube")

    url = input("URL >> ")
    substring = "playlist"

    if substring in url: # detecta que é uma playlist
        playlist = True
        pl = Playlist(url)
        escolha()
        print(f"Titulo da playlist: {pl.title}")
        print("Download concluido.")

    else:
        yt = YouTube(url, on_progress_callback = on_progress)
        escolha()
        print(f"Titulo do video: {yt.title}")
        print("Download concluido.")

    novamente = input("Deseja baixar novamente? s/n")
    if novamente == "n":
        exit
    else:
        pytube()

pytube()
