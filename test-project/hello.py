#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------
import torch
import cv2
print("This container is using GPU:" + str(torch.cuda.current_device()))
print("torch version:" + str(torch.__version__))
print("opencv version" + str(cv2.__version__))