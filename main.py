from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from WL_Kernel import wl_kernel
import my_graphs
import OptimModelGraphs


# g1=my_graphs.graphs["y = 2*x + 3"]
# g2 = my_graphs.graphs["y = (4*x)/2 + 3"]

# sim_self = wl_kernel(g1, g1, n_iterations=3)
# print("similarity graph with itself:", sim_self)

# sim_diff = wl_kernel(g1, g2, n_iterations=3)
# print("computing the similarity between two diff graphs: {:.3f}".format(sim_diff))

# print('\n')


# testing out mathematical formulas 

gt = OptimModelGraphs.graphs_math["GroundTruth"]
var1 = OptimModelGraphs.graphs_math["Variant1"]
var2 = OptimModelGraphs.graphs_math["Variant2"]
var3 = OptimModelGraphs.graphs_math["Variant3"]
var4 = OptimModelGraphs.graphs_math["Variant4"]

sim_self = wl_kernel(gt, gt, n_iterations=3)
print("similarity graph with groundtruth with itself:", sim_self)

sim_diff = wl_kernel(gt, var1, n_iterations=3)
print("computing the similarity between ground truth and variant1: {:.3f}".format(sim_diff))

sim_diff = wl_kernel(gt, var2, n_iterations=3)
print("computing the similarity between ground truth and variant2: {:.3f}".format(sim_diff))

sim_diff = wl_kernel(gt, var3, n_iterations=3)
print("computing the similarity between ground truth and variant3: {:.3f}".format(sim_diff))

sim_diff = wl_kernel(gt, var4, n_iterations=3)
print("computing the similarity between ground truth and variant4: {:.3f}".format(sim_diff))
