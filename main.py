import numpy as np
import matplotlib.pyplot as plt


# Спотворення синусоїди
def generate_sequence(N, A, n, phi, deviation):
    x = np.linspace(0, 2, N)
    y_true = A * np.sin(n * x + phi)
    y = y_true + deviation
    return x, y, y_true


# Обчислення середніх значень
def mean_arithmetic(data):
    return np.mean(data)

def mean_harmonic(data):
    return len(data) / np.sum(1 / data)

def mean_geometric(data):
    data = np.where(data <= 0, np.nan, data)
    return np.nanprod(data) ** (1 / np.sum(~np.isnan(data)))


# Порівняння з точним значенням
def compare_with_true(approximate, exact):
    absolute_error = np.abs(approximate - exact)
    relative_error = absolute_error / np.abs(exact)
    return absolute_error, relative_error


# Відображення результатів
def plot_data(x, y, y_exact):
    plt.plot(x, y, label='Зі спотвореннями', color='yellow')
    plt.plot(x, y_exact, label='Точне значення', color='black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


# Основний блок
n = 20   # номер студента у журналі
N = n*100  # N>=n*100
A = 1   # амплітуда
phi = np.pi / 4  # зсув по фазі
deviation = np.random.uniform(-0.05 * A, 0.05 * A, N)  # відхилення від точного значення

# Генерація даних
x, data, true_data = generate_sequence(N, A, n, phi, deviation)

# Обчислення середніх значень
arithmetic_mean = mean_arithmetic(data)
harmonic_mean = mean_harmonic(data)
geometric_mean = mean_geometric(data)

print(f'Середнє арифметичне: {arithmetic_mean}')
print(f'Середнє гармонійне: {harmonic_mean}')
print(f'Середнє геометричне: {geometric_mean}')

# Порівняння з точним значенням
x_true = A * np.sin(n * x + phi)
abs_error, rel_error = compare_with_true(data, x_true)
print(f'Максимальна абсолютна похибка: {np.max(abs_error)}')
print(f'Мінімальна абсолютна похибка: {np.min(abs_error)}')
print(f'Максимальна відносна похибка: {np.max(rel_error)}')
print(f'Мінімальна відносна похибка: {np.min(rel_error)}')

# Візуалізація результатів
plot_data(x, data, true_data)
