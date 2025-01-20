import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import threading
import time

class ServerNode(Node):
    def __init__(self):
        super().__init__('server_node')

        # 서비스 서버 생성
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.handle_add_two_ints)
        self.timestamp = 0
        # 반복 작업 실행
        self.thread = threading.Thread(target=self.repetitive_task, daemon=True)
        self.thread.start()

    def handle_add_two_ints(self, request, response):
        """서비스 요청 처리"""
        # self.get_logger().info(f'Received request: {request.a} + {request.b}')
        response.sum = self.timestamp
        return response

    def repetitive_task(self):
        """반복적으로 실행되는 작업"""
        while rclpy.ok():
            self.timestamp += 1
            self.get_logger().info(f'self.timestamp : {self.timestamp}')
            

def main():
    rclpy.init()
    node = ServerNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
