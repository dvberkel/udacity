import re

def sumnums(sentence):
    regexp = r"[0-9]+"
    numbers = re.findall(regexp, sentence)
    
    total = 0
    for number in numbers:
        total = total + int(number)
    
    return total
