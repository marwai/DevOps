class Fizzbuzz:
    def fizzbuzz():
        # In a given range of 1 to 100
        for fz in range(1,101):
            # if there a is a number that is divisible by 3 and 5 it prints fizzbuzz
            if fz % 3 == 0 and fz % 5 == 0:
                print("fizzbuzz")
                continue
             # divisible by 3 produces fizz
            elif fz % 3 == 0:
                print("fizz")
                continue
            # divisible by 5 produces buzz
            elif fz % 5 == 0:
                print("buzz")
                continue
            print(fz)
# recalls instance of the class
Fizzbuzz.fizzbuzz()
