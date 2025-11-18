# ros2_yolov5_depth_detection
A ROS 2 Humble project for real-time object detection using YOLOv5 and depth estimation using Intel RealSense D435i.

This project uses Intel RealSense D435i camera to detect the name of various objcets and their distance / depth from the camera sensor. It has predefined classes for the objcets and has scope to focus on just any object for example if only person or just the vehicle has to be detected and could give the distance of the required object. 

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
