import time
from multiprocessing import Pool

data = [1, 2, 3]

def f(x):
    time.sleep(2)
    print(x*x)

p = Pool(8)
p.map(f, data)
p.close()
p.join()
