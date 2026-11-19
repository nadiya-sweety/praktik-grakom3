import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# ==========================================
# ALGORITMA DDA
# ==========================================

# Titik awal dan titik akhir
x1, y1 = 1, 2
x2, y2 = 9, 7

# Menghitung delta x dan delta y
dx = x2 - x1
dy = y2 - y1

# Menentukan jumlah langkah
steps = max(abs(dx), abs(dy))

# Menghitung kenaikan setiap langkah
x_inc = dx / steps
y_inc = dy / steps

# Nilai awal
x = x1
y = y1

titik_dda = []


# Perhitungan DDA
for i in range(steps + 1):

    # Pembulatan ke pixel terdekat
    pixel_x = int(x + 0.5)
    pixel_y = int(y + 0.5)

    titik_dda.append((pixel_x, pixel_y))

    x = x + x_inc
    y = y + y_inc


# Menampilkan hasil
print("HASIL ALGORITMA DDA")
print("--------------------")

for i, titik in enumerate(titik_dda):
    print("Step", i, ":", titik)


# ==========================================
# DIAGRAM DDA
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
for px, py in titik_dda:

    kotak = Rectangle(
        (px - 0.5, py - 0.5),
        1,
        1,
        alpha=0.25
    )

    ax.add_patch(kotak)


# Titik hasil DDA
x_pixel = [t[0] for t in titik_dda]
y_pixel = [t[1] for t in titik_dda]

ax.plot(
    x_pixel,
    y_pixel,
    'o',
    label='Titik hasil DDA'
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
ax.set_title('Ilustrasi Hasil DDA')

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