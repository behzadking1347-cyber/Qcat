# Qcat 🐱

**Qcat** یک جعبه‌ابزار ساده و توسعه‌پذیر پایتون برای بازی‌سازی دوبعدی، محاسبات برداری و کار با داده‌هاست؛ با تکیه بر **Pygame، NumPy و Pandas**.

> وضعیت پروژه: نسخه�� اولیه (`0.1.0`). API ممکن است در نسخه‌های آینده تغییر کند.

## نصب

### نصب مستقیم از GitHub

```bash
python -m pip install git+https://github.com/behzadking1347-cyber/Qcat.git
```

یا ابتدا مخزن را clone و در پوشهٔ آن نصب کنید:

```bash
git clone https://github.com/behzadking1347-cyber/Qcat.git
cd Qcat
python -m pip install .
```

برای توسعه و اجرای تست‌ها:

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

پس از انتشار در PyPI می‌توانید با `python -m pip install qcat` نصب کنید. تا قبل از انتشار، دستور نصب از GitHub بالا را استفاده کنید.

## شروع سریع: بازی

```python
import pygame
from qcat import Entity, QcatGame


game = QcatGame(title="بازی من", size=(800, 600), background=(20, 24, 35))
player = game.add(Entity(100, 100, 48, 48, color=(70, 210, 150), speed=260))


def update(game, dt):
    keys = pygame.key.get_pressed()
    player.vx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player.speed
    player.vy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player.speed


game.run(on_update=update)
```

برای خروج از بازی `Escape` یا دکمهٔ بستن پنجره را بزنید. `dt` زمان سپری‌شده از فریم قبلی بر حسب ثانیه است، بنابراین سرعت حرکت مستقل از نرخ فریم می‌ماند.

## محاسبات

```python
from qcat import clamp, distance, lerp, normalize

print(distance((0, 0), (3, 4)))     # 5.0
print(normalize((3, 4)))            # [0.6 0.8]
print(lerp(10, 20, 0.25))           # 12.5
print(clamp(120, 0, 100))           # 100
```

توابع برداری از آرایه‌های NumPy استفاده می‌کنند و ورودی‌های سازگار با آرایه، مانند tuple و list، می‌پذیرند.

## داده‌ها

```python
from qcat import load_csv, moving_average

scores = load_csv("scores.csv")
print(scores.head())
print(moving_average([10, 12, 8, 20], window=2).tolist())
```

## API پایه

- `QcatGame(...)`: پنجره و حلقهٔ بازی؛ از `add()` برای افزودن موجودیت استفاده کنید.
- `Entity(x, y, width, height, ...)`: موجودیت مستطیلی با سرعت، رنگ، به‌روزرسانی، رسم و بررسی برخورد.
- `clamp(value, minimum, maximum)`, `lerp(start, end, amount)`, `distance(a, b)`, `normalize(vector)`.
- `load_csv(path)` و `moving_average(values, window)`.

Qcat فعلاً یک پایهٔ کوچک است، نه موتور کامل بازی. مدیریت صحنه، فیزیک پیشرفته، انیمیشن و صدا می‌توانند در نسخه‌های بعد اضافه شوند.

## مجوز

این پروژه تحت مجوز BSD 3-Clause منتشر شده است؛ فایل `LICENSE` را ببینید.
