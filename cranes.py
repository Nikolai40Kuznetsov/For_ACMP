input_data = open('input.txt', 'r')
data = input_data.readline()
a = int(data) / 6
b = a * 4
c = a
output_data = open('output.txt', 'w')
output_data.write(str(int(a)))
output_data.write(' ')
output_data.write(str(int(b)))
output_data.write(' ')
output_data.write(str(int(c)))
input_data.close()
output_data.close()