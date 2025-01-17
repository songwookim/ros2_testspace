from setuptools import find_packages, setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='songwoo',
    maintainer_email='thddn191@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],

    # 노드 추가
    entry_points={
            'console_scripts': [
                    'talker = py_pubsub.publisher_member_function:main',
                    'listener = py_pubsub.subscriber_member_function:main',
            ],
    },
)
