# VALIDACIONES DEL BLOG

from blog.datos import estados_post


# Opción 4: revisa si un post está bien armado
# Retorna True/False y un mensaje
def validar_post(post):
    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    # revisamos que estén todas las claves obligatorias
    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_obligatorias:
        if clave not in post:
            return False, f'falta la clave "{clave}"'

    if not isinstance(post["titulo"], str) or post["titulo"].strip() == "":
        return False, "el título está vacío"

    if not isinstance(post["contenido"], str) or post["contenido"].strip() == "":
        return False, "el contenido está vacío"

    if not isinstance(post["autor"], dict):
        return False, "el autor no es un diccionario"

    if "nombre" not in post["autor"]:
        return False, "el autor no tiene nombre"

    if not isinstance(post["tags"], list):
        return False, "los tags no son una lista"

    if post["estado"] not in estados_post:
        return False, f'el estado "{post["estado"]}" no es válido'

    return True, "válido"
