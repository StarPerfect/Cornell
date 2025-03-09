letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
cipher = {letters[i]: letters[(i-3) % len(letters)] for i in range(len(letters))}


def transform_message(message, cipher):
    """Transforms (encodes or decodes) a message using a cipher dictionary.

    If a character is not mapped in the cipher, the encoded message will leave
    the character unchanged.

    Examples:
        transform_message('Hello', {'H':'I','l':'m'}) returns 'Iemmo'
        transform_message('Iemmo', {'I':'H','m':'l'}) returns 'Hello'
  
    Parameters:
        message: string to be transformed (encoded or decoded)
        cipher: dictionary that maps a single character to another character
    """
    tmsg = ""

    for c in message:
        if c in cipher.keys():
            tmsg += cipher.get(c)
        else:
            tmsg += c

    return tmsg

test = "I come to bury Caesar, not to praise him."
test_encoded = transform_message(test, cipher)

decoder = {v:k for k,v in cipher.items()}