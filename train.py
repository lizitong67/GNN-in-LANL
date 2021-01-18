import dgl
import numpy as np
import time
import torch as th
import torch.nn as nn
from auth_to_graph import graph_construction
from EGAT import EGATLayer

def graph_embedding():
    egat = EGATLayer(20, 4, 25)
    egat_optimizer = th.optim.Adam(egat.parameters())

    for epoch in range(1):
        egat.train()
        t0 = time.time()
        loss_list = []
        rst = egat(graph, node_feats, edge_feats)
        print(rst.shape)
        print(rst.view(rst.shape[0], -1).shape)

    #     features = batched_graph.ndata['feat'].float()
    #     loss = dgi(batched_graph, features)decoder
    #     egat_optimizer.zero_grad()
    #     loss.backward()
    #     egat_optimizer.step()
    #     loss_list.append(loss.item())
    #     print("Epoch {:05d} | Time(s) {:.4f} | Loss {:.4f}".format(epoch, time.time()-t0, np.mean(loss_list)))
    # th.save(dgi.state_dict(), 'best_dgi.pkl')
    # print("[+] The best graph embedding model has been saved.")


if __name__ == '__main__':
    graph, edge_feats, node_feats, labels, train_mask = graph_construction()
    print("[+] Graph Constructing...")
    print("The graph information is as follows:")
    print(graph)
    print(edge_feats.shape)
    print(node_feats.shape)
    print("--------------------------------------------------------------- ")
    rst = graph_embedding()
