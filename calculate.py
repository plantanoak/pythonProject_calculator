a = input()
calculate = compile(a, 'string', 'eval')
print(eval(calculate))

a = float(input())
b = float(input())
act = input()

if (act == "/" or act == "mod" or act == "div") and b == 0:
    c = "Деление на 0!"
elif act == "+":    c = a + b
elif act == "-":    c = a - b
elif act == "/":    c = a / b
elif act == "*":    c = a * b
elif act == "mod":  c = a % b
elif act == "pow":  c = a ** b
elif act == "div":  c = a // b

print (c)
