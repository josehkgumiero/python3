from time import perf_counter

from math import sqrt

start = perf_counter()

test_repeats = 10_000_000

for _ in range(test_repeats):
    math.sqrt(2)

end = perf_counter()

elapsed_direct_symbol = end - start

print(f'Elapsed: {elapsed_direct_symbol}')