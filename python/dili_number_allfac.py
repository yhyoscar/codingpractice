

def check_prime(num):
    for i in range(2, num//2):
        if num % i == 0: return False
    return True


def all_factor(num):
    k = 2
    while abs(num) > 1:
        if num % k == 0 and check_prime(k): 
            print(k)
            num = num // k
        else:
            k += 1
    return

all_factor(1559)

