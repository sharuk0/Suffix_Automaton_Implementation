import networkx as nx

def build_graph(automaton):
    G = nx.DiGraph()
    for i, state in enumerate(automaton.states):
        for char, target in state.edges.items():
            G.add_edge(i, target, label=char)
    return G
