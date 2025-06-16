import random as rd
import numpy as np
class Agente:
    def __init__(self, id, xy, estado, tam):
        self.id = id
        self.x, self.y = xy
        self.estado = estado
        self.tam = tam

    def getXy(self):
        return [self.x, self.y]    

    def mover(self):
        if(self.x == 0 and self.y == 0):
            x = rd.choice([0, 1])
            y = rd.choice([0, 1])
            self.x += x
            self.y += y
        elif(self.x == self.tam-1 and self.y == self.tam-1):
            x = rd.choice([0, -1])
            y = rd.choice([0, -1])
            self.x += x
            self.y += y  
        elif(self.x == self.tam-1 and self.y == 0):
            x = rd.choice([0, -1])
            y = rd.choice([0, 1])
            self.x += x
            self.y += y
        elif(self.x == 0 and self.y == self.tam-1):
            x = rd.choice([0, 1])
            y = rd.choice([0, -1])
            self.x += x
            self.y += y          
        elif(self.x == 0):
            x = rd.choice([0, 1])
            y = rd.choice([0, 1, -1])    
            self.x += x
            self.y += y
        elif(self.y == 0):
            x = rd.choice([0, 1, -1])
            y = rd.choice([0, 1])    
            self.x += x
            self.y += y
        elif(self.x == self.tam-1):
            x = rd.choice([0, -1])
            y = rd.choice([0, 1, -1])    
            self.x += x
            self.y += y
        elif(self.y == self.tam-1):
            x = rd.choice([0, 1, -1])
            y = rd.choice([0, -1])    
            self.x += x
            self.y += y
        else:
            x = rd.choice([0, 1, -1])
            y = rd.choice([0, 1, -1])    
            self.x += x
            self.y += y
#Quantidade de agentes, tamanho do grid, quantidade inicial de infectados, porcentagem de infecção
class Ambiente:
    def __init__(self, quan, tam, quanInicial, PorcenInfec, quanDias):
        self.quan = quan
        self.tam = tam
        self.grid = np.zeros((tam, tam))
        self.quanInicial = quanInicial
        self.PorcenInfec = PorcenInfec
        self.quanDias = quanDias
        self.listaAgentes = []
        
    def gerarAgentes(self):
        estado = 'S'
        id = 1
        x = 0
        y = 0
        for n in range(self.quan):
            if(self.quanInicial != 0):
                estado = 'I'
                self.quanInicial -= 1
            else:
                estado = 'S'
            x = rd.randint(0, self.tam-1)
            y = rd.randint(0, self.tam-1)
            a = Agente(id, [x, y], estado, self.tam)
            self.grid[y, x] += 1
            self.listaAgentes.append(a)
            id += 1

    def printarGrid(self):
        for linha in self.grid:
            print(linha)
        print("\n")


    def simulacao(self):
        self.gerarAgentes()
        self.printarGrid()

        for d in range(self.quanDias):
            for a in self.listaAgentes:
                valoresXY = a.getXy()
                self.grid[valoresXY[1], valoresXY[0]] -= 1
                a.mover()
                valoresXY = a.getXy()
                self.grid[valoresXY[1], valoresXY[0]] += 1
            self.printarGrid()    

        self.printarGrid()   





amb = Ambiente(10, 5, 2, 0.1, 10)
amb.simulacao()




