from remove_punctuation import remove_punctuation as rmp
import json
from remove_stopwords import remove_stopwords
import math


class GetProb:

    def __init__(self, text, class_name):
        self.text = text
        self.class_name = class_name
        self.sample = []
        self.category_lib = []

    def load(self):
        direction = 'trained_model/'
        filename = direction + self.class_name + '_model.json'
        with open(filename) as json_file:
            self.category_lib = json.load(json_file)

    def catch(self):
        raw = open(self.text, encoding='ISO-8859-1')
        raw = rmp(raw.read())
        raw = raw.lower().split()
        raw = remove_stopwords(raw)
        self.sample = raw
        return self.sample

    def get_prob(self):
        e = math.e
        prob = 0
        for word in self.sample:
            for index in self.category_lib:
                if word == index['Word']:
                    prob += math.log(index['Frequency'], e)
        return prob


def calculate_prob(text, category):
    y = GetProb(text, category)
    y.load()
    y.catch()
    outcome = y.get_prob()
    return outcome


def maximum_likelihood(give_list):
    max_prob = 0
    max_likelihood = ''
    for index in give_list:
        if index['Prob'] >= max_prob:
            max_prob = index['Prob']
            max_likelihood = index['Class']
    return max_likelihood


def classify(text):
    outcome_list = []
    catalog = ['alt_atheism', 'comp_graphics', 'comp_os_ms_windows-misc',
               'comp_sys_ibm_pc_hardware', 'comp_sys_mac_hardware', 'comp_windows_x',
               'misc_forsale', 'rec_autos', 'rec_motorcycles', 'rec_sport_baseball',
               'rec_sport_hockey', 'sci_crypt', 'sci_electronics', 'sci_med', 'sci_space',
               'soc_religion_christian', 'talk_politics_guns', 'talk_politics_mideast',
               'talk_politics_misc', 'talk_religion_misc']
    for name in catalog:
        directory = name
        probability = calculate_prob(text, directory)
        post_prob = {'Class': name, 'Prob': probability}
        outcome_list.append(post_prob)
    outcome = maximum_likelihood(outcome_list)
    return outcome


#  removing the '#' to classify a single text
#  x = classify('data_test/comp.sys.ibm.pc.hardware/comp_sys_ibm_pc_hardware00533')
#  z = classify('data_test/sci.electronics/sci_electronics00506')
#  print(x)
#  print(z)



