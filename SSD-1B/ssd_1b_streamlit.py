import os
import subprocess
import sys

import streamlit as st
import torch
from diffusers import StableDiffusionXLPipeline
from PIL import Image

# To run streamlit, setup streamlit port as 80 and run 'streamlit run SSD-1B_streamlit.py --server.port=80'
st.set_page_config(layout="wide")

pipe = StableDiffusionXLPipeline.from_pretrained(
    "/model", torch_dtype=torch.float16, use_safetensors=True, variant="fp16"
)
pipe.to("cuda")

Input_query = "A Beatiful Seoul in Korea"  # Your prompt here
prompt = st.text_input("Input Query", Input_query)
negative = "crime, negative, politics, dirty"  # Negative prompt here
neg_prompt = st.text_input("Negative Things", negative)
image = pipe(prompt=prompt, negative_prompt=neg_prompt).images[0]

process = f"python SSD-1B_inference.py --prompt '{prompt} --neg_prompt {neg_prompt}'"

generated_image = prompt + ".jpg"
image.save(generated_image)
image_path = "./" + generated_image
generated_img = Image.open(image_path)
st.image(generated_img)
