import numpy as np

def cohens_kappa(r1, r2):

    r1 = np.array(r1)
    r2 = np.array(r2)

    if len(r1) != len(r2):
        raise ValueError("Length mismatch")

    labels = np.unique(np.concatenate([r1, r2]))
    k = len(labels)

    label_to_index = {label:i for i, label in enumerate(labels)}

    cm = np.zeros((k, k))

    for a, b in zip(r1, r2):
        cm[label_to_index[a], label_to_index[b]] += 1

    n = cm.sum()

    # observed agreement
    p0 = np.trace(cm) / n

    # expected agreement
    row_marginals = cm.sum(axis=1)
    col_marginals = cm.sum(axis=0)

    pe = np.sum(row_marginals * col_marginals) / (n*n)

    if pe == 1:
        return 1.0

    return (p0 - pe) / (1 - pe)