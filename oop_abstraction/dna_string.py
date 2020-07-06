# Method 1
class DNA:

    def dna_count():
        number = input("Enter your DNA sample here:\n")
        print("Adenine: " + str(number.count("A")),"\nCystosine: "+ str(number.count("C")),
              "\nGuanine: " + str(number.count("G")), "\nThymine: " + str(number.count("T")))


DNA.dna_count()
Result Adenine: 17 Cystosine: 11 Guanine: 16 Thymine: 21

# # Method 2
def DNA_two(dna_code):
    dict = {}  # Empty dictionary
    for n in dna_code:
        keys = dict.keys()  # initialising the keys in the dictionary
        if n in keys:
            dict[
                n] += 1  # If it finds the character in a string, it adds 1 to the tally of how many characters there are
        else:
            dict[
                n] = 1  # Everytime, there is a new character, it adds 1 and the process repeats. It continues to find more characters
    return dict

print(DNA_two("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))
