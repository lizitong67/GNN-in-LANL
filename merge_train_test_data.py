from time import *
def merge(list_1, list_2):
    list_3 = []
    while len(list_1) > 0 and len(list_2) > 0:
        time_stamp_1 = int(list_1[0].split(',')[0])
        time_stamp_2 = int(list_2[0].split(',')[0])

        if time_stamp_1 < time_stamp_2:
            list_3.append(list_1[0])
            del list_1[0]
        else:
            list_3.append(list_2[0])
            del list_2[0]
    list_3.extend(list_1)
    list_3.extend(list_2)
    return list_3


if __name__ == '__main__':
    start_time = time()
    train_data = []
    test_data = []
    with open('/data/LANL/data_including_all_malhosts/train/train_auth.txt', 'r', encoding='utf-8') as file:
        for line in file:
            train_data.append(line)
        file.close()
    with open('/data/LANL/data_including_all_malhosts/test/test_auth.txt', 'r', encoding='utf-8') as file:
        for line in file:
            test_data.append(line)
        file.close()
    rst = merge(train_data, test_data)
    with open('/data/LANL/data_including_all_malhosts/data_with_mask.txt', 'a+', encoding='utf-8') as file:
        for item in rst:
            file.writelines(item)
        file.close()
    end_time = time()
    print("Time used: " + str(end_time - start_time))


