import cv2

def draw_social_distancing(frame, boxes, statuses, risky_pairs):
    color_map = {
        "safe": (0, 255, 0),
        "low_risk": (0, 255, 255),
        "high_risk": (0, 0, 255)
    }

    for idx, (x1, y1, x2, y2) in enumerate(boxes):
        cv2.rectangle(frame, (x1, y1), (x2, y2), color_map[statuses[idx]], 2)

    for (i, j) in risky_pairs:
        pt1 = ((boxes[i][0]+boxes[i][2])//2, (boxes[i][1]+boxes[i][3])//2)
        pt2 = ((boxes[j][0]+boxes[j][2])//2, (boxes[j][1]+boxes[j][3])//2)
        cv2.line(frame, pt1, pt2, (0, 0, 255), 2)

    return frame
