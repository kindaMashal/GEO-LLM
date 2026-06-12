import my_graphs
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# note: this code was implemented using this paper: https://www.jmlr.org/papers/volume12/shervashidze11a/shervashidze11a.pdf
# the paper above deals with undirected graphs so a small ulteration was done on this code to suit the directed graphs 

def wl_relabel(G, label_dict, label_counter, iteration):
        new_labels = {}
        for node in G.nodes():
            current_label = label_dict[G][node]
            
            neighbor_labels = sorted(
                [label_dict[G][n] for n in G.predecessors(node)] +
                [label_dict[G][n] for n in G.successors(node)]
            )
            
            signature = f"iter{iteration}_{current_label}_{'_'.join(map(str, neighbor_labels))}"
            if signature not in label_counter:
                label_counter[signature] = len(label_counter)
            new_labels[node] = label_counter[signature]
        
        return new_labels


def init_labels(G,label_counter):
    labels = {}
    for node in G.nodes():
        lbl = G.nodes[node].get("label", str(node))
        if lbl not in label_counter:
            label_counter[lbl] = len(label_counter)
        labels[node] = label_counter[lbl]
    return labels


def get_histogram(G, labels):
    return Counter(labels[node] for node in G.nodes())


def dot_product(c1, c2):
        return sum(c1[k] * c2[k] for k in c1 if k in c2)



def wl_kernel(G1, G2, n_iterations=3):

    label_counter = {} 
    label_dict = {
        G1: init_labels(G1,label_counter),
        G2: init_labels(G2,label_counter)
    }
    
    feature_G1 = Counter()
    feature_G2 = Counter()
    
    for iteration in range(n_iterations + 1):  
        feature_G1 += get_histogram(G1, label_dict[G1])
        feature_G2 += get_histogram(G2, label_dict[G2])
        
        new_labels_G1 = wl_relabel(G1, label_dict, label_counter, iteration)
        new_labels_G2 = wl_relabel(G2, label_dict, label_counter, iteration)
        label_dict[G1] = new_labels_G1
        label_dict[G2] = new_labels_G2
    
    kernel_value = dot_product(feature_G1, feature_G2)
    norm = (dot_product(feature_G1, feature_G1) * dot_product(feature_G2, feature_G2)) ** 0.5
    similarity = kernel_value / norm if norm > 0 else 0.0
    
    return similarity
