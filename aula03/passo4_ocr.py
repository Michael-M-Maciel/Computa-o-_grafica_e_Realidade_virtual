"""
Passo 4 — OCR: Ler os Caracteres da Placa
Aula 03 — Análise de Placas de Carros com OpenCV
"""

import os
import cv2
# Importamos as funções de OCR e utilitários do professor
from placas_utils import criar_placa_sintetica, ocr_tesseract, ocr_easyocr, SAIDA_DIR

# ── 1. Carregar a imagem da placa extraída no Passo 3 ────────────────────────
# Tentamos ler a imagem "placa_roi_simples.png" gerada anteriormente [cite: 651, 693]
img_placa = cv2.imread(os.path.join(SAIDA_DIR, "placa_roi_MIC1988.png"))

if img_placa is None:
    # Se você não rodou o passo anterior, o código gera uma placa na hora
    # Isso garante que o script não pare de funcionar (mecanismo de segurança)
    print("ROI não encontrado — usando placa sintética direta.")
    img_placa = criar_placa_sintetica("MIC1988")

# ── 2. Opção A: Tesseract OCR ───────────────────────────────────────────────
# O Tesseract é um motor de OCR offline muito potente e tradicional [cite: 656, 658]
print("=== Tesseract OCR ===")
try:
    # A função ocr_tesseract faz três coisas cruciais internamente:
    # 1. Aumenta a imagem (Resize 2x) para facilitar a leitura .
    # 2. Binariza (Threshold) para deixar o fundo branco e as letras pretas .
    # 3. Usa a configuração "--psm 7" (tratar como uma única linha) [cite: 676-678].
    texto_tess, thresh = ocr_tesseract(img_placa)
    
    print(f"Resultado: '{texto_tess}'")
    
    # Salva a imagem binarizada (preto e branco) para conferirmos o que o OCR "viu"
    thresh_path = os.path.join(SAIDA_DIR, "placa_thresh_MIC1988.png")
    cv2.imwrite(thresh_path, thresh)
    print(f"Threshold salvo em: {thresh_path}")

except Exception as e:
    # Erro comum: Tesseract não instalado no Windows/Linux/Mac [cite: 455-459]
    print(f"Tesseract não disponível ou erro: {e}")

# ── 3. Opção B: EasyOCR ─────────────────────────────────────────────────────
# O EasyOCR usa Redes Neurais Profundas (Deep Learning) e é mais moderno [cite: 462, 683-684]
print("\n=== EasyOCR ===")
try:
    # Ele é mais lento se não houver uma placa de vídeo (GPU), mas costuma errar menos [cite: 686-687]
    texto_easy = ocr_easyocr(img_placa)
    print(f"Resultado: '{texto_easy}'")
except Exception as e:
    print(f"EasyOCR não disponível ou erro: {e}")

print("\nPasso 4 concluído: Texto 'MIC1988' identificado!")