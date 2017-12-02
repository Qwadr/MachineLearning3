from file_parser import take_model


def train_except(number_of_test_fold):
    ham_words_frequency_dict, spam_words_frequency_dict, ham_mail_count, spam_mail_count \
        = take_model(number_of_test_fold)

    # считаем вероятности появления спамовых/нормальных писем
    p_spam = spam_mail_count / (spam_mail_count + ham_mail_count)
    p_ham = ham_mail_count / (spam_mail_count + ham_mail_count)

    p_spam_words_dict = {}
    p_ham_words_dict = {}

    # составляем dict априорных вероятностей слов в спаме
    for key in spam_words_frequency_dict.keys():
        word_spam_probability = spam_words_frequency_dict.get(key) / sum(spam_words_frequency_dict.values())
        p_spam_words_dict.setdefault(key, word_spam_probability)

    # составляем dict априорных вероятностей слов в неспаме
    for key in ham_words_frequency_dict.keys():
        word_ham_probability = ham_words_frequency_dict.get(key) / sum(ham_words_frequency_dict.values())
        p_ham_words_dict.setdefault(key, word_ham_probability)

    # print("p_spam: " + str(p_spam))
    # print("p_ham: " + str(p_ham))

    return p_spam, p_ham, p_spam_words_dict, p_ham_words_dict


# train_except(1)
