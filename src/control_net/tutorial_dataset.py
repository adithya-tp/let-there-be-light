import json
import cv2
import numpy as np

from torch.utils.data import Dataset
import torchvision.transforms as transforms
from PIL import Image


class MyDataset(Dataset):
    def __init__(self):
        self.data = []
        with open('../../control/prompt.json', 'rt') as f:
            for line in f:
                self.data.append(json.loads(line))
                
        # Define transform to resize source images to 32x32
        self.transform = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.ToTensor() # convert PIL image to PyTorch tensor
        ])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        source_filename = item['source']
        target_filename = item['target']
        prompt = item['prompt']

        source_filename = f"{source_filename}.png" if not source_filename.endswith('.png') else source_filename
        target_filename = f"{target_filename}.png" if not target_filename.endswith('.png') else target_filename
        
        # Load images using PIL
        source = Image.open('../../control/' + source_filename).convert('RGB')
        target = Image.open('../../control/' + target_filename).convert('RGB')

        # Apply transforms to source and target images
        source = self.transform(source)
        target = self.transform(target)

        source = source.permute(1, 2, 0)
        # Normalize target images to [0, 1].
        # target = (target.float() / 0.5) - 1.0
        target = target.permute(1, 2, 0)
        # print(source.shape)
        # print(target.shape)

        return dict(jpg=target, txt=prompt, hint=source)

# import json
# import cv2
# import numpy as np

# from torch.utils.data import Dataset


# class MyDataset(Dataset):
#     def __init__(self):
#         self.data = []
#         with open('../../data/fill50k/prompt.json', 'rt') as f:
#             for line in f:
#                 self.data.append(json.loads(line))

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, idx):
#         item = self.data[idx]

#         source_filename = item['source']
#         target_filename = item['target']
#         prompt = item['prompt']

#         source = cv2.imread('../../data/fill50k/' + source_filename)
#         target = cv2.imread('../../data/fill50k/' + target_filename)

#         # Do not forget that OpenCV read images in BGR order.
#         source = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)
#         target = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)

#         # Normalize source images to [0, 1].
#         source = source.astype(np.float32) / 255.0

#         # Normalize target images to [-1, 1].
#         target = (target.astype(np.float32) / 127.5) - 1.0
#         print(source.shape, target.shape)

#         return dict(jpg=target, txt=prompt, hint=source)
