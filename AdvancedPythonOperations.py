"""
friends_last_seen = {
  'Rolf': 31,
  'Jen': 1,
  'Anne': 7
}

print(id(friends_last_seen))
#The id shows the address of the object in memory

friends_last_seen = {
  'Rolf': 31,
  'Jen': 1,
  'Anne': 7
}

print(id(friends_last_seen))

friends_last_seen['Rolf'] = 0
print(id(friends_last_seen))
#reference id stays the same regardless of content changes in the object

my_int = 5
print(id(my_int))

my_int += 1
print(id(my_int))
#variable will change, meaning that this is mutable
#list, set, dict

#immutable types will not change id upon object change
#tuples, string, integer, floats
#immutable - all functions return new objects

def see_friend(friends, name):
  print(friends == friends_last_seen)
  friends[name] = 0

print(id(friends_last_seen))
print(id(friends_last_seen['Rolf']))

see_friend(friends_last_seen, 'Rolf')

print(id(friends_last_seen['Rolf']))
print(id(friends_last_seen))

age = 20
def increase_age(current_age):
  current_age = current_age + 1

print(id(age))
increase_age(age)
print(id(age))

accounts = {
  'checking': 1958.00,
  'savings': 3695.50
}

def add_balance(amount: float, name: str = 'checking') -> float:
  #function to update the valance of an account and return the new balance
  accounts[name] += amount
  return accounts[name]

transactions = [
  (-180.67, 'checking'),
  (-229.99, 'checking'),
  (220.00, 'savings'),
  (-15.70, 'checking'),
  (-23.90, 'checking'),
  (-13.00, 'checking'),
  (1579.50, 'checking'),
  (-600.50, 'checking'),
  (600.50, 'savings'),
]

for t in transactions:
  add_balance(*t)
  #add_balance(amount = t[0], name = t[1])
  #add_balance(t[0], t[1])
  #double star indicates a dictionary unpacking!

add_balance(500.00)
print(accounts['checking'])

def create_account(name: str, holder: str, account_holders: list = []):
  account_holders.append(holder)
  
  return {
    'name': name, 
    'main_account_holder': holder,
    'account_holders': account_holders
  }

a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Jen')

print(a2)
"""

#Queus and Data Collections
"""
Counter
defaultdict
ordereddict
namedtuple
deque
"""
#counts number of iterations in the collection
from collections import Counter

device_temperatures = [13.5, 13.0, 14.0, 14.5, 14.5, 15.0, 16.0]
temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])

#creates a default dictionary with a specific type of elements (specified) that are empty
#Helps with instantiation, so you can just append or compute operations into the empty elements of dictionary
from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_maters = defaultdict(list)

for coworker, place in coworkers:
  alma_maters[coworker[0]].append(coworker[1])

my_company = 'Teclado'
coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)
for person, company in other_coworkers:
  coworker_companies[person] = company

print(coworker_companies[coworkers[0]])
print(coworker_companies['Rolf'])

#orders the dictionary based on preference and own operations
from collections import OrderedDict
o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)

o.move_to_end('Rolf')
o.move_to_end('Jen', last=False)
print(o)
o.popitem()
print(o)

#creates dictionary connection where data of a tuple acan be classified to a specific name for readability
from collections import namedtuple
account = ('checking', 1850.90)

Account = namedtuple('Account', ['name', 'balance'])

accountNamedTuple = Account(*account)

print(accountNamedTuple._asdict())


from collections import deque

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')

print(friends)

friends.pop()
friends.popleft()
print(friends)

unknown = 'Unknown'
harry = defaultdict(lambda: unknown)
"""
arg_od = OrderedDict()
arg_od.popitem()
arg_od.pop(0)
arg_od.move_to_end('Bob')
arg_od.move_to_end('Dan', last=False)


temp_tuple = (name, club)
Player = namedtuple('Player', ['name', 'club'])
Playernamedtuple = Player(*temp_tuple)
return Playernamedtuple

arg_deque = deque
arg_deque.pop()
left = arg_deque.popleft()
arg_deque.append(left)
arg_deque.appendleft("Zack")


#datetime structures
from datetime import datetime, timezone, timedelta

print(datetime.now())
print(datetime.now(timezone.utc))
#utc gives a margin of error object to offset time

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1) #weeks, seconds, etc.
print(today)
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M:%S'))

user_date = input('Enter the date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')
print(user_date)


#identify runtime in programs
import time

def measure_runtime(func):
  start = time.time()
  func()
  end = time.time()
  print(end - start)

def powers(limit):
  return[x**2 for x in range(limit)]

measure_runtime(lambda: powers(5000000))

#performs the timing function together on one text line
import timeit
print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))
"""
#Regular Expressions are a language not programming lang
#Regex is a matter of seeing patterns between regular expressions
"""
Four important components
- anything: letters, numbers, symbols
+ "one or more of"
* "zero or more of"
? "zero or one of"

#Regex expressions in python
#Must import re for regex operations
import re

email = 'abhinavkolli@gmail.com'
expression = '[a-z]+'

matches = re.findall(expression, email)
print(matches)
name = matches[0]
domain = f'{matches[1]}.{matches[2]}'
print(name)
print(domain)

import re
price = 'Price: $18,953.50'
expression = 'Price: \$([0-9,]*\.[0-9]*)'

matches = re.search(expression, price)
print(matches.group(0)) #entire match
print(matches.group(1)) #first thing in brackets

price_without_comma = matches.group(1).replace(',', '')
price_number = float(price_without_comma)
print(price_number)
"""
"""
#logging functions
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]:%(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)

logger = logging.getLogger('books')

logger.info('This will not show up.')
logger.warning('This will.')
logger.debug('This is a debug message.')
logger.critical('A critical error occurred.')


DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

#Higher order functions

def greet():
  print("Hello")

def before_and_after(func):
  print("Before...")
  func()
  print("After...")

before_and_after(greet)
