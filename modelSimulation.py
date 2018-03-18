__author__ = 'Bhavin.Parekh'
import networkx as nx
import random

import ndlib.models.ModelConfig as mc
import ndlib.models.CompositeModel as gc
import ndlib.models.compartments.NodeCategoricalAttribute as ns

# Network generation
g = nx.erdos_renyi_graph(1000, 0.1)

# Setting node attribute
attr = {n: {"Sex": random.choice(['male', 'female'])} for n in g.nodes()}
nx.set_node_attributes(g, attr)

# Composite Model instantiation
model = gc.CompositeModel(g)

# Model statuses
model.add_status("Susceptible")
model.add_status("Infected")
model.add_status("Removed")

# Compartment definition
c1 = na.NodeCategoricalAttribute("Sex", "male", probability=0.6)

# Rule definition
model.add_rule("Susceptible", "Infected", c1)

# Model initial status configuration
config = mc.Configuration()
config.add_model_parameter('percentage_infected', 0)

# Simulation execution
model.set_initial_status(config)
iterations = model.iteration_bunch(100)