

class Dog :
    def __init__(self,age,name):

       self.age = age
       self.name = name
    def roll_over(self) :
        print(f"'{self.name} is rolled over ")

    def sit(self) :
        print(f"{self.name} is sitting now " )

if __name__ == '__main__':

    print("Dog class definition")

