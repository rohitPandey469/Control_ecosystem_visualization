from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'messages_and_services'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch/'), glob('launch/*launch.[pxy][yma]')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rohit',
    maintainer_email='rohit@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'clientNode = messages_and_services.client_node:main',
            'serviceNode = messages_and_services.service_node:main',
            'listenerNode = messages_and_services.listener_node:main',
            'talkerNode = messages_and_services.talker_node:main',
        ],
    },
)
