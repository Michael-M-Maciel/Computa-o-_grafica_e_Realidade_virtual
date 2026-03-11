"""
Passo 1 — Criar Imagem de Teste e Pré-processar
Aula 03 — Análise de Placas de Carros com OpenCV
"""

import os
import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')   # backend sem janela (ideal para salvar arquivos direto)
import matplotlib.pyplot as plt

# Importamos as ferramentas que o professor definiu no arquivo de utilitários
from placas_utils import criar_placa_sintetica, pre_processar, SAIDA_DIR

# ── 1. Gerar a placa com seu nome ─────────────────────────────
# Mudamos o texto dentro das aspas para o seu nome personalizado
placa = criar_placa_sintetica("MIC1988") 

# Definimos onde salvar essa imagem (na pasta de saída configurada)
PLACA_PATH = os.path.join(SAIDA_DIR, "placa_Michael.png")
cv2.imwrite(PLACA_PATH, placa) 
print(f"Placa criada com sucesso: {PLACA_PATH}")

# ── 2. Pré-processar (Limpar a imagem) ────────────────────────
# Carregamos a imagem que acabamos de salvar
img = cv2.imread(PLACA_PATH) 

# Aplicamos os filtros: Cinza -> Blur -> Bordas (Canny)
cinza, blur, bordas = pre_processar(img) 

# ── 3. Visualizar o Resultado ─────────────────────────────────
# Criamos um painel com 4 colunas para ver a evolução do processo
fig, axes = plt.subplots(1, 4, figsize=(18, 4))
titles = ["Original (MIC1988)", "Cinza", "Gaussian Blur", "Canny Edges"]
imgs   = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cinza, blur, bordas]
cmaps  = [None, 'gray', 'gray', 'gray']

for ax, titulo, im, cmap in zip(axes, titles, imgs, cmaps):
    ax.imshow(im, cmap=cmap)
    ax.set_title(titulo, fontsize=12)
    ax.axis('off')

plt.tight_layout()
fig_path = os.path.join(SAIDA_DIR, "pipeline_pre_proc.png")
plt.savefig(fig_path, dpi=120)
print(f"Figura do pipeline salva em: {fig_path}")

print("\nPasso 1 concluído! O computador já consegue 'ver' os contornos da placa.")