# MENÚ DEL BLOG

# Muestra el menú y retorna la opción elegida
def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        opcion = int(input("Elegí una opción: "))
    except ValueError:
        print("Error: tenés que ingresar un número.")
        return None

    return opcion
