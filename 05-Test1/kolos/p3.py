def f(detector):
    people = 0
    maxPeople = 0
    last = False
    for i in detector:
        if i == "+":
            people+=1
            maxPeople+=1
            last = True
        else:
            people-=1
            last = False
        if last:
            maxPeople+=1
        else:
            maxPeople=0
        if maxPeople >=3:
            return True
    return False