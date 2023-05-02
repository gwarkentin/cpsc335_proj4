SQRT_5 = 2.2360679775

def fib_gr_3(n):
    return int(((1+SQRT_5)**n - (1-SQRT_5)**n) / (2**n * SQRT_5))
    
def fib_gr_4(n, p, f_p):
    return int(f_p * ((1+SQRT_5)/2)**(n-p))

def fib_gr_5(n_1):
    return int(fib_gr_3(n_1-1) * ((1+SQRT_5) / 2))


def main_a():
    print('''
    Part a. 
    ''')
    p = None
    while p is None:
        try:
            p = int(input('Enter p (a +int):'))
        except ValueError:
            print("Invalid integer!")
 
    n = None
    while n is None:
        try:
            n = int(input('Enter n (a +int):'))
        except ValueError:
            print("Invalid integer!")
        
    f_p = fib_gr_3(p)
    f_n = fib_gr_4(n, p, f_p)
    
    print(f'p: {p}\tf_p: {f_p}\tn: {n}\tf_n:{f_n} ratio: {f_n/f_p}')
    return p

def main_b(p):
    print('''
    Part b.
    ''')

    for n in range(1,40):

        f_p = fib_gr_3(p)
        gr4_f_n = fib_gr_4(n, p, f_p)
        gr5_f_n = fib_gr_5(n)

        if gr4_f_n > 0:
            ratio = gr5_f_n / gr4_f_n
        else:
            ratio = 0

        print(f'p: {p: <3}\tf_p: {f_p: <4}\tn: {n: <5}\tEq4 f_n:{gr4_f_n: >10}\tEq5 f_n:{gr5_f_n: >10}\tratio: {ratio:.2f}\tvar: {(gr4_f_n-gr5_f_n):<5}')


if __name__ == "__main__":
    print('''
    Welcome to the Golden Ratio Fibonacci approach!
   ''')

    p = main_a()
    input('Enter to continue')
    main_b(p)



