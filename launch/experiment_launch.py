from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import os


def generate_launch_description():
    # Declare the experiment name argument
    save_location_arg = DeclareLaunchArgument(
        "save_location",
        default_value="default_experiment",
        description="Location to save the experiment data",
    )

    # Get the experiment name
    save_location = LaunchConfiguration("save_location")
    record_all_topics = [
        "ros2",
        "bag",
        "record",
        "-a",
        "-o",
        save_location,
        "--storage",
        "sqlite3",
    ]

    ros_bagger = ExecuteProcess(
        cmd=record_all_topics,
        shell=True,
        name="record_all_topics",
        output="screen",
        emulate_tty=False,
    )

    """
    Put your nodes here.
    """

    return LaunchDescription(
        [
            save_location_arg,
            ros_bagger,
            # Put you node names here
        ]
    )
