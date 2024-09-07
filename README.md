
# Python Basics Outline for OOP Class

## Lesson 1: Introduction to Programming
- *Class Objective*: Understand basic programming concepts.
- *Topics*:
  - What is programming?
  - Python installation & setup.
  - Writing your first Python program: "Hello, World!"
  - Basic syntax: variables, data types (integers, strings, floats, booleans).
  - Printing output.

### Problem Statement
Create a program that stores a person’s information (name, age, height, gender) and prints it out in a formatted manner.

**Sample output:**
```python
Person's Information
------------------------
Name: John Doe
Age: 20 years
Height: 5.5 ft
Is Male: False/True
```

---

## Lesson 2: Control Structures
- *Class Objective*: Learn how to control the flow of a program.
- *Topics*:
  - Conditional statements (if, else, elif).
  - Logical operators (and, or, not).
  - Loops: for and while.
  - Practice: Writing a simple program with conditions and loops.

### Problem Statement
Write a program that takes a user's age and checks if they are eligible to vote (age ≥ 18). If not, print how many years are left until they can vote. Also, print a countdown from the current age to zero.

**Sample output:**
```python
Enter your age: 16
You are not eligible to vote.
You will be eligible in 2 years.
Countdown from your age:
16, 15, 14, ..., 0
```

---

## Lesson 3: Functions and Code Organization
- *Class Objective*: Understand how to organize code into reusable blocks.
- *Topics*:
  - Defining functions (def).
  - Function parameters and return values.
  - Practice: Write a function to calculate basic operations (addition, subtraction, etc.).
  - Scope of variables (local vs global).

### Problem Statement
Create a function that accepts two numbers and an operator (e.g., +, -, *, /) and performs the corresponding operation. The program should print the result of the operation.

**Sample output:**
```python
Enter first number: 5
Enter second number: 3
Choose operation (+, -, *, /): *
Result: 5 * 3 = 15
```

---

## Lesson 4: Lists and Dictionaries
- *Class Objective*: Learn how to work with collections of data.
- *Topics*:
  - Lists: creating, modifying, and accessing elements.
  - Dictionaries: key-value pairs, accessing values.
  - Iterating through lists and dictionaries.
  - Practice: Program to store and manage simple data (e.g., a contact list).

### Problem Statement
Create a program that stores the names and ages of 5 people in a dictionary. The program should then print out the names of the people who are above 18 years old.

**Sample output:**
```python
People: {'Alice': 22, 'Bob': 17, 'Charlie': 25, 'Diana': 16, 'Eve': 19}
Adults: ['Alice', 'Charlie', 'Eve']
```

---

## Lesson 5: Basic File Handling
- *Class Objective*: Learn how to read from and write to files.
- *Topics*:
  - Opening files: open(), reading, writing, and closing files.
  - Exception handling with try, except.
  - Practice: Writing a program that saves data to a file and reads from it.

### Problem Statement
Create a program that asks the user for their favorite movie and saves it to a file called `favorites.txt`. Then, read the file and display the list of favorite movies.

**Sample output:**
```python
Enter your favorite movie: Inception
Movie saved!

Reading from file:
Favorite movies:
- Inception
```

---

## Lesson 6: Introduction to Object-Oriented Programming (OOP)
- *Class Objective*: Transition into the basics of OOP.
- *Topics*:
  - What is OOP?
  - Classes and objects.
  - Defining a simple class with attributes and methods.
  - Practice: Create a basic class (e.g., a Car class with attributes like make and methods like start()).

### Problem Statement
Create a `Car` class with attributes like `make`, `model`, and `year`. Include a method to `start` the car that prints out "The [year] [make] [model] is starting."

**Sample output:**
```python
my_car = Car('Toyota', 'Corolla', 2022)
my_car.start()

# Output:
The 2022 Toyota Corolla is starting.
```

---

## Lesson 7: Wrap-Up and Mini Project
- *Class Objective*: Reinforce learning with a project.
- *Topics*:
  - Combine the previous concepts to create a small project (e.g., a simple shopping cart or inventory management system).
  - Focus on applying control structures, functions, and basic OOP concepts.

### Problem Statement
Create a program that simulates a simple shopping cart. The program should allow users to:
1. Add items to the cart (item name, price).
2. Display all items in the cart.
3. Calculate the total price of items in the cart.

**Sample output:**
```python
Item added: Apple ($1.50)
Item added: Bread ($2.00)

Cart:
- Apple: $1.50
- Bread: $2.00

Total price: $3.50
```
