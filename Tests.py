import Knapsack
import time
import copy

# Created by zperkowski on 17/06/2016.


def compare_algorithms(input_tab, capacity):

    start_time = time.time()
    greedy_result = Knapsack.greedy(copy.deepcopy(input_tab), capacity)
    elapsed_time = time.time() - start_time
    greedy_time = str(round(elapsed_time, 4)) + " "

    start_time = time.time()
    dynamic_result = Knapsack.dynamic(copy.deepcopy(input_tab), capacity)
    elapsed_time = time.time() - start_time
    dynamic_time = str(round(elapsed_time, 4)) + " "

    result = str(measure_tolerance(greedy_result, dynamic_result))

    return result, greedy_result, greedy_time, dynamic_result, dynamic_time


def measure_tolerance(tab_greedy_result, tab_dynamic_result):
    greedy_value = 0
    dynamic_value = 0
    for i in range(0, len(tab_greedy_result)):
        greedy_value += tab_greedy_result[i][1]
    for i in range(0, len(tab_dynamic_result)):
        dynamic_value += tab_dynamic_result[i][1]
    tolerance = greedy_value / dynamic_value
    return tolerance
