# 🎥 Pipeline de Automação e ETL de Mídia com Python

Este projeto foi desenvolvido para criar um fluxo automatizado de tratamento, redimensionamento, compressão e concatenação de arquivos de vídeo.

O objetivo principal foi aplicar conceitos de Engenharia de Dados e ETL (Extract, Transform, Load) no processamento de mídias não estruturadas utilizando Python.

---

# 🛠 Tecnologias e Bibliotecas

- **Python 3.11**
- **MoviePy**
- **FFmpeg**
- **Static FFmpeg**
- **HTML5 Video**
- **GitHub**

---

# 🚀 Funcionalidades

✅ Leitura automatizada de vídeos  
✅ Padronização de resolução  
✅ Conversão de codecs incompatíveis  
✅ Compressão inteligente para web  
✅ Compatibilidade com navegadores  
✅ Geração de vídeo otimizado para GitHub  

---

# 📂 Estrutura do Projeto

```bash
python-video-etl-automation/
│
├── ajuste_video.py/
│   ├── limpar_video.py
│   ├── projeto_github.mp4
│
└── README.md
```

---

# 🧠 Desafios Técnicos Solucionados (Data Cleaning & Otimização)

### 1. Tratamento de Arquivo Corrompido
Correção do erro crítico de leitura de frames:

```python
OSError: failed to read the first frame
```

Reconstruindo os metadados dos vídeos através do FFmpeg.

---

### 2. Padronização de Resolução
Correção automática de dimensões incompatíveis com `libx264`:

```python
width not divisible by 2
height not divisible by 2
```

Ajustando largura e altura para valores pares.

---

### 3. Compatibilidade de Codecs
Conversão otimizada utilizando:

- `libx264`
- `aac`
- `yuv420p`

Garantindo reprodução em:
- GitHub
- Navegadores
- Players HTML5

---

### 4. Compressão para Web
Redução inteligente de bitrate:

```python
bitrate="2500k"
```

Diminuindo drasticamente o tamanho do arquivo sem perda visual relevante.

---

# 🎬 Demonstração do Resultado Final

<video 
src="https://github.com/carolinecunha-coder/python-video-etl-automation/raw/main/ajuste_video.py/projeto_github.mp4" 
controls 
width="900">
</video>

---

# ▶ Assistir Diretamente

👉 [Clique aqui para assistir ao vídeo final](https://github.com/carolinecunha-coder/python-video-etl-automation/raw/main/ajuste_video.py/projeto_github.mp4)

---

# 💻 Exemplo de Código Utilizado

```python
from moviepy import VideoFileClip

video = VideoFileClip("projeto_final_web.mp4")

video.write_videofile(
    "projeto_github.mp4",
    codec="libx264",
    audio_codec="aac",
    bitrate="2500k"
)
```

---

# 📈 Conceitos Aplicados

- Engenharia de Dados
- ETL
- Data Cleaning
- Compressão de mídia
- Automação com Python
- Manipulação de vídeo
- Tratamento de erros
- Otimização para Web
- Compatibilidade multiplataforma

---

# 👩‍💻 Autora

**Caroline Cunha**  
Especialista em Investimentos, Inteligência de Mercado & Seguros de Vida  
Em transição para Data Analytics e Engenharia de Dados.

GitHub:  
https://github.com/carolinecunha-coder
