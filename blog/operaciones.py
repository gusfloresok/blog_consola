# OPERACIONES DEL BLOG

# Opción 1: muestra todos los posts
def listar_posts(lista):
    print("\nPosts disponibles:")
    for post in lista:
        # .get() evita errores si falta alguna clave
        titulo = post.get("titulo", "Sin título")
        estado = post.get("estado", "Sin estado")
        autor = post.get("autor")

        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre", "Autor desconocido")
        else:
            nombre_autor = "Autor desconocido"

        print(f"- {titulo} | Autor: {nombre_autor} | Estado: {estado}")


# Opción 2: retorna los posts cuyo título contiene el término
def buscar_por_titulo(lista, termino):
    resultados = []

    for post in lista:
        if termino.lower() in post.get("titulo", "").lower():
            resultados.append(post)

    return resultados


# Opción 3: retorna los posts que tienen el tag buscado
def filtrar_por_tag(lista, tag):
    resultados = []

    for post in lista:
        tags = post.get("tags", [])
        # solo recorremos los tags si realmente son una lista
        if isinstance(tags, list):
            for etiqueta in tags:
                if etiqueta.lower() == tag.lower():
                    resultados.append(post)

    return resultados
