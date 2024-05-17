# Importaciones para "controlar" la consola
from os import system
from time import sleep
from functools import reduce

# Obtener los casos de prueba del usuario
def obtenerCuadrados() -> list:
    cantCuadros:int = 0
    listaCuadros = []

    while(True):
        system('cls')
        print(f"Introduce la información del cuadro {cantCuadros + 1}")

        try:
            tamanioCuadro:int = int(input("Tamaño del cuadrado (0 para terminar la entrada): \n"))

            # Validar tamaño
            if(tamanioCuadro == 0):
                break
            elif(tamanioCuadro < 2 or tamanioCuadro > 1024):
                print("El tamaño debe ser mayor o igual a 2 y menor a 1024. \nIntentalo de nuevo...")
                sleep(2)
                continue

            celdas = input("Valores de las celdas: ").split(' ')
            celdas = list(map(int, celdas)) # Convertir a lista de enteros
            listaCuadros.append({'size': tamanioCuadro, 'values': celdas})

        except Exception as e:
            print("Ocurrio un error: ", e)
            sleep(1.5)
    
    return listaCuadros

def evaluarCuadro(cuadro:dict) -> str:
    n:int = cuadro['size']; celdas:list = cuadro['values'];
    constMagica:int; constMagic2:int;
    resultado:str = "NO"

    # Evaluar que el cuadro cuente con los n^2 elementos ingresados
    if(len(celdas) == n**2):
        # Variable para controlar calculos de la constante mágica
        res = set()

    # Evaluar si cumple con caracteristicas "Diabolicas"
        for indice in range(n):
            fila = indice * n   # Calcula la posición inicial de la siguiente fila
    #   Verificación horizontal: Sumar valores desde el inicio de la fila hasta n posiciónes más
            cmHorizontal = reduce(sumaCeldas, celdas[fila:fila + n])
            
    #   Verificación vertical: Sumar valores desde el indice en intervalos de n (columna)
            cmVertical = reduce(sumaCeldas, celdas[indice::n])

            res.update({cmHorizontal, cmVertical})

    #   Verificación diagonales
        # Diagonal izquierda
        res.add(reduce(sumaCeldas, celdas[::n + 1]))

        # Diagonal derecha
        res.add(reduce(sumaCeldas, celdas[n-1:-1:n - 1]))

    # Si es diabolico, evaluar ESOTÉRICO
        if(len(res) < 2):
            constMagica = list(res)[0]

            constMagic2 = int((4 * constMagica) / n)

            res.add(constMagic2)

            resultado = "DIABOLICO"     # Resultado preeliminar

    #   Verificación de cifras1 a n^2
            if(list(range(1, n**2 + 1)) == sorted(celdas)):
    
    #   Verificación de esquinas
                listAux = celdas[0:n:(n - 1)]
                listAux.extend(celdas[-1:-(n+1):-(n-1)])

                res.add(reduce(sumaCeldas, listAux))

     #   Verificación de laterales
                impar = bool(n % 2 != 0)
                iMedio = n // 2
                iLatral = n * iMedio if impar else n* (iMedio - 1)

                # Obtener centros horizontales 
                listAux = celdas[iLatral:iLatral+ (n if impar else n*2):iMedio]

                if(impar):
                    # Obtener centros verticales
                    listAux.extend(celdas[iMedio::(n**2)-n])

                    centro = listAux.pop(1)
                    res.add(centro*4)
                    res.add(reduce(sumaCeldas, listAux))
                else:
                    listAux.append(0)
                    listAux.extend(celdas[(iLatral+iMedio-1):iLatral+(n*2):iMedio])

                    centros = listAux[::2]
                    centrales = listAux[1::2]
                    del listAux

                    # Obtener centros verticales
                    centros.extend(celdas[iMedio::(n**2)-n])
                    centros.extend(celdas[iMedio-1::(n**2)-n])

                    # Suma de casillas centrales = CM2
                    res.add(reduce(sumaCeldas, centrales))

                    # Suma Laterales = CM2*2
                    valLaterales = reduce(sumaCeldas, centros)

                    if(valLaterales != (constMagic2*2)): res.add(valLaterales)
                
                if(len(res) <= 2):
                    resultado = "ESOTÉRICO"

    return resultado

def sumaCeldas(x:int, y:int) -> int:
    return x + y

def main():
    cuadros = obtenerCuadrados()

    for i, cuadro in enumerate(cuadros):
        print(f"Cuadro #{i + 1}: {evaluarCuadro(cuadro)}")

if __name__ == "__main__":
    main()