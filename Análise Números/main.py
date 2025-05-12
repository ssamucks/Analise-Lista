def analisar_lista(numeros):
    if not numeros:
        return "Lista vazia."

    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    pares = [num for num in numeros if num % 2 == 0]
    qtd_pares = len(pares)

    return {
        "media": round(media, 2),
        "maior": maior,
        "menor": menor,
        "quantidade_pares": qtd_pares
    }