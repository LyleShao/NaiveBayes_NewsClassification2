from Object_Prob import classify
import os
from remove_punctuation import remove_punctuation

test_folder = 'data_test/'
folders = ['alt.atheism/',
           'comp.graphics/',
           'comp.os.ms-windows.misc/',
           'comp.sys.ibm.pc.hardware/',
           'comp.sys.mac.hardware/',
           'comp.windows.x/',
           'misc.forsale/',
           'rec.autos/',
           'rec.motorcycles/',
           'rec.sport.baseball/',
           'rec.sport.hockey/',
           'sci.crypt/',
           'sci.electronics/',
           'sci.med/',
           'sci.space/',
           'soc.religion.christian/',
           'talk.politics.guns/',
           'talk.politics.mideast/',
           'talk.politics.misc/',
           'talk.religion.misc/', ]


def catch_file_name(directory):
    true_directory = test_folder + directory
    for root, dirs, files in os.walk(true_directory):
        return files


def class_accuracy(class_name):
    correct_amount = 0
    processed_amount = 0
    texts = catch_file_name(class_name)
    for text in texts:
        full_directory = test_folder + class_name + '/' + text
        outcome = classify(full_directory)
        j1 = remove_punctuation(outcome)
        j2 = remove_punctuation(class_name)
        if j1 == j2:
            correct_amount += 1
            processed_amount += 1
            rate = format(100 * float(correct_amount)/float(processed_amount), '.2f')
            print(f"Accuracy: {correct_amount}/{processed_amount}  rate: {rate}%")
        else:
            processed_amount += 1
            rate = format(100 * float(correct_amount) / float(processed_amount), '.2f')
            print(f"Accuracy: {correct_amount}/{processed_amount}  rate: {rate}%")

    assessment = f"{class_name} - finished! The accuracy is {correct_amount}/{processed_amount}  rate: {rate}"
    return assessment


class_accuracy('sci.space')
