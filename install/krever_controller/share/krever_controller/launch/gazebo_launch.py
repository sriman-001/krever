import os
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import Command, LaunchConfiguration
import launch_ros.actions

def generate_launch_description():
    # Define the path to the xacro file
    xacro_file = '/home/parallels/project/krever/src/krever_controller/description/body.xacro'
    
    # Ensure the xacro file exists
    if not os.path.exists(xacro_file):
        raise FileNotFoundError(f"Xacro file not found: {xacro_file}")

    # Set the robot description parameter (convert xacro to urdf on the fly)
    robot_description = Command(['ros2 run xacro xacro ', xacro_file])

    # Gazebo executable command with the environment variable to use software rendering
    gazebo_command = [
        'bash', '-c', 'LIBGL_ALWAYS_SOFTWARE=1 ign gazebo -r'
    ]
    
    # Define nodes and processes to be launched
    return LaunchDescription([
        # Declare robot_description parameter
        DeclareLaunchArgument(
            name='robot_description',
            default_value=robot_description,
            description='Robot URDF description generated from Xacro'
        ),
        
        # Launch the robot_state_publisher
        launch_ros.actions.Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': LaunchConfiguration('robot_description')}]
        ),


        launch_ros.actions.Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-file', '/home/parallels/project/krever/src/krever_controller/sdf/body.sdf',
                '-entity', 'Krever'
            ],
            output='screen',
        ),



        # Launch Gazebo with the software rendering workaround
        ExecuteProcess(
            cmd=gazebo_command,
            output='screen',
        ),
    ])
