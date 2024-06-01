import os
os.system("cls")

# FIZZ BUZZ

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

#fizzbuzz()

# ANAGRAMA

def anagram(wordOne, wordTwo):
    if wordOne.lower() == wordTwo.lower():
        return False
    return sorted(wordOne.lower()) == sorted(wordTwo.lower())

print(anagram("amor", "roma"))

# FIBONACCI

def fibonacci():
    
    prev = 0
    next = 1

    for i in range(0,51):
        print(f"{i}: {prev}")

        fib = prev + next
        prev = next
        next = fib

# fibonacci()

# PRIMO

def primo():
    
    for numero in range(1,101):
        if numero >= 2: 
            divisible = False    
            for i in range(2, numero):
                if numero % i == 0:
                    divisible = True
                    break
            if not divisible:
                print(numero)

#primo()

