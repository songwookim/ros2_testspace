from setuptools import find_packages, setup
from glob import glob

package_name = 'py_async_thread'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
                # Launch 파일 복사
        ('share/py_async_thread/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='songwoo',
    maintainer_email='thddn191@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service1 = py_async_thread.async_io:main',
            'service2 = py_async_thread.thread:main',
            'client = py_srvcli.client_member_function:main',
            'real = py_async_thread.jkiis_real:main',
            'sim = py_async_thread.jkiis_sim:main',
            'sensor = py_async_thread.jkiis_sensor:main',
            
        ],
    },

)
