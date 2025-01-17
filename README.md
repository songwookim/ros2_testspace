```
ros2 pkg executables py_srvcli
ros2 pkg executables py_pubsub
```

### 1. Simple topic Example
```
ros2 run py_srvcli service

ros2 run py_srvcli service
```

### Miscellaneous
```
export COLCON_PREFIX_PATH=''
export CMAKE_PREFIX_PATH=''
export AMENT_PREFIX_PATH=''

```
```
sudo apt-get update -y && sudo apt-get upgrade -y 
sudo apt-get install gdbserver
sudo apt-get install gdb

colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=RelWithDebInfo

ros2 run --prefix 'gdbserver localhost:3000' py_srvcli client


```

- launch.json
```

* ROS Extension : ctrl+shift+b -> colcon build
        {
            "name": "ROS: Attach",
            "type": "ros",
            "request": "attach"
        },
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
```