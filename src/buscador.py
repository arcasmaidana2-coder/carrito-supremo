import csv

def cargar_precios(ruta_archivo):
    productos= []

    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            fila['precio'] = float(fila['precio'])
            productos.append(fila)

    return productos

def buscar_producto(productos, texto_busqueda):
    resultados = []

    for producto in productos:
        nombre_producto = producto['producto'].lower()
        texto=texto_busqueda.lower()

        if texto in nombre_producto:
            resultados.append(producto)

    return resultados        

def ordenar_por_precio(productos):
    return sorted(productos, key=lambda producto: producto["precio"])


def mostrar_resultados(productos):
    if not productos:
        print("No se encontraron productos.")
        return

    for producto in productos:
        print(
            f'{producto["producto"]} | '
            f'{producto["tienda"]} | '
            f'{producto["precio"]} € | '
            f'confianza: {producto["confianza"]}'
        )


def main():
    ruta = "data/precios.csv"
    productos = cargar_precios(ruta)

    busqueda = input("¿Qué producto quieres buscar? ")

    resultados = buscar_producto(productos, busqueda)
    resultados_ordenados = ordenar_por_precio(resultados)

    mostrar_resultados(resultados_ordenados)


if __name__ == "__main__":
    main()