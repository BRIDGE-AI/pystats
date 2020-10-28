# -*- coding: utf-8 -*-

def generate_data(fname):
    labels = ["#No", "Name", "Score", "ETC."]

    conv = []
    for idx in range(10):
        cols = []
        for jdx in range(len(labels)):
            if jdx != 2:
                col = "%s%d" % (labels[jdx].strip("#").lower(), idx + 1)
            else:
                # str, float, list, dict
                col = str(idx + 1)
            cols.append(col)

        # x = ["a", "b", "c"]
        # " ".join(x) --> "a b c"
        # "\t".join(x) --> "a\tb\tc" --> "a    b   c"
        conv.append("\t".join(cols))

    open(fname, "w").write("\n".join(conv))

    return 0

def main():
    fname = "data.txt"

    generate_data(fname)

    text = open(fname).read()
    print(text)

main()

