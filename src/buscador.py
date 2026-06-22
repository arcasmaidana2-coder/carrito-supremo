import csv
from pathlib import Path


RUTA_PRECIOS = Path(__file__).resolve().parent.parent / "data" / "precios.csv"


def cargar_precios(ruta_archivo=RUTA_PRECIOS):
    productos = []

    with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            fila["precio"] = float(fila["precio"])
            productos.append(fila)

    return productos


def normalizar_texto(texto):
    return texto.strip().lower()


def buscar_producto(productos, texto_busqueda):
    resultados = []
    texto = normalizar_texto(texto_busqueda)

    if not texto:
        return resultados

    for producto in productos:
        nombre_producto = normalizar_texto(producto["producto"])

        if texto in nombre_producto:
            resultados.append(producto)

    return resultados


def ordenar_por_precio(productos):
    return sorted(productos, key=lambda producto: producto["precio"])


def formatear_producto(producto):
    return (
        f'{producto["producto"]} | '
        f'{producto["tienda"]} | '
        f'{producto["precio"]} € | '
        f'confianza: {producto["confianza"]}'
    )


def mostrar_resultados(productos):
    if not productos:
        print("No se encontraron productos.")
        return

    for producto in productos:
        print(formatear_producto(producto))


def ejecutar_busqueda():
    productos = cargar_precios()

    busqueda = input("¿Qué producto quieres buscar? ")

    resultados = buscar_producto(productos, busqueda)
    resultados_ordenados = ordenar_por_precio(resultados)

    mostrar_resultados(resultados_ordenados)


if __name__ == "__main__":
    ejecutar_busqueda()