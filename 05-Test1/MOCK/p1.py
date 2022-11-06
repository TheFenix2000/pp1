def f(card_number):
    result = card_number[:2]
    result+="*"*10
    result+=card_number[-4:]
    return result
