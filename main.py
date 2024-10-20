# This is a sample Python script.
#import car
#from car import electricCar
import dog


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    my_dog = dog.Dog(27, 'William')
    print(f'my dog name is {my_dog.name}')
    print(f'my dog age is {my_dog.age}')
    my_dog.sit()
    my_dog.roll_over()
    my_dog.barking()








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
