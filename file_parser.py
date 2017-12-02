import os
from utils import union_two_dict


def read_files_except(number_of_training_fold):
    all_ham_strings = []
    all_spam_strings = []

    spam_mail_count = 0
    ham_mail_count = 0

    os.chdir("D:\\Учеба\\4 курс\\Интеллектуальные системы и технологии\\3 лаба\\pu1\\")
    # print(os.listdir())
    for folder in os.listdir():
        if folder[4:] == str(number_of_training_fold):
            continue
        # print(str(folder) + ': ' + os.listdir(os.curdir + '/' + folder))
        # print(os.listdir(os.curdir + '/' + folder))
        # print(folder + ": ")
        # print(os.listdir(folder))
        for filename in os.listdir(folder):
            f = open(os.path.abspath(folder) + '\\' + filename)
            # print(os.path.abspath(folder) + '\\' + filename)
            data = f.read()
            if filename.find('legit') > 0:
                ham_mail_count += 1
                all_ham_strings.append(data)
            if filename.find('spmsg') > 0:
                spam_mail_count += 1
                all_spam_strings.append(data)

    return all_ham_strings, all_spam_strings, ham_mail_count, spam_mail_count


def parse_mail(mail):
    end_of_subj = mail.find('\n')
    subject = mail[:end_of_subj]
    body = mail[end_of_subj + 2:]

    return subject.strip(), body.strip()


def get_frequency_dict_from_mail(mail):
    frequency_dict = {}

    subject, body = parse_mail(mail)
    # TODO: вот здесь пока что все будет под одну гребёнку, но можно разделять заголовок и тело письма
    # TODO: дадим каждому слову в заголовке больший вес
    # subject = subject + ' ' + body

    for num in subject.split():
        if num.isdigit():
            frequency_dict.setdefault(int(num), 0)
            frequency_dict[int(num)] += 30

    for num in body.split():
        if num.isdigit():
            frequency_dict.setdefault(int(num), 0)
            frequency_dict[int(num)] += 1

    return frequency_dict


def generate_frequency_dict(emails):
    frequency_dicts = []
    for mail in emails:
        frequency_dict = get_frequency_dict_from_mail(mail)
        frequency_dicts += [frequency_dict]

    frequency_dict_final = {}
    for f_dict in frequency_dicts:
        frequency_dict_final = union_two_dict(frequency_dict_final, f_dict)

    return frequency_dict_final


def take_model(number_of_test_fold):
    all_ham_strings, all_spam_strings, ham_mail_count, spam_mail_count = read_files_except(number_of_test_fold)
    spam_words_frequency = generate_frequency_dict(all_spam_strings)
    ham_words_frequency = generate_frequency_dict(all_ham_strings)

    # print('ham_mail_count: ' + str(ham_mail_count))
    # print('spam_mail_count: ' + str(spam_mail_count))
    # print(spam_words_frequency.__len__())
    # print(ham_words_frequency.__len__())
    # print("ALL RIGHT")

    return ham_words_frequency, spam_words_frequency, ham_mail_count, spam_mail_count
