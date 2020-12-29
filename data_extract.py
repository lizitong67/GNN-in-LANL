def list_abnormal_hosts():
    hosts = []
    with open('/data/LANL/uncompressed/redteam.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.split(',')
            src_host = fields[2]
            dst_host = fields[3]
            hosts.append(src_host.strip('\n'))
            hosts.append(dst_host.strip('\n'))
    hosts_without_duplication = list(set(hosts))
    return hosts_without_duplication

# time,source computer,computer resolved
def extract_dns():
    with open('/data/LANL/uncompressed/dns.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.split(',')
            src_host = fields[1]
            dst_host = fields[2]
            if src_host in abnormal_hosts or dst_host in abnormal_hosts:
                with open('/data/LANL/data_including_all_malhosts/dns.txt', 'a+', encoding='utf-8') as f:
                    f.write(line)
    print("[+] All dns data including malicious hosts are extracted !")

# time,duration,source computer,source port,destination computer,destination port,protocol,packet count,byte count
def extract_flows():
    with open('/data/LANL/uncompressed/flows.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.split(',')
            src_host = fields[2]
            dst_host = fields[4]
            if src_host in abnormal_hosts or dst_host in abnormal_hosts:
                with open('/data/LANL/data_including_all_malhosts/flows.txt', 'a+', encoding='utf-8') as f:
                    f.write(line)
    print("[+] All flow data including malicious hosts are extracted !")


# time,source user@domain,destination user@domain,source computer,destination computer,
# authentication type,logon type,authentication orientation,success/failure
def extract_auth():
    with open('/data/LANL/uncompressed/auth.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.split(',')
            src_host = fields[3]
            dst_host = fields[4]
            if src_host in abnormal_hosts or dst_host in abnormal_hosts:
                with open('/data/LANL/data_including_all_malhosts/auth.txt', 'a+', encoding='utf-8') as f:
                    f.write(line)
    print("[+] All auth data including malicious hosts are extracted !")

if __name__ == '__main__':
    abnormal_hosts = list_abnormal_hosts()
    extract_dns()
    extract_flows()
    extract_auth()


