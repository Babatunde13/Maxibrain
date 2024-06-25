''' This is a basic Python script'''

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__=='__main__':
    n = 9
    print(fib(n - 1) + fib(n - 2))
