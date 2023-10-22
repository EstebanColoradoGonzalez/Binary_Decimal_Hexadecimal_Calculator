import os

def hexadecimal_a_binario(numero_hexadecimal):
    numero_decimal = int(numero_hexadecimal, 16)
    numero_binario = bin(numero_decimal)[2:]
    return numero_binario

def hexadecimal_a_decimal(numero_hexadecimal):
    numero_decimal = int(numero_hexadecimal, 16)
    return numero_decimal

def binario_a_hexadecimal(numero_binario):
    numero_decimal = int(numero_binario, 2)
    numero_hexadecimal = hex(numero_decimal)[2:]
    return numero_hexadecimal

def decimal_a_hexadecimal(numero_decimal):
    numero_hexadecimal = hex(numero_decimal)[2:]
    return numero_hexadecimal

def binario_a_decimal(numero_binario):
    numero_decimal = int(numero_binario, 2)
    return numero_decimal

def decimal_a_binario(numero_decimal):
    numero_binario = bin(numero_decimal)[2:]
    return numero_binario

def limpiar_consola():
    os.system('cls')
    
def procesar_opcion(opcion_menu):
    if opcion_menu == 1:
        limpiar_consola()
        numero = input("Ingresa el número decimal: ")
        print(decimal_a_binario(int(numero)))
    elif opcion_menu == 2:
        limpiar_consola()
        numero = input("Ingresa el número binario: ")
        print(binario_a_decimal(numero))
    elif opcion_menu == 3:
        limpiar_consola()
        numero = input("Ingresa el número decimal: ")
        print(decimal_a_hexadecimal(int(numero)))
    elif opcion_menu == 4:
        limpiar_consola()
        numero = input("Ingresa el número binario: ")
        print(binario_a_hexadecimal(numero))
    elif opcion_menu == 5:
        limpiar_consola()
        numero = input("Ingresa el número hexadecimal: ")
        print(hexadecimal_a_decimal(numero))
    elif opcion_menu == 6:
        limpiar_consola()
        numero = input("Ingresa el número hexadecimal: ")
        print(hexadecimal_a_binario(numero))

def menu():
    while True:
        try:
            opcion_menu = int(input("Ingresa opción del menú: "))
        except ValueError:
            limpiar_consola()
            continue

        if 1 <= opcion_menu <= 6:
            procesar_opcion(opcion_menu)
            input("Presiona Enter para continuar...")
            limpiar_consola()
        else:
            break

def main():
    menu()

if __name__ == "__main__":
    main()