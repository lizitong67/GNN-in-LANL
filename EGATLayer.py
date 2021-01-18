#! /usr/bin/env python
"""
GAT Layer with edge features encoded
Author:	Alston
Date: 2021.1.10
"""
import dgl
import torch as th
import torch.nn as nn
import dgl.function as fn
from dgl.utils import expand_as_pair
from dgl.ops import edge_softmax
from dgl.nn.pytorch import GATConv
from time import *


class EGATLayer(nn.Module):
    def __init__(self,
                 in_feats,
                 out_feats,
                 edata_channels):
        super(EGATLayer, self).__init__()
        self._edata_channels = edata_channels
        self._in_src_feats, self._in_dst_feats = expand_as_pair(in_feats)
        self._out_feats = out_feats

        self.fc = nn.Linear(self._in_src_feats, self._out_feats * edata_channels, bias=False)
        self.edge_fc = nn.Linear(self._edata_channels, self._edata_channels, bias=False)
        self.nfeat_with_e_fc = nn.Linear(out_feats+1, out_feats , bias=False)
        self.attn_l = nn.Parameter(th.FloatTensor(size=(1, edata_channels, out_feats)))
        self.attn_r = nn.Parameter(th.FloatTensor(size=(1, edata_channels, out_feats)))
        self.leaky_relu = nn.LeakyReLU(0.2)
        self.reset_parameters()

    def reset_parameters(self):
        """
        Description
        -----------
        Reinitialize learnable parameters.

        Note
        ----
        The fc weights :math:`W^{(l)}` are initialized using Glorot uniform initialization.
        The attention weights are using xavier initialization method.
        """
        gain = nn.init.calculate_gain('relu')
        nn.init.xavier_normal_(self.fc.weight, gain=gain)
        nn.init.xavier_normal_(self.edge_fc.weight, gain=gain)
        nn.init.xavier_normal_(self.attn_l, gain=gain)
        nn.init.xavier_normal_(self.attn_r, gain=gain)

    def forward(self, graph, node_feat, edge_feat):
        with graph.local_scope():
            h_src = h_dst = node_feat
            feat_src = feat_dst = self.fc(h_src).view(-1, self._edata_channels, self._out_feats)
            e_feat = self.edge_fc(edge_feat).view(-1, self._edata_channels, 1)
            graph.edata.update({'feat': e_feat})
            el = (feat_src * self.attn_l).sum(dim=-1).unsqueeze(-1)
            er = (feat_dst * self.attn_r).sum(dim=-1).unsqueeze(-1)
            graph.srcdata.update({'feat': feat_src, 'el': el})
            graph.dstdata.update({'er': er})

            # compute edge attention, el and er are a_l Wh_i and a_r Wh_j respectively.
            graph.apply_edges(fn.u_add_v('el', 'er', 'e'))
            e = graph.edata.pop('e') * e_feat
            e = self.leaky_relu(e)

            # compute softmax
            graph.edata['a'] = edge_softmax(graph, e)

            # message passing
            def message_func(edges):
                feat_with_e = th.cat([edges.src['feat'], edges.data['feat']], 2)
                # apply a fc layer to adjust the dim of node feat that concatenate E_p to the out_feat_dim
                feat_with_e = self.nfeat_with_e_fc(feat_with_e)
                return {'m': edges.data['a'] * feat_with_e}

            graph.update_all(message_func,
                             fn.sum('m', 'ft'))
            rst = graph.dstdata['ft']
            rst = th.sigmoid(rst)
            return rst


# test
# start_time = time()
# num_nodes = 5
# num_edges = 4
# node_feat_dim = 3
# edge_feat_dim = 2
# out_node_feat_dim = 4
# g = dgl.rand_graph(num_nodes,num_edges)
# model = EGATLayer(node_feat_dim, out_node_feat_dim, edge_feat_dim)
# rst = model(g, th.randn(num_nodes,node_feat_dim), th.randn(num_edges,edge_feat_dim))
# print(rst)
# end_time = time()
# print("Time used: " + str(end_time - start_time))





