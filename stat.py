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

def calc_stat(datalist):
    _stat = {}
    for item in datalist:
        year = item["year"]

        if year not in _stat:
            _stat[year] = {
                "m":{
                    "sum":0,
                    "cnt":0,
                },
                "f":{
                    "sum":0,
                    "cnt":0,
                }
            }

        gen = item["gender"]
        _stat[year][gen]["sum"] += item["score"]
        _stat[year][gen]["cnt"] += 1

    return _stat

def __merge(_stat):
    _merge = {}

    for key in _stat:
        #print("key:%d, val:%d" % (key, _sum[key]))
        avg_m = _stat[key]["m"]["sum"] / _stat[key]["m"]["cnt"]
        avg_f = _stat[key]["f"]["sum"] / _stat[key]["f"]["cnt"]

        _merge[key] = {
            "m":{
                "year":key,
                "sum":_stat[key]["m"]["sum"],
                "cnt":_stat[key]["m"]["cnt"],
                "avg":avg_m
            },
            "f":{
                "year":key,
                "sum":_stat[key]["f"]["sum"],
                "cnt":_stat[key]["f"]["cnt"],
                "avg":avg_f
            }
        }

    return _merge

def plot(data):
    import matplotlib.pyplot as plt

    x = sorted([item["m"]["year"] for year, item in data.items()])

    fig, ax = plt.subplots()

    ax.set_ylim([0.8, 5.2])

    # Using set_dashes() to modify dashing of an existing line
    y = [data[key]["m"]["avg"] for key in sorted(x)]
    line1, = ax.plot(x, y, label='MALE')
    #line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break

    # Using plot(..., dashes=...) to set the dashing when creating a line
    y = [data[key]["f"]["avg"] for key in sorted(data.keys())]
    line2, = ax.plot(x, y, label='FEMALE')

    ax.legend()
    plt.show()

def stat(fname):
    import math
    import json

    text = open(fname).read()
    datalist = json.loads(text)

    if not datalist:
        print("no data loaded")
        return

    _stat = calc_stat(datalist)

    _merge = __merge(_stat)

    open("out.json", "w").write(json.dumps(_merge, indent=4))

    """
    print("YEAR\tM-AVG(SCORE)\tF-AVG(SCORE)")
    keys = sorted(_merge.keys(), reverse=True)
    for key in keys:
        print("%d\t%f\t%f" % (_merge[key]["f"]["year"], _merge[key]["m"]["avg"], _merge[key]["f"]["avg"]))
    """

    plot(_merge)

def main():
    flag = 1
    fname = "data.json"

    if flag == 1:
        stat(fname)
    else:
        generate_data(fname)

main()

