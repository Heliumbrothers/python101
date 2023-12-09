import re
class txt:
    def __init__(self) -> None:
        pass

    current_index = 0
        
    def convert_type(self, filename):
        output = []
        with open(filename, "r") as filename:
            if re.search(('int[') or ('str['), filename):
                check = False
                object = str()
            if re.search('list[', filename):
                object = []
                while filename[self.current_index] != ']':
                    if filename[self.current_index] != '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9': 
                        check = True
                    object += filename[self.current_index]
                    self.current_index += 1
                if check == False:
                    int(object)
                    output.append(object)
                else:
                    output.append()
                if re.search('dict[', filename):
                    object = {}
                    while filename[self.current_index] != ']':
                        if filename[self.current_index] + filename[self.current_index] == 'k:':
                            value = None
                            while filename[self.current_index] != ':':
                                value += str(filename(self.current_index))
                                if filename[self.current_index] + filename[self.current_index] == 'k:':
                                    value = None
                                    while filename[self.current_index] != ':':
                                        value += str(filename(self.current_index))
                

text = txt()