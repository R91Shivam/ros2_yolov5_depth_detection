import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge

import cv2
import numpy as np
import torch


class YOLOv5DepthNode(Node):
    def __init__(self):
        super().__init__('yolov5_depth_node')

        # Load YOLOv5 model
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

        self.bridge = CvBridge()

        # Depth scale for RealSense
        self.depth_scale = 0.0010000000474974513

        # Subscribers
        self.create_subscription(Image, '/camera/camera/color/image_raw', self.color_callback, 10)
        self.create_subscription(Image, '/camera/camera/depth/image_rect_raw', self.depth_callback, 10)

        # Publisher (class + distance)
        self.distance_pub = self.create_publisher(String, '/detected_object_distance', 10)

        # Buffers
        self.color_image = None
        self.depth_image = None

        self.get_logger().info("YOLOv5 Depth Node started. Waiting for frames...")


    def color_callback(self, msg):
        self.color_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        self.process_frames()


    def depth_callback(self, msg):
        self.depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')


    def process_frames(self):
        if self.color_image is None or self.depth_image is None:
            return

        color_img = self.color_image.copy()
        depth_img = self.depth_image.copy() * self.depth_scale

        # YOLO inference
        results = self.model(color_img)

        for det in results.xyxy[0]:
            x1, y1, x2, y2, conf, cls_id = det

            # Extract class name
            class_name = self.model.names[int(cls_id)]

            # Depth ROI
            depth_roi = depth_img[int(y1):int(y2), int(x1):int(x2)]
            if depth_roi.size == 0:
                continue

            object_depth = float(np.median(depth_roi))

            # Visualize
            label = f"{class_name}: {object_depth:.2f}m"
            cv2.rectangle(color_img, (int(x1), int(y1)), (int(x2), int(y2)), (252, 119, 30), 2)
            cv2.putText(color_img, label, (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (252, 119, 30), 2)

            # Create and publish message
            msg = String()
            msg.data = f"{class_name}: {object_depth:.2f} m"
            self.distance_pub.publish(msg)

            self.get_logger().info(f"Published: {msg.data}")

        cv2.imshow("YOLOv5 Depth Detection", color_img)
        cv2.waitKey(1)



def main(args=None):
    rclpy.init(args=args)
    node = YOLOv5DepthNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

