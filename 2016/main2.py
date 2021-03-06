import datetime

def solution(a,b) :
    date = ['MON','TUE','WED','THU','FRI','SAT', 'SUN']
    return date[datetime.date(2016, a, b).weekday()]

print(solution(1 , 1))