
import sympy as sp
import networkx as nx
import matplotlib.pyplot as plt

#define symbols
x1,x2= sp.symbols('x1 x2')
x, y = sp.symbols('x y')

ground_truth= {
    "objective": 10*x1 + 12*x2,
    "constraints": [
        sp.Le(5*x1 + 4*x2,50),
        sp.Le(2*x1 + 4*x2,30),
        sp.Le(x1 + 2*x2,20),
        sp.Ge(x1, 0), 
        sp.Ge(x2, 0)
    ]
}

variant1={
    "objective": 10*x1 + 12*x2,
    "constraints": [
        sp.Le(5*x1 + 4*x2,50),
        sp.Le(2*x1 + 4*x2,30),
        sp.Ge(x1, 0), 
        sp.Ge(x2, 0) 
    ]
}

variant2 = {
    "objective": 10*x1 + 12*x2,
    "constraints": [
        sp.Le(5*x1,50 - 4*x2),
        sp.Le(4*x2,30 - 2*x1),
        sp.Le(x1 + 2*x2,20),
        sp.Ge(x1, 0),   
        sp.Ge(x2, 0) 
    ]
}

variant3= {
    "objective": 10*x1 + 12*x2,
    "constraints":[
        sp.Le(5*x1,50 - 4*x2),
        sp.Le(4*x2,30 - 2*x1),
        sp.Ge(x1, 0),  
        sp.Ge(x2, 0) 
    ]
}

variant4= {
    "objective": 10*x + 12*y,
    "constraints": [
        sp.Le(5*x + 4*y,50),
        sp.Le(2*x + 4*y,30),
        sp.Le(x + 2*y,20),
        sp.Ge(x, 0),  
        sp.Ge(y, 0) 
    ]
}

models= {
    "GroundTruth":ground_truth,
    "Variant1":variant1,
    "Variant2":variant2,
    "Variant3":variant3,
    "Variant4":variant4
}

def canonical_constraint(constraint):
    expr= constraint.lhs - constraint.rhs
    return sp.expand(expr)

def extract_variables(model):
    vars_set = set()
    vars_set |= model["objective"].free_symbols

    for c in model["constraints"]:
        vars_set |= c.free_symbols

    print(vars_set)
    return list(vars_set)


def build_model_graph(model,name):
    
    G= nx.DiGraph()
    G.add_node("MODEL",type="model")

    variables= extract_variables(model)

    # add the variable nodes
    for v in variables:
        G.add_node(str(v),type="variable")

    # add the objective node
    G.add_node("OBJECTIVE", type="objective")
    G.add_edge("OBJECTIVE","MODEL")

    obj_expr= sp.expand(model["objective"])

    for v in variables:
        coef= float(obj_expr.coeff(v))
        coef_node= f"obj_coef_{v}"

        G.add_node(coef_node,value=coef)

        G.add_edge(coef_node,str(v))
        G.add_edge(str(v), "OBJECTIVE")

    #add the constraints
    for i, c in enumerate(model["constraints"]):
        cname= f"C{i+1}"

        G.add_node(cname,type="constraint")
        G.add_edge(cname,"MODEL")

        expr= canonical_constraint(c)

        for v in variables:
            coef= float(expr.coeff(v))
            coef_node= f"{cname}_coef_{v}"

            G.add_node(coef_node,value=coef)

            G.add_edge(coef_node,str(v))
            G.add_edge(str(v),cname)

        constant= float(expr.subs({v:0 for v in variables}))
        const_node= f"{cname}_const"

        G.add_node(const_node,value=constant)

        G.add_edge(const_node,cname)

    return G

graphs_math={}

for name,model in models.items():
    graphs_math[name]= build_model_graph(model,name)




