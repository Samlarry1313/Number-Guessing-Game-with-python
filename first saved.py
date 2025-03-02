Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Higher or Lower
... def higher_lower():
...     print("Welcome to the Higher or Lower Game!")
... 
...     number_to_guess = random.randint(1, 100)
...     attempts = 0
... 
...     while True:
...         guess = int(input("Guess the number (between 1 and 100): "))
...         attempts += 1
... 
...         if guess < number_to_guess:
...             print("Higher!")
...         elif guess > number_to_guess:
...             print("Lower!")
...         else:
...             print(f"Congratulations! You guessed the number in {attempts} attempts.")
...             break
