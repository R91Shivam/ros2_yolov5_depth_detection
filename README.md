# ros2-yolov5-depth-detection
A ROS 2 Humble project for real-time object detection using YOLOv5 and depth estimation using Intel RealSense D455.

## The node subscribes to:
- /camera/color/image_raw
- /camera/depth/image_rect_raw

## And Publishes:
- Bounding boxes + Labels(OpenCV window)
- detected_object_info
    contains class name + distance in meters

## Features
✔ Real-time YOLOv5 detection
✔ Depth estimation using RealSense
✔ ROS 2 Humble Node
✔ Custom message: ObjectInfo.msg
✔ Publishes class name + distance
✔ Easy to extend for robotics / navigation projects


## Installation 

1. Clone the repository
    ```bash
    cd ~/ros2_ws/src
    git clone https://github.com/R91Shivam/ros2-yolov5-depth-detection.git
    ```
   
3. Install Python dependencies

   ```bash
   pip install -r requirements.txt
   ```
    
5. Build the ROS 2 package
   ```bash
   cd ~/ros2_ws
   colcon build --packages-select yolov5_depth_node
   source install/setup.bash
    ```

## Run the Node
1. Make sure RealSense is running (realsense2_camera):

       ros2 launch realsense2_camera rs_launch.py align_depth:=true

3. Then run:

       ros2 run yolov5_depth_node depth_node

5. Echo the published info:

       ros2 topic echo /detected_object_info

Author
---    
- Shivam Raichure
    
- Robotics Engineer | Autonomous Mobility | AI & Perception
