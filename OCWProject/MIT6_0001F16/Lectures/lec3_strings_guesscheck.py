# MIT6.0001- LECTURE 3: STRINGS MANIPULATION, GUESS AND CHECK, APPROXIMATIONS, BISECTION


# # Exhaustive Enumeration
# x = int(input('Enter an integer: '))
# ans = 0
# while ans ** 3 < abs(x):
#     ans += 1
# if ans ** 3 != x:
#     print(x, 'is not perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube of', x, 'is', ans)


# Exhaustive Square-Root Enumeration
# x = 250000
# eps, ans, numGuesses = 0.01, 0, 0
# step = eps ** 2
# while abs(ans ** 2 - x) > eps:
#     numGuesses += 1
#     ans += step
# print('Exhaustive numGuesses = ', numGuesses)
# if abs(ans ** 2 - x) > eps:
#     print('Failed on square root of', x)
# else:
#     print('Square root of', x, 'is', ans)


# # Bisection Square-root Enumeration
# x = 0.125*0.125
# eps = 0.0001
# numGuesses = 0
# # Pre-process with negative case
# isPositive = True
# if x < 0:
#     isPositive = False
# if not isPositive:
#     x = -x
# # Initiation values
# low, hi = 0.0, max(1.0, float(x))
# ans = (low + hi) / 2
# while abs(ans ** 2 - x) > eps:
#     numGuesses += 1
#     ans = (low + hi) / 2
#     if ans ** 2 > x:
#         hi = ans
#     else:
#         low = ans
# # With negative case of input
# if not isPositive:
#     ans = -ans
# print('Bisection numGuesses = ', numGuesses)
# print('Square root of', x, 'is: ', ans)


# Float problems
# There do not exist integer sig and exp such that sig * (2^-exp) = 0.1
# So computer use approximations to represent 0.1
# Usually Python use 53bits like "0.1000000000000000055511151231257827021181583404541015625"
# So when work with float numbers we should use abs(x - y) < eps rather than x == y

# x = 0.0
# for i in range(10):
#     x += 0.1
# if x == 1.0:
#     print(x, '= 1.0')
# else:
#     print(x, 'is not 1.0')


# # Newton-Raphson
# # Formunal newt guess = guess - (guess^2 - k)/(2*guess)
# k = 0.25*0.25
# eps = 0.0001
# guess = k / 2.0
# numGuesses = 0
# while abs(guess ** 2 - k) > eps:
#     numGuesses += 1
#     guess = guess - (guess ** 2 - k)/(2 * guess)
#
# print('Newton-Raphson numGuess = ', numGuesses)
# print('Newton-Raphson root of', k, 'is', guess)


# # Extended Newton-Raphson with exp = n
# k = 3*3*3*3
# exp = 4
# eps = 0.000001
# guess = k / 2.0
# numGuesses = 0
# while abs(guess ** exp - k) > eps:
#     numGuesses += 1
#     guess = guess - (guess ** exp - k)/((exp - 1) * guess ** (exp - 1))
#
# print('Newton-Raphson numGuess = ', numGuesses)
# print('Newton-Raphson root of', k, 'is', guess)
