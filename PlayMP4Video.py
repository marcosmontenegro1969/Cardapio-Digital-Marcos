import vlc
import tkinter as tk
from tkinter import ttk

'''
Este código mostra como reproduzir um arquivo de vídeo MP4 (video e audio) usando o VLC Media Player,
embutido em um frame tkinter. Antes da execução, é definido o tamanho e posição da janela de exibição.'''

def play_video_vlc(file_path):
    # Cria uma instância do frame tkinter
    root = tk.Tk()
    window_width = 400
    window_height = 225
    screen_width = root.winfo_screenwidth()  # Obtém a largura da tela
    screen_height = root.winfo_screenheight()  # Obtém a altura da tela

    # Calcula as coordenadas x e y para a janela Tk root
    x = (screen_width/2) - (window_width/2)
    
    # Posiciona y um pouco abaixo do centro, vamos dizer 20% abaixo
    vertical_offset = screen_height * 0.20  # 20% da altura da tela
    y = (screen_height / 2 - window_height / 2) + vertical_offset
    
    # Define a geometria da janela tkinter e posiciona no centro
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

    # Cria o player VLC
    player = vlc.MediaPlayer(file_path)

    # Incorpora o player VLC em um frame na janela tkinter
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    video_panel = ttk.Frame(frame)
    video_panel.pack(fill=tk.BOTH, expand=True)

    # Obtém o identificador para o frame de vídeo e passa para o VLC
    video_handle = video_panel.winfo_id()  # Obtém o ID da janela do frame
    player.set_hwnd(video_handle)  # Passa para o VLC renderizar o vídeo neste frame

    # Começa a reproduzir o vídeo
    player.play()

    # Monitora a reprodução e fecha quando terminar
    def check_end():
        if player.get_state() == vlc.State.Ended:
            player.stop()
            root.destroy()
        else:
            root.after(1000, check_end)  # Verifica a cada 1000ms

    check_end()

    # Inicia o loop de eventos do tkinter
    root.mainloop()

# Finalmente executa o vídeo
play_video_vlc(r"C:\Cesar_School\PROJETO\Codigo_Python\Strogonoff.mp4")
