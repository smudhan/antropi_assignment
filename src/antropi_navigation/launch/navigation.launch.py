from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare('turtlebot3_navigation2'),
                    'launch',
                    'navigation2.launch.py'
                ])
            ),
            launch_arguments={
                'map': '/home/smudhan/antropi_ws/src/antropi_navigation/maps/map1/map.yaml',
                'use_sim_time': 'True',
                'slam': 'False',
            }.items()
        )
    ])