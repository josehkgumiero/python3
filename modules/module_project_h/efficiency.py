def my_func(a):
    import math
    return mat.sqrt(a)

from time import perf_counter

from collections import namedtuple

Timings = namedtuple('Timings', 'timing_1 timing_2, abs_diff rel_diff_perc')

def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1)/timing1 * 100

    timings = Timings(
        round(timing1, 1),
        round(timing2, 1),
        round(timing2 - timing1, 1),
        round(rel_diff, 2)
    )

    return print(timings)

compare_timings(1, 2)


##############################################

test_repeats = 10_000_000

##############################################

import math
start = perf_counter()

for _ in range(test_repeats):
    math.sqrt(2)

end = perf_counter()

elapsed_fully_qualified = end - start
print(f'Elapsed: {elapsed_fully_qualified}')

##############################################

from math import sqrt

start = perf_counter()

for _ in range(test_repeats):
    math.sqrt(2)

end = perf_counter()

elapsed_direct_symbol = end - start

print(f'Elapsed: {elapsed_direct_symbol}')

##############################################

compare_timings(elapsed_fully_qualified, elapsed_direct_symbol)

##############################################

import math

def func():
    math.sqrt(2)

start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()

elapsed_function_wrapper = end - start

print(f'Elapsed: {elapsed_function_wrapper}')

##############################################

from math import sqrt

def func():
    sqrt(2)

start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()

elapsed_function_wrapper_directed_symbol = end - start

print(f'Elapsed: {elapsed_function_wrapper_directed_symbol}')

##############################################

def func():
    import math
    math.sqrt(2)

start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()

elapsed_nested_fully_qualified = end - start

print(f'Elapsed: {elapsed_nested_fully_qualified}')

##############################################

compare_timings(elapsed_fully_qualified, elapsed_nested_fully_qualified)