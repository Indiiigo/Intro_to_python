class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def number_of_words(self):
        return len(self.words)

    def describe(self):
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Words {} can say {}'.format(self.name, ', '.join(self.words)))
        
# Example usage:
if __name__ == "__main__":
    parrot1 = Parrot("Polly", 5)
    parrot1.add_word("Hello")
    parrot1.add_word("Goodbye")
    parrot1.add_word("Polly wants a cracker")

    print(f"{parrot1.name} can say {parrot1.number_of_words()} words.")
    parrot1.describe()