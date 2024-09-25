from decimal import Decimal
input_data = open('input.txt', 'r')
data = input_data.read()
e =  Decimal("2.7182818284590452353602875")
b = int(data)
a = (round(e, b))
if a == 3.0:
    a = 3
output_data = open('output.txt', 'w')
output_data.write(str(a))
input_data.close()
output_data.close()