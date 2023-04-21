from share import *

import pytorch_lightning as pl
from torch.utils.data import DataLoader
from tutorial_dataset import MyDataset
from cldm.logger import ImageLogger
from cldm.model import create_model, load_state_dict


# Configs
resume_path = '../../../models/control_sd15_ini.ckpt'
batch_size = 1
logger_freq = 200
learning_rate = 1e-5
sd_locked = True
only_mid_control = False

# First use cpu to load models. Pytorch Lightning will automatically move it to GPUs.
model = create_model('./models/cldm_v15.yaml').cpu()
model.load_state_dict(load_state_dict(resume_path, location='cpu'))
model.learning_rate = learning_rate
model.sd_locked = sd_locked
model.only_mid_control = only_mid_control


# Misc
dataset = MyDataset()
dataloader = DataLoader(
    dataset, num_workers=4, batch_size=batch_size, shuffle=True
)
print("length of data loader:", len(dataloader))

next_batch = next(iter(dataloader))
print(
    "Shape of data loader first batch:", 
    next_batch['jpg'].shape, next_batch['hint'].shape
)
print("First batch of prompts:", next_batch['txt'])
logger = ImageLogger(batch_frequency=logger_freq)
trainer = pl.Trainer(
    accelerator='gpu', devices=1, precision=32, callbacks=[logger]
)


# Train!
trainer.fit(model, dataloader)
