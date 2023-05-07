import csv
from registro import Registro

class ManejadorRegistro:

    def __init__(self):
        self.__listabidim = [[Registro(None, None, None) for _ in range (24)] for _ in range(3)]

    def cargarArchivo(self):
        archivo = open ('registrovariables.csv')
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
            dia = int(fila[0])
            hora = int(fila[1])
            temperatura = float(fila[2])
            humedad = float(fila[3])
            presion = float(fila[4])
            instancia = Registro(temperatura,humedad,presion)
            self.__listabidim[dia-1][hora] = instancia
        archivo.close
        return self.__listabidim

    def menorTemperatura(self):
        minimo = 1000000000
        minimoDia = 0
        minimoHora = 0
        for i in range(3):
            for j in range(24):
                if  self.__listabidim[i][j].retornaTemp() < minimo:
                    minimo = self.__listabidim[i][j].retornaTemp()
                    minimoDia = i + 1
                    minimoHora = j
        print("El minimo es {} en el dia {} a la hora {}".format(minimo, minimoDia, minimoHora))                    

    def mayorTemperatura(self):
        maximo = -1000000000
        maximoDia = 0
        maximoHora = 0
        for i in range(3):
            for j in range(24):
                if  self.__listabidim[i][j].retornaTemp() > maximo:
                    maximo = self.__listabidim[i][j].retornaTemp()
                    maximoDia = i + 1
                    maximoHora = j
        print("El maximo es {} en el dia {} a la hora {}".format(maximo, maximoDia, maximoHora))
    
    def menorHumedad(self):
        minimo = 1000000000
        minimoDia = 0
        minimoHora = 0
        for i in range(3):
            for j in range(24):
                if  self.__listabidim[i][j].retornaHum() < minimo:
                    minimo = self.__listabidim[i][j].retornaHum()
                    minimoDia = i + 1
                    minimoHora = j
        print("El minimo es {} en el dia {} a la hora {}".format(minimo, minimoDia, minimoHora))  
    
    def mayorHumedad(self):
        maximo = -1000000000
        maximoDia = 0
        maximoHora = 0
        for i in range(3):
            for j in range(24):
                if  self.__listabidim[i][j].retornaHum() > maximo:
                    maximo = self.__listabidim[i][j].retornaHum()
                    maximoDia = i + 1
                    maximoHora = j
        print("El maximo es {} en el dia {} a la hora {}".format(maximo, maximoDia, maximoHora))  

    def menorPresion(self):
        minimo = 1000000000
        minimoDia = 0
        minimoHora = 0
        for i in range(3):
            for j in range(24):
                if  self.__listabidim[i][j].retornaPre() < minimo:
                    minimo = self.__listabidim[i][j].retornaPre()
                    minimoDia = i + 1 
                    minimoHora = j
        print("El minimo es {} en el dia {} a la hora {}".format(minimo, minimoDia, minimoHora))  
    
    def mayorPresion(self):
        maximo = -1000000000
        maximoDia = 0
        maximoHora = 0
        for i in range(3):
            for j in range(24):
                if  self.__listabidim[i][j].retornaPre() > maximo:
                    maximo = self.__listabidim[i][j].retornaPre()
                    maximoDia = i + 1
                    maximoHora = j
        print("El maximo es {} en el dia {} a la hora {}".format(maximo, maximoDia, maximoHora))


    
    def promedioTempMensual(self):
        for j in range(24):
            acum = 0
            for i in range (3):
                acum += self.__listabidim[i][j].retornaTemp()
                print("La temperatura promedio de la hora {} en el mes es de: {:.2f}". format(j,acum/3))



    def listarValores(self, dia):
        
        print("Valores registrados del dia {}".format(dia))
        print ("DIA:---{}--- ".format(dia))
        print("Hora\tTemperatura\tHumedad\t\tPresion")
        for hora in range(24):
            print("{}\t{}\t\t{}\t\t{}".format(hora,self.__listabidim[dia-1][hora].retornaTemp(),self.__listabidim[dia-1][hora].retornaHum(),self.__listabidim[dia-1][hora].retornaPre()))


    