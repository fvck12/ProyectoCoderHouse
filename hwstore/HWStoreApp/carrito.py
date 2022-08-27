class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito= self.session["carrito"]

        if not carrito:
            self.session["carrito"]= {}
            self.carrito = self.session ["carrito"]

        else:
            self.carrito = carrito
    
    def agregar(self, productos):
        id = str (productos.id)
        if id not in  self.carrito.keys():
            self.carrito[id]={
                "productos_id": productos.id,
                "nombre": productos.nombre,
                "marca": productos.marca,
                "acumulado": productos.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] +=1
            self.carrito[id]["acumulado"] += productos.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified= True

    def eliminar(self, productos):
        id =str (productos.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, productos):
        id = str (productos.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= productos.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(productos)
            self.guardar_carrito()
    def limpiar(self):
        self.session["carrito"]= {}
        self.session.modified= True