def capitalize_string(string):
    return string.upper()
def capitalize_words(string):
    return ' '.join(word.capitalize() for word in string.split())