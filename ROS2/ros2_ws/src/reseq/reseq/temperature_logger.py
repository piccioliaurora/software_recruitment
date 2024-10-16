import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from datetime import datetime

class TemperatureLogger(Node):
    def __init__(self, log_file: str):
        super().__init__('temperature_logger')
        self.log_file = log_file
        self.subscription = self.create_subscription(
            Float32,
            'temperature',  # Nome del topic dal quale si ascolta
            self.callback,
            10)
        self.subscription  # prevent unused variable warning

    def callback(self, msg: Float32):
        temperature = msg.data
        if temperature >= 50.0:
            # Logga la temperatura e il timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.log_file, 'a') as f:
                f.write(f'{timestamp} - Temperature: {temperature}\n')
            self.get_logger().info(f'Logged: {timestamp} - Temperature: {temperature}')

def main(args=None):
    rclpy.init(args=args)
    logger = TemperatureLogger("log.txt")  # Nome del file di log
    rclpy.spin(logger)
    logger.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
