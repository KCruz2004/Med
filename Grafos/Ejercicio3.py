class CasaComercial:
    def __init__(self):
        self.grafo = {}
    
    def agregar_categoria(self, categoria):
        if categoria not in self.grafo:
            self.grafo[categoria] = []
    
    def agregar_producto_a_categoria(self, categoria, producto):
        if categoria in self.grafo:
            if producto not in self.grafo[categoria]:
                self.grafo[categoria].append(producto)
    
    def mostrar_grafo(self):
        for categoria, productos in self.grafo.items():
            if productos:
                print(f"{categoria} tiene los siguientes productos: {', '.join(productos)}")
            else:
                print(f"{categoria} no tiene productos asociados.")
    
productos = CasaComercial()
productos.agregar_categoria('Alimentos')
productos.agregar_categoria('Ropa')
productos.agregar_categoria('Celulares')
productos.agregar_producto_a_categoria('Alimentos', 'Cafe')
productos.agregar_producto_a_categoria('Alimentos', 'Arroz')
productos.agregar_producto_a_categoria('Alimentos', 'Frijoles')
productos.agregar_producto_a_categoria('Ropa', 'Camisa')
productos.agregar_producto_a_categoria('Ropa', 'Pantalon')
productos.agregar_producto_a_categoria('Ropa', 'Short')
productos.agregar_producto_a_categoria('Celulares', 'Iphone')
productos.agregar_producto_a_categoria('Celulares', 'Samsung')
productos.mostrar_grafo()