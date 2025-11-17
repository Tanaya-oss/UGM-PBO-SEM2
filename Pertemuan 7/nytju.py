def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dipanggil.")
        func()
        print("Setelah fungsi dipanggil.")
    return wrapper

@my_decorator
def say_hello():
    print("Halo!")

# Memanggil fungsi yang telah didekorasi
say_hello()