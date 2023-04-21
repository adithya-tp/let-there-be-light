import os
import shutil
import json

source_folder = "../data/"
source_dir = "../control/source"
target_dir = "../control/target"
prompts_file = "../control/prompt.json"

# create directories if they don't exist
os.makedirs(source_dir, exist_ok=True)
os.makedirs(target_dir, exist_ok=True)

prompts = []

for filename in os.listdir(source_folder):
    if filename.endswith("_flash.png"):
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(target_dir, filename.replace("_flash.png", "_ambient.png"))
        prompt = "picture in ambient lighting"
        # move flash file to source folder
        shutil.move(source_path, os.path.join(source_dir, filename))
        # move ambient file to target folder
        shutil.move(os.path.join(source_folder, filename.replace("_flash.png", "_ambient.png")), os.path.join(target_dir, filename.replace("_flash.png", "_ambient.png")))
        # add prompt to list
        prompts.append({"source": os.path.join("source", filename), "target": os.path.join("target", filename.replace("_flash.png", "_ambient.png")), "prompt": prompt})

# write prompts to file
with open(prompts_file, "w") as f:
    json.dump(prompts, f)
