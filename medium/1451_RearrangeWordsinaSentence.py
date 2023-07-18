class Solution:
    def arrangeWords(self, text: str) -> str:
        wordLen = 0
        word = ''
        wordLenArray = []
        wordArray = []

        textLen = 0
        for i in text:
            # print(i)
            textLen += 1
            if textLen == 1:
                i = chr(ord(i)+32)
            if i == ' ':
                wordLenArray.append(wordLen)
                wordArray.append(word)
                word = ''
                wordLen = 0
                continue
            word += i
            wordLen += 1
        
        wordLenArray.append(wordLen)
        wordArray.append(word)

        wordLenMin = 100000
        wordLenMaxPosition = 0
        newSentence = ''
        while wordArray:
            n = 0
            wordLenMin = 100000
            # print(wordArray)
            for i in wordLenArray:
                # print('  ', i)
                if i<wordLenMin:
                    # print('    ', 'here')
                    wordLenMin = i
                    wordLenMaxPosition = n
                n += 1
            if newSentence == '':
                shift = -32
            else:
                shift = 0
            newSentence += chr(ord(wordArray[wordLenMaxPosition][0])+shift)
            newSentence += wordArray[wordLenMaxPosition][1:]
            newSentence += ' '
            wordLenArray.pop(wordLenMaxPosition)
            wordArray.pop(wordLenMaxPosition)

        return newSentence[:-1]
                
            

# sol = Solution()
test = 'This is test so fucking happy'
# res = sol.arrangeWords(test)
# print(res)
