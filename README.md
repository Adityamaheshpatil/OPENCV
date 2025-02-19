# 🎯 REAL-TIME OBJECT TRACKING & MOTION DETECTION  

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)  
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=flat&logo=opencv)  
![Status](https://img.shields.io/badge/Status-Active-success?style=flat)

## 🚀 Introduction  
This project implements **real-time object tracking** and **motion detection** using **OpenCV** and **Python**.  
🔍 Select an object in a live webcam feed, and the program will track it using the **MeanShift** algorithm.  
🛑 Motion detection highlights movement in the scene and triggers an **ALERT** when the object enters a predefined zone.  

## ✨ Features  
✅ **Real-time Object Tracking** using **MeanShift Algorithm**  
✅ **Trajectory Visualization** – Draws the movement path of the object  
✅ **Motion Detection** – Highlights moving objects in the frame  
✅ **Alert System** – Notifies when the object enters a defined area  
✅ **Performance Metrics** – Displays **FPS** & object coordinates  
✅ **Video Recording** – Saves the tracked video as an `.avi` file  

## 🛠️ Dependencies  
Before running, install the required dependencies:  
```bash
pip install numpy opencv-python
📌 How to Run
1️⃣ Clone the repository
git clone https://github.com/your-username/realtime-object-tracking.git
cd realtime-object-tracking
2️⃣ Run the script
python tracking.py
3️⃣ Follow the on-screen instructions:


Select an object in the ROI selection window
The program will track and display the object's motion
Press ESC to exit the program
🖥️ Output Preview
🟢 Tracked object bounding box
🟢 Motion detection zones
🟢 Trajectory visualization
🟢 Live FPS & object position display
