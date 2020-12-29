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
    return count_edges



if __name__ == '__main__':
    count_edges = get_max_edge_numbers('dns')
    print(count_edges)
