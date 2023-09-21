#7 三次方
#Xn+1 = Xn - f(Xn)/f'(Xn)
def tri_search(x):
    guess = x/10
    while abs(guess ** 3 - x) >= 0.00001:
        guess = (2 * guess + x / guess ** 2)/3
    print(guess)
tri_search(8)