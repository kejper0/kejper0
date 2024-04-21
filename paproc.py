import matplotlib.pyplot as plt
import numpy as np

funkcje = [
    (lambda x, y: (0.0, 0.16 * y), 0.01),
    (lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6), 0.85),
    (lambda x, y: (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6), 0.07),
    (lambda x, y: (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44), 0.07)
]
x, y = 0.0, 0.0
max_punkty = 100000
punkty = []

for _ in range(max_punkty):
    rand = np.random.rand()
    szansa = 0.0
    chosen_func = None
    for func, prob in funkcje:
        szansa += prob
        if rand < szansa:
            chosen_func = func
            break
    x, y = chosen_func(x, y)
    
    punkty.append((x, y))
plt.figure(figsize=(8, 8))
plt.scatter([p[0] for p in punkty], [p[1] for p in punkty], s=1, color='green')
plt.title('Paproć Barnsleya')
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.show()
