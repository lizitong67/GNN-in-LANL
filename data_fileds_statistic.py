"""
Statistics the data field to set feature space
Author:	Alston
Date:	2021.1.9
"""

file_name = "/data/LANL/data_including_all_malhosts/train/auth.txt"
with open(file_name, 'r', encoding='utf-8') as file:
    list_user_domian = []
    list_authentication_type = []
    list_logon_type = []
    list_authentication_orientation = []

    for line in file:
        line = line.strip('\n')
        fields = line.split(',')
        src_user_domain = fields[1]
        dst_user_domain = fields[2]
        auth_type = fields[5]
        logon_type = fields[6]
        auth_ori = fields[7]

        # U66@DOM1 largest malicious items with 236
        if (src_user_domain == 'U66@DOM1' ) and (src_user_domain not in list_user_domian):
            list_user_domian.append(src_user_domain)
        if (dst_user_domain == 'U66@DOM1' ) and (dst_user_domain not in list_user_domian):
            list_user_domian.append(dst_user_domain)
        if auth_type not in list_authentication_type:
            list_authentication_type.append(auth_type)
        if logon_type not in list_logon_type:
            list_logon_type.append(logon_type)
        if auth_ori not in list_authentication_orientation:
            list_authentication_orientation.append(auth_ori)

    file.close()

print(list_user_domian)
print(list_authentication_type)
print(list_logon_type)
print(list_authentication_orientation)





