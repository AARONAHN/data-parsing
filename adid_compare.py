import csv

with open('../data/1490_postback.csv', encoding='utf-8') as csvfile:
    postback = csv.reader(csvfile, delimiter=',')

    error_cnt = 0
    head = None
    for i, row in enumerate(postback):
        if i == 0:
            head = row
            continue

        pb_dic = dict(zip(head, row))

        advertising_id = pb_dic.get('advertising_id', '')
        device_id = pb_dic.get('device_id', '')

        if advertising_id == device_id:
            continue
        else:
            print("ERROR in line %d" % i)
            error_cnt += 1
    print("There are %d errors" % error_cnt)



