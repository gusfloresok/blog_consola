# ARCHIVO PRINCIPAL DEL BLOG

from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


if __name__ == "__main__":

    # bucle
    while True:
        opcion = mostrar_menu()

        # Opción 1 mostrar todos los posts
        if opcion == 1:
            listar_posts(posts)

        # Opción 2 buscar posts por título
        elif opcion == 2:
            busqueda = input("Buscar por titulo: ").strip()

            if busqueda == "":
                print("Error: la búsqueda no puede estar vacía.")
            else:
                resultados = buscar_por_titulo(posts, busqueda)

                if not resultados:
                    print("No se encontraron posts con ese título.")
                else:
                    print("\nResultados encontrados:")
                    for post in resultados:
                        print(f"- {post['titulo']}")

        # Opción 3 filtrar posts por tag
        elif opcion == 3:
            tag_buscado = input("Ingresá un tag: ").strip()

            if tag_buscado == "":
                print("Error: el tag no puede estar vacío.")
            else:
                resultados = filtrar_por_tag(posts, tag_buscado)

                if not resultados:
                    print("No se encontraron posts con ese tag.")
                else:
                    print(f"\nPosts con el tag {tag_buscado}:")
                    for post in resultados:
                        print(f"- {post['titulo']}")

        # Opción 4 validar posts
        elif opcion == 4:
            print("\nValidación de posts:")
            for numero, post in enumerate(posts, start=1):
                es_valido, mensaje = validar_post(post)
                if es_valido:
                    print(f"Post {numero}: válido")
                else:
                    print(f"Post {numero}: error - {mensaje}")

        # Opción 5 salir
        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        # otra opción es inválida
        elif opcion is not None:
            print("Opción inválida, intenta de nuevo")
