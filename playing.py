import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Параметри
D = 100        # Початкова доза (мг)
k_a = 1.0      # Швидкість всмоктування (1/год)
k_e = 0.3      # Швидкість виведення (1/год)

# Система рівнянь
def model(t, y):
    A, C = y
    dA_dt = -k_a * A
    dC_dt = k_a * A - k_e * C
    return [dA_dt, dC_dt]

# Початкові умови
y0 = [D, 0]

# Час (від 0 до 24 год)
t_span = (0, 24)
t_eval = np.linspace(*t_span, 500)

# Чисельне розв'язання
sol = solve_ivp(model, t_span, y0, t_eval=t_eval)

# Побудова графіка
plt.plot(sol.t, sol.y[0], label='Ліки в шлунку (A)')
plt.plot(sol.t, sol.y[1], label='Ліки в крові (C)')
plt.xlabel('Час (год)')
plt.ylabel('Кількість ліків (мг)')
plt.title('Модель перорального введення ліків')
plt.legend()
plt.grid(True)
plt.show()
