punctuations = '''=!|()-+[]{};:'"\,<>./?@#$%^&*_~1234567890'''


def remove_punctuation(with_punctuation):
    without_punctuation = ""
    for char in with_punctuation:
        if char not in punctuations:
            without_punctuation = without_punctuation + char
        else:
            char = " "
            without_punctuation = without_punctuation + char
    return without_punctuation


