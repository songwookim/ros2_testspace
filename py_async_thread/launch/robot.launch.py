from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_async_thread',
            executable='sim',
            name='simulation'
        ),
        Node(
            package='py_async_thread',
            executable='real',
            name='robot'
        ),
        Node(
            package='py_async_thread',
            executable='sensor',
            name='listener_node'
        ),
    ])
