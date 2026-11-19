import numpy as np
import matplotlib.pyplot as plt
def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    pixels = []
    for _ in range(steps + 1):
        pixels.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    return pixels
# Contoh penggunaan
x1, y1 = 1, 2
x2, y2 = 9, 7
pixels = dda_line(x1, y1, x2, y2)
print("Koordinat piksel:", pixels)
# Visualisasi hasil
x_vals, y_vals = zip(*pixels)
plt.figure(figsize=(6, 4))
plt.plot([x1, x2], [y1, y2], 'b--', label='Garis ideal')
plt.plot(x_vals, y_vals, 'r-o', label='Hasil DDA')
plt.xticks(range(0, 10))
plt.yticks(range(0, 9))
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Implementasi DDA: Garis (1,2) ke (9,7)')
plt.show()