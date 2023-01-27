def f(n):
    res = ""
    couter = 0
    if n > 0:
        while n > 0:
            
            res+="/"
            couter+=1
            n-=1
            if couter % 5 == 0 and n != 0:
                couter=0
                res += "-"

    return res

def main():
    print(f(-4)=="")
    print(f(0)=="")
    print(f(10) == "/////-/////")
    print(f(11) == "/////-/////-/")


if __name__ == "__main__":
    main()
