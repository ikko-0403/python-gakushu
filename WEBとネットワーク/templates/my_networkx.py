import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_node(1)#グラフ G にノード（頂点）「1」を追加する

G.add_nodes_from([2, 3])#ノード 2 と 3 を一気にグラフ G に追加する

G.add_edge(1,2)#ード 1 とノード 2 の間に「辺（エッジ）」を1本追加する
G.add_edge(2,3)


nx.draw(G)
plt.show()