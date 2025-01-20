import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import asyncio

class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')

        # Service 서버 생성
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.handle_add_two_ints)

        # 반복 작업 실행
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self.repetitive_task())

    def handle_add_two_ints(self, request, response):
        # Service 요청 처리
        self.get_logger().info(f'Received request: {request.a} + {request.b}')
        response.sum = request.a + request.b
        return response

    async def repetitive_task(self):
        while rclpy.ok():
            # 반복적으로 수행할 작업
            self.get_logger().info('Performing repetitive task...')
            await asyncio.sleep(1)  # 1초 간격으로 작업 실행

def main():
    rclpy.init()

    # 노드 생성 및 실행
    node = MyNode()
    executor = rclpy.executors.SingleThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
