# Exemplo de busca binaria simples
def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
        
        if chute ==  item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1 
    return None
    
minha_lista = [1, 2, 3, 4, 6, 8, 12, 14 ,23, 50, 100]

print(busca_binaria(minha_lista, 100))