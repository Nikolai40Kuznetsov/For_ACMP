input_data = open('input.txt', 'r')
data = input_data.read()
a = int(data) * 100 + 90 + 9 - int(data)
output_data = open('output.txt', 'w')
output_data.write(str(a))
input_data.close()
output_data.close()