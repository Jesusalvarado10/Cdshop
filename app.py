import random
from customers import Customers
from invoice import Invoice
class App():
    inventary={}
    factura={}
    n=0
    def __init__(self):
        self.people=[]
    
    def start(self):
        self.actualizar_datos()
        print(self.factura)
        print(len(self.people))
        for x in self.people:
            x.show_atributes()
        print("////////Bienvenido////////")
        while True:     
            option=input("\n\n1.Cliente.\n2.Empleado.\n3.Salir\n-------------> ")
            while option!="1" and option!="2" and option!="3":
                option=input("1.Cliente.\n2.Empleado.\n3.Salir\n-------------> ")
            print("\n\n")
            if option=="1":
                self.menu_customer_1(2)
                
            elif option=="2":
                self.menu_customer_1(1)
            else:
                self.create_txt_inventary()
                self.create_txt_person()
                break

    def menu_customer_1(self,n):
        while True:
            option=input("\n\n1.Iniciar sesion.\n2.Registrarse.\n-------------> ")
            while option!="1" and option!="2" :
                    option=input("1.Iniciar sesion.\n2.Registrarse.\n-------------> ")  
            print("\n\n")
            if option=='1':
                if n==1:
                    if self.sign_in(1)!=False:
                        break
                else:
                    if self.sign_in(2)!=False:
                        break
            else:
                if n==1:
                    self.register(1)
                    break
                else:
                    self.register(2)
                    break
    
    def search_dni(self,dni,name,n):
        for x in self.people:
            if n==1:
                if x.dni==dni and x.name==name:
                    return True
            else:
                if  x.dni==dni:
                    return x
        return False

    def sign_in(self,n):
        name=input("Coloque su usuario: ").capitalize()
        while not name.isalpha():
            name=input("Coloque su usuario: ").capitalize()
        while True:
            try:
                dni=int(input("Contrasena: "))
                if dni>2022 and dni<1800:
                    raise Exception
                break
            except:
                print("Error")
        try:
            if len(self.people)==0:
                raise Exception
            else:
                if self.search_dni(dni,name,1)==False:
                    print(f"{name.capitalize()} debe registrarse antes.Por favor registrese y regrese")
                else:  
                    if n==1:
                        person=self.search_dni(dni,name,2)
                        if self.validate_sign_in(person)!=False:
                            raise Exception
                        print(f"Bienvenido {name.capitalize()}")
                        self.menu_customer_2()
                    else:
                        person=self.search_dni(dni,name,2)
                        if self.validate_sign_in(person)!=True:
                            raise Exception
                        print(f"Bienvenido {name.capitalize()}")
                        self.nemu_invoice(person)      
        except:
            print("No hay nadie registrado/No puede ingresar aca.")  
        
    def validate_sign_in(self,person):
        if person.rol=="Trabajador":
            return False
        return True
    def register(self,n):
        while True: 
            name=input("Ingrese su nombre: ").capitalize()
            while not name.isalpha():
                name=input("Ingrese su nombre: ").capitalize()
            last_name=input("Ingrese su apellido: ").capitalize()
            while not last_name.isalpha():
                last_name=input("Ingrese su apellido: ").capitalize()
            while True:
                try:
                    dni=int(input("Ingrese su cedula: "))
                    if dni<4000000:
                        raise Exception
                    break
                except:
                    print("Error")
            if self.search_dni(dni,name,2)!=False or self.search_dni(dni,name,1)==True:
                print("El nombre con esa cedula ya existe/La cedula ya existe, por favor revise sus datos.")
            else:
                break
        if n==1:
            print("\n\nSu nombre sera su usuario y su contrasena sera el dni.")
            person=Customers(name,last_name,dni)
            self.people.append(person)
            print(f"\n\n\n\nBienvenido {name.capitalize()}")
            self.menu_customer_2()

        else:
            print("\n\nSu nombre sera su usuario y su contrasena sera el dni.")
            print(f"\n\n\n\nBienvenido {name.capitalize()}")
            person=Invoice(name,last_name,dni)
            self.nemu_invoice(person)

    
    def menu_customer_2(self):
        while True:
            print(self.inventary)
            option=input("1.Anadir discos.\n2.Eliminar discos.\n3.Estadisticas.\n4.Salir.\n-------------> ")
            while option!="1" and option!="2" and option!="3" and option!="4":
                option=input("1.Anadir discos.\n2.Eliminar discos.\n3.Estadisticas.\n4.Salir.\n-------------> ")
            if option=="1":
                self.add_cd()
            elif option=="2":
                try:
                    if len(self.inventary)==0:
                        raise Exception
                except :
                    print("No hay nada en el inventario")
                self.eliminate_cd()
            elif option=="3":
                if len(self.factura)==0:
                    print("No se ha comprado nada. ")                
                else:
                    self.estadisitca()
            else:
                break

    def add_cd(self):
        print("\n\n")
        name_cd=input("Ingrese el nombre del disco: ")
        name_artis_cd=input("Ingrese el nombre del artista/banda: ")
        while True:    
            try:
                year_cd=int(input("Ingrese el año del producto: "))
                if year_cd>2023 or year_cd<1700:
                    print("Ese año no existe.")
                    raise Exception
                break
            except:
                print("Error")
        while True:    
            try:
                gross_price=float(input("El precio en bruto del disco: "))
                price=float(input("El precio del disco al publico: "))
                if gross_price>price:
                    print("Colabora, tendras perdidas.")
                    raise Exception
                break
            except:
                print("Error")
        id=self.random_id()
        while self.search_id(id,1)==False:
            id=self.random_id()
        producs={'id': id,
        'titulo': name_cd,
        'artista': name_artis_cd,
        'año_publicacion': year_cd,
        'costo': gross_price,
        'precio_venta': price
  
        }
        gender=self.gender()
        if not gender in self.inventary:
                self.inventary[gender]=[]
        self.inventary[gender].append(producs)
    

        print("Producto anadido exitosamente.")

    def random_id(self):
        nums=[]
        for x in range(0,1000):
            nums.append(x)
        return random.choice(nums)

    def eliminate_cd(self):
        while True:
            try:
                id=int(input("Ingrese el id del producto: "))
                if self.search_id(id,1)==True:
                    raise Exception
                break
            except:
                print("Error.")
        self.inventary[self.search_id(id,2)].pop(self.inventary[self.search_id(id,2)].index(self.search_id(id,3)))
        print(f"Felicidades el prodcuto {id} fue eliminado.")

    def search_id(self,id,n):
        for k,x in self.inventary.items():
            for j in x:
                if n==1:
                    if len(self.inventary)==0:
                        return False
                    else:
                        if j["id"]==id:
                            return False
                elif n==2:
                    if j["id"]==id:
                        return k
                else:
                    if j["id"]==id:
                        return j

        return True
    def show_inventary(self,k):
        for x in self.inventary.values():
            for j in x:
                print("---------------------------")
                for s in j:
                    if k==j:
                        if "id"==s:
                            print(f'ID: {j[s]}')
                        elif "precio_venta"==s:
                            print(f'{j[s]} $')
                        elif 'costo'==s:
                            pass
                        else:
                            print(j[s])
        print("---------------------------")
    
    def nemu_invoice(self,person):
        n=input("(1)Ver alfabeticamente.\n(2)Ver por ano.\n(3)Ver por precio.\n------------> ")
        while not n in "1,2,3":
            n=input("(1)Ver alfabeticamente.\n(2)Ver por ano.\n(3)Ver por precio.\n------------> ")
        self.show_orden(int(n))
        print("\n\n")
        while True:
            n=0
            option=input("\n1.Anadir disco.\n2.Eliminar disco.\n3.Mostrar el carrito de compra\n4.Pagar.\n5.Salir.\n-------------> ")
            while option!="1" and option!="2" and option!="3" and option!="4" and option!="5":
                option=input("\n1.Anadir disco.\n2.Eliminar disco.\n3.Mostrar el carrito de compra\n4.Pagar.\n5.Salir.\n-------------> ")
            if option=="1":
                n+=1
                j=self.invoice_ad_cd(1)
                count=input("\nIngrese la cantidad de discos que desea: ")
                while not count.isnumeric():
                    count=input("Ingrese la cantidad de discos que desea:")
                if "cantidad" in j:
                    j["suma"]=int(count)
                else:
                    j["cantidad"]=int(count)
                x=self.search_id(j["id"],2)
                if person.empty()== False:
                    person.shopping_car.append([x,j])
                else:
                    person.shopping_car.append([x,j])
                    person.double_item(id)
                print("\n------------------")
                print("Orden añadida")
                print("------------------")
            elif option=="2":
                if person.empty()== False:
                    print("\nNo hay ningun elemento en el carro.")
                else:
                    print(self.inventary)
                    n-=1
                    person.id=self.invoice_ad_cd(2)
                    person.eliminate_shopping_car()
                    print("\n------------------")
                    print("Orden eliminada")
                    print("------------------")
            elif option=="3":
                if person.empty()== False:
                    print("\nNo hay ningun elemento en el carro.")
                else:
                    person.show_atributes()
            elif option=="4":
                if person.empty()== False:
                    print("\nNo hay ningun elemento en el carro.")
                else:
                    person.product_free()
                    person.show_shop_car()
                decision=input("\nEsta seguro (S)(N)").upper()
                while not decision in "S,N":
                   decision=input("Esta seguro (S)(N)").upper() 
                if decision=="S":
                    person.compro=True
                    self.people.append(person)
                    self.create_txt_facturas()
                    self.create_txt_especiales()
                    person.clear_list()
                    person.total=0
                    break 
                else:
                    person.total=0
                    pass
            else:
                person.clear_list()
                self.people.append(person)
                self.create_txt_especiales()
                break
    def invoice_ad_cd(self,n):
        while True:
            try:
                id=int(input("Ingrese el id del producto: "))
                if self.search_id(id,3)==True:
          
                    raise Exception
                break
            except:
                print("Error.")
        if n==1:
            return self.search_id(id,3)
        else:
            return id 
    def gender(self):
        gender=["Rap","K-pop","Rock","Electrónica","Pop","Folk","Flamenco","Jazz","Reguetón","Reggae","Punk"]
        for k,x in enumerate(gender):
            print(f"{k+1}.{x}")
        while True:
            try:
                option=int(input("Genero del disco:(Coloque el numero) "))
                if not option in range(1,12):
                    raise Exception
                break
            except:
                print("Error")
        return gender[option-1]

    def estadisitca(self):
        print(self.factura)
        estadistica={}
        compras={}
        contador={}
        for k, i in self.factura.items():
            if not i[-1] in compras:
                compras[i[-1]]=0
            compras[i[-1]]+=(len(i)-2)
        estadistica["Compras"]={"Top 1":"","Top 2":"","Top 3":""}
        try:
            dni_1=max(compras, key=compras.get)
            compras.pop(dni_1)
            estadistica["Compras"]["Top 1"]=dni_1
            dni_2=max(compras, key=compras.get)
            compras.pop(dni_2)
            estadistica["Compras"]["Top 2"]=dni_2
            dni_3=max(compras, key=compras.get)
            estadistica["Compras"]["Top 3"]=dni_3
        except:
            pass
        for j in self.factura.values():
            for x in j:
                try:
                    if not x[-1] in contador:
                        contador[x[-1]]=1
                    else:
                        contador[x[-1]]+=1
                except:
                    pass        
        estadistica["Genero"]={"Top 1":"","Top 2":"","Top 3":""}
        try:
            top_1=max(contador, key=contador.get)
            contador.pop(top_1)
            estadistica["Genero"]["Top 1"]=top_1
            top_2=max(contador, key=contador.get)
            contador.pop(top_2)
            estadistica["Genero"]["Top 2"]=top_2
            top_3=max(contador, key=contador.get)
            estadistica["Genero"]["Top 3"]=top_3
        except:
            pass
        contador.clear()
        for d in self.factura.values():
            for x in d:
                try:
                    if not x[0]["artista"] in contador:
                        contador[x[0]["artista"]]=1
                    else:
                        contador[x[0]["artista"]]+=1
                except:
                    pass
        estadistica["Artistas"]={"Top 1":"","Top 2":"","Top 3":"","Top 4":"","Top 5":""}
        try:
            top_1_1=max(contador, key=contador.get)
            contador.pop(top_1_1)
            estadistica["Artistas"]["Top 1"]=top_1_1
            top_2_1=max(contador, key=contador.get)
            contador.pop(top_2_1)
            estadistica["Artistas"]["Top 2"]=top_2_1
            top_3_1=max(contador, key=contador.get)    
            contador.pop(top_3_1)
            estadistica["Artistas"]["Top 3"]=top_3_1
            top_4=max(contador, key=contador.get) 
            contador.pop(top_4) 
            estadistica["Artistas"]["Top 4"]=top_4
            top_5=max(contador, key=contador.get) 
            estadistica["Artistas"]["Top 5"]=top_5  
        except:
            pass
        
    def show_orden(self,n):
        orden=[]
        for i in self.inventary.values():
            for j in i:
                if n==1:
                    orden.append(j["titulo"])
                elif n==2:
                    orden.append(j["año_publicacion"])
                else:
                    orden.append(j["precio_venta"])
        orden.sort()
        print(orden)
        for x in orden:
            for i in self.inventary.values():
                for j in i:
                    if n==1:
                        if x==j['titulo']:
                            k=j
                            self.show_inventary(k)
                    elif n==2:
                        if x==j['año_publicacion']:
                            k=j
                            self.show_inventary(k)
                    else:
                        if x==j['precio_venta']:
                            k=j
                            self.show_inventary(k)
    def create_txt_inventary(self):
        with open("Inventario.txt","w") as f: 
            for k,x in self.inventary.items():
                for j in x:
                    f.write(f"{k}/{j['id']}/{j['titulo']}/{j['artista']}/{j['año_publicacion']}/{j['costo']}/{j['precio_venta']}\n")
    def create_txt_person(self):
        with open("Personas.txt","w") as f:
            for x in self.people:
                if x.rol=="Trabajador":
                    f.write(f"{x.rol}/{x.name}/{x.last_name}/{x.dni}\n")
                else:
                    f.write(f"{x.rol}/{x.name}/{x.last_name}/{x.dni}\n")
    def actualizar_datos(self):
        with open("Inventario.txt") as p:  
            for i in p:
                producs={"id":int(i.split("/")[1]),"titulo":i.split("/")[2],"artista":i.split("/")[3],"año_publicacion":int(i.split("/")[4]),"costo":float(i.split("/")[5]),"precio_venta":float(i.split("/")[6])}
                if  i.split("/")[0] in self.inventary:
                    self.inventary[i.split("/")[0]].append(producs)
                else:
                    self.inventary[i.split("/")[0]]=[]
                    self.inventary[i.split("/")[0]].append(producs)

        
        with open("Personas.txt") as j:
            for x in j:
                if x.split("/")[0]=="Trabajador":
                    peron=Customers(x.split("/")[1],x.split("/")[2],int(x.split("/")[3]))
                    if not peron in self.people:
                        self.people.append(peron)
                    else:
                        self.people.append(peron)
                else:
                    peron=Invoice(x.split("/")[1],x.split("/")[2],int(x.split("/")[3])) 
                    if not peron in self.people:
                        self.people.append(peron)
                    else:
                        self.people.append(peron)
                    
        n=1
        with open("Facturas.txt") as l:
            for u in l:
                if u.split("/")[1]=="Factura":
                    factura={"id":int(u.split("/")[3]),"titulo":u.split("/")[4],"artista":u.split("/")[5],"año_publicacion":int(u.split("/")[6]),"costo":float(u.split("/")[7]),"precio_venta":float(u.split("/")[8]),"cantidad":int(u.split("/")[9])}
                    if self.factura.get(n)==None:
                        self.factura[n]=[]
                        self.factura[n].append([factura,u.split("/")[2]])
                    else:
                        self.factura[n].append([factura,u.split("/")[2]])   
                elif u.split("/")[1]=="Total":
                    self.factura[n].append(float(u.split("/")[2]))
                    self.factura[n].append(int(u.split("/")[0]))
                    n+=1
    def create_txt_facturas(self):
        with open("Facturas.txt","a") as f:
            for x in self.people:
                if x.rol=="Cliente":
                    if len(x.shopping_car)!=0:
                        f.write("\n")
                        for s in x.shopping_car:
                            f.write(f"{x.dni}/Factura/{s[0]}/{s[1]['id']}/{s[1]['titulo']}/{s[1]['artista']}/{s[1]['año_publicacion']}/{s[1]['costo']}/{s[1]['precio_venta']}/{s[1]['cantidad']}\n")
                        f.write(f"{x.dni}/Total/{x.total}\n")   
    def create_txt_especiales(self):
        with open("Especiales.txt","a") as f:
            for x in self.people:
                if x.rol=="Cliente":
                    if x.descuento==True:
                        f.write(f"Descuento\n")
                    if x.compro==False:
                        f.write(f"No Compro/\n")   
    def show_estadistica(self,estadistica):
        with open("Especiales.txt")as f:
            for x in f:
                if x=="Descuento":
                    if not "Descuento" in estadistica:
                        estadistica["Descuento"]=1
                    else:
                        estadistica["Descuento"]+=1
                else:
                    if not "No_compro" in estadistica:
                        estadistica["No_compro"]=1
                    else:
                        estadistica["No_compro"]+=1
        print("\nEstadisticas\n")
        print("--------------------")
        for d,i in estadistica.items():
            print(d)
            for k in i:
                if i[k]!="":
                    print(f"{k}: {i[k]}")
            print("\n--------------------")
        if not "Descuento" in estadistica:
            print("Todavia no se aplico nigun descuento.")
        if not "No_compro" in estadistica:
            print("Todas las personas han comprado por ahora.")


        

  

            
