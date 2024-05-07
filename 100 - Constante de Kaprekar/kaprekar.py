# Obtener los casos de prueba del usuario, validarlos y devolver el resultado
def getCases() -> list:
    casesLenght = int(input("Introduce el número de casos a probar: \n"))
    cases = []

    for i in range(casesLenght):
        introducedCase = input(f"Introduce el caso #{i+1} \n")

        # Validar que el caso introducido cumpla las caracteristicas
        if(validateCase(introducedCase)):
            cases.append(introducedCase)

    return cases

def validateCase(case: str) -> bool:
    isCorrect: bool = False

    # Comprobar que sea un número y tenga 4 digitos
    if(case.isdigit() and len(case) == 4):
        """ # Comprobar el tamaño y al menos 2 digitos diferentes
        if(len(case) == 4 and len(set(case)) >= 2): """
        isCorrect = True

    return isCorrect

def kaprekar(case: str) -> int:
    digitList: list = list(case)
    auxCase: int = int(''.join(digitList))
    attemps: int = 0

    # Descartar "repdigits"
    if(len(set(digitList)) > 1):
        while(auxCase != 6174):
            # Ordenar y convertir a entero la lista de dígitos
            ascNumber = int(''.join(sorted(digitList, reverse=True)))
            descNumber = int(''.join(sorted(digitList)))

            # Restar el número menor al número mayor
            auxCase = ascNumber - descNumber

            # Convertir el número obtenido a una lista de dígitos
            digitList = list(str(auxCase))

            # Agregar un '0' extra para mantener la relación de 4 dígitos
            if(auxCase < 1000): digitList.append('0')

            attemps += 1
    else:
        attemps = 8

    return attemps

def main():
    # Obtener los datos introducidos por el usuario
    userCases = getCases()

    # Buscar respuesta siempre que haya casos
    if(len(userCases)):
        print("\nSALIDAS")
        for case in userCases:
            print(f"{case}: {kaprekar(case)} intentos")

if __name__ == '__main__':
    main()