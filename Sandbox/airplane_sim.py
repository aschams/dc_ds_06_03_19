import numpy as np
import random
import time

def airplane_sim2(n_passengers=100):
    x = np.arange(n_passengers)
    x[0] = np.random.randint(n_passengers)
    for p in range(1, n_passengers):
        if p in x[:p]:
#             print(p)
            x[p] = np.random.randint(p+1, n_passengers+1) % n_passengers
    lggas = x[n_passengers - 1].astype(bool).sum()
    return lggas

def airplane_sim3(n_passengers=100):
    x = np.arange(n_passengers)
    x[0] = np.random.randint(n_passengers)
    for p in range(1, n_passengers):
        if p in x[:p]:
            switch_with = random.sample(range(p, n_passengers), 1)[0]
            x[[p, switch_with]] = x[[switch_with, p]]
    lggas = x[n_passengers - 1].astype(bool).sum()
    return lggas

def airplane_sim4(n_passengers=100, n_planes=100):
    # Once someone is assigned 0, every subsequent person will then take their own seat.
    x = np.arange(n_passengers)
    y = np.repeat(x, n_planes, axis = 0)
    y = y.reshape((n_passengers, n_planes))
    y[0,:] = np.random.randint(n_passengers, size=n_planes)
    for p in range(1, n_passengers):
        q = np.where(y[:p] == p)[1]
#         print(y)
#         print(np.where(y[:p] == p))
#         print(q)
        y[p,q] = np.random.randint(p+1, n_passengers+1, size=len(q)) % n_passengers
    lggas = y[n_passengers - 1,:].astype(bool).sum()
    return lggas / n_planes

now = time.time()
airplane_sim4(100,1000)
print(time.time() - now)