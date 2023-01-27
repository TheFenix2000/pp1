class C:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        result = ""
        suma=0
        for num in self.data:
            result+=str(num)+"+"
            suma+=int(num)
        return str(result[:-1] + "=" +str(suma))
        
        
def main():
    print(C([5,12]))
    print(C([6,0,15]))
if __name__ == "__main__":
    main()