#  the program in main is built to show the over all accuracy of the classifier.
from Accuracy_Verification import class_accuracy
from Save_Load import save_assessment
test_classes = ['alt.atheism',
           'comp.graphics',
           'comp.os.ms-windows.misc',
           'comp.sys.ibm.pc.hardware',
           'comp.sys.mac.hardware',
           'comp.windows.x',
           'misc.forsale',
           'rec.autos',
           'rec.motorcycles',
           'rec.sport.baseball',
           'rec.sport.hockey',
           'sci.crypt',
           'sci.electronics',
           'sci.med',
           'sci.space',
           'soc.religion.christian',
           'talk.politics.guns',
           'talk.politics.mideast',
           'talk.politics.misc',
           'talk.religion.misc', ]

overall_assessment = ''
ct = 0
for cls in test_classes:
    ct += 1
    print(f"processing the test samples of {cls}")
    process = f"{ct} / 20"
    assessment = class_accuracy(cls)
    overall_assessment += assessment

save_assessment(overall_assessment, 'test_assessment')


