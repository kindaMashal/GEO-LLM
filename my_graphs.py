import networkx as nx
import matplotlib.pyplot as plt

# equation 1 (original): y= 2*x + 3
def build_eq1():
    G= nx.DiGraph()
    G.add_nodes_from([
        ("x",{"label":"x"}),
        ("2",{"label":"2"}),
        ("3",{"label":"3"}),
        ("*",{"label":"*"}),
        ("+",{"label":"+"}),
        ("y",{"label":"y"}) ])

    G.add_edges_from([
        ("x","*"),
        ("2","*"),
        ("*","+"),
        ("3","+"),
        ("+","y") ])

    return G

# equation 2: y= 3 + 2*x
def build_eq2():
    G= nx.DiGraph()
    G.add_nodes_from([
        ("x",{"label":"x"}),
        ("2",{"label":"2"}),
        ("3",{"label":"3"}),
        ("*",{"label":"*"}),
        ("+",{"label":"+"}),
        ("y",{"label":"y"}) ])

    G.add_edges_from([
        ("x","*"),
        ("2","*"),
        ("3","+"),
        ("*","+"),
        ("+","y") ])

    return G


# equation 3: y= (4*x)/2 + 3
def build_eq3():
    G= nx.DiGraph()
    G.add_nodes_from([
        ("x",{"label":"x"}),
        ("4",{"label":"4"}),
        ("2",{"label":"2"}),
        ("3",{"label":"3"}),
        ("*",{"label":"*"}),
        ("/",{"label":"/"}),
        ("+",{"label":"+"}),
        ("y",{"label":"y"}) ])

    G.add_edges_from([
        ("4","*"),
        ("x","*"),
        ("*","/"),
        ("2","/"),
        ("/","+"),
        ("3","+"),
        ("+","y") ])

    return G


#equation 4: y - 2*x - 3 =0, represented as: ( (y-(2*x))-3 ) =0
def build_eq4():
    G= nx.DiGraph()
    G.add_nodes_from([
        ("y",{"label":"y"}),
        ("x",{"label":"x"}),
        ("2",{"label":"2"}),
        ("3",{"label":"3"}),
        ("*",{"label":"*"}),
        ("-1",{"label":"-"}),
        ("-2",{"label":"-"}),
        ("0",{"label":"0"}) ])

    G.add_edges_from([
        ("2","*"),
        ("x","*"),
        ("y","-1"),
        ("*","-1"),
        ("-1","-2"),
        ("3","-2"),
        ("-2","0") ])

    return G


graphs= {
    "y = 2*x + 3": build_eq1(),
    "y = 3 + 2*x": build_eq2(),
    "y = (4*x)/2 + 3": build_eq3(),
    "y - 2*x - 3 = 0": build_eq4()
    }

graphs["y = 2*x + 3"]




# graph visualization 

# import networkx as nx
# import matplotlib.pyplot as plt

# def visualize_graph(G, title):
#     plt.figure(figsize=(6, 5))
    
#     pos = nx.spring_layout(G, seed=42)

#     labels = nx.get_node_attributes(G, "label")
 
#     nx.draw_networkx_nodes(G, pos, node_size=2500, node_color="lightblue")
 
#     nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle="->", arrowsize=20)
 
#     nx.draw_networkx_labels(G, pos, labels, font_size=12, font_weight="bold")
    
#     plt.title(title)
#     plt.axis("off")
#     plt.tight_layout()
#     plt.show()


# for name, graph in graphs.items():
#     visualize_graph(graph, name)











