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


class EGATLayer(nn.Module):
    def __init__(self,
                 in_feats,
                 out_feats,
                 edata_channels):
        super(EGATLayer, self).__init__()
        self._edata_channels = edata_channels
        self._in_src_feats, self._in_dst_feats = expand_as_pair(in_feats)
        self._out_feats = out_feats

        self.fc = nn.Linear(self._in_src_feats, out_feats * edata_channels, bias=False)
        self.edge_fc = nn.Linear(self._edata_channels, self._edata_channels, bias=False)
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
        nn.init.xavier_normal_(self.attn_l, gain=gain)
        nn.init.xavier_normal_(self.attn_r, gain=gain)


    def forward(self, graph, node_feat, edge_feat):
        with graph.local_scope():
            h_src = h_dst = node_feat
            feat_src = feat_dst = self.fc(h_src).view(-1, self._edata_channels, self._out_feats)
            e_feat = self.edge_fc(edge_feat).view(-1, self._edata_channels, 1)
            el = (feat_src * self.attn_l).sum(dim=-1).unsqueeze(-1)
            er = (feat_dst * self.attn_r).sum(dim=-1).unsqueeze(-1)
            graph.srcdata.update({'ft': feat_src, 'el': el})
            graph.dstdata.update({'er': er})

            # compute edge attention, el and er are a_l Wh_i and a_r Wh_j respectively.
            graph.apply_edges(fn.u_add_v('el', 'er', 'e'))
            e = self.leaky_relu(graph.edata.pop('e'))
            e = e * e_feat

            # compute softmax
            graph.edata['a'] = edge_softmax(graph, e)

            # # message passing




g = dgl.rand_graph(4,5)
g.ndata['feat'] = th.randn(4,2)
g.edata['feat'] = th.randn(5,3)
model = EGATLayer(2, 3, 3)
model(g, g.ndata['feat'], g.edata['feat'])







