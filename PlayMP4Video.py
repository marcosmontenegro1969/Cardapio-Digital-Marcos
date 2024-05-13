import vlc
import tkinter as tk
from tkinter import ttk
import sys

def play_video_vlc(file_path):
    root = tk.Tk()
    window_width = 400
    window_height = 225
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)
    vertical_offset = screen_height * 0.20
    y = (screen_height / 2 - window_height / 2) + vertical_offset

    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

    # Configura as opções do VLC para suprimir logs, defina 'verbose' para 0.
    vlc_instance = vlc.Instance('--quiet', '--verbose=0')

    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(file_path)
    media.add_option('input-repeat=-1')  # Opção para repetir vídeo se necessário.
    player.set_media(media)

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    video_panel = ttk.Frame(frame)
    video_panel.pack(fill=tk.BOTH, expand=True)

    video_handle = video_panel.winfo_id()
    player.set_hwnd(video_handle)
    player.play()

    def check_end():
        if player.get_state() == vlc.State.Ended:
            player.stop()
            root.destroy()
        else:
            root.after(1000, check_end)

    check_end()
    root.mainloop()

if len(sys.argv) > 1:
    video_path = sys.argv[1]
    play_video_vlc(video_path)
else:
    print("Nenhum arquivo de vídeo foi especificado.")
