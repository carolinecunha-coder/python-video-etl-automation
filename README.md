# 🎥 Pipeline de Automação e ETL de Mídia com Python

Este projeto foi desenvolvido para criar um fluxo automatizado de tratamento, redimensionamento, compressão e otimização de arquivos de vídeo utilizando Python.

O objetivo principal foi aplicar conceitos de Engenharia de Dados e ETL (Extract, Transform, Load) no processamento de mídias não estruturadas.

---

# 🚀 Objetivos do Projeto

✅ Automatizar tratamento de vídeos  
✅ Corrigir incompatibilidades de codec  
✅ Padronizar resolução  
✅ Reduzir tamanho final do arquivo  
✅ Garantir compatibilidade com navegadores  
✅ Criar mídia otimizada para GitHub  

---

# 🛠 Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.11 | Automação |
| MoviePy | Manipulação de vídeo |
| FFmpeg | Conversão e compressão |
| VS Code | Desenvolvimento |
| GitHub | Versionamento |

---

# 📂 Estrutura do Projeto

```bash
python-video-etl-automation/
│
├── ajuste_video.py/
│   ├── limpar_video.py
│   ├── projeto_final_web.mp4
│   └── projeto_github.mp4
│
└── README.md
```

---

# ⚙️ Funcionalidades Implementadas

## ✅ Compressão Inteligente

Conversão otimizada para web utilizando:

```python
codec="libx264"
audio_codec="aac"
bitrate="2500k"
```

---

## ✅ Compatibilidade HTML5

Exportação utilizando:

```python
-pix_fmt yuv420p
-movflags +faststart
```

Permitindo reprodução em:
- GitHub
- Navegadores
- Players HTML5

---

## ✅ Correção Automática de Resolução

Tratamento automático para resolver erros:

```python
width not divisible by 2
height not divisible by 2
```

Ajustando largura e altura para números pares.

---

# 🧠 Conceitos Aplicados

- ETL
- Data Cleaning
- Engenharia de Dados
- Compressão de mídia
- Automação com Python
- Tratamento de erros
- Compatibilidade web
- Processamento de arquivos multimídia

---

# 🎬 Demonstração do Resultado Final

<video 
src="https://raw.githubusercontent.com/carolinecunha-coder/python-video-etl-automation/main/ajuste_video.py/projeto_github.mp4" 
controls 
width="900">
</video>

---

# ▶ Assistir Diretamente

👉 [Clique aqui para assistir ao vídeo](https://raw.githubusercontent.com/carolinecunha-coder/python-video-etl-automation/main/ajuste_video.py/projeto_github.mp4)

---

# 💻 Exemplo do Código Utilizado

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

# ▶ Como Executar

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/carolinecunha-coder/python-video-etl-automation.git
```

---

## 2️⃣ Acesse a pasta

```bash
cd python-video-etl-automation
```

---

## 3️⃣ Instale as dependências

```bash
pip install moviepy
```

---

## 4️⃣ Execute o script

```bash
python limpar_video.py
```

---

# 📈 Resultados Obtidos

✅ Redução significativa do tamanho do vídeo  
✅ Compatibilidade com GitHub  
✅ Compatibilidade HTML5  
✅ Reprodução em navegadores  
✅ Pipeline automatizado de mídia  

---

# 👩‍💻 Autora

## Caroline Cunha

Especialista em Investimentos, Inteligência de Mercado & Seguros de Vida  
Em transição para Data Analytics e Engenharia de Dados.

🔗 GitHub:  
https://github.com/carolinecunha-coder

---
