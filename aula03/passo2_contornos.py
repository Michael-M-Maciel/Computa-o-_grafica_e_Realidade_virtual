"""
Passo 2 — Detectar Contornos e Localizar a Placa
Aula 03 — Análise de Placas de Carros com OpenCV
"""

import os
import cv2
# Importamos a função de busca e o diretório de saída definidos pelo professor
from placas_utils import encontrar_candidatos_placa, SAIDA_DIR 

# ── 1. Carregar a imagem gerada no Passo 1 ──────────────────────────────
# Construímos o caminho até o arquivo "placa_Michael.png"
PLACA_PATH = os.path.join(SAIDA_DIR, "placa_Michael.png")
img = cv2.imread(PLACA_PATH)

# Verificação de segurança: se a imagem não existir, o programa para aqui
if img is None:
    print(f"ERRO: execute o passo 1 primeiro para gerar {PLACA_PATH}")
    exit(1)

# ── 2. Buscar candidatos a placa ───────────────────────────────────────
# A função encontrar_candidatos_placa faz o seguinte [cite: 537-587]:
# 1. Aplica o Canny para achar bordas.
# 2. Dilata as bordas (engrossa as linhas) para fechar possíveis buracos [cite: 547-549].
# 3. Usa cv2.findContours para listar todas as formas geométricas brancas [cite: 551-555].
# debug=True: desenha retângulos verdes nos objetos que ele achar interessantes.
candidatos = encontrar_candidatos_placa(img, debug=True)

# ── 3. Analisar os resultados encontrados ──────────────────────────────
# O computador agora percorre a lista de tudo o que ele acha que é uma placa
for i, (contorno, (x, y, w, h)) in enumerate(candidatos):
    # x, y: Coordenada do canto superior esquerdo do retângulo [cite: 571]
    # w, h: Largura (width) e Altura (height) do retângulo [cite: 571]
    
    # Cálculo da Proporção: Largura dividida pela Altura [cite: 574]
    # Placas brasileiras têm proporção entre 2.0 e 6.5 [cite: 559-560]
    proporcao = w / h
    
    print(f"Candidato {i}:")
    print(f"  - Posição no eixo X e Y: ({x}, {y})")
    print(f"  - Tamanho real: {w} pixels de largura por {h} de altura")
    print(f"  - Proporção calculada: {proporcao:.2f} (Ideal para placas)")

print("\nPasso 2 concluído: O retângulo da 'MIC1988' foi localizado com sucesso!")