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


# Порівняння з точним значенням
x_true = A * np.sin(n * x + phi) + n
absolute_errors, relative_errors = [], []

approx_values = [arithmetic_mean, harmonic_mean, geometric_mean]
for approx_value in approx_values:
    absolute_error, relative_error = compare_with_true(approx_value, x_true)
    absolute_errors.append(absolute_error)
    relative_errors.append(relative_error)

# Виведення результатів
print("Середнє арифметичне:", arithmetic_mean)
print("Максимальна абсолютна похибка:", np.nanmax(absolute_errors[0]))
print("Мінімальна абсолютна похибка:", np.nanmin(absolute_errors[0]))
print("Максимальна відносна похибка:", np.nanmax(relative_errors[0]))
print("Мінімальна відносна похибка:", np.nanmin(relative_errors[0]))

print("\nСереднє гармонійне:", harmonic_mean)
print("Максимальна абсолютна похибка:", np.nanmax(absolute_errors[1]))
print("Мінімальна абсолютна похибка:", np.nanmin(absolute_errors[1]))
print("Максимальна відносна похибка:", np.nanmax(relative_errors[1]))
print("Мінімальна відносна похибка:", np.nanmin(relative_errors[1]))

print("\nСереднє геометричне:", geometric_mean)
print("Максимальна абсолютна похибка:", np.nanmax(absolute_errors[2]))
print("Мінімальна абсолютна похибка:", np.nanmin(absolute_errors[2]))
print("Максимальна відносна похибка:", np.nanmax(relative_errors[2]))
print("Мінімальна відносна похибка:", np.nanmin(relative_errors[2]))

# Візуалізація результатів
plot_data(x, data, true_data)
