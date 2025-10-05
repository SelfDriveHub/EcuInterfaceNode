FROM ros:jazzy

ARG USERNAME=robo
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Remove existing user with same UID (optional)
RUN if id -u $USER_UID > /dev/null 2>&1; then userdel $(id -un $USER_UID); fi

# Create new user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install dependencies
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y python3-pip

ENV SHELL=/bin/bash

WORKDIR /ws

COPY . .

# ROS dependencies
RUN sudo rosdep update \
    && if [ -d src ]; then sudo rosdep install --from-paths src --ignore-src -y; fi

RUN sudo chown -R $USERNAME:$USERNAME /ws/

# Build workspace
RUN /bin/bash -c "source /opt/ros/jazzy/setup.bash && colcon build"

# Source workspace in final shell
RUN echo "source /ws/install/setup.bash" >> /home/$USERNAME/.bashrc

USER $USERNAME
#CMD ["ros2", "run", "ecu_interface", "ecu_interface_node"]
#CMD ["/bin/bash"]

# Automatically source setup and run your node
CMD ["/bin/bash", "-c", "source /opt/ros/jazzy/setup.bash && source /ws/install/setup.bash && ros2 run ecu_interface ecu_interface_node"]
