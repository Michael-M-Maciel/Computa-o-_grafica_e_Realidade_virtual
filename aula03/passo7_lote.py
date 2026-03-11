"""
Passo 7 — Processar Múltiplas Imagens em Lote
Aula 03 — Análise de Placas de Carros com OpenCV
"""

import cv2
import numpy as np
import os
import json
from datetime import datetime

# Importamos as funções de utilidade e os diretórios de trabalho [cite: 815-818]
from placas_utils import criar_placa_sintetica, pipeline_leitura_placa, SAIDA_DIR, CARROS_DIR

def processar_lote(pasta_imagens, saida_json=None):
    # Se não definirmos um nome de arquivo, ele salva como registros.json na pasta de saída
    if saida_json is None:
        saida_json = os.path.join(SAIDA_DIR, "registros_Michael.json")
    
    # Lista as extensões de imagem permitidas [cite: 827]
    extensoes = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    
    # Procura na pasta todos os arquivos que terminam com as extensões acima [cite: 828-830]
    arquivos = [
        f for f in os.listdir(pasta_imagens)
        if f.lower().endswith(extensoes)
    ]

    print(f"Encontradas {len(arquivos)} imagens em '{pasta_imagens}'")

    registros = [] # Lista que vai guardar os dicionários de cada carro

    # Loop que processa cada imagem encontrada [cite: 833]
    for i, arquivo in enumerate(sorted(arquivos)):
        caminho = os.path.join(pasta_imagens, arquivo)
        print(f"\n[{i+1}/{len(arquivos)}] Processando: {arquivo}")

        # Chama o Pipeline (Passo 6) para cada foto [cite: 836]
        res = pipeline_leitura_placa(caminho, debug=False)

        # Cria o "bilhete de entrada" do carro com metadados [cite: 837-849]
        registro = {
            "id":        i + 1,
            "arquivo":   arquivo,
            "horario":   datetime.now().isoformat(), # Data e hora da detecção [cite: 844]
            "placa":     res["placa"],
            "valido":    res["valido"],
            "formato":   res["formato"],
            "confianca": round(res["confianca"], 3),
        }
        registros.append(registro)

        # Mostra o status rápido no console
        status = "✓" if res["valido"] else "?"
        print(f"  {status} Placa: {res['placa']}  |  Confiança: {res['confianca']:.0%}")

    # Salva todos os registros em um arquivo JSON [cite: 856-858]
    with open(saida_json, "w", encoding="utf-8") as f:
        json.dump(registros, f, ensure_ascii=False, indent=2)

    # Cálculos para o relatório final [cite: 860-864]
    total     = len(registros)
    validos   = sum(1 for r in registros if r["valido"])
    invalidos = total - validos

    # Imprime o resumo do dia [cite: 865-873]
    print("\n" + "="*50)
    print("RELATÓRIO DO LOTE - ESTACIONAMENTO UNIFG")
    print("="*50)
    print(f"Total processado   : {total}")
    print(f"Placas válidas     : {validos} ({validos/total:.0%})")
    print(f"Não identificadas  : {invalidos} ({invalidos/total:.0%})")
    print(f"Log salvo em       : {saida_json}")

    return registros

# ── PARTE DO ALUNO: Criar pasta de teste personalizada ────────
# Adicionei referências ao Flamengo (CRF) e Saudali (SAU) para seus testes
placas_teste = ["MIC1988", "CRF1895", "SAU2026", "ABC1234", "BRA2E23"]

for placa in placas_teste:
    # Gera a imagem da placa (branca com bordas azuis)
    img = criar_placa_sintetica(placa, largura=500, altura=150)

    # Cria um fundo cinza escuro simulando a lataria do carro (80, 80, 80)
    fundo = np.full((300, 700, 3), (80, 80, 80), dtype=np.uint8)
    
    # Cola a placa no meio do fundo
    fundo[100:250, 150:650] = img

    # Adiciona ruído aleatório para testar a resistência do código 
    ruido = np.random.randint(0, 25, fundo.shape, dtype=np.uint8)
    fundo = cv2.add(fundo, ruido)

    # Salva a imagem final na pasta de carros
    cv2.imwrite(os.path.join(CARROS_DIR, f"carro_{placa}.png"), fundo)

print(f"Geradas {len(placas_teste)} imagens de carros para teste em {CARROS_DIR}/\n")

# ── Executar o processamento em lote ──────────────────────────
registros = processar_lote(CARROS_DIR)

print("\nPasso 7 concluído: Sistema de log em lote funcionando!")