import numpy as np

def calculate_social_distancing(points, threshold=100):
    risky_pairs = []
    statuses = []

    for i, pt1 in enumerate(points):
        status = "safe"
        for j, pt2 in enumerate(points):
            if i != j:
                dist = np.linalg.norm(np.array(pt1) - np.array(pt2))
                if dist < threshold:
                    risky_pairs.append((i, j))
                    if dist < threshold / 2:
                        status = "high_risk"
                    elif status != "high_risk":
                        status = "low_risk"
        statuses.append(status)
    return risky_pairs, statuses
