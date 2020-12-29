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
                    "sum2":0,
                },
                "f":{
                    "sum":0,
                    "cnt":0,
                    "sum2":0,
                }
            }

        gen = item["gender"]
        _stat[year][gen]["sum"] += item["score"]
        _stat[year][gen]["cnt"] += 1
        _stat[year][gen]["sum2"] += item["score"] ** 2

    return _stat

def __merge(_stat):
    _merge = {}

    for key in _stat:
        #print("key:%d, val:%d" % (key, _sum[key]))
        avg_m = _stat[key]["m"]["sum"] / _stat[key]["m"]["cnt"]
        avg_f = _stat[key]["f"]["sum"] / _stat[key]["f"]["cnt"]

        dev_m = _stat[key]["m"]["sum2"] / _stat[key]["m"]["cnt"] - avg_m ** 2
        dev_f = _stat[key]["f"]["sum2"] / _stat[key]["f"]["cnt"] - avg_f ** 2

        _merge[key] = {
            "m":{
                "year":key,
                "sum":_stat[key]["m"]["sum"],
                "cnt":_stat[key]["m"]["cnt"],
                "avg":avg_m,
                "var":dev_m,
            },
            "f":{
                "year":key,
                "sum":_stat[key]["f"]["sum"],
                "cnt":_stat[key]["f"]["cnt"],
                "avg":avg_f,
                "var":dev_f,
            }
        }

    return _merge

def plot(data):
    import matplotlib.pyplot as plt

    x = sorted([item["m"]["year"] for year, item in data.items()])

    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    ax1.set_ylim([0.8, 5.2])
    ax2.set_ylim([0.8, 5.2])

    y = [data[key]["m"]["avg"] for key in sorted(x)]
    yerr = [data[key]["m"]["var"] ** 0.5 for key in sorted(x)]

    line1, = ax1.plot(x, y, c=(0.5, 0.5, 0.8), label='MALE')
    ax1.errorbar(x, y, yerr=yerr, label='MALE')
    #ax1.fill_between(x, [y + err for (y, err) in zip(y, yerr)], [y - err for (y, err) in zip(y, yerr)], color='gray', alpha=0.2)
    #line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break

    # Using plot(..., dashes=...) to set the dashing when creating a line
    y = [data[key]["f"]["avg"] for key in sorted(data.keys())]
    yerr = [data[key]["f"]["var"] ** 0.5 for key in sorted(x)]
    #line2, = ax.plot(x, y, label='FEMALE')
    ax2.errorbar(x, y, c=(0.8, 0.5, 0.5), yerr=yerr, label='FEMALE')

    ax1.legend()
    ax2.legend()
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

