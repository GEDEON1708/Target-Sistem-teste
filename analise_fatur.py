import json

def analyze_faturamento(file_path):
    # Carregar os dados do arquivo JSON
    with open(file_path, 'r') as file:
        faturamento = json.load(file)

    # Filtrar os valores diferentes de 0 (ignorar finais de semana/feriados)
    valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

    # Cálculos
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

    # Resultados
    print(f"Menor valor de faturamento: R${menor_valor:.2f}")
    print(f"Maior valor de faturamento: R${maior_valor:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")

# Linkar o arquivo JSON (deve estar no mesmo diretório do script)
file_path = "dados.json"

# Executar a análise
analyze_faturamento(file_path)
