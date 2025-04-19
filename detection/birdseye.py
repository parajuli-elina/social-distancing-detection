import cv2
import numpy as np

class BirdEyeTransformer:
    def __init__(self, src_points):
        dst_points = np.float32([
            [0, 0],
            [400, 0],
            [400, 400],
            [0, 400]
        ])
        self.matrix = cv2.getPerspectiveTransform(np.float32(src_points), dst_points)

    def transform_points(self, points):
        points_array = np.array(points, dtype='float32').reshape(-1, 1, 2)
        transformed = cv2.perspectiveTransform(points_array, self.matrix)
        return [tuple(pt[0]) for pt in transformed]
