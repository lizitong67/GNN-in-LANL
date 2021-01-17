import torch as th
import dgl
import torch.nn as nn
import dgl.function as fn

#
#
# file_name = "/data/LANL/data_including_all_malhosts/test/auth.txt"
# with open(file_name, 'r', encoding='utf-8') as file:
#     dict_user_domian = {}
#
#     for line in file:
#         line = line.strip('\n')
#         fields = line.split(',')
#         src_user_domain = fields[1]
#         dst_user_domain = fields[2]
#
#         if src_user_domain not in dict_user_domian.keys():
#             dict_user_domian[src_user_domain] = 1
#         else:
#             dict_user_domian[src_user_domain] += 1
#
#         if dst_user_domain not in dict_user_domian.keys():
#             dict_user_domian[dst_user_domain] = 1
#         else:
#             dict_user_domian[dst_user_domain] += 1
#
# print(dict_user_domian)
# '''
# {'U620@DOM1': 2, 'U748@DOM1': 52, 'U6115@DOM1': 2, 'U636@DOM1': 4, 'U1723@DOM1': 38, 'U737@DOM1': 60,
#  'U825@DOM1': 4, 'U1653@DOM1': 30, 'U293@DOM1': 62, 'U8946@DOM1': 22, 'U10379@C3521': 4, 'U8601@DOM1': 26,
#  'U212@DOM1': 8, 'U4978@DOM1': 10, 'U3905@DOM1': 2, 'U995@DOM1': 8, 'U288@DOM1': 2, 'U2837@DOM1': 30, 'U349@DOM1': 8,
#  'U250@DOM1': 2, 'U1600@DOM1': 8, 'U4353@DOM1': 10, 'U4856@DOM1': 2, 'U5087@DOM1': 24, 'U9763@DOM1': 12, 'U795@DOM1': 4,
#  'U9947@DOM1': 30, 'U882@DOM1': 6, 'U8777@C583': 6, 'U1450@DOM1': 22, 'U8777@C1500': 4, 'U8777@C3388': 10, 'U374@DOM1': 6,
#  'U2575@DOM1': 20, 'U3718@DOM1': 4, 'U342@DOM1': 24, 'U6572@DOM1': 4, 'U162@DOM1': 22, 'U314@DOM1': 4, 'U642@DOM1': 4,
#  'U3635@DOM1': 36, 'U1480@DOM1': 24, 'U66@DOM1': 236, 'U1164@DOM1': 2, 'U7394@DOM1': 6, 'U1048@DOM1': 18, 'U5254@DOM1': 6,
#  'U7375@DOM1': 14, 'U4448@DOM1': 28, 'U218@DOM1': 26, 'U4112@DOM1': 6, 'U12@DOM1': 12, 'U13@DOM1': 4, 'U1289@DOM1': 6,
#  'U3277@C2519': 2, 'U1519@DOM1': 2, 'U7761@C2519': 4, 'U7004@C2519': 2, 'U207@DOM1': 4, 'U1145@DOM1': 24, 'U453@DOM1': 4,
#  'U9263@DOM1': 18, 'U20@DOM1': 2, 'U7507@DOM1': 24, 'U415@DOM1': 12, 'U1569@DOM1': 4, 'U1581@DOM1': 6, 'U6764@DOM1': 2,
#  'U1789@DOM1': 2, 'U6691@DOM1': 4, 'U78@DOM1': 4, 'U3005@DOM1': 72, 'U1133@DOM1': 10, 'U3486@DOM1': 4, 'U2231@DOM1': 10,
#  'U1592@DOM1': 12, 'U1025@DOM1': 12, 'U737@C10': 2, 'U86@C10': 6, 'U2758@DOM1': 2, 'U9407@DOM1': 2, 'U24@DOM1': 10,
#  'U655@DOM1': 6, 'U86@DOM1': 16, 'U3549@DOM1': 26, 'U8170@DOM1': 8, 'U8168@C19038': 2, 'U1506@DOM1': 8, 'U7594@DOM1': 2,
#  'U114@DOM1': 8, 'U1106@DOM1': 4, 'U3575@DOM1': 2, 'U3206@DOM1': 2, 'U8777@DOM1': 2, 'U227@DOM1': 2, 'U8168@C685': 6,
#  'U679@DOM1': 4, 'U7311@DOM1': 4, 'U524@DOM1': 4, 'U8840@DOM1': 2, 'U1306@DOM1': 2, 'U3764@DOM1': 2, 'U1467@C3597': 2,
#  'U3406@DOM1': 2}
# '''
#

u, v = th.tensor([0, 1, 3, 3]), th.tensor([4, 5, 6, 6])
g = dgl.graph((u, v))
g.edata['feat'] = th.ones(4,2)
print(g.edata['feat'][0])




