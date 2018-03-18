__author__ = 'Bhavin.Parekh'
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def main():

    # Make a graph and add 3 nodes: Susceptible, Infected and Recovered
    G = nx.Graph()
    G.add_nodes_from("SIR")

    # Simulation Parameters
    t_steps = 1000  # simulation time
    N_total = 1000  # total population size (N)
    beta = 0.1         # infection rate (beta)
    gamma = 0.05       # recovery rate (gamma)

    # Set initial conditions
    init_values = {'S': N_total - 1,
                   'I': 1,
                   'R': 0 }
    for node in "SIR":
        G[node]['t'] = np.empty( (t_steps), dtype='float16' )
        G[node]['t'][0] = init_values[node]

    # Run the simulation.
    for t in range(1, t_steps):
        s, i, r = G['S']['t'][t-1], G['I']['t'][t-1], G['R']['t'][t-1]
        G['S']['t'][t] = s + (-beta * i * s / N_total)
        G['I']['t'][t] = i + (beta * i * s / N_total) - (gamma * i)
        G['R']['t'][t] = r + (gamma * i)

    # Print the number of susceptibles, infected and recovered at a few time points.
    print(G)
    print(G, 100)
    print(G, t_steps-1)
    main()

    # Plot the time course of infection for each compartment.
    plt.plot(G['S']['t'], 'g.')
    plt.plot(G['I']['t'], 'b.')
    plt.plot(G['R']['t'], 'r.')
    plt.show()
