def decorator(count):
    def dec(function):
        import time
        def wrapper(*args, **kwargs):
            print(f"starting function {function}")
            start = time.time()
            for c in range(count):
                result = function(*args, **kwargs)
                print(f"{c} - {result}")
            # result = function("Alex", **kwargs) <- we can change the value
            finish = time.time()
            print(f"function {function} completed for {finish - start}")
            return result
        return wrapper
    return dec

@decorator(count=5)
def hello_world(name):
    hello_name = f"Hello {name}"
    return hello_name

test = hello_world("Boris")
print(test)