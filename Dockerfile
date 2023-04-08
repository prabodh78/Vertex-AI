# YOLOv5 🚀 by Ultralytics, GPL-3.0 license

# Start FROM NVIDIA PyTorch image https://ngc.nvidia.com/catalog/containers/nvidia:pytorch
FROM gcr.io/deeplearning-platform-release/pytorch-gpu.1-12
RUN rm -rf /opt/pytorch  # remove 1.2GB dir

# Downloads to user config dir
ADD https://ultralytics.com/assets/Arial.ttf https://ultralytics.com/assets/Arial.Unicode.ttf /root/.config/Ultralytics/

# Install linux packages
RUN apt update && apt install --no-install-recommends -y zip htop screen libgl1-mesa-glx


# Create working directory
# RUN mkdir -p /usr/src
WORKDIR /

# Copy contents
COPY . /

# Install pip packages
RUN pip install -r requirements.txt

# Sets up the entry point to invoke the trainer.
ENTRYPOINT ["python", "-m", "tasks"]
# ENTRYPOINT ["python", "task.py"]



