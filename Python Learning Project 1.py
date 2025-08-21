'''This is an ever-growing project, and will be added to over time...

Duke Valenzuela[Python Learning Project 1.py](https://github.com/user-attachments/files/21927193/Python.Learning.Project.1.py)
Links to the YouTube Videos Credited / Referenced in Order:

Hackingtons Code School : https://www.youtube.com/watch?v=m8DXAsyaMK0&pp=ygUXaGFja2luZ3RvbnMgQ29kZSBTY2hvb2w%3D
Abhijay Potluri : https://www.youtube.com/watch?v=SEc0khTZ4e4&list=PLVJIaQIN1-U7R3uJ16FP6xKWFEc6uZRee
Tech With Tim : https://www.youtube.com/watch?v=qqp6QN20CpE&pp=ygUUdGVjaCB3aXRoIHRpbSBweXRob24%3D
'''


"""This Follows Along With The First Video"""

"""This is a Joke / Riddle Machine that pulls Values contained in Variables... You can try it out by changing the Values of the Variables to anything that you want... :)"""

#-----------------------Strings and Variables-----------------------

#-----------------------First, Greet the User-----------------------

print("Welcome to the joke program! ")
print()

#-----------------------Second, Store an Animal Input as a Variable-----------------------

animal_1 = input("Name an animal: ")
print()

#-----------------------Third, Print Their Answer and Change Their Mind-----------------------

print("Did you say", animal_1, "...??? Those things are silly... You're also silly, and apparently your face is silly as well... And since we're on the subject of your late mother, like her late husband, we'll just settle for a cow instead...")
print()

#-----------------------Fourth, Ask Them a Question-----------------------

joke_response_1 = input("What do you call a cow with no legs? ")
print()

#-----------------------Now, Print the Joke-----------------------

print("No, not a", joke_response_1, "You call it, ground beef...!!! ")
print()

#-----------------------Let's Ask Them if They Want to Try Another Joke-----------------------

print("Would you like to try a go at another joke...??? ")
print()

#-----------------------We'll Store Another Animal Input as a Variable-----------------------

animal_2 = input("Name another animal: ")
print()

#-----------------------We'll Print Their Answer and Change Their Mind Again-----------------------

print("Why on earth would you choose", animal_2, "...??? Let's just use a chicken instead... ")
print()

#-----------------------Now We Ask Them Another Question-----------------------

joke_response_2 = input("What do you call a chicken with a bazooka...??? ")
print()

#-----------------------Print the Joke-----------------------

print("No, You call it whatever it wants you to call it...!!! ")
print()

print("You're obviously here to prove yourself, once more, as the official village idiot... The correct answer obviously was not", joke_response_2, "so let's give it another go, shall we...??? ")
print()

body_part = input("Name a body part. ")
print("You chose", body_part, "...??? Do you have some kind of", body_part, "fettish we should know about...??? Everyday it's", body_part ,"this, and", body_part, "that... let's tell a joke about eyes instead...!!! ")
print()

joke_3 = input("What do you call a cat with no eyes, but who happens to also be holding a bazooka...??? This is a very dangerous farm by the way... ")
print()

print("No, not a", joke_3, "not even close...!!! You call it whatever it wants you to call it...!!!")
print()

print("Change of pace...!!!")
print()

subject = input("Choose a subject in school that you absolutely love. ")
print()

print("You chose", subject, ", A typical response from a basic bitch like you... Not my favourite, so let's tell a joke about science instead...!!! ")
print()

joke_3 = input ("What do you call a science techer outside of class? ")
print()

print("No, not", joke_3, "You call it a, yo Tontrell, that tweaker bitch out there tryin to steal your ten speed again, muh nizzle...!!! ")
print()

#-----------------------Riddle Machine-----------------------

#-----------------------First, Greet the User-----------------------

print("That all appears to check out, so let's switch gears again here... Would you like to hear a riddle this time...??? ")
print()

#-----------------------Store Their Response Input as a Variable-----------------------

response_1 = input("Yes or No? ")
print()

#-----------------------Print Their Answer and Change Their Mind-----------------------

print("Well, despite a response of", response_1, " I'm gonna tell you a riddle anyway.")
print()

#-----------------------Ask the User a Riddle-----------------------

response_2 = input("What has neither sides, nor corners...??? ")
print()

#-----------------------Print the Answer-----------------------

print("No, it's not", response_2, "It's a ball, you silly goose...!!! ")
print()

#-----------------------Ask Them if They Want to Try Another Riddle-----------------------

print("Would you like to try another riddle...??? ")
print()

#-----------------------Store Another Response Input as a Variable-----------------------

response_3 = input("Yes or No? ")
print()

#-----------------------Print Their Answer and Change Their Mind Again-----------------------

print("Well, again, piss off with your answer of", response_1, "I'm gonna tell you another riddle anyway... You're just going to sit there, and continue making faces apparently... ")
print()

#-----------------------Ask Them Another Riddle-----------------------

response_3 = input("What did theDetective Plonkers say before heading out the door...??? ")
print()

#-----------------------Print the Answer-----------------------

print("No, it's not", response_3, "It's a very well known fact that she indeed did say, Ya'll can just eat a biscuit...!!! This was of course followed by an enthusiastic applause, a graceful bow from the cast, credits, and then cut...!!!")

print()
exit()
'''
#--------------------------------------------------------------------------------------------

#-----------------------This is Where the Multi-Part YouTube Tutorial Begins:

#-----------------------Printing Types of Variables-----------------------
'''
s1 = 'hello'
s2 = "hello"
print(type(s1))
print(type(s2))
s3 = """hello
my name is (name)...!!! """
print(s3)

#-----------------------Casting Floats into Integers-----------------------

x = 4 #Int
y = 10.9 #Float
print(x)
print(y)
print(type(x))
print(type(y))
x1 = float(x)
y1 = int(y)
print(x1)
print(y1)
print(type(x1))
print(type(y1))


#-----------------------Casting From a String Into a Number-----------------------

v = "8" 
print(type(v))
y = int(v)
print(type(y))

#-----------------------Booleans-----------------------

v = 10 == 10
print(v)
print( 11 < 6)
'''

#--------------------------------------------------------------------------------------------

#-----------------------Collection Data Types------------------------------------------------
#
#-----------------------Lists, Tuples, Sets, Dictionary--------------------------------------

#-----------------------Lists-----------------------

#--------------------------------------------------------------------------------------------
'''
"""list of fruits"""

apple
banana
orange
pear
grapes

#-----------------------Remember: Indexes always have square brackets-----------------------

fruits = ["apples", "bananas", "oranges", "pears", "grapes",]

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

 # "Anything".pop Removes the Specified Indexed Value... In this case (fruits.pop(3) would be removing "pears" from the list because it holds the third or [3] value... Idk, I couldn't get it to work or whatever... Maybe you can... I was using Visual Studio Code for all of this silliness, but I'll also try and run it through PyCharm and Replit and see if the .pop thing works in one of those...

"""fruits.pop(3)"""

"""Tuples"""

Ordered
Duplicates
Unchangeable

#These are almost like an Ordered List, in that they are both Ordered and can have Duplicates, however they are Unchangeable, so once they're assigned to an Indexed Location Value, that Value remains the same forever...

fruits = ("Apple", "Pears")

"""Sets"""

No_Duplicates_Allowed
Unchangeable
Unordered

#These only share a commonality with Ordered Tuples in that they are both Unchangeable...

fruits = {"Apples", "Pears"} 

#Remember: Another use of "Apples" or "Pears" Cannot be added to this List because an Ordered Set Does Not allow for Duplicates...!!!

"""Dictionary"""
'''
Collection_Data_Types_That_Go_By_Keyed_Value_Pairs

_____    :    ______  
key    pair   value

Changeable
Ordered
No_Duplicates_Allowed

fruit_colours = {}

"apple   :    red"      #---Notice the "Quotes" Being Open and Closed---
   V      V      V
  Key    Pair  Value

fruit_colours = {}
"apple:red","orange:orange","grape:purple"
'''

#Lists
#
#--------------------------------------------------------------------------------------------
Fruits = ["Apple", "Pears", "Mango"]
print(Fruits)
print(Fruits[0])
print(Fruits[1])
print(Fruits[2])
print(Fruits)
Fruits.append("Pears")

#---You'll notice that using the ".append" will move the word "Pears" to the end of the list...---

print(Fruits)

#---Tuple---
#
#--------------------------------------------------------------------------------------------

Fruits = ("Apple", "Pears", "Mango", "Apple")
print(Fruits)
print(Fruits[2])

#---Set---
#
#--------------------------------------------------------------------------------------------

Fruits = {"Apple", "Pears", "Mango"}
print(Fruits)

#Using the run button here will print the Sets in different (Unorganised or Non Specific) orders each time because #Sets are Unordered...

#Also: Duplicates will be ignored because Sets do not recognise them...
#Fruits = {"Apple", "Pears", "Mango", "Apples"}
#
#The word "Apples" will not show up twice when the program is ran because duplicates are ignored... 


#Dictionary
#
#--------------------------------------------------------------------------------------------

Fruit_Colours = {
"Banana":"Yellow",
"Apple":"Red",
"Pears":"Green"
}
print(Fruit_Colours)

#For a specific value you can use something like: print(Fruit_Colours["Apple"]) to get the colour for just Apple in #this case...

print(Fruit_Colours["Apple"])

#Also: Libraries function much like Sets in the fact that they completely Ignore Duplicates...
'''

#--------------------------------------------------------------------------------------------

'''
"""Conditionals"""

#if
#elif
#else

num1 = int(input("enter a number "))
num2 = int(input("enter another number "))

#==, !=, <, <=, >, >=, and, or, not
if num1 > num2 :
        if num1 > 10:   #-------------------------Use Tab to Nest If Statements-------------------------          
                print(f"{num1} is greater than ten")             
        print(f"{num1} is greater than {num2}")          
elif num1 < num2:
        print(f"{num1} is less than {num2}")
else :
        print(f"{num1} is equal to {num2}")

#Another example

if num1 > num2 and num1 > 5:  #-------The "and" can be switched out for "or" as well as "not"------
        print("Success")
else: 
    print("Fail")

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------

"""from random import *"""

print("""*********************************************
Welcome to my Rock, Paper Scissors Game...!!! 
Have Fun...!!!"

      Here are the Rules:
      There are 3 options Rock, Paper, Scissors

      Rock beats Scissors
      Scissors beats Paper
      Paper beats Rock
      Or, The Computer Just Wins Because It Says So...!!!
      **********************************************""")

options = ["Rock", "Paper", "Scissors"]
user_choice = input("What is your choice...??? Rock, Paper or Scissors...???    :")
computer_choice = choice(options)
print("Computer Choice Is: " , computer_choice)

if (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Scissors" and computer_choice == "Paper") or (user_choice == "Paper" and computer_choice == "Rock") :
        print("You Win...!!!")

elif (user_choice == "Rock" and computer_choice == "Rock") or (user_choice == "Paper" and computer_choice == "Paper") or (user_choice == "Scissors" and computer_choice == "Scissors") :
        print("You Tied...!!!")

else:
        print("You Lose...!!!")
print()
print()
print()
exit()
'''
#-------------------------------------------------------------------------------------------
#At this point in the set of tutorial videos, you'll be directed to https://trinket.io
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#If you want, we can skip that let's just make a ChatBot instead...
#-------------------------------------------------------------------------------------------

"""from random import *"""

'''

print("""Welcome to the Legendary Fun ChatBot
      My Name is Marlo the Magnificent
      Type 1 if you want to ask a Yes or No Question
      Type 2 if you want to Hear a Joke
      Type 3 if you want to Know Your Fortune""")
print()

list1 = ["YES", "NO"]
jokes_list = ["What did the fish say when he swam into the wall: DAM...!!!", "What do you call a cow with no legs: Go Back to the Beginning of This Tutorial for the Answer...!!!"]
fortune_list = ["You Have a Relatively Low Chance at Ever Winning at Bingo...!!!", "You're Probably Not Going to Discover Time Travel...!!!"]

user_choice = input()

if user_choice == "1":
    input("Type Your Question and Press Enter : ")
    print("Marlo Says :", choice(list1))

if user_choice == "2":
    print(choice(jokes_list))

if user_choice == "3":
    print("Marlo's prediction of your Fortune Today : " ,choice(fortune_list))

if user_choice > "3":
    print("It's an Easy Choice, Even For Someone Like Yourself... 1, 2, or 3")

exit()
'''
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

#----------------Dunder (Double UnderLined) / Magic Methods in Python---------------

'''
class Counter:
        def __init__(self):
                self.value = 1

        def count_up(self):
                self.value += 1
        
        def count_down(self):
                self.value -= 1

        def __str__(self):
                return f"Count={self.value}"

        def __add__(self, other):
                if isinstance(other, Counter):
                        return self.value + other.value
                raise Exception("Invalid Type")

count1 = Counter()
count2 = Counter()

count1.count_up()
count2.count_up()

print(count1, count2)
print(count1 + count2)

class Car:
        def __init__(self, make, model, year):
                self.make = make
                self.model = model
                self.year = year
        
        # __str__ is used for user-friendly output

        def __str__(self):
                return f"{self.year} {self.year} {self.model}"
        
        # __repr__ is meant for a more detailed, unambiguous output

        def __repr__(self):
                return f"Car(make ='{self.make}', model='{self.model}', year='{self.year})"


#Create an Instance of the Car Class

my_car = Car('Toyota', 'Corolla', 2021)

#Example Usage

print(str(my_car))       # User-Friendly Output: Toyota Corolla
print(rpr(my_car))       # Developer-Friendly Output: Car(make='Toyota', model='Corolla', year=2021)  



class InventoryItem:
    """A class to demonstrate operator overloading for inventory management"""
    
def __init__(self, name, quantity):
                self.name = name
                self.quantity = quantity

def __repr__(self):
                return f"Inventory Item(name='{self.name}', Quantity='{self.quantity})"
    


        #------------------Arithmetic Operators------------------

def __add__(self, other):
                if isinstance(other, InventoryItem) and self.name == other.name:
                      return InventoryItem(self.name, self.quantity + other.quantity)
                raise ValueError("Cannot add Items of Different Types... ")
        
def __sub__(self, other):
                if isinstance(other, InventoryItem) and self.name == other.name:
                        if self.quantity >= other.quantity:                  
                                return InventoryItem(self.name, self.quantity - other.name)
                raise ValueError("Cannot Subtract more than the available quantity... ")
raise ValueError("Cannot Subtract Items of Different Types... ")
        
def __mul__(self, factor):
                if isinstance(factor, (int, float)):
                      return InventoryItem(self.name, int(self.quantity * factor))
                raise ValueError("Multiplication Factor Must be a Number... ")

def __truediv__(self, other):
                if isinstance(factor, (int, float)):
                        return InventoryItem(self.name, int(self.quantity / factor))
                raise ValueError("Division Factor Must be a Non-Zero Number... ")

#------------------Comparison Operators------------------

def __eq__(self, other):
               if isinstance(other, InventoryItem):
                      return self.name == other.name and self.quantity == other.quantity
               return False
        
def __lt__(self, other):
                if isinstance(other, InventoryItem):
                       return self.quantity < other.quantity
                raise ValueError("Cannot Compare Items of Different Types... ")
    
def __gt__ (self, other):
                if isinstance(other, InventoryItem):
                       return self.quantity > other.quantity
                raise ValueError("Cannot Compare Items of Different Types... ")
    
#------------------Create Some Inventory Items------------------

item1 = InventoryItem("Apple", 50)
item2 = InventoryItem("Apple", 30)
item3 = InventoryItem("Orange", 20)

#------------------Adding Quantities of the Same Item------------------

result_add = item1 + item2
print(result_add) # Output: InventoryItem(name='Apple', quantity=80)

#------------------Subtracting Quantities of the Same Item------------------

result_subtract = item1 - item2
print(result_subtract) # Output: InventoryItem(name='Apple', quantity=20)

#------------------Multiplying Item Quantities by a Factor------------------

result_mul = item1 * item2
print(result_mul) # Output: InventoryItem(name='Apple", quantity=100)

#------------------Comparing item Quantities------------------

print(item1 > item2) # Output: True
print(item1 == InventoryItem("Apple", 50)) # Output:True

#------------------Trying to Add Items of Different Types------------------

try:
       result_invalid = item1 + item3
except ValueError as e:
       print(e) # Output: Cannot Add Items of Different Types

#------------------Trying to Subtract More Than Available Quantity------------------

try:
       result_invalid = item2 - item1
except ValueError as e:
       print(e) # Output: Cannot Subtract More Than the Available Quantity------------------

class LinkedList:
    
        def __init__(self):
                self.head = None
                self.size = 0 

        def __len__(self):
                """Define Bahavour of Len()."""
                return self.size
        
        def __getitem__(self, index):
                """Enable Indexing (obj[index])."""
                if index < 0 or index >= self.size:
                        raise IndexError("Index Out of Range")
                current = self.head 
                for _ in range(index):
                        current = current.next
                return current.value

        def __setitem__(self, index, value):
                """Enable Item Assignment (obj[index] = value)."""
                if index < 0 or index >= self.size:
                        raise IndexError("Index Out of Range")
                current = self.head
                for _ in range(index):
                        current = current.next
                current.value = value

        def __delitem__(self, index):
                """Delete an Item (del obj[index])."""
                if index < 0 or index >= self.size:
                        raise IndexError("Index Out of Range")
                if index == 0:
                        self.head = self.head.next
                else:
                        current = self.head
                        for _ in range(index - 1):
                                current = current.next
                        current.next = current.next.next
                self.size -= 1

        def __contains__(self, value):
                """Define Behavour for 'in' Keyword"""
                current = self.head
                while current:
                        if current.value == value:
                                return True
                        current = current.next
                return False
        
        def append(self, value):
                """Add a New Node to the End of the List."""
                new_node = Node(value)
                if not self.head:
                        self.head = new_node
                else: 
                        current = self.head
                        while current.next:
                                current = current.next
                        current.next = new_node
                self.size += 1

        def __str__(self):
                """User-Friendly String Representation."""
                values = []
                current = self.heaf
                while current:
                        values.append(str(current.value))
                        current = current.next
                return " -> ".join(values)
        
        #------------------Example Usage------------------

        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        print(len(ll))  # Output: 3
        print(ll[1])  # Output: 20
        ll[1] = 25
        print(ll)  # Output: 10 -> 25 -> 30
        del ll[1]
        print(ll)  # Output: 10 -> 30
        print(30 in ll)  # Output: True
                        
#------------------DataBase Connection Example------------------

class DatabaseConnection:

        """Simulate a Database Connection with Context Management."""

        def __inti__(self, db_name):
                self.db_name = db_name
                self.connected = False

        def __enter__(self):
                """Establish the Connection."""
                self.connected = True
                print(f"Connected to the Database '{self.db_name}'.")
                return self

        def __exit__    (self, exc_type, exc_value, traceback):
                """Close the Connection"""
                self.connected = False
                print(f"Disconnected From the Database '{self.db_name}'.")
                

#------------------Handle Any Exceptions------------------

                if exc_type:
                        print(f"An Exception Occurred: {exc_value}")
                return True  #  Suppresses Exceptions if They Occur

with DatabaseConnection("ExampleDB") as db:
        print(f"Are you Connected...??? {db.connected}")

class Countdown:
        """A Simple Iterator That Counts Down From a Given Number."""
        def __init__(self, start):
                self.current = start

        def __iter__(self):
                """Returns the Iterator Object Itself."""
                return self

        def __next__(self):
                """Returns The Next Value In The Countdown."""
                if self.current > 0:
                        value = self.current
                        set.current -= 1
                        return value
                else: 
                        raise StopIteration
                
for number in Countdown(5):
        print(number)

# __iter__(CountDown(5)) -> CountDown(5)
# __next__(CountDown(5)) -> 5
# __next__(CountDown(5)) -> 4
# __next__(CountDown(5)) -> 3
# __next__(CountDown(5)) -> raise StopIteration
