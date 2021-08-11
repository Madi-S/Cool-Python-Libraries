'''
This example demonstrates trange usage (useful in nested loops)
'''
from time import sleep
from tqdm import trange


for i in trange(10, desc='Main Task'):
    for j in trange(100, desc=f'Tiny Task #{i}', total=100):
        sleep(.01)
