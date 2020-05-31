from divisor_master import IsPrime
from divisor_master import delimeter
from divisor_master import maxd
from divisor_master import Factor

n = int(input("Введите целое число от 1 до 1000: "))
if n not in range (1, 1001):
   print ("число вне диопазона")

z= IsPrime(n)
z1= delimeter(n)
z2= maxd(n)
z3 = Factor(n)
