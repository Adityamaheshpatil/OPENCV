# 🚀 **Real-Time Object Tracking & Motion Detection**

This project implements **real-time object tracking** using OpenCV’s **MeanShift algorithm** and integrates **motion detection** to identify frame changes. Additionally, an **alert system** notifies when the tracked object enters a defined region.

---

## 🎯 **Key Features**
✅ **Object Tracking** – Uses MeanShift for tracking based on color histograms.
✅ **Trajectory Mapping** – Draws the tracked object's movement path over time.
✅ **Motion Detection** – Detects motion by comparing frames and highlighting movement.
✅ **Alert System** – Raises an alert when the object enters a predefined area.
✅ **FPS Display** – Shows real-time frames per second.
✅ **Video Recording** – Saves the tracking output to an AVI file.

---

## ⚙️ **Installation & Setup**
### 📌 **1. Install Dependencies**
Ensure Python and OpenCV are installed. Run the following command:

```bash
pip install numpy opencv-python
```

### 📌 **2. Run the Script**
Save the script as `tracking.py` and execute it:

```bash
python tracking.py
```

---

## 🎬 **How It Works**
### 📍 **Step 1: Initialize the Camera**
- The script starts by capturing video from the webcam (`cv.VideoCapture(0)`).

### 📍 **Step 2: Select Object to Track**
- A window appears for manual selection of the object to track.

### 📍 **Step 3: Object Tracking**
- The MeanShift algorithm tracks the selected object using color histograms.
- The bounding box (`bbox`) updates in each frame.

### 📍 **Step 4: Motion Detection**
- Uses frame difference to detect moving objects.
- Draws bounding boxes around detected motion.

### 📍 **Step 5: Alert System**
- If the tracked object enters a predefined "alert area," a warning is displayed.

### 📍 **Step 6: Display & Save Output**
- The tracking window displays the object, trajectory, and motion.
- The output is saved as `output.avi`.

---

## ⏹️ **How to Stop the Program**
Press `Esc` (`27` in ASCII) to exit.

---

## 🔥 **Future Enhancements**
🚀 Implement **Kalman filter** for smoother tracking.
🚀 Add **multi-object tracking** support.
🚀 Improve **motion detection** to ignore minor movements.
🚀 Integrate **YOLO or OpenCV DNN** for better object tracking.

---

💡 *Want to contribute? Fork the repository and submit a PR!* 😃
