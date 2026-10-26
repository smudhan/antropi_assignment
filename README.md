# TurtleBot3 Autonomous Navigation using ROS 2 Nav2

## Overview

This project demonstrates autonomous navigation of a TurtleBot3 Burger robot in a custom Gazebo environment using ROS 2 Humble and the Navigation2 (Nav2) stack.

The robot navigates toward user-defined goals while using laser scan data, localization, path planning, and obstacle avoidance.

Developed as part of the **Robotics Software Intern Assignment at Antropi Robotics**.

<img width="1846" height="1167" alt="Screenshot from 2026-10-25 17-15-40" src="https://github.com/user-attachments/assets/30fdacb2-482c-4479-adea-db4db63f90b8" />

## Features

- TurtleBot3 Burger simulation in Gazebo Classic.
  <img width="1846" height="1167" alt="Screenshot from 2026-10-25 17-15-54" src="https://github.com/user-attachments/assets/ef39302b-5f3e-47f4-bdb5-2974a4bd8419" />

- Custom world containing walls and obstacles.
- Pre-generated occupancy-grid map created using SLAM.
- AMCL-based robot localization.
- Autonomous navigation using Nav2.
- RViz visualization of the map, robot pose, laser scans, and navigation path.
- Separate launch files for simulation and navigation.

## Technology Stack

| Component | Technology |
|---|---|
| Operating System | Ubuntu 22.04 LTS |
| Middleware | ROS 2 Humble |
| Simulator | Gazebo Classic 11 |
| Robot | TurtleBot3 Burger |
| Navigation | Nav2 |
| Localization | AMCL |
| Visualization | RViz2 |
| Mapping | SLAM Toolbox |

## Repository Structure

```text
antropi_assignment/
└── src/
    └── antropi_navigation/
        ├── CMakeLists.txt
        ├── package.xml
        ├── include/
        │   └── antropi_navigation/
        ├── src/
        ├── launch/
        │   ├── simulation.launch.py
        │   └── navigation.launch.py
        ├── maps/
        │   └── map1/
        │       ├── map.pgm
        │       └── map.yaml
        ├── rviz/
        │   └── rviz_config.rviz
        └── worlds/
            └── custom.world
```

## Prerequisites

These instructions target **Ubuntu 22.04 LTS with ROS 2 Humble**. Other operating systems or ROS distributions may require changes.

Install ROS 2 Humble using the [official ROS 2 installation guide](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html).

Install the required packages:

```bash
sudo apt update

sudo apt install -y \
  ros-humble-desktop \
  ros-humble-gazebo-ros-pkgs \
  ros-humble-navigation2 \
  ros-humble-nav2-bringup \
  ros-humble-turtlebot3 \
  ros-humble-turtlebot3-msgs \
  ros-humble-turtlebot3-gazebo \
  ros-humble-turtlebot3-navigation2 \
  python3-colcon-common-extensions \
  python3-rosdep \
  git
```

Initialize rosdep if it has not already been initialized:

```bash
sudo rosdep init
rosdep update
```

If rosdep is already initialized, skip `sudo rosdep init`.

Set the TurtleBot3 model:

```bash
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
```

## Installation and Build

### 1. Clone the repository

```bash
mkdir -p ~/antropi_ws/src
cd ~/antropi_ws/src

git clone https://github.com/smudhan/antropi_assignment.git
```

### 2. Install dependencies

```bash
source /opt/ros/humble/setup.bash

cd ~/antropi_ws

rosdep install --from-paths src --ignore-src -r -y
```

### 3. Build the workspace

```bash
cd ~/antropi_ws

colcon build --symlink-install
```

Source the workspace:

```bash
source ~/antropi_ws/install/setup.bash
```

For each new terminal, source ROS 2 and the workspace:

```bash
source /opt/ros/humble/setup.bash
source ~/antropi_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger
```

## Running the Simulation

### 1. Launch Gazebo

<img width="1846" height="1167" alt="Screenshot from 2026-10-25 17-15-06" src="https://github.com/user-attachments/assets/c65ae2c3-146c-4a50-89bd-bf842d7d71e6" />

Open Terminal 1:

```bash
source /opt/ros/humble/setup.bash
source ~/antropi_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger

ros2 launch antropi_navigation simulation.launch.py
```

This launches the custom Gazebo world and spawns the TurtleBot3 Burger robot. Wait until the world and robot have loaded.

### 2. Launch Nav2

Open Terminal 2:

```bash
source /opt/ros/humble/setup.bash
source ~/antropi_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger

ros2 launch antropi_navigation navigation.launch.py
```

The navigation launch file loads the saved map, uses Gazebo simulation time, and disables SLAM because a map has already been generated.

**Portability note:** The launch file must resolve the map from the installed package share directory (or otherwise use a path valid on the current machine). Avoid hard-coding a developer-specific path such as `/home/smudhan/...`.

### 3. Open RViz

<img width="1846" height="1167" alt="Screenshot from 2026-10-25 17-16-15" src="https://github.com/user-attachments/assets/eb721ec8-bada-478e-9d69-3d3eb4bc61ca" />

If RViz does not open automatically, run this in another terminal:

```bash
source /opt/ros/humble/setup.bash
source ~/antropi_ws/install/setup.bash

rviz2
```

Set the **Fixed Frame** to `map`. Add or enable the Map, LaserScan, and TF displays as needed. The repository includes an RViz configuration at `rviz/rviz_config.rviz`.

## Localization and Autonomous Navigation

### 1. Initialize localization

After Nav2 starts, select **2D Pose Estimate** in RViz. Click the robot's approximate position on the map and drag an arrow to indicate its orientation.

Wait for AMCL to converge. Check that the laser scan aligns with walls and obstacles on the map.

### 2. Send a navigation goal

<img width="1846" height="1167" alt="Screenshot from 2026-10-25 17-17-01" src="https://github.com/user-attachments/assets/28d1b90b-7657-411b-af2a-c95a4b9380cd" />

1. Select **2D Goal Pose** in RViz.
2. Click a reachable, obstacle-free destination on the map.
3. Drag to specify the desired final orientation.
4. Release the mouse to send the goal.
5. Observe the planned path in RViz and the robot moving in Gazebo.

Nav2 plans and executes a path toward the goal while accounting for obstacles detected by the robot's sensors and represented in its costmaps.

<img width="1175" height="878" alt="Screenshot from 2026-10-25 17-17-27" src="https://github.com/user-attachments/assets/79f22d1e-aadd-4834-99db-1d145debc07b" />

## Map Information

The pre-generated map is stored in:

```text
maps/map1/map.yaml
maps/map1/map.pgm
```

The YAML file contains the map image reference, resolution, origin, and occupancy thresholds. The PGM file contains the occupancy grid used by Nav2's map server.

The map was generated previously using SLAM and is reused for localization and navigation.

## Troubleshooting

### Gazebo does not start

Check that Gazebo Classic and the ROS Gazebo packages are installed:

```bash
gazebo --version
ros2 pkg list | grep gazebo_ros
```

### Nav2 cannot find the map

Check that both map files exist:

```bash
ls -lh ~/antropi_ws/src/antropi_navigation/maps/map1/
```

Confirm that `map.yaml` references `map.pgm` and that the path used by the launch file matches the current workspace.

### Robot does not move

Check that the required topics exist:

```bash
ros2 topic list
ros2 topic echo /scan
ros2 topic echo /odom
```

Confirm that Nav2 started successfully, localization is initialized, and a valid navigation goal has been sent.

### Localization is inaccurate

Use **2D Pose Estimate** in RViz to reset the initial pose. Verify that the saved map corresponds to the current Gazebo world and that the laser scan aligns with the map.

### Gazebo reports missing `model.config` warnings

Gazebo Classic may print model-discovery warnings when scanning ROS package directories. If the world and robot load correctly, these warnings may be unrelated to navigation. Investigate further if models fail to load or the simulation does not work.

## Demo

The assignment demo should show:

- The custom Gazebo environment and TurtleBot3 robot.
- The saved map and robot localization in RViz.
- A navigation goal and the resulting planned path.
- Autonomous movement and obstacle avoidance.
- Successful arrival at the destination.

**Demo video:** https://drive.google.com/file/d/17t2zkxPz6EJQ86vSr2eHhPzbkRNX07FF/view?usp=sharing

## Assignment

Prepared for the Robotics Software Intern application at Antropi Robotics.

**Author:** Shubham Udhan

**Repository:** https://github.com/smudhan/antropi_assignment
