# DATOS BASE DEL BLOG

# diccionario
perfil_autor = {
    "nombre": "Gustavo Flores",
    "bio": "Desarrollador web.",
    "especialidad": "Python y Django",
    "redes_sociales": ["@gustii.f", "@gustii.f2"]
}

# tupla
estados_post = ("borrador", "publicado", "archivado")

# set
etiquetas_blog = {"Python", "Web", "Backend", "Python"}

# Lista de posts
posts = [
    {
        "id": 1,
        "titulo": "Proyecto Python",
        "contenido": "En este post muestro un proyecto hecho con Python.",
        "autor": perfil_autor,
        "categoria": "Programación",
        "tags": ["Python", "Aplicaciones"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Sobre mi",
        "contenido": "Les cuento quién soy y cómo empecé a programar.",
        "autor": perfil_autor,
        "categoria": "Desarrollo Web",
        "tags": ["Python", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "App Python",
        "contenido": "Una aplicación simple usando diccionarios en Python.",
        "autor": perfil_autor,
        "categoria": "Programación",
        "tags": ["Python", "Diccionarios", "Backend"],
        "estado": "archivado"
    },
    # Post incompleto: le falta "contenido" (para probar validaciones)
    {
        "id": 4,
        "titulo": "Post sin contenido",
        "autor": perfil_autor,
        "categoria": "Programación",
        "tags": ["Python"],
        "estado": "publicado"
    }
]
