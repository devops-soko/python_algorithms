def solution(a,b) :
    date = ['FRI','SAT', 'SUN','MON','TUE','WED','THU',]
    more =[1,3,5,7,8,10,12]
    less =[4,6,9,11]
    total =0
    if a != 1:
        for i in range(1, a):
            if i in more :
                total += 31
            elif i in less :
                total +=30
            else :
                total += 29
    total += b
    if total <8 :
        return date[total-1]
    else :
        return date[total%7-1]

print(solution(1 , 1))