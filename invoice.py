from user import User

class Invoice(User):

    rol="Cliente"

    def __init__(self, name, last_name, dni):
        super().__init__(name, last_name, dni)
        self.id=0
        self.shopping_car=[]
        self.total=0
        self.compro=False
        self.descuento=False
    def show_atributes(self):
        print(f"{self.name} {self.last_name}")
        print("Carrito de compra")
        print("----------------------------------------")
        for x in self.shopping_car:
            print(f"id: {x[1]['id']}")
            print(f'Titulo: {x[1]["titulo"]}\nArtista: {x[1]["artista"]}\nAño: {x[1]["año_publicacion"]}\nPrecio: {x[1]["precio_venta"]}$\nCantidad:{x[1]["cantidad"]}')
        print("----------------------------------------")
    def product_free(self):
        for x in self.shopping_car:
            sum=0
            for j in str(x[1]["id"]):
                sum+=int(j)
            if sum==7:
                x[1]["precio_venta"]=0
                self.descuento=True
        if self.descuento==True:
            print("Felicidades el prodcuto le sale gratis.")
        else:
            print("Lamentablemente no tiene ningun tipo de descuento.")
    def show_shop_car(self):
        for x in self.shopping_car:
            print("----------------------------------------")
            print(f'                id: {x[1]["id"]}')
            i=x[1]["cantidad"]*x[1]["precio_venta"]
            self.total+=i
            print(f'Titulo: {x[1]["titulo"]}\nArtista: {x[1]["artista"]}\nAño: {x[1]["año_publicacion"]}\nPrecio: {x[1]["precio_venta"]}$')
            print("----------------------------------------")
        print("\n\n")
        print(f"Total: {self.total}$")
        print("\n\n\n\n")
    def eliminate_shopping_car(self):
        for x in self.shopping_car:
            if x[1]['id']==self.id:
                self.shopping_car.pop()
    def double_item(self,id):
        for x in self.shopping_car:
            if "suma" in x:
                if x[1]["id"]==self.shopping_car[-1][1]["id"]:
                    x[1]["cantidad"] +=self.shopping_car[-1][1]["suma"]
                    self.id=self.shopping_car[-1][1]["id"]
                    self.eliminate_shopping_car()
    def empty(self):
        if len(self.shopping_car)!=0:
            return True
        else:
            return False
    def clear_list(self):
        self.shopping_car.clear()

