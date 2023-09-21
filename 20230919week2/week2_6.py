#6 根号x 牛顿法

n = int(input())
def newton_search(x):
    guess = x/n
    while abs(guess ** 2 - x) >= 0.00001:
        guess = (guess + x / guess)/2
    print(guess)
newton_search(2)