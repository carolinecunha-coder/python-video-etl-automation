# 🎥 Pipeline de Automação e ETL de Mídia com Python

Este projeto foi desenvolvido para criar um fluxo automatizado de tratamento, redimensionamento, compressão e concatenação de arquivos de vídeo. O objetivo principal foi aplicar conceitos de Engenharia de Dados e ETL (Extract, Transform, Load) para o gerenciamento de mídias não estruturadas.

## 🛠️ Tecnologias e Bibliotecas
* **Python 3.11**
* **MoviePy v2.0** (Manipulação, corte e renderização de vídeo)
* **FFmpeg / static_ffmpeg** (Correção de metadados brutos e transcodificação de áudio)

## 🚀 Desafios Técnicos Solucionados (Data Cleaning & Otimização)
1. **Tratamento de Arquivo Corrompido:** Correção do erro crítico de leitura de frames (`OSError: failed to read the first frame`) reconstruindo os metadados dos clipes de origem através do FFmpeg.
2. **Padronização de Resolução:** Ajuste dinâmico de escala utilizando o método `.resized(width=1280)` para garantir a integridade visual (HD) entre clipes de fontes distintas.
3. **Compatibilidade de Codecs:** Configuração de saída otimizada com os codecs `libx264` e `aac` para garantir a reprodução fluida diretamente em navegadores web.
4. **Compressão Eficiente para Web:** Ajuste fino de taxa de dados (`bitrate="4000k"`), reduzindo o tamanho do arquivo final de 53,3 MB para 30,1 MB. Isso eliminou os alertas de limite do GitHub e otimizou o carregamento da página para os visitantes.

<img width="1016" height="714" alt="image" src="https://github.com/user-attachments/assets/e09227ba-0725-4b4d-add6-52e9833bc4c5" />

