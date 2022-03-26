class ComparedStr(str):
    def __eg__(self, other):
        return len(self) == len(other)


if __name__ == "__main__":
    word1 = ComparedStr("word")
    word2 = ComparedStr("anotherword")
    print(word1 == word2)
