from pulp import *

# Створюємо змінні для кількості "Лимонаду" та "Фруктового соку"
lemonade = LpVariable("Lemonade_units", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Fruit_juice_units", lowBound=0, cat='Integer')

# Створюємо задачу максимізації
problem = LpProblem("MaximizeProduction", LpMaximize)

# Додаємо обмеження на використання ресурсів
problem += 2 * lemonade + fruit_juice <= 100  # вода
problem += 1 * lemonade <= 50  # цукор
problem += 1 * lemonade <= 30  # лимонний сік
problem += 2 * fruit_juice <= 40  # фруктове пюре

# Додаємо функцію мети для максимізації кількості продуктів
problem += lemonade + fruit_juice

# Розв'язуємо задачу
problem.solve()

print("Optimal production:")
print("Lemonade units:", value(lemonade))
print("Fruit juice units:", value(fruit_juice))
