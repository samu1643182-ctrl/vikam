# ══════════════════════════════════════════════════════════════
# proyecto.py · Ficha 3236582 · SENA CTM Itagüí
# Completá con los datos reales de tu proyecto
# ══════════════════════════════════════════════════════════════

nombre_proyecto = "Vikam"           # nombre de tu proyecto
descripcion     = "App ,ultiplataforma habitos saludables"           # qué problema resuelve
tecnologias     = ["HTML","PHYTON","postgrestSQL"]           # ["HTML", "Python", "MySQL"]
integrantes     = ["Samuel Lopez","Miguel Arenas","Miguel Reyes"]           # ["Nombre 1", "Nombre 2"]
funcionalidades = ["Login","Registro","CRUD","Gamificacion"]           # ["Login", "Registro", "Reportes"]


def mostrar_info():
    print(f"Proyecto:      {nombre_proyecto}")
    print(f"Descripción:   {descripcion}")
    print(f"Equipo:        {', '.join(integrantes)}")
    print(f"Tecnologías:   {', '.join(tecnologias)}")
    print(f"Funcionalidades:")
    for f in funcionalidades:
        print(f"  - {f}")


mostrar_info()