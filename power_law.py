import numpy as np
import matplotlib.pyplot as plt

pc = 10
pm = 5
h = 1

def powerlaw(z, n, pc, pm, h):
    return (pc-pm)*(0.5+z/h)**n + pm

z_values = np.linspace(-h/2, h/2, 500)

n_values = np.linspace(10, 0.1, 100)

plt.figure(figsize=(10, 6))

for n in n_values:
    p_values = powerlaw(z_values, n, pc, pm, h)
    plt.plot(z_values, p_values, label=f'n={n}')

plt.title('Power Law Distribution in FGM')
plt.xlabel('z')
plt.ylabel('p(z)')
plt.legend()
plt.grid(True)
plt.show()