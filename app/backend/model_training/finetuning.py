# !pip install -q accelerate peft bitsandbytes transformers trl
# pip install trl
# !hf auth login

import os
import torch
import tensorflow as tf
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
)
from peft import LoraConfig, PeftModel
from trl import SFTTrainer

import transformers



# ...........................inference before pre-finetuning (hugging-face)

# model_id = "meta-llama/Llama-3.1-8B"
model_id = "Qwen/Qwen2.5-7B-Instruct"

pipeline = transformers.pipeline(
    "text-generation", 
    model=model_id, 
    model_kwargs={
        "torch_dtype": torch.bfloat16
    }, 
    device_map="auto"
)

print(pipeline("Hey how are you doing today?"))

#...............................inference locally

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.1-8B") #download locally base model
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B") #download locally tokenizaer for base model

model.save_pretrained("./llama3_model")
tokenizer.save_pretrained("./llama3_model")

# inference
prompt = "Explain transformers in simple words"
inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=150,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))

