class WordsFinder:
    trans_table = str.maketrans['.!,:;=?', '    ']


    def __init__(self, *file_names: str):
        self.file_names = file_names


    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name) as file:
                line = file.read()
                line = line.lower() \
                    .replace(' - ', ' ') \
                    .translate(self.trans_table)
                line = ' '.join(line.split())
                all_words[file_name] = line.split()
        return all_words

    def find(self, search_word: str):
        search_word = search_word.lower()
        found_words = {}
        for file_name, words in self.get_all_words().items():
            found = False
            for i in range(len(words)):
                if words[i] == search_word:
                    found = True
                    break
            if found:
                found_words[file_name] = i + 1
        return found_words


    def count(self, search_word, str):
        search_word = search_word.lower()
        word_number = {}
        for file_name, words in self.get_all_words().items():
            word_number[file_name] = words.count(search_word)
        return word_number

if __name__ == '__main__':
    finder2 = WordsFinder('test_file.tet')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))