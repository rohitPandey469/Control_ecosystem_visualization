# Control Ecosystem Visualization Task 1

## Setup Instructions

### 1. Clone and build the repository
```bash
git clone https://github.com/rohitPandey469/Control_ecosystem_visualization
cd Control_ecosystem_visualization
source /opt/ros/humble/setup.bash 
rosdep install --from-paths src --ignore-src -y --rosdistro humble
colcon build
source install/setup.bash
```

### 2. Running the Pub/Sub Nodes
```bash
ros2 launch messages_and_services talker_listener.launch.py
```

### 3. Running the Service/Client Nodes
In one terminal
```bash
ros2 run messages_and_services serviceNode
```
In second terminal pass two args
```bash
ros2 run messages_and_services clientNode <number1> <number2>
```
