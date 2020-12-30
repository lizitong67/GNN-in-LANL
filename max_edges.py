# get max edge numbers of any 2 pair of nodes
def get_max_edge_numbers(data_type):
    if data_type == 'dns':
        count_edges = {}
        with open('/data/LANL/data_including_all_malhosts/dns.txt', 'r', encoding='utf-8') as file:
            for line in file:
                fields = line.split(',')
                src_host = fields[1].strip('\n')
                dst_host = fields[2].strip('\n')
                key = src_host + ',' + dst_host
                if key not in count_edges.keys():
                    count_edges[key] = 1
                else:
                    count_edges[key] += 1
        print("[+] Edge counting for dns is done!")
        return count_edges

    if data_type == 'flows':
        count_edges = {}
        with open('/data/LANL/data_including_all_malhosts/flows.txt', 'r', encoding='utf-8') as file:
            for line in file:
                fields = line.split(',')
                src_host = fields[2].strip('\n')
                dst_host = fields[4].strip('\n')
                key = src_host + ',' + dst_host
                if key not in count_edges.keys():
                    count_edges[key] = 1
                else:
                    count_edges[key] += 1
        print("[+] Edge counting for flows is done!")
        return count_edges

    if data_type == 'auth':
        count_edges = {}
        with open('/data/LANL/data_including_all_malhosts/auth.txt', 'r', encoding='utf-8') as file:
            for line in file:
                fields = line.split(',')
                src_host = fields[3].strip('\n')
                dst_host = fields[4].strip('\n')
                key = src_host + ',' + dst_host
                if key not in count_edges.keys():
                    count_edges[key] = 1
                else:
                    count_edges[key] += 1
        print("[+] Edge counting for auth is done!")
        return count_edges

if __name__ == '__main__':
    for data_type in ['dns', 'flows', 'auth']:
        count_edges = get_max_edge_numbers(data_type)
        with open('/data/LANL/data_including_all_malhosts/count_'+data_type+'_edges.txt', 'a+', encoding='utf-8') as file:
            for item in count_edges.items():
                file.write(str(item))


