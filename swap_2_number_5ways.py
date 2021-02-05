# 1. Swapping with help of 2 numbers
# ==================================

a = 10
b = 20
print("The value of a is:", a, '\n\n', "The value of b is", b)
print("\n After swap")
print("================\n")
c = a
a = b
b = c

print("The value of a is:", a, '\n\n', "The value of b is", b)

# 2. Just using x,y=y,x:
# ============================
a = 10
b = 20
print("The value of a is:", a, '\n\n', "The value of b is", b)
print("\n After swap")
print("================\n")
a, b = b, a
print("The value of a is:", a, '\n\n', "The value of b is", b)

# 3. Using division and multiplication
# =======================================
a = 10
b = 20
print("The value of a is:", a, '\n\n', "The value of b is", b)
print("\n After swap")
print("================\n")
a = a * b
b = a / b
a = a / b
print("The value of a is:", int(a), '\n\n', "The value of b is", int(b))

# 4. Using bitwise XOR operations:
# ==================================

a = 10
b = 20
print("The value of a is:", a, '\n\n', "The value of b is", b)
print("\n During  swap")
print("================\n")
a ^= b
print("Value of a is", a)
b ^= a
print("value of b is ", b)
a ^= b
print("Value of a is", a)
print("\n After swap")
print("================\n")
print("The value of a is:", a, '\n\n', "The value of b is", b)

# 5. Addition and subtraction ways:
# =================================

a = 10
b = 20
print("The value of a is:", a, '\n\n', "The value of b is", b)
a=a+b
b=a-b
a=a-b

print("\n After swap")
print("================\n")
print("The value of a is:", a, '\n\n', "The value of b is", b)



