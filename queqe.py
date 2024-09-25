input_data = open('input.txt', 'r')
output_data = open('output.txt', 'w')
data = input_data.read()
if int(data) == 1 or int(data) == 0:
    output_data.write(str(0))
    output_data.write(' ')
    output_data.write(str(0)) 
elif int(data) >= 146:
    output_data.write("NO")
else: 
    a = int(data) * 5
    int(a)
    b = a % 60 - 5
    if b == -5:
        b = 55
        a -= 1
    int(b)
    c = (a - b) / 60 
    output_data.write(str(int(c)))
    output_data.write(" ")
    output_data.write(str(b))
input_data.close()
output_data.close()