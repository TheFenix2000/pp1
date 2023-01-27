class C:
    @staticmethod
    def m1(n):
        new_number = ""
        for digit in str(n):
            if (int(digit) % 2 == 0):
                new_number += digit
        return int(new_number)
    
    @staticmethod
    def m2(n):
        for i in range(1, len(str(n))):
            if int(str(n)[i]) < int(str(n)[i-1]):
                return False
        return True
    
    @staticmethod
    def m3(n):
        missing = ""
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for num in nums:
            if str(num) not in str(n):
                missing+=str(num)
        return missing
            



def main():
    print(C.m1(4231564)==4264)
    print(C.m1(79381)==8)
    print(C.m2(125579) == True)
    print(C.m2(4557879) == False)
    print(C.m3(23557) == "014689")
    print(C.m3(12340) == "56789")

if __name__ == "__main__":
    main()
