from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'krever_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # Install the package.xml
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # Install launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        
        # Install RViz configuration files
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),

        # Install the Xacro files
        (os.path.join('share', package_name, 'xacro'), glob('xacro/*.xacro')),


        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='parallels',
    maintainer_email='sriman2205@gmail.com',
    description='ROS 2 package for launching RViz with Krever robot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
