import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

def find_similar_patterns(X, y, top_k=30):
    """
    Find historical patterns similar to the most recent pattern.
    """
    current_pattern = X[-1].reshape(1, -1)
    historical_patterns = X[:-1].reshape(X.shape[0] - 1, -1)

    distances = euclidean_distances(current_pattern, historical_patterns)[0]

    similar_indices = np.argsort(distances)[:top_k]

    similar_outcomes = y[similar_indices]

    return similar_outcomes, similar_indices
