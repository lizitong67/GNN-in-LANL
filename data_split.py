def list_abnormal_hosts():
    hosts = []
    with open('/data/LANL/data_including_all_malhosts/redteam.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        fields = lines[0].strip('\n').split(',')
        print(fields)

# time,source computer,computer resolved
def split_dns():
    with open('/data/LANL/rawdata/dns.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.split(',')
            time = fields[0].strip('\n')
            src_host = fields[1].strip('\n')
            dst_host = fields[2].strip('\n')

            save_to_train = 0
            for redteam_line in red_team:
                if src_host == redteam_line[2] or dst_host in redteam_line[3]:
                    save_to_train = 1
                if time == redteam_line[0] and src_host == redteam_line[2] and dst_host == redteam_line[3]:
                    with open('/data/LANL/data_including_all_malhosts/test/dns.txt', 'a+', encoding='utf-8') as f:
                        f.write(line)
                        f.close()
                        break
            if save_to_train:
                with open('/data/LANL/data_including_all_malhosts/train/dns.txt', 'a+', encoding='utf-8') as f:
                    f.write(line)
                    f.close()
        file.close()
    print("[+] All dns data including malicious hosts are split !")


# time,duration,source computer,source port,destination computer,destination port,protocol,packet count,byte count
def split_flows():
    with open('/data/LANL/rawdata/flows.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.split(',')
            time = fields[0].strip('\n')
            src_host = fields[2].strip('\n')
            dst_host = fields[4].strip('\n')

            save_to_train = 0
            for redteam_line in red_team:
                if src_host == redteam_line[2] or dst_host in redteam_line[3]:
                    save_to_train = 1
                if time == redteam_line[0] and src_host == redteam_line[2] and dst_host == redteam_line[3]:
                    with open('/data/LANL/data_including_all_malhosts/test/flows.txt', 'a+', encoding='utf-8') as f:
                        f.write(line)
                        f.close()
                        break
            if save_to_train:
                with open('/data/LANL/data_including_all_malhosts/train/flows.txt', 'a+', encoding='utf-8') as f:
                    f.write(line)
                    f.close()
        file.close()
    print("[+] All flows data including malicious hosts are split !")


# time,source user@domain,destination user@domain,source computer,destination computer,
# authentication type,logon type,authentication orientation,success/failure
def split_auth():
    for i in range(0, 11):
        file_name = 'auth_00'+str(i).zfill(2)
        with open('/data/LANL/rawdata/'+file_name, 'r', encoding='utf-8') as file:
            for line in file:
                fields = line.split(',')
                time = fields[0].strip('\n')
                src_user_domain = fields[1].strip('\n')
                src_host = fields[3].strip('\n')
                dst_host = fields[4].strip('\n')

                save_to_train = 0
                for redteam_line in red_team:
                    if (src_host == redteam_line[2] or dst_host == redteam_line[3]) and src_user_domain == redteam_line[1]:
                        save_to_train = 1
                    if time == redteam_line[0] and src_user_domain == redteam_line[1] and \
                            src_host == redteam_line[2] and dst_host == redteam_line[3]:
                        with open('/data/LANL/data_including_all_malhosts/test/auth.txt', 'a+', encoding='utf-8') as f:
                            f.write(line)
                            f.close()
                            break
                if save_to_train:
                    with open('/data/LANL/data_including_all_malhosts/train/auth.txt', 'a+', encoding='utf-8') as f:
                        f.write(line)
                        f.close()
            file.close()
        print("[+] All auth data file " + str(i).zfill(2) + " including malicious hosts are split !")


if __name__ == '__main__':
    red_team = []
    with open('/data/LANL/data_including_all_malhosts/redteam.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        fields = line.strip('\n').split(',')
        red_team.append(fields)
    print(red_team)

    split_dns()
    # split_flows()
    # split_auth()


