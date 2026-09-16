"""P5 QA personal submission fixture."""


def normalize_score(score):
    return score / 20


assert normalize_score(80) == 4
print("P5_QA_PERSONAL_20260914: OK")
