"""
Construct data into homo-graph
Author:	Alston
Date:	2021.1.9
"""
import dgl
import torch as th
from time import *


def graph_construction():
    # malicious events
    mal_events = []

    # map of graph node ids and host names.
    # The index is node id in graph, and the values is the host name in auth.txt
    host_name = []

    # source and destination nodes in homograph
    u, v = [], []

    # One-hot encoding for edges
    edge_feats = []

    labels = []
    train_mask = []


    with open("/data/LANL/data_including_all_malhosts/test/test_auth.txt", 'r', encoding='utf-8') as file:
        for line in file:
            mal_events.append(line.strip('\n'))
        file.close()

    # raining and testing data
    with open("/data/LANL/data_including_all_malhosts/train_and_test.txt", 'r', encoding='utf-8') as file:
        for line in file:

            line = line.strip('\n')
            fields = line.split(',')
            src_host = fields[3]
            dst_host = fields[4]
            auth_type = fields[5]
            logon_type = fields[6]
            auth_ori = fields[7]
            success_failure = fields[8]

            if src_host not in host_name:
                host_name.append(src_host)
            u.append(host_name.index(src_host))
            if dst_host not in host_name:
                host_name.append(dst_host)
            v.append(host_name.index(dst_host))

            # one-hot encoding for node and edge features
            feat_0 = [0] * len(list_authentication_type)
            feat_1 = [0] * len(list_logon_type)
            feat_2 = [0] * len(list_authentication_orientation)
            feat_3 = [0] * len(list_failure_success)

            feat_0[list_authentication_type.index(auth_type)] = 1
            feat_1[list_logon_type.index(logon_type)] = 1
            feat_2[list_authentication_orientation.index(auth_ori)] = 1
            feat_3[list_failure_success.index(success_failure)] = 1
            feat = feat_0 + feat_1 + feat_2 + feat_3
            edge_feats.append(feat)

            # edge label and train mask
            if line in mal_events:
                labels.append([1])
                train_mask.append([1])
            else:
                labels.append([0])
                train_mask.append([0])
        file.close()

    # save the map of graph node-ids and host names.
    # with open('/data/LANL/data_including_all_malhosts/train/map_of_NodeId_and_HostName.txt', 'a+', encoding='utf-8') as f:
    #     for i in range(0, len(host_name)):
    #         line = str(i) + ':' +host_name[i]
    #         f.writelines(line)

    # graph construction
    u_ids, v_ids = th.tensor(u), th.tensor(v)
    g = dgl.graph((u_ids, v_ids), idtype=th.int32)
    edge_feats = th.tensor(edge_feats)
    labels = th.tensor(labels)
    train_mask = th.tensor(train_mask)

    # To eliminate 0-in-degree nodes
    # bg = dgl.add_reverse_edges(g, copy_ndata=True, copy_edata=True)
    # return bg
    return g, edge_feats, labels, train_mask


if __name__ == "__main__":
    start_time = time()
    list_user_domian = ['U66@DOM1']
    list_authentication_type = ['?', 'NTLM', 'Kerberos', 'Negotiate', 'MICROSOFT_AUTHENTICATION_PACKAGE_V1_0', 'N']
    list_logon_type = ['?', 'Network', 'Batch', 'NetworkCleartext', 'Unlock', 'RemoteInteractive', 'Interactive', 'Service','CachedInteractive', 'NewCredentials']
    list_authentication_orientation = ['TGS', 'TGT', 'LogOn', 'LogOff', 'AuthMap', 'ScreenLock', 'ScreenUnlock']
    list_failure_success = ['Fail', 'Success']

    graph, edge_feats, labels, train_mask = graph_construction()
    print(graph) 
    print(edge_feats.shape)
    print(labels.shape)
    print(train_mask.shape)
    # dgl.save_graphs('/data/LANL/data_including_all_malhosts/train/auth.bin', [graph])
    # print("[+] graph of auth has been saved!")
    end_time = time()
    print("Time used: " + str(end_time - start_time))