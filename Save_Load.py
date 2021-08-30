import json


def save(file, path):
    doc = file
    direction = 'trained_model/'
    filename = direction + path + '_model.json'
    with open(filename, 'w') as f:
        json.dump(doc, f)


def save1(file, path):
    doc = file
    direction = 'test_datasets/'
    filename = direction + path
    with open(filename, 'w') as f:
        json.dump(doc, f)


def load(file):
    direction = 'trained_model/'
    filename = direction + file + '_model.json'
    with open(filename) as json_file:
        doc = json.load(json_file)
    return doc


def load1(file):
    direction = 'test_datasets/'
    filename = direction + file
    with open(filename) as json_file:
        doc = json.load(json_file)
    return doc


def save_assessment(file, name):
    direction = 'Assessment/' + name
    with open(direction, 'w') as f:
        json.dump(file, f)





