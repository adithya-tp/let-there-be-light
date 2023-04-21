from share import *

import pytorch_lightning as pl
from cldm.model import create_model, load_state_dict


trained_model = '../../lightning_logs/version_2/epoch=115-step=9048.ckpt'
batch_size = 1
logger_freq = 78

model = create_model('./models/cldm_v15.yaml').cpu()
model.load_state_dict(load_state_dict(trained_model, location='cpu'))

input = {
    {"source": "source/N_3.png", "target": "target/N_3.png", "prompt": "white picture of alphabet 'N' against black background"}
}