import numpy as np

def factnum(num,factors=[],sugg=2,step=1):
    a = int(num ** 0.5)
    if num >= 2:
        y=t=0
        if sugg>=3:
            step = max(step,2)
        for x in range(sugg, max(a+1, 3),step):
            if num % x == 0:
                factors.append(x)
                y = int(num//x)
                #print(x)
                if x==y:
                    factors.append(y)
                if y>x:
                    t=x
                    factnum(y,factors,x,step)
                    break
        if y==0:
            factors.append(num)
            #print(num)
    return factors


def find_fact(num,sugg=2,step=1):
    if num>=1:
        if num==1:
            factors = [1]
        else:
            factors = [1]
            factors = factnum(num,factors,sugg,step)

        unq_factors = sorted(set(factors))
        fact_dict = {}

        fac=''
        tf = 1
        for f in unq_factors:
            if f>1:
                fact_dict[f]=factors.count(f)
                if fac!='':
                    fac=fac+" * "
                fac+=str(f)
                nf=factors.count(f)

                if nf>1:
                    fac = fac +"^"+str(nf)
                tf*=(nf+1)
                #print(tf)

        num_factor = [1]
        if num>3:
            if num in fact_dict:
                fact_dict.pop(num)
            for index,(i,n) in enumerate(fact_dict.items()):
                nf = num_factor.copy()
                for j in range(n):
                    for f in nf:
                        af = (f*(i**(j+1)))
                        #print(af)
                        num_factor.append(af)
            if num not in num_factor:
                num_factor.append(num)
        return num_factor


    #    print(fac,"\n",tf)
    #    print(num_factor)
    #    if sum(num_factor)/2==num:
    #        print("The number is perfect.")

        #print(fact_dict)

        #print("Number of Factors : ",len(factors))
    else:
        return 'Wrong Number'


if __name__ == "__main__":
    num = int(input("Enter any positive integer : "))
    print("Factors are : ", end='')
    print(find_fact(num))
