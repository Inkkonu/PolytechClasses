import re
import matplotlib.pyplot as plt


def analyse(filename) -> dict:
    d = dict()
    with open(filename, "r") as infile:
        data = infile.read()

    data = data.lower()
    total = 0

    for l in data:
        if re.match("[a-z]", l):
            total += 1
            if l not in d.keys():
                d[l] = 1
            else:
                d[l] += 1
    for k in d.keys():
        d[k] = d[k] / total * 100

    return d


def plot_dict(d: dict, n: str) -> None:
    keys = sorted(list(d.keys()))
    values = []
    for k in keys:
        values.append(d[k])
    plt.bar(keys, values)
    plt.title(n)
    plt.show()


def get_greatest_gaps(d1: dict, d2: dict) -> list:
    d3 = dict()
    for l in list(map(chr, range(97, 123))):
        if l not in d1.keys():
            d1[l] = 0
        if l not in d2.keys():
            d2[l] = 0
    for k in d1.keys():
        d3[k] = abs(d1[k] - d2[k])
    l = []
    for k in list(map(chr, range(97, 123))):
        keymax = max(zip(d3.values(), d3.keys()))[1]
        l.append((keymax, d3[keymax]))
        del d3[keymax]
    return l[:10]


if __name__ == "__main__":
    d_prevert = analyse("data_inventaire_prevert.txt")
    d_force = analyse("la_force.txt")
    plot_dict(d_prevert, "Prevert")
    plot_dict(d_force, "La force")
    l = get_greatest_gaps(d_prevert, d_force)
    for i in range(10):
        print(f"{i+1}. {l[i][0]} : {l[i][1]:.02f}%")
