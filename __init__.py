from .pytorch_openpose import *

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "pytorch_openpose":pytorch_openpose
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "pytorch_openpose":"pytorch_openpose"
}
