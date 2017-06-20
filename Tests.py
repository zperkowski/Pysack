import Knapsack
import time

# Created by zperkowski on 17/06/2016.


def compare_algorithms(input_tab, capacity):
    result = str(capacity) + " " + str(len(input_tab)) + " "

    start_time = time.time()
    greedy_result = Knapsack.greedy(input_tab[:], capacity)
    elapsed_time = time.time() - start_time
    result += str(round(elapsed_time, 4)) + " "

    start_time = time.time()
    dynamic_result = Knapsack.dynamic(input_tab[:], capacity)
    elapsed_time = time.time() - start_time
    result += str(round(elapsed_time, 4)) + " "

    result += str(measure_tolerance(greedy_result, dynamic_result))

    return result


def measure_tolerance(tab_greedy_result, tab_dynamic_result):
    greedy_value = 0
    dynamic_value = 0
    for i in range(0, len(tab_greedy_result)):
        greedy_value += tab_greedy_result[i][1]
    for i in range(0, len(tab_dynamic_result)):
        dynamic_value += tab_dynamic_result[i][1]
    tolerance = greedy_value / dynamic_value
    return tolerance
