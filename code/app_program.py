list_viajeros = []
sw = True
import os 

def fnt_limpiar():
    os.system('cls')
    print('Autor: AleXxxBb')
    print('Copyright(c) 2024')
    print('Univercidad catolica luis amigo')

def fnt_agente(op):
    fnt_limpiar()
    if op == '1':
        print('<<< AGREGAR VIAJEROS >>>\n')
        viajero = ''
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        edad = input('edad: ')
        if int(edad)> 0 and int(edad)<= 25:
            viajero = nombre + ' ' + apellido + ' ' + edad
            list_viajeros.append(viajero)
            print('Viajero agregado correctamente\n')
            print('Presione <ENTER> para continuar...')
        else:
            print('edad incorrecta\n')
            print('presione <ENTER>para continuar...')
            
    if op =='2':
        
            


while sw == True:
    fnt_limpiar()
    opcion = input('<<<<< MENU PRINCIPAL >>>>>\n1. AGREGAR\n2. MOSTRAR\n3. SALIR\n4. ->')
    fnt_agente(opcion)