import csv
partidos = []
votos = []
total = []

def ingresar_partido():
    codigo = input("Ingrese el codigo del partido")
    nombre = input("Ingrese el nombre del partido")
    siglas = input("Ingrese las siglas del partido")

    datos = {
        "codigo": codigo,
        "nombre": nombre,
        "siglas": siglas,
    }
    partidos.append(datos)

    continuar = input("Desea realizar otra consulta? S/N:")
    if continuar == "S" or continuar == "s":
        ingresar_partido()
    if continuar == "N" or continuar == "n":
        main()

def ingresar_acta():
    mesa = input("Ingrese el numero de mesa")
    departamento = input("Ingrese el departamento")
    municipio = input("Ingrese el municipio")
    partido = input("Ingrese el codigo del partido")
    votos = input("Ingrese la cantidad de votos validos")

    datos = {
        "partido": partido,
        "votos": votos
    }
    a = 0
    b = 0
    while a == 0:
        continuar = input("Desea ingresar datos de otro partido? S/N:")
        if continuar == "S" or continuar == "s":
            a = 0
            partido = input("Ingrese el codigo del partido")
            votos = input("Ingrese la cantidad de votos validos")
            datos = {
                "partido": partido,
                "votos": votos
            }
            votos.append(datos)
        if continuar == "N" or continuar == "n":
            a = 2

    while b == 0:
        continuar = input("Desea ingresar otra acta? S/N:")
        if continuar == "S" or continuar == "s":
            b = 0
            ingresar_acta()
        if continuar == "N" or continuar == "n":
            b = 2
            main()

def resultados():
    print("Partido    /   Votos")
    for i in partidos:
        votos = 0
        partido = partidos[i]
        for z in votos:
            if partido == votos["partido"]:
                votos = votos + int(votos["votos"])
        print(partido, "/", votos)
        resultados = {
            "partido":partido,
            "votos":votos
        }
        total.append(resultados)
    main()

def exportar():
    with open("resultados.csv", "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        encabezados = ["Partido", "Resultados"]
        escritor.writerow(encabezados)

        for x in total:
            escritor.writerow([
                x["partido"], x["votos"]
            ])

    main()


def main():
    print("1. Ingresar partido politico")
    print("2. Ingresar actas")
    print("3. Ver resultados")
    print("4. Exportar resultados")
    print("5. Salir")
    opcion = int(input("Ingrese el numero de la accion que desea realizar:"))

    if opcion == 1:
        ingresar_partido()
    if opcion == 2:
        ingresar_acta()
    if opcion == 3:
        resultados()
    if opcion == 4:
        exportar()
    if opcion == 5:
        print("Fin del programa")


main()
