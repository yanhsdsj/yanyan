#5 根号2 牛顿法
def newton_search(x):
    guess = x/2
    while abs(guess ** 2 - x) >= 0.00001:
        guess = (guess + x / guess)/2
    print(guess)
newton_search(2)