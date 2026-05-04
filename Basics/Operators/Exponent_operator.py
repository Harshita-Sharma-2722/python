print(2**10)
base=int(input("enter base= "))
exp=int(input("enter exponent= "))
result_operator=base**exp
print(result_operator)
result_pow=pow(base,exp)
print(result_pow)
if result_operator == result_pow:
    print("both are same")
else:
    print("not same")