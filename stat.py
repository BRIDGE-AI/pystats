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

def calc_avg(text):
    lines = text.split("\n")

    _sum = 0
    for line in lines:
        tabs = line.split("\t")
        _sum += int(tabs[2]) # _sum = _sum + int(..)

    count = len(lines)
    avg = _sum / count
    s = "sum[%d]:%d, avg:%.2f" % (count, _sum, avg)
    print(s)

def calc_var(text):
    import math

    lines = text.split("\n")

    _sum = 0
    _sum2 = 0
    for line in lines:
        tabs = line.split("\t")
        x = int(tabs[2])
        _sum += x
        _sum2 += x ** 2

    count = len(lines)
    avg = _sum / count

    var = _sum2 / len(lines) - avg ** 2
    print("sum[%d]:%d, avg:%.2f, var:%.2f, dev:%.2f, dev2:%.2f" % (count, _sum, avg, var, math.sqrt(var), var ** 0.5))

def calc_dev(text):
    pass

def main():
    fname = "data.txt"

    generate_data(fname)

    text = open(fname).read()
    print(text)

    #avg : 3.0
    calc_avg(text)
    calc_var(text)
    #calc_y(text)

main()

