import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# ==========================================
# ALGORITMA BRESENHAM
# ==========================================

# Titik awal dan titik akhir
x1, y1 = 1, 2
x2, y2 = 9, 7

# Menghitung delta x dan delta y
dx = x2 - x1
dy = y2 - y1

# Parameter keputusan awal
p = 2 * dy - dx

# Nilai awal
x = x1
y = y1

titik_bresenham = [(x, y)]


# Perhitungan Bresenham
while x < x2:

    if p < 0:

        # Pilih E
        x = x + 1

        p = p + 2 * dy

    else:

        # Pilih NE
        x = x + 1
        y = y + 1

        p = p + 2 * dy - 2 * dx

    titik_bresenham.append((x, y))


# Menampilkan hasil
print("HASIL ALGORITMA BRESENHAM")
print("--------------------------")

for i, titik in enumerate(titik_bresenham):
    print("Step", i, ":", titik)


# ==========================================
# DIAGRAM BRESENHAM
# ==========================================

fig, ax = plt.subplots(figsize=(8, 6))

# Garis ideal
ax.plot(
    [x1, x2],
    [y1, y2],
    '--',
    label='Garis ideal'
)


# Kotak pixel
for px, py in titik_bresenham:

    kotak = Rectangle(
        (px - 0.5, py - 0.5),
        1,
        1,
        alpha=0.25
    )

    ax.add_patch(kotak)


# Titik hasil Bresenham
x_pixel = [t[0] for t in titik_bresenham]
y_pixel = [t[1] for t in titik_bresenham]

ax.plot(
    x_pixel,
    y_pixel,
    'o',
    label='Titik hasil Bresenham'
)


# Label titik awal
ax.annotate(
    '(1,2)',
    (1, 2),
    xytext=(0.7, 1.4)
)

# Label titik akhir
ax.annotate(
    '(9,7)',
    (9, 7),
    xytext=(8.3, 7.3)
)


# Pengaturan diagram
ax.set_title('Ilustrasi Hasil Bresenham')

ax.set_xlabel('X')
ax.set_ylabel('Y')

ax.set_xlim(0, 10)
ax.set_ylim(1, 8)

ax.set_xticks(range(0, 11))
ax.set_yticks(range(1, 9))

ax.grid(True)

ax.set_aspect('equal')

ax.legend()

plt.show()