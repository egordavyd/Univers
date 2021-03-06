class Word:
    Words = 'abcdefghijklmnopqrstuvwxyz'
    Key =    '1234567890!@#$%^&*)(_+-=}['
    @classmethod
    def Encrypt(cls, text: str) -> str:
        '''Шифрует введенную строку'''
        Keys = ''
        for i in range(len(text)):
            k = cls.Words.find(text[i].lower())
            if k >= 0:
                Keys += cls.Key[k]
            else:
                Keys += text[i]
        return Keys   
    @classmethod         
    def Decrypt(cls, code: str) -> str:
        '''Расшифровывает введенный код'''
        text = ''
        for i in range(len(code)):
            k = cls.Key.find(code[i].lower())
            if k >= 0:
                text += cls.Words[k]
            else:
                text += code[i]
        return text       
print(Word.Encrypt('Hello'))
print(Word.Decrypt('85@@%'))



