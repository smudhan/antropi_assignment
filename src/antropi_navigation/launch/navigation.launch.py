from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    map_file = PathJoinSubstitution([
        FindPackageShare('antropi_navigation'),
        'maps',
        'map1',
        'map.yaml'
    ])

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
                'map': map_file,
                'use_sim_time': 'True',
                'slam': 'False',
            }.items()
        )
    ])