def f(d):
    arr = []
    for car in d:
        if car[1] == "in":
            arr.append(car[0])
        else:
            arr.pop(arr.index(car[0]))
    return sorted(arr)

def main():
    cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],["BA111","in"],["BA123","out"],["KR234","in"]]
    print(f(cars)==["BA111","GX444","KR234"])

if __name__ == "__main__":
    main()
