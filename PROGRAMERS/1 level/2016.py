from datetime import datetime

def solution(a, b):
    answer = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    date = datetime(2016, a, b).weekday()

    return answer[date]
    
a = 5
b = 24
print(solution(a,b))
