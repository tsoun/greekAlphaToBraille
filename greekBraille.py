capitalAccent = {'Ά': 'Α', 'Έ': 'Ε', 'Ό': 'Ο', 'Ύ': 'Υ', 'Ί': 'Ι', 'Ή': 'Η'}
lowerAccent = {'ά': 'α', 'έ': 'ε', 'ό': 'ο', 'ύ': 'υ', 'ί': 'ι', 'ή': 'η'}


class text:
    def __init__(self, lexicon):
        self.greekAlpha = []
        self.greekBraille = []
        self.lexicon = lexicon

    def read(self):
        self.greekAlpha = input()

    def transcribe(self):
        for letter in self.greekAlpha:
            try:  # TODO: EVERYTHING
                self.greekBraille.append(self.lexicon[letter])
            except:
                if letter in capitalAccent:
                    self.greekBraille.append(
                        self.lexicon["CAPITAL"]+self.lexicon[capitalAccent[letter].lower()]+self.lexicon['΄'])
                else:
                    if letter in lowerAccent:
                        self.greekBraille.append(
                            self.lexicon['΄']+self.lexicon[lowerAccent[letter]])
                    else:
                        if letter.isupper():
                            try:
                                self.greekBraille.append(
                                    self.lexicon["CAPITAL"]+self.lexicon[letter.lower()])
                            except:
                                pass
                        else:
                            self.greekBraille.append(letter)
        self.greekBraille = "".join(self.greekBraille)
        self.greekAlpha = "".join(self.greekAlpha)

    def printLexicon(self):
        print(self.lexicon)


def main():
    lexicon = readLexicon()
    TEXT = text(lexicon)
    TEXT.read()
    TEXT.transcribe()
    print(TEXT.greekBraille)


def readLexicon():
    d = {}
    with open("lexicon.txt", encoding="utf-8") as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
    return d


if __name__ == "__main__":
    main()
