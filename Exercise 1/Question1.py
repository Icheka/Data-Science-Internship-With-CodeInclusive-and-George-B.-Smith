'''
Question 1: Write a program that accepts a comma-separated list sequence of words as
input and prints the words in a comma-separated sequence after sorting them alphabetically
'''

class Alph:
    def clean(self, word):
        return word.strip()


    def alph(self, array):
        words = sorted(array)
        new_words = []
        for word in words:
            new_words.append(self.clean(word))

        return new_words

    def main(self):
        words = input(">>> Enter a comma-separated list of words to sort: ")
        print("=========")
        words = words.split(",")
        print(self.alph(words))
        input("Enter to exit...")
    

alph = Alph()
alph.main()
