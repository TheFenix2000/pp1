def f1(t):

    obj = {}
    symbols_to_remove = ["!", ".", ","]

    for symbol in symbols_to_remove:
        t = t.replace(symbol, "")

    t = t.split()

    for i in range(len(t)):
        if t[i] == "is":
            obj[t[i-1]] = int(t[i+1])

    obj = dict(sorted(obj.items()))

    return obj

def f2(d):
    age = 0
    for i in d.values():
        age+=i
    return age

def main():
    print(f1("Mark is 24 and Ann is 27") == {"Ann":27, "Mark":24})
    print(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!") == {"Barbara":7, "John":103, "Peter":11}) 
    print(f2(f1("Mark is 24 and Ann is 27"))==51)
    print(f2(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))==121) 


if __name__ == "__main__":
    main()
