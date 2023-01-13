import json
def f(age, course, average):
    count = 0
    with open("data.json", "r") as file:
        data = json.load(file)
        for chunk in data:
            if chunk['age'] >=age:
                for courseItem in chunk['studies']['courses']:
                    if courseItem['name'] == course:
                        suma = 0
                        for num in courseItem['grades']:
                            suma+=num
                        if suma/len(courseItem['grades']) >= average:
                            count+=1
    return count