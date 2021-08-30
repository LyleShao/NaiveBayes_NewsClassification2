def remove_stopwords(raw):
    stopwords1 = ['i', 'you', 'we', 'it', 'not', 'yes', 'no', 'he', 'she', 'him', 'her', 'do', 'did', 'done', 'be',
                  'am']
    stopwords2 = ['are', 'were', 'was', 'have', 'has', 'had', 'too', 'also', 'both', 'always', 'same', 'can', 'cant']
    stopwords3 = ['could', 'would', 'might', 'may', 'sure', 'must', 'should', 'if', 'while', 'a']
    stopwords4 = ['get', 'gets', 'got', 'for', 'my', 'how', 'from', 'is', 'me', 'who', 'whom', 'what', 'which', 'of']
    stopwords5 = ['the', 'they', 'an', 'in', 'into', 'onto', 'now', 'this', 'that', 'whose', 'been', 'yet', 'as', 'ok']
    stopwords6 = ['re', 'tow', 'and', 'by', 'to', 't', 'here', 'and', 'on', 'out', 'there', 'their', 's', 'd']
    stopwords7 = ['like', 'com', 'cmu', 'edu', 'cs', 'hp', 'at', 'because', 'r', 'x', 'date', 'with', 'or', 'some',]
    stopwords8 = ['newsgroup', 'newsgroups']
    stopwords = stopwords1 + stopwords2 + stopwords3 + stopwords4 + stopwords5 + stopwords6 + stopwords7 + stopwords8

    for stop_word in stopwords:
        for word in raw:
            if stop_word == word:
                raw.remove(word)
    return raw



