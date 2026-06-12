from  my_graphs import graphs
from grakel import Graph, OddSth  
from grakel.kernels import WeisfeilerLehman, VertexHistogram
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from OptimModelGraphs import graphs_math
import finaloptimgraphing



# # graphkeL format requires each graph to be a tuple of (edge_list, node_labels)
# edges_g1 = [
#     ("x", "*"), ("2", "*"),  
#     ("*", "+"), ("3", "+"),   
#     ("+", "y")            
# ]
# node_labels_g1 = {
#     "x": "x", "2": "2", "3": "3",
#     "*": "*", "+": "+", "y": "y"
# }


# edges_g3 = [
#     ("4", "*"), ("x", "*"),   
#     ("*", "/"), ("2", "/"),   
#     ("/", "+"), ("3", "+"),  
#     ("+", "y")                
# ]
# node_labels_g3 = {
#     "x": "x", "4": "4", "2": "2", "3": "3",
#     "*": "*", "/": "/", "+": "+", "y": "y"
# }


# g1 = Graph(
#     initialization_object=edges_g1,
#     node_labels=node_labels_g1
# )
# g2 = Graph(
#     initialization_object=edges_g3,
#     node_labels=node_labels_g3
# )

# kernel = WeisfeilerLehman(n_iter=3, base_graph_kernel=VertexHistogram)
# k = kernel.fit_transform([g1, g2]) # note: the k here is a similarity matrix 
# # so k[0,0] is the similarity of g1 with itself, k[1,1] is the similarity of g3 with itself, and k[0,1] (or k[1,0]) is the similarity between g1 and g3

# norms = np.sqrt(np.diag(k))
# k_norm = k / np.outer(norms, norms)

# print("the similarity between graph 1 and itself: {:3f}".format(k_norm[0,0]))
# print("the similarity between graph 1 and graph 2: {:3f}".format(k_norm[0, 1]))


def nx_to_grakel(graph):
    edges= list(graph.edges())
    node_labels= {node: graph.nodes[node].get("label", str(node)) for node in graph.nodes()}
    return Graph(edges, node_labels=node_labels)



# grakel_graphs= [nx_to_grakel(g) for g in graphs.values()]
# graph_names= list(graphs.keys())

math_grakel_graphs= [nx_to_grakel(g) for g in graphs_math.values()]

wl_kernel_math = WeisfeilerLehman(n_iter=10, base_graph_kernel=VertexHistogram, normalize=True)
sim_math = wl_kernel_math.fit_transform(math_grakel_graphs)
print("WL graph_kel")
print("ground truth with ground truth",sim_math[0,0])
print("ground truth with var1: {:.2f}".format(sim_math[0,1]))
print("ground truth with var2: {:.2f}".format(sim_math[0,2]))
print("ground truth with var3: {:.2f}".format(sim_math[0,3]))
print("ground truth with var4: {:.2f}\n".format(sim_math[0,4]))

odd_kernel_math = OddSth(h=10, normalize=True)
sim_math = odd_kernel_math.fit_transform(math_grakel_graphs)
print("OddSth graph_kel")
print("ground truth with ground truth",sim_math[0,0])
print("ground truth with var1: {:.2f}".format(sim_math[0,1]))
print("ground truth with var2: {:.2f}".format(sim_math[0,2]))
print("ground truth with var3: {:.2f}".format(sim_math[0,3]))
print("ground truth with var4: {:.2f}".format(sim_math[0,4]))


# wl_kernel = WeisfeilerLehman(n_iter=3, base_graph_kernel=VertexHistogram, normalize=True)
# sim = wl_kernel.fit_transform(grakel_graphs)

# print(sim[0,0])
# print(sim[0,2])


# odd_kernel = OddSth(h=3, normalize=True)
# sim = odd_kernel.fit_transform(grakel_graphs)

# print(sim[0, 0])
# print(sim[0, 2])

# problems: does not work well with networkx and igraph 
# has compatibility issues with Numpy2 (this code did not even run)

# why different similarity score?
# the wl in graphkel only considers undirected graphs (so outgoing edges)

from finaloptimgraphing import graphs, bipartite_graphs


grakel_graphs = [nx_to_grakel(g) for g in graphs.values()]
graph_names = list(graphs.keys())

bipartite_grakel_graphs = [nx_to_grakel(g) for g in bipartite_graphs.values()]

-
wl_kernel = WeisfeilerLehman(n_iter=10, base_graph_kernel=VertexHistogram, normalize=True)
sim = wl_kernel.fit_transform(grakel_graphs)

print("WL Kernel: Model Graphs")
print(f"ground truth with ground truth: {sim[0,0]:.2f}")
for i in range(1, len(graph_names)):
    print(f"ground truth with {graph_names[i]}: {sim[0,i]:.2f}")


odd_kernel = OddSth(h=10, normalize=True)
sim_odd = odd_kernel.fit_transform(grakel_graphs)

print("\nOddSth Kernel: Model Graphs")
print(f"ground truth with ground truth: {sim_odd[0,0]:.2f}")
for i in range(1, len(graph_names)):
    print(f"ground truth with {graph_names[i]}: {sim_odd[0,i]:.2f}")


wl_kernel_bi = WeisfeilerLehman(n_iter=10, base_graph_kernel=VertexHistogram, normalize=True)
sim_bi = wl_kernel_bi.fit_transform(bipartite_grakel_graphs)

print("\n WL Kernel: Bipartite Graphs")
print(f"ground truth with ground truth: {sim_bi[0,0]:.2f}")
for i in range(1, len(graph_names)):
    print(f"ground truth with {graph_names[i]}: {sim_bi[0,i]:.2f}")


odd_kernel_bi = OddSth(h=10, normalize=True)
sim_odd_bi = odd_kernel_bi.fit_transform(bipartite_grakel_graphs)

print("\nOddSth Kernel: Bipartite Graphs")
print(f"ground truth with ground truth: {sim_odd_bi[0,0]:.2f}")
for i in range(1, len(graph_names)):
    print(f"ground truth with {graph_names[i]}: {sim_odd_bi[0,i]:.2f}")
