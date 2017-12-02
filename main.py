import scipy
from trains import train_except
from test import test
from metric import get_f_measure


confusion_matrix = scipy.array([[0, 0], [0, 0]])
for test_fold in range(1, 11):
    print('Номер тестовой выборки: ' + str(test_fold))
    p_spam, p_ham, p_spam_words_dict, p_ham_words_dict = train_except(test_fold)

    confusion_matrix_at_this_step = test(test_fold, p_spam, p_ham, p_spam_words_dict, p_ham_words_dict)
    confusion_matrix = confusion_matrix + confusion_matrix_at_this_step
    # print(confusion_matrix)

f_measure = get_f_measure(confusion_matrix)
print(confusion_matrix)
print("F-мера = " + str(f_measure))
