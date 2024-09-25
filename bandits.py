input_data = open('input.txt', 'r')
n, m = input_data.readline().split()
a = int(m) - 1
b = int(n) - 1
output_data = open('output.txt', 'w')
output_data.write(str(a))
output_data.write(' ')
output_data.write(str(b))
input_data.close()
output_data.close()