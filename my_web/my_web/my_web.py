import reflex as rx

#Creamos una clase que hereda de rx.State. Esta clase en un futuro crear aplicaciones interactivas.
class State(rx.State):
    pass

#Creamos una función que tiene que devolver un componente para representar la parte gráfica.
def index() -> rx.Component: 
    return rx.text("Hola Reflex!", color="red")

#Para ejecutar el programa, tenemos que crear una instancia de rx.App.
app = rx.App()
app.add_page(index) #Mediante este método agregamos por ahora la única página que tenemos que es nuestro index.
app.compile() #Ejecutamos el programa.    


    

