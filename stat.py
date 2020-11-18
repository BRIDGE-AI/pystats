# -*- coding: utf-8 -*-

MaxItems = 10000

def generate_data(fname):
    import random
    import json

    # adds 'Gender' and 'Year'
    # calc stats by Gender/Year
    # compare the preference for the item by Gender/Year
    labels = ["No", "Name", "Score", "ETC."]

    datalist = []
    for idx in range(MaxItems):
        item = {}
        for jdx in range(len(labels)):
            if jdx == 0:
                item["no"] = "%s%d" % (labels[jdx].lower(), idx + 1)
            elif jdx == 1:
                item["name"] = "%s%d" % (labels[jdx].upper(), idx + 1)
            elif jdx == 2:
                item["score"] = random.choice([1, 2, 3, 4, 5])
            else:
                item["etc"] = ""

        datalist.append(item)

    jstr = json.dumps(datalist, indent=2)
    open(fname, "w").write(jstr)

    return 0

def stat(fname):
    import math
    import json

    text = open(fname).read()

    datalist = json.loads(text)

    if not datalist:
        return

    #print(datalist)

    nums = [item["score"] for item in datalist]
    _sum = sum(nums)
    count = len(nums)
    avg = _sum / count

    _sum2 = sum([num ** 2 for num in nums])
    var = _sum2 / count - avg ** 2
    dev = math.sqrt(var)

    #var, dev = calc_var(count, avg, nums)

    print("sum[%d]:%d, avg:%.2f, var:%.2f, dev:%.2f" % (count, _sum, avg, var, dev))


def main():
    flag = 2
    fname = "data.json"

    if flag == 1:
        stat(fname)
    else:
        generate_data(fname)

main()

