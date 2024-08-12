## Object-Detection-and-Tracking-With-Yolov8-And-EnhancedSTC-Tracker
Object detection and tracking is a crucial aspect of many computer vision applications, where you need to identify and monitor objects in real-time. Integrating YOLOv8 for object detection with the Enhanced Spatio-Temporal Context (EnhancedSTC) tracker is a powerful approach to achieve this. This model is utilized to predict the object's location in the next frame, based on the context in the current frame.
# System Requirements
  
   - **Python Version:** Python 3.8 or later
   - **Libraries:** OpenCV, PyTorch, Ultralytics YOLOv8, and EnhancedSTC tracker library

# Create a Virtual Environment
   - **Why Use a Virtual Environment?**
     Creating a virtual environment helps isolate project dependencies, ensuring that your project runs smoothly without conflicts.
   - **Steps to Create a Virtual Environment:**
     ```bash
     python -m venv yolov8-enhancedstc-env
     source yolov8-enhancedstc-env/bin/activate  # On Windows: yolov8-enhancedstc-env\Scripts\activate
     ```

# Install Required Libraries
   - **Install YOLOv8 and Other Dependencies:**
     ```bash
     pip install ultralytics opencv-python torch torchvision
     ```
   - **Install EnhancedSTC Tracker (if available):**
     - You may need to install the EnhancedSTC tracker from a specific GitHub repository or custom implementation.
     - Example (assuming a custom GitHub repository):
       ```bash
       git clone https://github.com/username/EnhancedSTC.git
       cd EnhancedSTC
       python setup.py install
       ```
# Project Structure
   - **Organizing Your Project Files:**
     ```
     yolov8-enhancedstc/
     ├── yolov8-enhancedstc-env/  # Virtual environment folder
     ├── data/                    # Folder for your dataset
     │   ├── images/
     │   └── labels/
     ├── scripts/                 # Folder for scripts
     │   └── detect_and_track.py  # Main script for detection and tracking
     └── models/                  # Folder for trained models
     ```

# Project Setup
   - **Clone the YOLOv8 and EnhancedSTC Repositories (if needed):**
     ```bash
     git clone https://github.com/ultralytics/yolov8.git
     cd yolov8
     ```
   - **Download Pre-trained YOLOv8 Weights:**
     ```bash
     wget https://path/to/yolov8-weights.pt
     ```
   - **Prepare Your Dataset:**
     - Place your dataset in the `data/images/` folder.
     - Label your dataset using LabelImg (detailed below).

# Using LabelImg to Label Your Dataset
   - **Install LabelImg:**
     ```bash
     pip install labelImg
     ```
   - **Launch LabelImg:**
     ```bash
     labelImg
     ```
   - **Load Your Dataset:**
     - Open the `data/images/` folder in LabelImg.
   - **Label Objects in Images:**
     - Draw bounding boxes around objects and assign class labels.

# Label Images
   - **Creating Bounding Boxes:**
     - Use the annotation tool in LabelImg to draw bounding boxes around objects in each image.
   - **Assigning Class Labels:**
     - Assign the appropriate class label to each bounding box (e.g., "person," "car").
   - **Save Annotations:**
     - Save the annotations in YOLO format (`.txt` files) in the `data/labels/` folder.

# Implement Object Detection and Tracking with YOLOv8 and EnhancedSTC Tracker
   - **Step 1: Initialize YOLOv8 Model**
     - Load the pre-trained YOLOv8 model and prepare it for object detection.
   - **Step 2: Capture Video Stream**
     - Use OpenCV to capture the video stream or load a video file.
   - **Step 3: Perform Object Detection**
     - Pass each frame through the YOLOv8 model to detect objects.
   - **Step 4: Initialize EnhancedSTC Trackers**
     - For each detected object, initialize an EnhancedSTC tracker with the detected bounding box.
   - **Step 5: Update Trackers Frame-by-Frame**
     - As you process each frame, update the position of each object using the EnhancedSTC tracker.

# Running the Detection and Tracking System
   - **Execute the Main Script:**
     - Run the script that performs detection and tracking, ensuring that all dependencies are correctly installed and configured.
   - **Monitor Output:**
     - View the real-time tracking results, where objects are detected, labeled, and tracked across frames.

# Conclusion
   - **Integrating YOLOv8 with EnhancedSTC:**
     - Combining YOLOv8's detection capabilities with the EnhancedSTC tracker's robust tracking provides a powerful solution for real-time object tracking.
   - **Future Enhancements:**
     - Consider optimizing the system for specific use cases, improving accuracy, and reducing processing time by fine-tuning both detection and tracking parameters.
