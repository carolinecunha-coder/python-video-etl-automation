# 🎬 Pipeline de Automação e ETL de Vídeo com Python

Projeto desenvolvido para automatizar o tratamento, padronização, compressão e concatenação de vídeos utilizando Python, MoviePy e FFmpeg.

O objetivo principal foi aplicar conceitos de Engenharia de Dados e ETL (Extract, Transform, Load) em arquivos de mídia não estruturados, simulando um pipeline real de processamento audiovisual.

---

# 🚀 Objetivos do Projeto

✔ Automatizar processamento de vídeos  
✔ Corrigir arquivos corrompidos  
✔ Padronizar resolução e codecs  
✔ Reduzir tamanho final do arquivo  
✔ Gerar saída compatível com navegadores web  
✔ Aplicar conceitos de ETL em mídia digital  

---

# 🛠 Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.11 | Lógica principal |
| MoviePy | Manipulação e renderização |
| FFmpeg | Conversão e tratamento de mídia |
| VS Code | Desenvolvimento |
| Git & GitHub | Versionamento |

---

# 📂 Estrutura do Projeto

```bash
python-video-etl-automation/
│
├── ajuste_video.py/
│   ├── limpar_video.py
│   └── projeto_final_web.mp4
│
└── README.md
```

---

# ⚙️ Funcionalidades Implementadas

## ✅ Tratamento de Arquivo Corrompido

Correção do erro crítico:

```python
OSError: failed to read the first frame
```

Utilizando reconstrução de metadados através do FFmpeg.

---

## ✅ Padronização de Resolução

Todos os vídeos foram convertidos dinamicamente para:

```python
1280x720 (HD)
```

Garantindo integridade visual entre diferentes arquivos de origem.

---

## ✅ Compatibilidade Web

Configuração otimizada utilizando:

```python
libx264
aac
```

Permitindo reprodução fluida diretamente em navegadores.

---

## ✅ Compressão Inteligente

Redução do arquivo final:

| Antes | Depois |
|---|---|
| 53,3 MB | 30,1 MB |

Com otimização de bitrate para carregamento mais rápido no GitHub.

---

# 🧠 Conceitos Aplicados

- ETL de mídia
- Data Cleaning
- Engenharia de Dados
- Processamento de arquivos
- Compressão de mídia
- Padronização de dados não estruturados
- Automação com Python

---

# 🎥 Demonstração do Resultado Final

Assista abaixo ao vídeo processado pelo pipeline:

<video 
src="https://github.com/carolinecunha-coder/python-video-etl-automation/raw/main/ajuste_video.py/projeto_final_web.mp4" 
controls 
width="900">
</video>

<br>

👉 Caso o player não carregue:

[Clique aqui para assistir diretamente](https://github.com/carolinecunha-coder/python-video-etl-automation/raw/main/ajuste_video.py/projeto_final_web.mp4)

---

# ▶️ Como Executar o Projeto

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

## 4️⃣ Execute o projeto

```bash
python ajuste_video.py
```

---

# 📈 Resultados Obtidos

✔ Correção automática de vídeos problemáticos  
✔ Redução significativa de tamanho  
✔ Compatibilidade multiplataforma  
✔ Pipeline automatizado de mídia  
✔ Estrutura preparada para escalabilidade  

---

# 👩‍💻 Autora

## Caroline Cunha

Especialista em Investimentos, Inteligência de Mercado & Seguros de Vida  
Em transição para Data Analytics e Engenharia de Dados.

🔗 GitHub:  
https://github.com/carolinecunha-coder

---
