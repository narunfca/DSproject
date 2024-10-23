import numpy as np
import time
import random


def prob_fact(last_num=30030,level=1,step=2,filter=None):
    arr_1 = np.array([[2, 3, 5, 7, 11,13]]).T
    arr_2 = np.arange(step+1, min(last_num,int(30030*step/2)+1), int(step))
    is_prime_arr = (arr_2 % arr_1).all(axis=0)
    prime1_arr = arr_2 * (is_prime_arr*1)
    prime1_arr = prime1_arr[prime1_arr != 0]
    arr_2 = np.concatenate((arr_1.flatten(), prime1_arr))
    t=0
    if np.max(arr_2)>=last_num:
        #print(last_num)
        arr_2 = arr_2[arr_2<=last_num]

    # if step>2:
    #     arr_2 = arr_2[(arr_2-1) % step == 0]

    #print (arr_2)

    # if level == 2:
        # if t==0:
        #     i_arr = arr_2+0
        #     con_arr = arr_2+0
        #     for i in range(1,step):
        #         con_arr = con_arr+27720
        #         i_arr = np.concatenate((i_arr,con_arr))
        #     # arr_2 = i_arr+0
        #     arr_2 = i_arr[i_arr <= last_num]

        # arr_2 = arr_2[(arr_2-1)%step==0]
        #print(arr_2.any(arr_2==179951))
        # arr_1 = np.array([[2, 3, 5, 7, 11,13]]).T
        # arr_2 = np.arange(13, 360360, 2)
        # is_prime_arr = (arr_2 % arr_1).all(axis=0)
        # prime1_arr = arr_2 * is_prime_arr
        # prime1_arr = prime1_arr[prime1_arr != 0]
        # arr_2 = np.concatenate((arr_1.flatten(), prime1_arr))
        # arr_2 = arr_2[arr_2<last_num]
    # if filter:
    #     arr_2=arr_2[(arr_2-1)%filter==0]
    #print(arr_2)
    return arr_2

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


def factnum(num,factors=[],sugg=2,step=1,prime_test=False):

    if is_probable_prime(num):
        if prime_test:
            return [1,num, 0]
        factors.append(num)
        return factors

    a = int(int(num) ** 0.5)


    if num >= 2:
        y=t=nof=0

        if num % a == 0:
            if a>=sugg:
                sub_factor = [a]
                print(a)
                sub_factor = sub_factor * 2
                factors.extend(sub_factor)
                return factors

        if num %2 ==0:
            nof=1
            factors.append(2)
            y = int(num//2)
            if prime_test:
                return [2, y,1]
            if y==2:
                factors.append(y)
            if y>2:
                t=2
                factnum(y,factors,2,step)

        else:

            step = max(step,2)
            sugg = max(3,sugg)
            if step>2:
                level = 2
                inc:int   = int((30030*step)/2)
            else:
                level = 1
                inc:int   = 30030


            if sugg<(inc - 1000*step):
                for x in range(sugg, min(sugg+999*step,max(a+1, 3)),step):
                    if num % x == 0:
                        y = int(num//x)
                        if prime_test:
                            return [x,y,1]
                        factors.append(x)
                        #print(x,y)
                        if x==y:
                            factors.append(y)
                            break
                        if y>x:
                            t=x
                            if y>=int(x)**2:
                                factnum(y,factors,x,step)
                            else:
                                factors.append(y)
                            break
                x = sugg + step*1000
            else:
                x = sugg

            if y==0:
                if step==2:
                    arr_base = prob_fact(a,1)
                else:
                    arr_base = prob_fact(a,2,step)
                if x<inc:
                    arr = arr_base[arr_base>=x]
                else:
                    x   = int(sugg//inc)*int(inc)
                    arr = arr_base + x
                    if not(arr_base[0]%2):
                        arr_base[0]-=1
                    # if x<inc:
                    #     arr = arr_base[arr_base>=x]
                    # else:
                    #     x   = int((sugg//inc)*inc)
                    #     arr = arr_base + x
                    # arr = arr_base[(arr_base-1)%step==0]
                    #print(f"<{arr.size}>")

            while x<=a and y==0:
                if x<inc:
                    x_new = int(inc)
                else:
                    x_new = int(x+inc)

                num_r = int(num) % arr
                nof   = int((np.any(num_r==0))*1)

                if nof:
                    num_idx = (np.where(num_r == 0))[0]
                    x = int(arr[num_idx[0]])
                    #print(x)
                    y = int(num//x)
                    if prime_test:
                        return [x, y,1]
                    factors.append(x)
                    #print(x,y)

                    if x==y:
                        factors.append(y)
                        break

                    if y>x:
                        t=x
                        if y >= int(x) ** 2:
                            factnum(int(y), factors, int(x), step)
                        else:
                            factors.append(y)
                        break

                if x<inc:
                    arr = arr_base.copy()

                arr = arr + inc
                if not (arr[0] % 2):
                    arr[0] -= 1


                x = x_new

        if y==0:
            if prime_test:
                return [num,1,0]
            factors.append(num)

            #print(num)
    return factors


def find_fact(num,sugg=2,step=1):
    if num>=1:
        factors = [1]
        if num!=1:
            factors = factnum(num,factors,sugg,step)

        unq_factors = sorted(set(factors))
        #print(unq_factors)
        fact_dict = {}

        fac=''
        tf = 1
        for f in unq_factors:
            if f>1:
                fact_dict[f]=factors.count(f)
                nf=factors.count(f)
                tf*=(nf+1)
        num_factor = [1]
        if num>1:
            if num in fact_dict:
                fact_dict.pop(num)
            for index,(i,n) in enumerate(fact_dict.items()):
                nf = num_factor.copy()
                for j in range(n):
                    for f in nf:
                        if j==0:
                            af = int(f)*int(i)
                        else:
                            af = (f*(i**(j+1)))
                        #print(af)
                        if af>0:
                            num_factor.append(af)
            if num not in num_factor:
                num_factor.append(num)
        return num_factor
    else:
        return 'Wrong Number'


if __name__ == "__main__":
    num = int(input("Enter any positive integer : "))
    t1 = time.perf_counter()
    factors = find_fact(num)
    print(f"Factors are : {factors}")
    print(f"No. of factors are {len(factors)}")
    t2 = time.perf_counter()
    print(f"Elapsed time is {t2-t1} seconds")