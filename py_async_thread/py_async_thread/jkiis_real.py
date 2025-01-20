import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from std_msgs.msg import String
import threading
import time
from std_msgs.msg import Int32

class ClientNode(Node):
    def __init__(self):
        super().__init__('client_node')

        # 토픽 구독
        self.subscription = self.create_subscription(
            Int32,
            'topic',
            self.listener_callback,
            10
        )

        # 서비스 클라이언트 생성
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        self.sensor_data = 0
        # 타이머로 주기적으로 서비스 요청
        self.timer = self.create_timer(0.0001, self.send_service_request)

    def listener_callback(self, msg):
        """토픽 메시지 수신 콜백"""
        self.sensor_data = msg.data
        self.get_logger().info(f'Sensor :  {msg.data}')

    def send_service_request(self):
        """비동기적으로 서비스 요청"""
        if not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Service not available, waiting...')
            return

        # 요청 생성 및 전송
        request = AddTwoInts.Request()
        request.a = self.sensor_data
        request.b = 0
        # self.get_logger().info('Sending service request: 2 + 3')

        future = self.client.call_async(request)
        future.add_done_callback(self.handle_service_response)

    def handle_service_response(self, future):
        """서비스 응답 처리 콜백"""
        try:
            response = future.result()
            self.get_logger().info(f'Service response: {response.sum}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {str(e)}')

def main():
    rclpy.init()
    node = ClientNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
