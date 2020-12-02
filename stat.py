# -*- coding: utf-8 -*-

MaxItems = 10000

def generate_data(fname):
    import random
    import json

    # adds 'Gender' and 'Year'
    # calc stats by Gender/Year
    # compare the preference for the item by Gender/Year
    labels = ["No", "Name", "Score", "Gender", "Year", "ETC."]

    datalist = []
    for idx in range(MaxItems):
        item = {}
        for jdx in range(len(labels)):
            if labels[jdx].lower() == "no":
                item["no"] = "%s%d" % (labels[jdx].lower(), idx + 1)
            elif labels[jdx].lower() == "name":
                item["name"] = "%s%d" % (labels[jdx].upper(), idx + 1)
            elif labels[jdx].lower() == "score":
                item["score"] = random.choice([1, 2, 3, 4, 5])
            elif labels[jdx].lower() == "gender":
                item["gender"] = random.choice(["m", "f"])
            elif labels[jdx].lower() == "year":
                item["year"] = random.randint(1970, 2020)
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
        print("no data loaded")
        return

    #print(datalist)

    _stat = {}
    for item in datalist:
        key = "%d-%s" % (item["year"], item["gender"])
        if key not in _stat:
            _stat[key] = {
                "sum":0,
                "cnt":0,
            }

        _stat[key]["sum"] += item["score"]
        _stat[key]["cnt"] += 1

    print(json.dumps(_stat, indent=2))
    open("tmp.json", "w").write(json.dumps(_stat, indent=4))

    #print(_sum)
    #print(_cnt)

    _merge = {}
    for key in _stat:
        #print("key:%d, val:%d" % (key, _sum[key]))
        avg = _stat[key]["sum"] / _stat[key]["cnt"]

        _merge[key] = {
            "year":key,
            "sum":_stat[key]["sum"],
            "cnt":_stat[key]["cnt"],
            "avg":avg
        }

    open("out.json", "w").write(json.dumps(_merge, indent=4))
    #print(_merge)
    #print("sum[%d]:%d, avg:%.2f, var:%.2f, dev:%.2f" % (count, _sum, avg, var, dev))

    print("YEAR\tAVG(SCORE)")
    keys = sorted(_merge.keys(), reverse=True)
    for key in keys:
        print("%s\t%f" % (_merge[key]["year"], _merge[key]["avg"]))

def main():
    flag = 1
    fname = "data.json"

    if flag == 1:
        stat(fname)
    else:
        generate_data(fname)

main()

