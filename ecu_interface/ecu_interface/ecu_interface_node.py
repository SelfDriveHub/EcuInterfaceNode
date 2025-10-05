import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from std_msgs.msg import String


class EcuInterface(Node):

    def __init__(self):
        super().__init__('ecu_interface')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    try:
        ecu_interface = EcuInterface()
        rclpy.spin(ecu_interface)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        ecu_interface.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()