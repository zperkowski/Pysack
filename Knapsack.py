import random

# Created by zperkowski on 17/06/2016.


def generator(quantity, weight_range, value_range):
    tab = [[0 for x in range(2)] for y in range(quantity)]
    for j in range(0, quantity):
        tab[j][0] = random.randint(1, weight_range)
        tab[j][1] = random.randint(1, value_range)
    return tab


def greedy(tab, capacity=0):
    for i in range(0, len(tab)):
        tab[i].append(round(tab[i][1] / tab[i][0], 4))
    tab.sort(key=lambda x: x[2], reverse=True)
    used_capacity = 0
    new_tab = []
    while tab != []:
        if used_capacity + tab[0][0] <= capacity:
            used_capacity += tab[0][0]
            new_tab.append(tab[0])
        tab.pop(0)
    return new_tab


def dynamic(tab, capacity=0):
    dynamic_tab = [[0 for x in range(capacity + 1)] for y in range(len(tab) + 1)]
    for j in range(1, len(tab) + 1):
        for i in range(1, capacity + 1):
            if i < tab[j - 1][0]:
                dynamic_tab[j][i] = dynamic_tab[j - 1][i]
            else:
                if dynamic_tab[j - 1][i] >= dynamic_tab[j - 1][i - tab[j - 1][0]] + tab[j - 1][1]:
                    dynamic_tab[j][i] = dynamic_tab[j - 1][i]
                else:
                    dynamic_tab[j][i] = dynamic_tab[j - 1][i - tab[j - 1][0]] + tab[j - 1][1]
    dynamic_result = []
    i = capacity
    j = len(tab)
    while (i != 0) and (j != 0):
        if dynamic_tab[j][i] == dynamic_tab[j - 1][i]:
            j -= 1
        else:
            dynamic_result.append(tab[j - 1])
            i -= tab[j - 1][0]
            j -= 1
    return dynamic_result
