def series_sum(n,x):
    if n==1:
        return 1

    return series_sum(n-1,x)+ (1/x ** (n-1))


n = int(input("Enter the number of terms:"))
x = int(input("Enter the value of x:"))

if x == 0:
    print("X can't be 0")
elif n < 0:
    print("Number of terms must be greater than 0")
else:
    print("Sum of series =",series_sum(n,x))