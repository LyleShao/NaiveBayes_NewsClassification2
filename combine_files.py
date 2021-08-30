import os
import os.path


def combine_class_articles(articles_path):

    sum_file = ""

    for file in os.listdir(articles_path):
        opened_file = open(os.path.join(articles_path, file), encoding='ISO-8859-1')
        opened_file_content = opened_file.read()
        sum_file = sum_file + opened_file_content

    return sum_file



