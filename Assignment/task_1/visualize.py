import networkx as nx 
import matplotlib.pyplot as plt
import pandas as pd 
import networkx as nx 

# Convert the data into networkx format
G = nx.from_pandas_edgelist(df[df["Item and Group"] != 'All items'], 
                            source = 'Item and Group', target = 'Parent', edge_attr = 'Weight')

# Set the positions of the nodes in the graph - other options are spring, planar or spectral
pos = nx.kamada_kawai_layout(G, weight = None)
for n, p in pos.items():
    G.nodes[n]['pos'] = p
    
# Add weight and depth attributes to the nodes
for x in df["Item and Group"]: 
    G.nodes[x]['Weight'] = df[df["Item and Group"] == x]["Weight"].values[0]
    G.nodes[x]['Depth'] = df[df["Item and Group"] == x]["Indent Level"].values[0]
    
# Add position info to edges
edge_x = []
edge_y = []

for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

# Draw the edges
edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []

for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

# Draw the nodes
node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Indent Level',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

node_depth = []
node_text = []

for n in G.nodes.items():
    node_depth.append(n[1]["Depth"])
    node_text.append(n[0] + " {0:.2f}%".format(n[1]["Weight"]))
                         
node_trace.marker.color = node_depth
node_trace.text = node_text

# Draw the full graph
graph = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='8-Level network graph',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
graph.show()

