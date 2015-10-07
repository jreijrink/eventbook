
def getTokensFromText(text):
    tokens = list()
    
    text_items = text.split(" ")
    for text_item in text_items:
        tokens.append(text_item)
    return tokens

def getTokensFromList(textList):
    tokens = list()
    for text in textList:
        tokens.append(text)            
    return tokens