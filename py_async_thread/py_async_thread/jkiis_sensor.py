import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Int32, 'topic', 10)
        timer_period = 0.0001     # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.time = 0

    def timer_callback(self):
        msg = Int32()
        self.time += 1
        msg.data = self.time
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

 
def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # node 삭제
    # (옵션 - 안해주면 garbage collector에 의해 알아서 진행된다.
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()