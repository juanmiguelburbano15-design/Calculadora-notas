def promedio(notas): 
    return sum(notas)/len(notas)

print(promedio([3.5, 4.0, 2.8]))

def nota_minima_requerida(notas, meta):
    faltante = meta*(len(notas)+1)-sum(notas)
    return faltante
