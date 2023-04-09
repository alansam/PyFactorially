'''
Factorial calculation. 
'''

'''
  MARK:  factorial
'''
def factorial(f_n):
  fac = 1
  if (f_n > 1): # protect against invalid input
    for f_ in range(2, f_n + 1):
      fac = fac * f_
  return fac

'''
  MARK:  main.
'''
print('PyFactorially\n')

fac = 54
for f_n in range(1, fac + 1):
  factorial_v = factorial(f_n)
  print('{:-4}! {:-80}'.format(f_n, factorial_v))

print()
