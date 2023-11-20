import graph_rep
import Imple_Suf_Atu
import graph_visualize

s = "abb"
automaton = Imple_Suf_Atu.SuffixAutomaton(s)
G = graph_rep.build_graph(automaton)
graph_visualize.visualize_automaton(G)
