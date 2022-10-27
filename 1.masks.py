
class MailMask:
    def __init__(self, mail, mask_symbol):
        self.mail = mail
        self.mask_symbol = mask_symbol
    
    def mask(self):
        string = ''

        for i in range(len(self.mail)):
            if self.mail[i] != '@':
                string += self.mail[i]
            else:
                break

        return self.mail.replace(string, self.mask_symbol * len(string))

obj_1 = MailMask('mood_123@mail.ru', 'x')
print(obj_1.mask())



class PhoneNumberMask:
    def __init__(self, number, mask_symbol, symbols_count = -3):

        self.number = number
        self.mask_symbol = mask_symbol
        self.symbols_count = symbols_count

    def mask(self):
        string = ''   
        valid_number = self.number

        # Убираем лишние пробелы
        valid_number = " ".join(self.number.split())  

        # Маскируем необходимую часть
        for i in valid_number[self.symbols_count::]:       
            string += i
        result = valid_number[:self.symbols_count:] + valid_number[self.symbols_count::].replace(string, self.mask_symbol * len(string))

        # Замена пробелов по индексу(для номера любой страны)
        result = list(result)                            
        for j in range(len(valid_number)):           
            if valid_number[j] == ' ':
                result[j] = ' '
                
        result = ''.join(result)
        return result


obj_2 = PhoneNumberMask('+7 911   033    023', 'x')
print(obj_2.mask())


class SkypeMask:

    def __init__(self, string):
        self.string = string

    def mask(self):
        index_1 = self.string.find(':')
        index_2 = self.string.find('?')

        if index_2 == -1:
            index_2 = None

        nickname = self.string[index_1 + 1 : index_2]
        self.string = self.string.replace(nickname, "x" * 3)
        return self.string
        

obj_3 = SkypeMask('href=\"skype:ale2123x.max?call\">skype</a>"')
print(obj_3.mask())