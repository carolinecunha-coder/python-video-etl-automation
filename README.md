🎥 Pipeline de Automação e Otimização de Vídeo com Python
Arquivos de vídeo não padronizados que quebram em navegadores ou estouram o limite de upload do GitHub são gargalos comuns em automações de mídia.

Desenvolvido para mitigar essas dores, este projeto implementa um pipeline inteligente em Python 3.11 que atua na limpeza e transformação de arquivos de vídeo. A automação valida a integridade das dimensões exigidas pelo FFmpeg, aplica compressão de bitrate otimizada e força a conversão para codecs universais (libx264/aac), garantindo compatibilidade multiplataforma imediata.

🛠 Highlights: Código Limpo | Tratamento de Erros em Tempo de Execução | Otimização de Performance Web

🚀 Funcionalidades
✅ Compressão inteligente de vídeo
✅ Conversão para codec compatível com navegadores
✅ Padronização automática de resolução
✅ Correção de incompatibilidades do FFmpeg
✅ Otimização para GitHub
✅ Reprodução HTML5
✅ Conversão de vídeo para GIF animado

🛠 Tecnologias Utilizadas
Python 3.11
MoviePy
FFmpeg
GitHub
HTML5 Video
EZGIF
📂 Estrutura do Projeto
ajuste_video.py/
├── limpar_video.py
├── projeto_github.mp4
├── preview.gif
└── README.md
⚙️ Principais Ajustes Técnicos
✅ Correção de resolução incompatível
Tratamento automático dos erros:

width not divisible by 2
height not divisible by 2
Ajustando largura e altura para números pares.

✅ Compatibilidade Web
Conversão utilizando:

codec="libx264"
audio_codec="aac"
Compatível com:

GitHub
Navegadores
HTML5
✅ Compressão otimizada
Redução do tamanho final do vídeo utilizando:

bitrate="2500k"
✅ Conversão para GIF
Utilização da ferramenta EZGIF para gerar prévia animada da automação exibida diretamente no README do GitHub.

Configurações utilizadas:

720p
FPS 10
Loop infinito
Otimização para web
🎞 Prévia da Automação
Preview do Projeto

📹 Vídeo Completo
▶ Clique aqui para assistir ao vídeo completo
💻 Código Principal
import os
from moviepy import VideoFileClip

pasta = r"C:\Projetos\ajuste_video.py"

arquivo_atual = os.path.join(pasta, "projeto_github.mp4")

video = VideoFileClip(arquivo_atual)

largura = video.w
altura = video.h

if largura % 2 != 0:
    largura -= 1

if altura % 2 != 0:
    altura -= 1

video = video.resized((largura, altura))

video.write_videofile(
    "video_otimizado.mp4",
    codec="libx264",
    audio_codec="aac",
    bitrate="2500k"
)
🌐 Ferramenta Utilizada para Conversão GIF
EZGIF:
https://ezgif.com/video-to-gif

📈 Conceitos Aplicados
ETL
Automação com Python
Processamento de mídia
Compressão de vídeo
Tratamento de erros
Compatibilidade web
Engenharia de Dados
👩‍💻 Autora
Caroline Cunha
Especialista em Investimentos, Inteligência de Mercado & Seguros de Vida
Em transição para Data Analytics e Engenharia de Dados.

🔗 GitHub:
https://github.com/carolinecunha-coder
