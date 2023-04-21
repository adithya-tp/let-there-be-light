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
