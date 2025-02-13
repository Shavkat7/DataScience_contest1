import time

def decorator_1(func):
    def wrapper(*args, **kwargs):
        boshlanish_vaqti = time.time()
        func(*args, **kwargs)
        tugash_vaqti = time.time()
        bajarilish_vaqti = tugash_vaqti - boshlanish_vaqti
        print(f"{func.__name__} chaqiruv bajarildi {bajarilish_vaqti:.4f} soniyada")
    return wrapper