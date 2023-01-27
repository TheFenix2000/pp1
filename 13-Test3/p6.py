class C:
    def __init__(self, counter):
        self.counter = counter
    
    def m1(self):
        return self.counter
    
    def m2(self):
        self.counter+=1
    
    def m3(self):
        self.counter-=1

    def m4(self, new_val):
        self.counter += new_val

def main():
    c=C(5)
    print(c.m1() == 5)
    c.m2()
    print(c.m1() == 6)
    c.m4(-8)
    print(c.m1() == -2)
    c.m3()
    print(c.m1() == -3)
    c.m4(10)
    print(c.m1() == 7)
if __name__ == "__main__":
    main()

