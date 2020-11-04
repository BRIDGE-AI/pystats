# -*- coding: utf-8 -*-

def generate_data(fname):
    import random

    labels = ["No", "Name", "Score", "ETC."]

    rows = []
    for idx in range(10):
        cols = []
        for jdx in range(len(labels)):
            if jdx == 0:
                col = "%s%d" % (labels[jdx].lower(), idx + 1)
            elif jdx == 1:
                col = "%s%d" % (labels[jdx].upper(), idx + 1)
            elif jdx == 2:
                col = str(random.choice([1, 2, 3, 4, 5]))
            else:
                col = "_"
            cols.append(col)

        rows.append("\t".join(cols))

    open(fname, "w").write("\n".join(rows))

    return 0

def main():
    import math

    fname = "data.txt"

    generate_data(fname)

    text = open(fname).read()
    print(text)

    nums = [int(line.split("\t")[2]) for line in text.split("\n")]
    _sum = sum(nums)
    count = len(nums)
    avg = _sum / count

    _sum2 = sum([num ** 2 for num in nums])
    var = _sum2 / count - avg ** 2
    dev = math.sqrt(var)

    #var, dev = calc_var(count, avg, nums)

    print("sum[%d]:%d, avg:%.2f, var:%.2f, dev:%.2f" % (count, _sum, avg, var, dev))


main()

