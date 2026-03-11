"""
Passo 3 — Extrair e Corrigir a Perspectiva da Placa
Aula 03 — Análise de Placas de Carros com OpenCV
"""

import os
import cv2
# Importamos as funções de extração e correção e o diretório de saída
from placas_utils import extrair_placa, corrigir_perspectiva, encontrar_candidatos_placa, SAIDA_DIR

# ── 1. Carregar a imagem da sua placa "MIC1988" ───────────────────────────
PLACA_PATH = os.path.join(SAIDA_DIR, "placa_Michael.png")
img = cv2.imread(PLACA_PATH)

if img is None:
    print(f"ERRO: execute o passo 1 e 2 primeiro.")
    exit(1)

# ── 2. Localizar novamente os candidatos (como no Passo 2) ────────────────
candidatos = encontrar_candidatos_placa(img, debug=False)

# ── 3. Processar a Extração da Região de Interesse (ROI) ──────────────────
if len(candidatos) > 0:
    # Pegamos o primeiro candidato encontrado (geralmente o melhor)
    contorno, bbox = candidatos[0] # bbox contém (x, y, w, h) [cite: 595-596]
    
    # MÉTODO A: Recorte simples (Crop)
    # A função extrair_placa recorta o retângulo e adiciona uma pequena margem [cite: 593-598]
    placa_recortada = extrair_placa(img, bbox)
    
    # MÉTODO B: Correção de Perspectiva (Warp)
    # Esta função identifica os 4 cantos e "estica" a placa para 400x130 pixels [cite: 606, 633]
    # É essencial para fotos tiradas em ângulos inclinados [cite: 608]
    placa_corrigida = corrigir_perspectiva(img, contorno)
    
    # ── 4. Salvar os resultados para o próximo passo (OCR) ────────────────
    # Salvamos a placa recortada "limpa" para que o Tesseract/EasyOCR possa ler depois
    ROI_PATH = os.path.join(SAIDA_DIR, "placa_roi_MIC1988.png")
    cv2.imwrite(ROI_PATH, placa_corrigida)
    
    print(f"Sucesso! Região da placa extraída e corrigida em: {ROI_PATH}")
    print(f"Tamanho da imagem final: {placa_corrigida.shape[1]}x{placa_corrigida.shape[0]} pixels")
else:
    print("Nenhum candidato a placa foi encontrado para extração.")

print("\nPasso 3 concluído com sucesso!")