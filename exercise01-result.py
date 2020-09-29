listaRegistro = []
clientes = 0
nc = int(input("cantidad de clientes: "))

while clientes < nc:
    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))

    # punto de programa
    # registro = {"cliente": cliente, "producto": producto, "costo": costo}
    registro = dict(cliente=cliente, producto=producto, costo=costo)
    # como agrego un elemento nuevo a una lista?
    listaRegistro.append(registro)
    # dejar de ocupar la variable registro
    # registro = None
    clientes += 1

for registro in listaRegistro:
    print(registro)

n = 0
for registro in listaRegistro:
    n += registro["costo"]
print("El costo total es de: " + str(n))
