import os, PySimpleGUI as sg # https://www.youtube.com/watch?v=dQw4w9WgXcQ
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress 

desktop = r"c:\Users\Miguel\Desktop"
youtube_pasta = 'YouTube Python Downloads'
youtube_desktop = r"c:\Users\Miguel\Desktop\YouTube Python Downloads"
caminho = os.path.join(desktop, youtube_pasta)
MP3 = os.path.join(youtube_desktop, 'MP3')
MP4 = os.path.join(youtube_desktop, 'MP4')
PLAYLIST_AUDIO = os.path.join(youtube_desktop, 'Playlist - Audio')
PLAYLIST_VIDEO = os.path.join(youtube_desktop, 'Playlist - Video')
os.makedirs(caminho, exist_ok=True)
os.makedirs(MP3, exist_ok=True)
os.makedirs(MP4, exist_ok=True)
os.makedirs(PLAYLIST_AUDIO, exist_ok=True)
os.makedirs(PLAYLIST_VIDEO, exist_ok=True)

sg.theme("Darkgray")
caixa1 = False
caixa2 = False
caixa3 = False
interface = [
[sg.Titlebar("YOUTUBE LOADER", None, "white", "Black")],
[sg.Text("URL:")],
[sg.Input(size=(50, 1), key="url")],
[sg.Text("Formato:")],
[sg.Combo(['MP3 (Audio)', 'MP4 (Video)', 'Playlist (Audio)', 'Playlist (Video)'], default_value='Escolha o formato', key='-MODE-')],
[sg.Button("Download")]
]
janela = sg.Window("window", interface)

while True:
    evento, valor = janela.read()
    mode = valor['-MODE-']
    if valor == sg.WIN_CLOSED:
        break
    if evento == "Download":
        if mode == 'MP3 (Audio)':
            link = janela["url"].get()
            audio = YouTube(link)
            stream = audio.streams.get_audio_only().download(MP3)
            print("Download concluido!")
        if mode == 'MP4 (Video)':
            link = janela["url"].get()
            video = YouTube(link)
            stream = video.streams.get_highest_resolution().download(MP4)
            print("Download concluido!")
        if mode == 'Playlist (Audio)':
            link = janela["url"].get()
            pl = Playlist(link)
            for video in pl.videos:
                ys = video.streams.get_audio_only()
                ys.download(PLAYLIST_AUDIO)
        if mode == 'Playlist (Video)':
            link = janela["url"].get()
            pl = Playlist(link)
            for video in pl.videos:
                ys = video.streams.get_highest_resolution()
                ys.download(PLAYLIST_VIDEO)
        
janela.close()
exit()
#02/01/2025     