import random
import csv
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos_trabajadores =[]
sueldos_aux =[]
sueldos_completos =[]
try:
    open("sueldos.csv","x")
except:
    print("Archivo creado exitosamene")
    

def sueldos(lista, lista2):
    sueldos_trabajadores.clear()
    for i in lista:
        lista_aux = []
        lista_aux.append(i)
        lista_aux.append(random.randint(300000, 2500000))
        lista2.append(lista_aux)

def clasificar_sueldos(lista):
    if sueldos_trabajadores == []:
        print ("Error: no se han asignado los sueldos")
        return False
    sueldos_menores_a_800 =[]
    sueldos1 =[]
    sueldos_mayores_a_800=[]
    sueldos2 = []
    sueldos_mayores_a_2mill =[]
    sueldos3 =[]
    sueldos4=[]
    for i in lista:
        if i[1] < 800000:
            sueldos_menores_a_800.append(i)
            sueldos1.append(i[1])
            sueldos4.append(i[1])
        elif i[1] > 800000 and i[1] < 2000000:
            sueldos_mayores_a_800.append(i)
            sueldos2.append(i[1])
            sueldos4.append(i[1])
        else:
            sueldos_mayores_a_2mill.append(i)
            sueldos3.append(i[1])
            sueldos4.append(i[1])
    print("="*50)
    print(f"Sueldos menores a $800.000 TOTAL: {sum(sueldos1)}\n")
    print ("Nombre empleado\tSueldo")
    print("-"*50)
    for i in sueldos_menores_a_800:
        print(f"{i[0]}\t${i[1]}")
    print()
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {sum(sueldos2)}\n")
    print ("Nombre empleado\tSueldo")
    print("-"*50)
    for i in sueldos_mayores_a_800:
        print(f"{i[0]}\t${i[1]}")
    print()
    print(f"Sueldos mayores a $2.000.000 TOTAL: {sum(sueldos2)}\n")
    print ("Nombre empleado\tSueldo")
    print("-"*50)
    for i in sueldos_mayores_a_2mill:
        print(f"{i[0]}\t${i[1]}")
    print()
    print(f"TOTAL SUELDOS:\t${sum(sueldos4)}")

def estadisticas(lista):
    contador = 0
    if sueldos_trabajadores ==[]:
        print("Error: no se ha asignado sueldos")
        return False
    print("="*50)
    promedio_sueldos=[]
    sueldo_mas_bajo = 2500000
    for i in lista:
        if i[1] < sueldo_mas_bajo:
            sueldo_mas_bajo= i[1]
            sueldo1 = i[0]
    print (f"El empleado con menor sueldo es {sueldo1} con sueldo de: ${sueldo_mas_bajo}\n")
    sueldo_mas_alto = 1
    for i in lista:
        if i[1] > sueldo_mas_alto:
            sueldo_mas_alto= i[1]
            sueldo2 = i[0]
    print (f"El empleado con mayor sueldo es {sueldo2} con sueldo de: ${sueldo_mas_alto}\n")
    for i in lista:
        promedio_sueldos.append(i[1])
    print (f"El promedio de los sueldos es de: ${round(sum(promedio_sueldos)/len(trabajadores))}\n")
    for i in lista:
        contador = contador + 1
        if contador == 5:
            print (f"La media geometrica corresponde al empleado: {i[0]} con un sueldo de: ${i[1]}")

def reporte (lista):
    if sueldos_trabajadores ==[]:
        print ("Error: no se ha asignado sueldos")
        return False
    print("="*50)
    for i in lista:
        salud = round(i[1] * 0.07)
        afp = round(i[1]* 0.12)
        sueldo_total = i[1] - salud - afp
        sueldos_completos.append([i[0],i[1],salud,afp,sueldo_total])
    print("Nombre empleado               Sueldo Base   Descuento salud    Descuento AFP    Sueldo Líquido")
    for i in sueldos_completos:
        espacio1= " "*(30-len(i[0]))
        espacio2= " "*(14-len(str(i[1])))
        espacio3= " "*(14-len(str(i[2])))
        espacio4= " "*(14-len(str(i[3])))
        
        print (f"{i[0]} {espacio1} ${i[1]} {espacio2 }${i[2]} {espacio3} ${i[3]} {espacio4} ${i[4]}")
        print("-"*50)
        
def guardar_archivo(archivo,lista):
    if sueldos_trabajadores == []:
        print("Error: No se han asignado sueldos")
        return False
    with open(archivo, "w", newline="") as archivo_csv:
        escritura_csv = csv.writer(archivo_csv)
        escritura_csv.writerow(["Trabajador","Sueldo base", "Descuento Salud", "Descuento AFP", "Sueldo liquido"])
        escritura_csv.writerows(lista)

while True:
    try:
        print("="*50)
        opcion = int (input("Menú de opciones:\n1.-Asignar sueldos aleatorios.\n2.-Clasificar Sueldos\n3.-Ver estadisticas\n4.-Reporte de sueldos\n5.-Generar Archivo CSV\n6.-Salir del programa\n>"))
        match opcion:
            case 1:
                print ("Asignando sueldos")
                sueldos(trabajadores, sueldos_trabajadores)
            case 2:
                print("Clasificando sueldos")
                clasificar_sueldos(sueldos_trabajadores)
            case 3:
                print("Viendo estadisticas")
                estadisticas(sueldos_trabajadores)
            case 4:
                print("Generando reporte de sueldos")
                reporte(sueldos_trabajadores)
                print (sueldos_completos)
            case 5:
                print("Generando archivo_csv")
                guardar_archivo("sueldos.csv", sueldos_completos)
            case 6:
                print("Saliendo del programa\nPrograma generado por: Sebastián Ulloa Henríquez\nRut: 20.239.092-7")
                break
            case _:
                print("Error: opción no indicada en el menú")
    except (ValueError):
        print("Error: Tipo de valor invalido")
