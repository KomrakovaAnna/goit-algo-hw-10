import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Генерування випадкових точок всередині прямокутника
n = 100000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)  # Верхня межа висоти - значення функції в точці b

# Підрахунок кількості точок, які потрапили під криву
points_under_curve = sum(y_random <= f(x_random))

# Визначення площі прямокутника
rectangle_area = (b - a) * f(b)

# Оцінка площі під кривою (інтеграла) за допомогою методу Монте-Карло
integral_estimate = rectangle_area * (points_under_curve / n)

print("Оцінка інтеграла методом Монте-Карло:", integral_estimate)

# Обчислення інтеграла за допомогою quad
result, error = spi.quad(f, a, b)

print("Точне значення інтеграла:", result)

# Обчислення абсолютної похибки
absolute_error = abs(integral_estimate - result)
print("Абсолютна похибка:", absolute_error)


# Візуалізація результатів

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
