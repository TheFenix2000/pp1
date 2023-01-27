class C:
    def __init__(self, d):
        self.d = d
    
    def m(self, n):
        students = []
        for x in self.d:
            suma = 0
            for num in self.d[x]:
                suma+=num
            avg = suma / len(self.d[x])
            if avg >= n:
                students.append(x)
        return ",".join(sorted(students)) if len(students) > 0 else ""

def main():
    s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
    print(s.m(4) == "Barbara,Peter")
    print(s.m(3) == "Barbara,Harry,Peter")
    print(s.m(5) == "")


if __name__ == "__main__":
    main()