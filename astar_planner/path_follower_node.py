import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path  # Assuming the A* node publishes a Path message

class PathFollower(Node):
    def __init__(self):
        super().__init__('path_follower')
        self.pose_pub = self.create_publisher(PoseStamped, '/robot_pose', 10)
        self.path_sub = self.create_subscription(Path, '/astar_path', self.path_callback, 10)
        self.path = []
        self.timer = None
        self.current_pose_index = 0

    def path_callback(self, msg):
        # Update the path with the received data
        self.path = [[pose.pose.position.x, pose.pose.position.y] for pose in msg.poses]
        self.current_pose_index = 0
        # Ensure timer is reset for new path
        if self.timer is not None:
            self.timer.cancel()
        self.timer = self.create_timer(1.0, self.publish_pose)

    def publish_pose(self):
        if self.current_pose_index < len(self.path):
            pose_msg = PoseStamped()
            pose_msg.header.stamp = self.get_clock().now().to_msg()
            pose_msg.header.frame_id = 'map'
            pose_msg.pose.position.x = self.path[self.current_pose_index][0]
            pose_msg.pose.position.y = self.path[self.current_pose_index][1]
            pose_msg.pose.orientation.w = 1.0  # Assuming no orientation change for simplicity
            self.pose_pub.publish(pose_msg)
            self.current_pose_index += 1
        else:
            if self.timer is not None:
                self.timer.cancel()  # Stop the timer when the end of the path is reached

def main(args=None):
    rclpy.init(args=args)
    node = PathFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
