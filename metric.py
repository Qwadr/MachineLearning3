def get_f_measure(confusion_matrix):
    tp = confusion_matrix[0][0]
    fn = confusion_matrix[0][1]
    fp = confusion_matrix[1][0]
    tn = confusion_matrix[1][1]

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    f_measure = 2 * precision * recall / (precision + recall)
    return f_measure
