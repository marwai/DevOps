class Fizzbuzz:
    def fizzbuzz():
        for fz in range(1,101):
            if fz % 3 == 0 and fz % 5 == 0:
                print("fizzbuzz")
                continue
            elif fz % 3 == 0:
                print("fizz")
                continue
            elif fz % 5 == 0:
                print("buzz")
                continue
            print(fz)

Fizzbuzz.fizzbuzz()
