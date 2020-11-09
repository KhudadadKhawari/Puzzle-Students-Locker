import math
students = int(input('number of Students: '))
lockers = int(input('number of Lockers: '))

def mostTouchedLockers(lockersNumber,studentsNumber):
    most_touched_list = []
    most_touched_count = 0
    most_touched_item = 0
    for a in range(1,lockersNumber+1):
        for b in range(1,studentsNumber+1):
            if a % b == 0:
                most_touched_list.append(a)
    for item in set(most_touched_list):
        counta = most_touched_list.count(item)
        if counta >= most_touched_count:
            most_touched_count = counta
            most_touched_item = item
    return f"{most_touched_item} is most touched Item which is touched {most_touched_count} Times"
    
def openLocks(number_of_lockers, number_of_students):
    lockersOpen = int(math.sqrt(number_of_lockers))
    lockersClosed = number_of_lockers - lockersOpen
    resultLuckerIsOpen = {}
    for a in range(1,number_of_lockers+1):
        resultLuckerIsOpen[a] = False
        for b in range(1,number_of_students+1):
            if a%b == 0:
                resultLuckerIsOpen[a] = not resultLuckerIsOpen[a]
    return f"total of Open Lockers: {lockersOpen} \n total of closed lockers {lockersClosed} "

print(openLocks(lockers,students))
print(mostTouchedLockers(lockers,students))