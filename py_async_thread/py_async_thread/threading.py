import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from example_interfaces.srv import AddTwoInts
import time
import threading

class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')

        # Service 서버 생성
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.handle_add_two_ints)

        # # 반복 작업을 실행할 스레드 시작
        # self.thread = threading.Thread(target=self.repetitive_task, daemon=True)
        # self.thread.start()
        self.time = 0
        

    def handle_add_two_ints(self, request, response):
        # Service 요청 처리
        self.get_logger().info(f'{self.time}:  Received request: {request.a} + {request.b}')
        response.sum = request.a + request.b
        return response

    def repetitive_task(self):
        while rclpy.ok():
            self.time +=1
            # 반복적으로 수행할 작업
            # self.get_logger().info('Performing repetitive task...')
            print(f"{self.time} hello!!")
            # time.sleep(1)  # 1초 간격으로 작업 실행

def main():
    rclpy.init()
    minimal_service = MyNode()
    print("minimal_service")
    try :
        # rclpy.spin(minimal_service)
        t1 = threading.Thread(target=rclpy.spin, args=(minimal_service,))
        t2 = threading.Thread(target=minimal_service.repetitive_task)
        t1.start()
        t2.start()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        rclpy.shutdown()
        t1.join()
        t2.join()
    # finally:
    #     minimal_service.destroy_node()
    # rclpy.shutdown()

if __name__ == '__main__':
    main()
