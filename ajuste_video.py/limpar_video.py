from moviepy import VideoFileClip, concatenate_videoclips
import os

# --- CONFIGURAÇÃO DE CAMINHOS ---
# Usamos o video1 original e o video2 que você acabou de corrigir
caminho1 = r"C:\Projetos\ajuste_video.py\video1.mp4"
caminho2 = r"C:\Projetos\ajuste_video.py\video2_fix.mp4" 

pasta = os.path.dirname(caminho1)
caminho_final = os.path.join(pasta, "projeto_final.mp4")

# --- CARREGAR OS VÍDEOS ---
print("Carregando vídeos...")
video1 = VideoFileClip(caminho1)
video2 = VideoFileClip(caminho2)

# --- AJUSTAR TAMANHO (Aumentar a imagem) ---
# Redimensionamos ambos para 1280px de largura para ficarem grandes e padronizados
print("Redimensionando para HD...")
v1_ajustado = video1.resized(width=1280)
v2_ajustado = video2.resized(width=1280)

# --- JUNTAR OS VÍDEOS ---
print("Unindo os clipes...")
video_combinado = concatenate_videoclips([v1_ajustado, v2_ajustado], method="compose")

# --- SALVAR O RESULTADO ---
# Usamos libx264 e aac para máxima compatibilidade com o player do GitHub
video_combinado.write_videofile(
    caminho_final,
    codec="libx264",
    audio=True,
    audio_codec="aac",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True
)

print("-" * 30)
print(f"CONCLUÍDO! Seu vídeo final está em: {caminho_final}")
print("-" * 30)