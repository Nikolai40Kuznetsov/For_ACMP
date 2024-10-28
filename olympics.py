def solve_competition(N, times):
    sorted_times = sorted(times)
    results = {
        5: {'solved': 0, 'penalty': 0},
        3: {'solved': 0, 'penalty': 0},
        1: {'solved': 0, 'penalty': 0}
    }
    current_time = 0
    for i in range(N):
        if current_time + times[i] <= 300:
            current_time += times[i]
            results[5]['solved'] += 1
            results[5]['penalty'] += current_time
        else:
            break
    current_time = 0
    for i in range(N-1, -1, -1):
        if current_time + times[i] <= 300:
            current_time += times[i]
            results[3]['solved'] += 1
            results[3]['penalty'] += current_time
        else:
            break
    current_time = 0
    for i in range(N):
        if current_time + sorted_times[i] <= 300:
            current_time += sorted_times[i]
            results[1]['solved'] += 1
            results[1]['penalty'] += current_time
        else:
            break
    winner = 1 
    for course in [3, 5]:
        if (results[course]['solved'] > results[winner]['solved']) or \
           (results[course]['solved'] == results[winner]['solved'] and results[course]['penalty'] < results[winner]['penalty']) or \
           (results[course]['solved'] == results[winner]['solved'] and results[course]['penalty'] == results[winner]['penalty'] and course < winner):
            winner = course
    return winner
inputFileName = 'input.txt'
outputFileName = 'output.txt'
with open(inputFileName, 'r') as f:
    N = int(f.readline().strip())
    times = list(map(int, f.readline().strip().split()))
winner = solve_competition(N, times)
with open(outputFileName, 'w') as f:
    f.write(str(winner))