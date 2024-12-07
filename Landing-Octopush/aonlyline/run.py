def convertir_a_una_linea(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as archivo:
        texto = archivo.read()

    # Reemplazar los saltos de línea y eliminar espacios adicionales
    texto_en_una_linea = ' '.join(texto.split())

    # Guardar el resultado en un nuevo archivo
    with open(archivo_salida, 'w') as archivo:
        archivo.write(texto_en_una_linea)

# Ejemplo de uso
convertir_a_una_linea('archivo_entrada.txt', 'archivo_salida.txt')
