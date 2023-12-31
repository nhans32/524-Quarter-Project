from spamassassin_client import SpamAssassin
from sklearn import metrics
import nltk

def run_sa(inputs, sa_lvl=3): # sa_lvl defined as 3 because problem model doesnt consider headers
    predictions = []
    actual = []
    records_corr_pred = []
    scores = []

    for idx, (text, label) in enumerate(inputs):
        try:
            sa = SpamAssassin(bytes(text, 'utf-8'))
            score = sa.get_score()
            pred = 1 if score > sa_lvl else 0

            predictions.append(pred)
            actual.append(label)
            scores.append(score)

            if pred == label:
                records_corr_pred.append((text, label))

            print(f"{idx+1}/{len(inputs)}", end=' ')
        except:
            continue
    print("\n")

    return predictions, actual, records_corr_pred, scores


def evaluate(inputs, sa_lvl=3):
    predictions, actual, records_corr_pred, scores = run_sa(inputs, sa_lvl)
    print(metrics.classification_report(actual, predictions))
    print(metrics.confusion_matrix(actual, predictions))
    return records_corr_pred, predictions, scores