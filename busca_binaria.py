# Exemplo de busca binaria simples
def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
        print("Chute ", chute)
        if chute ==  item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1 
    return None
    
minha_lista = [1, 2, 3, 4, 5, 6]

print(busca_binaria(minha_lista, 6))