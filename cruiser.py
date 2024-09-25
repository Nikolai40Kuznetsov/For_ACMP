input_data = open('input.txt', 'r')
a, b, c = input_data.readline().split()
v = int(a) * int(b) * int(c) * 2
output_data = open('output.txt', 'w')
output_data.write(str(v))
input_data.close()
output_data.close()