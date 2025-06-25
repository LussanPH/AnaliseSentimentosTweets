import random as rd
import numpy as np
class Agente:
    def __init__(self, id, xy, estado):
        self.id = id
        self.x, self.y = xy
        self.estado = estado

    def getXy(self):
        return [self.x, self.y]    
    
    def getId(self):
        return self.id
    
    def getEstado(self):
        return self.estado

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
        self.quanInicial = quanInicial
        self.PorcenInfec = PorcenInfec
        self.quanDias = quanDias
        self.listaAgentes = []
        
    def gerarAgentes(self, grid):
        estado = 'S'
        id = 1
        x = 0
        y = 0
        for n in range(self.quan):
            if(self.quanInicial != 0):
                estado = 'I'
                self.quanInicial -= 1

            x = rd.randint(0, self.tam-1)
            y = rd.randint(0, self.tam-1)
            a = Agente(id, [x, y], estado)
            grid[y][x].append(a.getId())
            id += 1

    def gerarGrid(self):
        grid = []
        for i in range(self.tam):
            listai = []
            grid.append(listai)
            for j in range(self.tam):
                listaj = []
                listai.append(listaj)
        return grid        

    def printarGrid(self, grid):
        for linha in grid:
            print(linha)
        print("\n")    

    def removerPessoa(self, valoresXy, id, grid):
        for a in grid[valoresXy[1], valoresXy[0]]:
            idAtual = a.getId()
            if idAtual == id:
                grid[valoresXy[1], valoresXy[0]].remove(a)
                return
            
    def adicionarPessoa(self, valoresXy) #Falta adicionar pessoa       
            

    def simulacao(self):
        grid = self.gerarGrid()
        self.gerarAgentes(grid)
        self.printarGrid(grid)

        for d in range(self.quanDias):

            for a in self.listaAgentes:

                valoresXY = a.getXy()
                estado = a.getEstado()
                id = a.getId()

                #if(pessoas > 1 and estado == 'I'):
                    #self.infectar(pessoas, self.listaAgentes)

                self.removerPessoa(valoresXY, id, grid)
                a.mover()
                valoresXY = a.getXy()
                grid[valoresXY[1], valoresXY[0]].append(a)

            self.printarGrid()    

        self.printarGrid()   





amb = Ambiente(10, 5, 2, 0.1, 10)
amb.simulacao()



