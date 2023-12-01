def f():
    for i in range(10):
        yield


if __name__ == "__main__":
    a = f()
    for i in a:
        print(i)
