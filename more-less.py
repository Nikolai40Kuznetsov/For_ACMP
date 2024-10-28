inputFileName = 'input.txt'
outputFileName = 'output.txt'
with open(inputFileName, 'r') as f:
    A = float(f.readline())
    B = float(f.readline())
if A > B:
    symbol = ">"
elif A < B:
    symbol = "<"
else:
    symbol = "="
with open(outputFileName, 'w') as f:
    f.write(symbol)