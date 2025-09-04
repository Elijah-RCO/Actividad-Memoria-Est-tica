# src/main.py
"""
Mini-Sistema de Registro de Calificaciones (Un estudiante fijo)
Autor: Johan Esteban Rodriguez Cornejo, Laura Andrea Paez Parra
"""

# -------------------------------
# Memoria Estática (Inmutable)
# -------------------------------
cursos = ("Matemáticas", "Física", "Programación", "Inglés")  # tupla fija
estudiante = "Nicolas Ramirez"  # nombre fijo

# -------------------------------
# Memoria Dinámica (Mutable)
# -------------------------------
calificaciones = [None] * len(cursos)  # lista con un espacio para cada curso

# -------------------------------
# Funciones
# -------------------------------
def mostrar_menu():
    print("\n=== 📚 Registro de Calificaciones ===")
    print(f"👤 Estudiante: {estudiante}")
    print("1️⃣ Agregar/Modificar calificación")
    print("2️⃣ Eliminar calificación")
    print("3️⃣ Mostrar calificaciones")
    print("4️⃣ Calcular promedio final")
    print("5️⃣ Salir")

def agregar_modificar():
    print("\nCursos disponibles:")
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. {curso}")

    try:
        idx = int(input("Seleccione el curso (número): ")) - 1
        if idx < 0 or idx >= len(cursos):
            print("❌ Opción inválida.")
            return
        nota = float(input(f"Ingrese la calificación para {cursos[idx]} (0.0 - 5.0): "))
        if 0.0 <= nota <= 5.0:
            calificaciones[idx] = nota
            print(f"✅ Calificación guardada: {cursos[idx]} → {nota:.2f}")
        else:
            print("⚠️ La nota debe estar entre 0.0 y 5.0.")
    except ValueError:
        print("❌ Entrada inválida, debe ser un número.")

def eliminar():
    print("\nCursos disponibles:")
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. {curso}")
    try:
        idx = int(input("Seleccione el curso (número): ")) - 1
        if idx < 0 or idx >= len(cursos):
            print("❌ Opción inválida.")
            return
        if calificaciones[idx] is None:
            print(f"⚠️ No había calificación registrada en {cursos[idx]}.")
        else:
            calificaciones[idx] = None
            print(f"🗑️ Calificación eliminada para {cursos[idx]}.")
    except ValueError:
        print("❌ Entrada inválida.")

def mostrar():
    print(f"\n📘 Calificaciones de {estudiante}:")
    for curso, nota in zip(cursos, calificaciones):
        if nota is None:
            print(f" - {curso}: ❌ Sin calificación")
        else:
            print(f" - {curso}: {nota:.2f}")

def promedio():
    notas = [n for n in calificaciones if n is not None]
    if notas:
        prom = sum(notas) / len(notas)
        print(f"📊 Promedio final: {prom:.2f}")
    else:
        print("⚠️ No hay calificaciones registradas.")

# -------------------------------
# Programa principal
# -------------------------------
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_modificar()
        elif opcion == "2":
            eliminar()
        elif opcion == "3":
            mostrar()
        elif opcion == "4":
            promedio()
        elif opcion == "5":
            print("👋 Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
# Finalización del código por Laura Paez 


