def angVetor(u, v):
    modulo_u = math.sqrt((math.pow(u[0],2) + math.pow(u[1],2)))
    modulo_v = math.sqrt((math.pow(v[0],2) + math.pow(v[1],2)))
    x = modulo_u * modulo_v
    uXv = u[0] * v[0] + u[1] * v[1]
    cosO = uXv / x
    angO = math.acos(cosO)
    return angO