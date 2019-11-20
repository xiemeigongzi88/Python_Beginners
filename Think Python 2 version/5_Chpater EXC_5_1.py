import math

def fermat(a,b,c,n):
    if(pow(a,n)+pow(b,n)==pow(c,n)):
        print("Holy smokes, Fermat was wrong!")
        return "work"
    else:
        return 'continue'

a=b=c=n=2

while(n>1):
    while(c>1):
        while(b>1):
            while(a>1):
                if(fermat(a,b,c,n)=="work"):
                    print(a,b,c,n)
                else:
                    a=a+1
            b+=1
        c+=1
    n+=1


