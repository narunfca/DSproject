import numpy as np
import time
import random
import Factors5 as fct


def is_probable_prime(n, k=10):
    """
    Perform a Probable Prime (PRP) test using Fermat's Little Theorem.

    Parameters:
    n (int): The number to test for primality.
    k (int): The number of test iterations for better accuracy (default is 5).

    Returns:
    bool: True if n is a probable prime, False if it is composite.
    """
    n=int(n)
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Perform Fermat's test k times
    for _ in range(k):
        # Choose a random base 'a' such that 2 <= a <= n-2
        a = random.randint(2, n - 2)

        # Compute a^(n-1) % n using modular exponentiation
        if pow(a, n - 1, n) != 1:
            return False

    return True

def perfect_num(num):

    l=1
    time_list = []
    stm = time.perf_counter()
    st  = time.perf_counter()
    n= (2**l)*(2**(l+1)-1)
    bias = 1.2
    global f2, fac,fac2
    while l<=num:

        factorsp = [1]
        notp=0

        if l>=8:
            c = int((l + 1) ** 0.5)

            for x in range(3, c + 1):
                if (l + 1) % x == 0:
                    notp = 1

            while notp==1:
                l += 2
                notp=0
                c = int((l+1)**0.5)
                for x in range(3,c+1):
                    if (l+1)%x==0:
                        notp=1
            if l>=num:
                break
            else:
                n = (2 ** l) * (2 ** (l + 1) - 1)


        a =int(n**0.5)

        f2=(2**(l+1)-1)
        b = int(f2**0.5)
        if l>20:
            b=int(b*bias/l)
        notp=0
        y=2*l+3
        step=2*l+2
        if l%3==1 and y<=b:
            if f2%y ==0:
                notp,fac,fac2=1,y,int(f2//y)
                y=b+1
            else:
                y+=step
        y+=step

        if b/step >10_000:
            if notp==0:
                fac,fac2,notp = fct.factnum(f2,[],y,2*(l+1),True)

        # while y<=b and notp==0:
        #
        #     while y <= b:
        #         arr = np.arange(y, min((y + step * 9998), b), step)
        #         arr_m=arr[arr%3!=0]
        #
        #         # ind_to_remove = np.arange(2, len(arr), 3)
        #         # arr_m = np.delete(arr, ind_to_remove)
        #         y_new = y + step * 9999
        #
        #         notp = p_fact(arr_m)
        #         #print (notp,fac,fac2)
        #         if notp:
        #             y = b+1
        #         else:
        #             y = min(y_new,b+1)
            #print (result)
        else:
            while y <= b:
                if f2%y ==0:
                    notp,fac,fac2=1,y,int(f2//y)
                    y=b+1
                else:
                    y+=step
                    if f2 % y == 0:
                        notp, fac,fac2 = 1, y,int(f2//y)
                        y = b + 1
                    else:
                        y += (step*2)
        #print(notp)

        if notp>0:
            if is_probable_prime(fac2):
                #print("pp")
                print(f"Factors of (2^{l + 1} - 1) {f2} are [{fac},{fac2}]")  # The ratio to order is {(fac-1)/(l+1)}
            else:
                print(f"Factors of (2^{l+1} - 1) {f2} are {fct.find_fact(f2,fac,(2*l+2))}")    # The ratio to order is {(fac-1)/(l+1)}

            et = time.perf_counter()
            elt = et - st
            time_list.append([l + 1, elt])
            st = time.perf_counter()

            if elt > 1:
                print((l + 1), f" Elapsed time : {elt} seconds")

            while notp==1:
                l += 2
                #print(l)
                notp=0
                c = int((l+1)**0.5)
                for x in range(3,c+1):
                    if (l+1)%x==0:
                        notp=1
            if l>=num:
                break
            else:
                n = (2 ** l) * (2 ** (l + 1) - 1)
            continue

        x=2
        while x<=a:
            if n%x ==0:
                factorsp.append(x)
                factorsp.append(n//x)
                x*=2


        if n%a==0 and n//a == a:
            factorsp.append(a)


        if sum(factorsp)==n:
            et = time.perf_counter()
            elt = et - st
            if elt > 1:
                print((l+1),f" Elapsed time : {elt} seconds")
            time_list.append([l + 1, elt])
            st = time.perf_counter()
            print("---------")
            print("PERFECT - ",n,"(2^",l," x 2^", (l+1) ,"-1) - ",factorsp)
            print("---------")

        if l>1:
            l+=2
            if l>num:
                break
        else:
            l+=1
        #print(l)
        n = (2 ** l) * (2 ** (l + 1) - 1)

    et = time.perf_counter()
    elt = et - st
    time_list.append([l-1,elt])
    telt = et-stm
    #print(time_list)
    print(f"Total Elapsed time : {telt} seconds")

def p_fact(arr_m):
    notp = 0
    global f2,fac,fac2
    f2_r = f2 % arr_m
    notp = (np.any(f2_r==0))*1
    #print(notp)
    if notp:
        f2_idx = (np.where(f2_r == 0))[0]
        fac  = arr_m[f2_idx[0]]
        fac2 = f2//fac
    return notp

fac=fac2=f2=0

if __name__ == '__main__':
    try:
        num = int(input("Enter a maximum power of 2 (not exceeding 100) for perfect number : "))
    except ValueError:
        print("Not seems to be valid number. \nLet me assume it as 86.")
        num = 86
    finally:
        if num>100:
            print("The value given is large for this computer.\nLet me take 100")
            num=100

        perfect_num(num)

