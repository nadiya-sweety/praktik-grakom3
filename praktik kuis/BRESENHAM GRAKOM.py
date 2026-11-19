import matplotlib.pyplot as plt
import numpy as np

def bresenham_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    p = 2 * dy - dx
    x, y = x1, y1
    pixels = [(x, y)]

    for _ in range(dx):
        if p < 0:
            x = x + 1
            p = p + 2 * dy
        else:
            x = x + 1
            y = y + 1
            p = p + 2 * dy - 2 * dx

        pixels.append((x, y))

    return pixels


# Contoh penggunaan
x1, y1 = 1, 2
x2, y2 = 9, 7

pixels = bresenham_line(x1, y1, x2, y2)
print("Koordinat piksel:", pixels)


# Visualisasi hasil
x_vals, y_vals = zip(*pixels)

plt.figure(figsize=(6, 4))
plt.plot(
    [x1, x2],
    [y1, y2],
    'b--',
    label='Garis ideal'
)

plt.scatter(
    x_vals,
    y_vals,
    c='red',
    s=100,
    marker='s',
    label='Pixel hasil Bresenham'
)

plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(range(0, 10))
plt.yticks(range(0, 9))
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.title('Implementasi Bresenham: Garis (1,2) ke (9,7)')

plt.show()