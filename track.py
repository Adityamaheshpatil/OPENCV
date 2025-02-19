import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

ret, frame = cap.read()
bbox = cv.selectROI('select', frame, False)

x, y, w, h = bbox

roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)),
                  np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

# Initialize video writer
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

track_points = []
prev_frame = None
alert_area = ((50, 50), (300, 300))  # Define alert area

while True:
    ret, frame = cap.read()

    if ret:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        ret, track_window = cv.meanShift(dst, bbox, term_crit)

        x, y, w, h = track_window
        img2 = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 2)

        # Add label to the tracked object
        cv.putText(img2, 'Object', (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Record the position of the tracked object
        track_points.append((x + w // 2, y + h // 2))

        # Draw the trajectory
        for i in range(1, len(track_points)):
            cv.line(img2, track_points[i - 1], track_points[i], (0, 255, 0), 2)

        # Show additional information
        fps = cap.get(cv.CAP_PROP_FPS)
        cv.putText(img2, f'FPS: {int(fps)}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        cv.putText(img2, f'Position: ({x}, {y})', (10, 60), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        # Draw alert area
        cv.rectangle(img2, alert_area[0], alert_area[1], (0, 0, 255), 2)

        # Check if object is within alert area
        if alert_area[0][0] < x < alert_area[1][0] and alert_area[0][1] < y < alert_area[1][1]:
            cv.putText(img2, 'ALERT!', (50, 90), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Motion detection
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (21, 21), 0)
        if prev_frame is None:
            prev_frame = gray
            continue

        frame_delta = cv.absdiff(prev_frame, gray)
        thresh = cv.threshold(frame_delta, 25, 255, cv.THRESH_BINARY)[1]
        thresh = cv.dilate(thresh, None, iterations=2)
        contours, _ = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            if cv.contourArea(contour) < 500:
                continue
            (mx, my, mw, mh) = cv.boundingRect(contour)
            cv.rectangle(img2, (mx, my), (mx+mw, my+mh), (0, 255, 0), 2)
        
        prev_frame = gray

        
        cv.putText(img2, 'REAL TIME OBJECT TRACKING', (10, 470), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        cv.imshow('Tracking', img2)

        
        out.write(img2)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
