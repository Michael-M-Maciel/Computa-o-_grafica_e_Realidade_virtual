"""
Passo 6 — Pipeline Completo: Foto → Texto
Aula 03 — Análise de Placas de Carros com OpenCV
"""

import os
# Importamos a função principal que executa todos os passos (1 a 5) automaticamente
from placas_utils import pipeline_leitura_placa, SAIDA_DIR

# Executamos o pipeline na sua placa personalizada "Michael"
# O parâmetro debug=True permite que o sistema salve imagens de cada etapa na pasta de rascunhos
res = pipeline_leitura_placa(os.path.join(SAIDA_DIR, "placa_Michael.png"), debug=True)

# --- Exibição dos Resultados ---
# O resultado (res) é um dicionário que guarda todas as informações encontradas pela IA
print("\n" + "="*50)
print("RESULTADO DO PIPELINE")
print("="*50)

# Mostra o texto final identificado (ex: MIC1988)
print(f"Placa detectada : {res['placa']}")

# Verifica o campo 'valido' (Booleano: True ou False) e mostra um ícone amigável
print(f"Válida          : {'Sim ✓' if res['valido'] else 'Não ✗'}")

# Indica se o padrão é Mercosul ou o Brasileiro Antigo
print(f"Formato         : {res['formato']}")

# Mostra a porcentagem de certeza que o motor de OCR teve ao ler os caracteres
print(f"Confiança       : {res['confianca']:.1%}")

# Mostra as coordenadas (x, y, largura, altura) de onde a placa estava na foto
print(f"Localização     : {res['bbox']}")

print("\nPasso 6 concluído com sucesso!")