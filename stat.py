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

    print("sum[%d]:%d, avg:%.2f" % (count, _sum, _sum / count))

def main():
    fname = "data.txt"

    generate_data(fname)

    text = open(fname).read()
    print(text)

    #avg : 3.0
    calc_avg(text)

main()

