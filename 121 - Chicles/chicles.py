def validaEntrada(entrada:str) -> list[int]:
    # Variable de Retorno
    numerosObtenidos:list[int] = []

    # Variables locales
    valores:list[str] = entrada.split(" ", 3)
    
    try:
        for valor in valores:
            numero:int = int(valor)

            if(numero <= 10**9):
                numerosObtenidos.append(numero)
            else:
                raise Exception("Se introdujeron cantidades mayores a 10^9")
    except Exception:
        raise Exception("Solo deben introducirse números!!")
        
    return numerosObtenidos

def calculaChicles(envNecesarios:int, chiPromocion:int, chiIniciales:int) -> list[str]:
    resultado:list[str] = None
    chiConsumidos:int = chiIniciales
    chiBonus:int = chiIniciales
    chiRegalados:int

    if(chiIniciales > 0 and envNecesarios > chiPromocion):
        while True:
            chiBonus = (chiBonus // envNecesarios) * chiPromocion
            chiConsumidos += chiBonus
            
            if(chiBonus < envNecesarios): break

        chiRegalados = chiConsumidos - chiIniciales

        if(chiRegalados < chiIniciales):
            resultado = [chiConsumidos ,chiBonus]

    return resultado


def main():
    # VARIABLES
    entrada:str
    envNecesarios = chiPromocion = chiIniciales = None

    # Verificar datos introducidos
    try:
        entrada = validaEntrada(input("Introduce la 'PROMOCIÓN':\n"))
        envNecesarios, chiPromocion, chiIniciales = entrada

        resultado = calculaChicles(envNecesarios, chiPromocion, chiIniciales)

        print(resultado if resultado else "RUINA")

    except Exception as e:
        print(f"Hubo un error en la entrada: {e}")

main()