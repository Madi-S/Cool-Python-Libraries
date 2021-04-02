'''
This example demonstrates random bar progression
'''
from time import sleep
from tqdm import tqdm
from random import randint



max_iter = 100000
total = 0
bar = tqdm(desc='Random progress bar progression', total=max_iter)


while total < max_iter:
    progress = randint(1, 100)
    bar.update(progress)
    total += progress
    sleep(.01)