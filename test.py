import scipy
import numpy
import os
import math
import file_parser


def test(test_fold, p_spam, p_ham, p_spam_words_dict, p_ham_words_dict):
    matrix = scipy.array([[0, 0], [0, 0]])
    folder = 'D:\\Учеба\\4 курс\Интеллектуальные системы и технологии\\3 лаба\\pu1\\part' + str(test_fold)

    for filename in os.listdir(folder):
        # блок читки, Кирилл, не ругайся
        f = open(os.path.abspath(folder) + '\\' + filename)
        # print(os.path.abspath(folder) + '\\' + filename)
        data = f.read()

        # это частотник слов в новом письме
        mail_word_dict = file_parser.get_frequency_dict_from_mail(data)

        # считаем первичные вероятности (логарифмы вероятностей) того, что письмо спамовое или нет
        log_p_mail_spam = get_log_p_mail_spam(mail_word_dict, p_spam, p_spam_words_dict)
        log_p_mail_ham = get_log_p_mail_ham(mail_word_dict, p_ham, p_ham_words_dict)

        # считаем нормированную вероятность того, что письмо спамовое
        # p_spam_mail = log_p_mail_spam / (log_p_mail_spam + log_p_mail_ham)
        # is_spam_mail = p_spam_mail > 0.5

        spam_percentage = 1 / (1 + numpy.exp(log_p_mail_ham - log_p_mail_spam))
        is_spam_mail = spam_percentage > 0.5

        # true positive (мы удачно нашли спамовое письмо)
        if is_spam_mail and filename.find('spmsg') > 0:
            matrix[0][0] += 1

        # false negative (мы отметили спамовое письмо как нормальное)
        if not is_spam_mail and filename.find('spmsg') > 0:
            matrix[0][1] += 1

        # false positive (мы отметили нормальное письмо как спамовое)
        if is_spam_mail and filename.find('legit') > 0:
            matrix[1][0] += 1

        # true negative (мы отметили нормальное письмо как нормальное)
        if not is_spam_mail and filename.find('legit') > 0:
            matrix[1][1] += 1

    return matrix


# TODO: тут может вылетать из-за обращения к ключу в виде строки числом или наоборот
def get_log_p_mail_spam(mail_word_dict, p_spam, p_spam_words_dict):
    coeff_blur = math.pow(10, -15)
    log_spam_probability = math.log(p_spam)
    for key in mail_word_dict.keys():
        # именно здесь мы не учитываем слова, которых не видели раньше вообще
        # if p_spam_words_dict.get(key, 0) != 0:
            # суммируем логарифм вероятности появления столько раз, сколько встретилось слово в письме
        log_spam_probability += (mail_word_dict.get(key)) * math.log(p_spam_words_dict.get(key, 0) + coeff_blur)
    return log_spam_probability


def get_log_p_mail_ham(mail_word_dict, p_ham, p_ham_words_dict):
    coeff_blur = math.pow(10, -15)
    log_ham_probability = math.log(p_ham)
    for key in mail_word_dict.keys():
        # именно здесь мы не учитываем слова, которых не видели раньше вообще,
        # if p_ham_words_dict.get(key, 0) != 0:
            # суммируем логарифм вероятности появления столько раз, сколько встретилось слово в письме
        log_ham_probability += (mail_word_dict.get(key)) * math.log(p_ham_words_dict.get(key, 0) + coeff_blur)
    return log_ham_probability
