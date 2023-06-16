def mesa(DPI):
    mesa = DPI[0]+DPI[1]+DPI[2]+DPI[3]
    return mesa

def centro(DPI):
    centro = DPI[4] + DPI[5] + DPI[6] + DPI[7]+ DPI[8]
    return centro

def departamento(DPI):

    el_departamento = DPI[9] + DPI[10]
    numero = int(el_departamento)
    while numero > 22:
        numero = numero - 1
    departamentos = {
        "1": "Guatemala",
        "2": "El progreso",
        "3": "Sacatepequez",
        "04": "Chimaltenango",
        "05": "Escuintla",
        "06": "Solola",
        "07": "Totonicapan",
        "08": "Quetzaltenango",
        "09": "Suchitepequez",
        "10": "Suchitepequez",
        "11": "Suchitepequez",
        "12": "Suchitepequez",
        "13": "Suchitepequez",
        "14": "Suchitepequez",
        "15": "Suchitepequez",
        "16": "Suchitepequez",
        "17": "Suchitepequez",
        "18": "Suchitepequez",
        "19": "Suchitepequez",
        "20": "Suchitepequez",
        "21": "Suchitepequez",
        "22": "Suchitepequez",
        
    }
    return departamentos[numero]

def main():
    fechas = []
    DPI = []
    print("Bienvenido")
    fecha = input("Porfavor ingrese su fecha de nacimiento (DDMMAAAA si espacios ni guiones)")

    for i in fecha:
        fechas.append(i)

    if int(fechas[6]) > 0 or int(fechas[7]) > 5:
        print("Usted es menor de edad por lo que no puede votar")
        continuar = input("Desea realizar otra consulta? S/N:")

        if continuar == "S" or continuar == "s":
            main()
        if continuar == "N" or continuar == "n":
            print("Fin del programa")
    else:
        CUI = input("porfavor ingrese su CUI:")

        for i in CUI:
            DPI.append(i)
        numero_de_mesa = mesa(DPI)
        el_centro = centro(DPI)
        el_departamento = departamento(DPI)
        el_municipio = "municipio"

        print("Departamento",el_departamento)
        print("Municipio", el_municipio)
        print("Centro de Votacion", el_centro)
        print("Mesa",numero_de_mesa)
        continuar = input("Desea realizar otra consulta? S/N:")
        if continuar == "S" or continuar == "s":
            main()
        if continuar == "N" or continuar == "n":
            print("Fin del programa")



main()
