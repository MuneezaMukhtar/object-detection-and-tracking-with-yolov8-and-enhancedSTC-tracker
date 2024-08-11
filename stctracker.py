import cv2
import numpy as np

class EnhancedSTCTracker:
    def __init__(self, frame, bbox):
        x, y, w, h = bbox
        self.bbox = (x, y, w, h)
        self.template = frame[y:y+h, x:x+w]
        self.method = cv2.TM_CCOEFF_NORMED
        self.threshold = 0.5  # Confidence threshold for reinitializing the tracker
        self.scale_factors = [0.9, 1.0, 1.1]  # Different scales for multi-scale matching

    def update(self, frame):
        best_val = -1
        best_bbox = self.bbox

        for scale in self.scale_factors:
            resized_template = cv2.resize(self.template, (0, 0), fx=scale, fy=scale)
            result = cv2.matchTemplate(frame, resized_template, self.method)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            if max_val > best_val:
                best_val = max_val
                x, y = max_loc
                w, h = int(resized_template.shape[1] / scale), int(resized_template.shape[0] / scale)
                best_bbox = (x, y, w, h)

        if best_val < self.threshold:
            return False, self.bbox

        self.bbox = best_bbox
        x, y, w, h = self.bbox
        self.template = frame[y:y+h, x:x+w]

        return True, self.bbox

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read the first frame.")
        exit()

    bbox = cv2.selectROI(frame, False)
    tracker = EnhancedSTCTracker(frame, bbox)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        success, bbox = tracker.update(frame)
        if success:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            # Try to reinitialize the tracker with a new ROI
            new_bbox = cv2.selectROI(frame, False)
            tracker = EnhancedSTCTracker(frame, new_bbox)

        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
