from remove_punctuation import remove_punctuation as rmp
from combine_files import combine_class_articles
from remove_stopwords import remove_stopwords


class CountFrequency:

    def __init__(self, path):
        self.path = path
        self.data_removed_punctuation = ''
        self.words = ''
        self.output_list = ''
        self.broken_data = ''

    def catch_data(self):

        raw_data = combine_class_articles(self.path)
        self.data_removed_punctuation = rmp(raw_data)

    def break_data(self):

        if self.data_removed_punctuation is not None:
            self.broken_data = self.data_removed_punctuation.lower().split()
            self.broken_data = remove_stopwords(self.broken_data)
            return self.broken_data
        else:
            return None

    def frequency_counter(self):
        class_prob = []
        self.output_list = set(self.broken_data)
        for processing_word in self.output_list:
            count = 0
            for each_word in self.broken_data:
                if each_word == processing_word:
                    count += 1
            new_dict = {'Word': processing_word, 'Frequency': count}
            class_prob.append(new_dict)
        return class_prob


def adjust_frequency(give_list):
    frequency = give_list
    for index in frequency:
        index['Frequency'] = 20000 * index['Frequency'] / len(frequency)
    return frequency

#  since we want to calculate the sum of log of frequencies, we need firstly divide the
#  frequency by the length of the words list, to balance the negative affect due to the difference
#  of total words number.
