#Index error
#When you try to access an index in a data structure that does not exist (out of range)
#friends = ['Rolf', 'Anne']
#friends[2]
#Index 2 does not exist in the list (only 0-1)

#Key Error
#Called incorrect key to retrieve value for dictionaries, hashes, etc.
#Ex: movie['release'] when it's supposed to be year

#Name error
#When item is not defined in python by you or the built in framework and is used.
#print(hello)
#very common to forget quotes around text like anove example

#Attribute error
#If you use the wrong attribute or method for a data structure, this will report
#list.intersection() would report error since it only applies to sets

#NotImplemented Error
#When you can report on your own to the user

#Runtime Error
#base time error. An error when you're running your program

#Syntax error
#When you mess up the python syntax. It will report while coding

#Indentation/Tab Error
#will report when code is not indented correctly

#TypeError
#Unsupported concatenation of data types

#ImportError
#When you want to import packages, apis, and materials, make sure to not attempt circular imports between files


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def __repr__(self):
        return f'<Car {self.make} {self.model}>'

class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a '{car.__class__.__name__}' to the garage, but you can only add 'Car' objects.")
        #raise NotImplementedError("We can't add cars to the garage yet.")
        self.cars.append(car)


ford = Garage()
car = Car('ford', 'Fiesta')
print(car)
ford.add_car(car)
try:
    ford.add_car('Fiesta')
except TypeError:
    print("Your car was not a Car!")
except ValueError:
    print('Somewhitn weird happened...')
finally:
    print(f'The garage now has {len(ford)} cars.')
print(len(ford))

def count_from_zero_to_n(n):
    if n < 0:
        raise ValueError(f"This is number {n} is less than 0, and must be a positive integer to work!")
    for x in range(0, n+1):
        print(x)

n = int(input("n: "))
count_from_zero_to_n(n)


#custom error creation
class RuntimeErrorWithCode(TypeError):
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

err = RuntimeErrorWithCode('Am error happened.', 500)
print(err.__doc__)


class UncountableError(ValueError):
    def __init__(self, wrong_value):
        super().__init__(f'Invalid value for n, {wrong_value}, n must be greater than 0.')

def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n+1):
        print(x)

n = int(input("n: "))
count_from_zero_to_n(n)

class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0
    def __repr__(self):
        return f'User {self.name}'

def email_engaged_user(user):
    try:
        user.score = perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function.')
    else:
        if user.score > 500:
            send_engagement_notification(user)
    #finally always runs at the end of a try or except case
    #Express else when you want to run something only if the error doesn't occur.

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_engagement_notification(user):
    print(f'Notification sent to {user}.')

my_user = User('Rolf', {'clicks': 61, 'hits': 100})
email_engaged_user(my_user)

def interact():
    while True:
        try:
            user_input = int(input("Please input an integer:"))
        except:
            print("Please input intgers only.")
        else:
            print("{} is {}.".format(user_input, 'even' if user_input % 2 == 0 else 'odd'))
            break
        finally:
            user_input = input('Do you want to play again? (y/N)')
            if user_input != 'y':
                print('Goodbye.')
                break


