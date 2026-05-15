import os
from moviepy import VideoFileClip

# Caminhos
pasta = r"C:\Projetos\ajuste_video.py"
arquivo_atual = os.path.join(pasta, "projeto_final.mp4")
arquivo_reduzido = os.path.join(pasta, "projeto_final_web.mp4")

print("Reduzindo o tamanho do vídeo para o GitHub...")

# Carrega o vídeo que você já criou
video = VideoFileClip(arquivo_atual)

# Salva com bitrate menor (isso vai garantir os < 50MB)
video.write_videofile(
    arquivo_reduzido,
    codec="libx264",
    bitrate="4000k", # Baixamos um pouco mais para garantir
    audio_codec="aac"
)

video.close()
print(f"PRONTO! Verifique o tamanho de: {arquivo_reduzido}")