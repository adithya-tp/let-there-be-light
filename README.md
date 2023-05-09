# let-there-be-light
Image illumination recovery experiments as part of 16-726, CMU's course on Learning Based Image Synthesis

# Control-Net setup

```
git clone https://github.com/adithya-tp/let-there-be-light.git
mkdir models/
(Download control_sd15_ini.ckpt from google drive into models/)

cd let-there-be-light
mkdir control/
(Download dataset containing source/, target/ and prompts.json into control/)
```

# Control-Net training
```
cd src/
python tutorial_train.py
```


# StyleGAN-NADA setup

```
cd src/stylegan_nada
```

There are 2 notebooks you can run.
(1) Finetuning__CLIP_Embeddings.ipynb
This is for finetuning the CLIP model on your own dataset.
(2) stylegan_nada_inference.ipynb
This is used for downloading pretrained generator models and training StyleGAN-NADA to output image domain shift.
