operand1 = int(input("masukkan operand 1: "))
operator = input("masukkan operator (*,/,+,-): ")
operand2 = int(input("masukkan opperand 2: "))

if operator == '*':
    hasil = operand1 * operand2
elif operator == '/':
    hasil = operand1 / operand2
elif operator == '+':
    hasil = operand1 + operand2
elif operator == '-':
    hasil = operand1 - operand2
else:
    print ("hasil error operator tidak valid")

print (f"hasil {hasil} yaitu ({operand1} {operator} {operand2})")