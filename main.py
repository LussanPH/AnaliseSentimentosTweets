import mesa
#print(mesa.__version__)

from mesa import Agent

class Habitante(Agent):
    def __init__(self, unique_id, model, idade, saneamento, infectado=False):
        super().__init__(unique_id, model)
        self.idade = idade
        self.saneamento = saneamento
        self.infectado = infectado

    def step(self):
        if self.infectado:
            vizinhos = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)#moore: Pega as 8 casas vizinhas a posição; include_center: Verifica se a célula que contém o elemento deve ser incluida; self.pos: Posição do agente no grid
            for agente in vizinhos:
                if not agente.infectado:
                    chance = 0.2
                    # Se não tem saneamento, chance aumenta
                    if not agente.saneamento:
                        chance += 0.3
                    if self.random.random() < chance:
                        agente.infectado = True
                        '''self.model.datacollector.add_table_row("tabela", {
                          "Agente": self.unique_id,
                          "Evento": "Infectado",
                          "Tempo": self.model.schedule.time
                        })'''
            
from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
import random

def agent_portrayal(agent):
    if agent.infectado:
      color = 'red'
    else:
      color = 'green'
    return {
        "Shape": "circle",
        "Filled": "true",
        "Layer": 0,
        "Color": color,
        "r": 0.5
    }

class ModeloVirus(Model):
    def __init__(self, N, largura, altura):
        super().__init__()
        self.num_agentes = N
        self.grid = MultiGrid(largura, altura, torus=False)#torus não permite que o agente saia da borda e apareca do outro lado do mapa
        self.schedule = RandomActivation(self)

        for i in range(self.num_agentes):
            idade = random.randint(0, 90)
            saneamento = random.random() < 0.7  # 70% com saneamento
            infectado = i == 0  # só o primeiro começa infectado

            agente = Habitante(i, self, idade, saneamento, infectado)
            self.schedule.add(agente)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agente, (x, y))

        self.datacollector = DataCollector(
            model_reporters={"Total Infected": lambda m: sum([a.infectado for a in m.schedule.agents])},
            agent_reporters={"Infected": "infectado"}
        )

        '''self.datacollector = DataCollector(
            tables={"tabela": ["Agente", "Evento", "Tempo"]}
        )'''    

    def step(self):
      self.datacollector.collect(self)
      self.schedule.step()

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

server = ModularServer(
    ModeloVirus,
    [grid],
    "Modelo de Infecção",
    {"N": 100, "largura": 10, "altura": 10}
)

server.port = 8522  # Porta padrão
server.launch()
