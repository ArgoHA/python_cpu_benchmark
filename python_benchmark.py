'''
This is a python benchmark which fully utilizes needed number of cores.

Usage:
python3 python_benchmark.py

Args:
--cores - how many cores to use. All by default, can be specified any number of existing cores
--iters - how many iterations to run. 1000 by default, nnumber will be devided to CPU core count
'''

import time
import argparse
import math
from tqdm import tqdm

import multiprocessing as mp


def get_cores(cores):
    if cores == 'all' or int(cores) > mp.cpu_count():
        cores = mp.cpu_count()
    else:
        cores = int(cores)

    return cores


def task(_):
   99999**99999


def start_task(cores, iters):
    pool = mp.Pool(processes=cores)
    iters = range(iters)

    for _ in tqdm(pool.imap_unordered(task, iters), total=len(iters)):
        pass


def parse_opt():
    parser = argparse.ArgumentParser()

    parser.add_argument('--cores', type=str, default='all', help='how many cores to use')
    parser.add_argument('--iters', type=int, default=1000, help='how many iterations to run')

    opt = parser.parse_args()
    return opt


def main(cores, iters):
    cores = get_cores(cores)

    print(f'Cores to use: {cores}')
    print(f'Iterations per core: {math.ceil(iters / cores)}')

    start_timer = time.perf_counter()
    start_task(cores, iters)
    total_time = round(time.perf_counter() - start_timer, 2)

    print(f'Time: {total_time} s')


if __name__ == '__main__':
    opt = parse_opt()
    main(**vars(opt))
