from manejadorRegistro import ManejadorRegistro as MR
from menu import Menu as M

def test():

    contolador = MR()
    contolador.cargarArchivo()
    print("SE CARGO EL ARCHIVO")
    menu = M()
    menu.opciones(contolador)


if __name__ == '__main__':
    test ()