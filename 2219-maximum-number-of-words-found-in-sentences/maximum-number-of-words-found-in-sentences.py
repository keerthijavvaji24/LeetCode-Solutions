class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = 0

        for sentence in sentences:
            print(sentence)
            count = 1
            for ch in sentence:
                if ch == " ":
                    count += 1

            maximum = max(maximum, count)

        return maximum