# EPP333-Mechatronics GUI-Based Serial Link Kinematics Solver

## 1. Introduction
This document presents the design and implementation of a GUI-Based Serial Link Kinematics Solver developed for the EPP333-Mechatronics course. The solver provides a user-friendly interface for solving forward and inverse kinematics problems and visualizing robot workspace.
<div style="text-align: right; padding-right: 40px;">
  <img src="/Lab3 GUI Based Kinamatics Solver/Validate1.png" alt="Pin Diagram" width="600">
</div>

## 2. GUI Design
The MATLAB App consists of:
- Forward and Inverse Kinematics Solver Panel
- Workspace Simulation UI (UIAxes)
- All Possible Points UI (UIAxes2)
- Input Fields for Joint Angles and Parameters
- Buttons for Kinematics Calculation
- Display Fields for Calculated Results

<div style="text-align: right; padding-right: 40px;">
  <img src="/Lab3 GUI Based Kinamatics Solver/Validate2.png" alt="Pin Diagram" width="600">
</div>

## 3. Forward Kinematics Solver
Forward kinematics determines the end effector's position and orientation based on the joint angles of a robot manipulator. The Denavit-Hartenberg (DH) parameters provided by the user are used for calculation.

## 4. Inverse Kinematics Solver
Inverse kinematics determines joint angles for the end effector's desired position. This GUI utilizes an iterative Jacobian transpose method for calculation until convergence or the maximum number of iterations is reached.

## 5. Robot Workspace Drawing
- The `allendeffectors` function computes all possible end effector positions based on specified joint angles.
- The `calculateEndEffectorPosition` function determines the end effector position using given joint angles.
- The `Simulation` function simulates the robot's movement by plotting its links and joints, along with a visualization of its location.
