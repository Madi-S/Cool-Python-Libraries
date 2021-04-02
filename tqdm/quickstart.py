'''
This example demonstrates tqdm basic usage
'''
from tqdm import tqdm
from time import sleep

a = 0

for i in tqdm(range(100)):
    a += i
    sleep(0.1)

print(a)


# So tqdm takes any iterable as an argument