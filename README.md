# ros2_yolov5_depth_detection
A ROS 2 Humble project for real-time object detection using YOLOv5 and depth estimation using Intel RealSense D435i.

This project implements a real-time object detection and distance-measurement system using the Intel RealSense D435i depth camera. It integrates RGB image processing with depth sensing to identify predefined object classes and calculate their distance from the camera with high accuracy.

The system uses a trained object-detection model to recognize various object categories (e.g., people, vehicles, everyday items) and leverages the D435i’s depth stream to determine how far each detected object is from the sensor. In addition to general detection, the application includes a filtering feature that allows users to focus on specific object types—such as detecting only persons or only vehicles—reducing unnecessary processing and enabling targeted monitoring.

##Key functionalities include:
	•	Real-time object detection using the D435i RGB camera.
	•	Accurate depth measurement for each detected object using the camera’s built-in depth sensor.
	•	Configurable object-class filtering, enabling focused detection on selected categories.
	•	Visualization of detected objects, with labels and distance values overlaid on the video stream.
	•	Potential applications in robotics, surveillance, autonomous navigation, and smart-safety systems.

This project demonstrates strong skills in computer vision, sensor integration, and real-time data processing

## The node subscribes to:
- camera/camera/color/image_raw
- camera/camera/depth/image_rect_raw

## And Publishes:
- Bounding boxes + Labels(OpenCV window)
- detected_object_info
    contains class name + distance in meters

## Features
✔ Real-time YOLOv5 detection.
✔ Depth estimation using RealSense.
✔ ROS 2 Humble Node.
✔ Custom message: ObjectInfo.msg .
✔ Publishes class name + distance.
✔ Easy to extend for robotics / navigation projects.


## Installation 

1. Clone the repository
    ```bash
    cd ~/ros2_ws/src
    git clone https://github.com/R91Shivam/ros2_yolov5_depth_detection.git
    ```
   
3. Install Python dependencies

   ```bash
   pip install -r requirements.txt
   ```
    
5. Build the ROS 2 package
   ```bash
   cd ~/ros2_ws
   colcon build
   source install/setup.bash
    ```

## Run the Node
1. Make sure RealSense is running (realsense2_camera):

       ros2 run realsense2_camera realsense2_camera_node 

3. Then run:

       ros2 run yolov5_realsense yolov5_depth_node 


5. Echo the published info:

       ros2 topic echo /detected_object_info

Author
---    
- Shivam Raichure
    
- Robotics Engineer | Autonomous Mobility | AI & Perception
