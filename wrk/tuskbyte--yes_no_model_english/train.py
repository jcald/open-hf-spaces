#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import platform
print(platform.python_version())
print("--------------------------------\n")

from transformers import GPT2Tokenizer, GPT2ForSequenceClassification, Trainer, TrainingArguments
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer

# Replace 'your-username/your-model-name' with the actual model identifier
model_id = 'tuskbyte/yes_no_model_english'
label_map=["Yes","NO","Invalid Input"]
# label_map = {'True': 0, 'False': 1, 'Invalid input': 2}

# Load the model
model = AutoModelForSequenceClassification.from_pretrained(model_id)

try:
    # Try to load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_id)
except OSError:
    # Fallback to a default tokenizer if loading fails
    print(f"Tokenizer for '{model_id}' not found. Using  gpt as fallback.")
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Initialize Trainer with dummy arguments for inference
training_args = TrainingArguments(
    output_dir='./results',  # specify your output directory
    per_device_eval_batch_size=1  # batch size for inference
)

trainer = Trainer(
    model=model,
    args=training_args,
    tokenizer=tokenizer
)

# Example input
question = "Would you like to paticipate ?"
answer = "yes i would"
input_text = f"{question} {answer}"

# Tokenize the input
inputs = tokenizer(input_text, return_tensors="pt")
model.to('cuda')
inputs.to('cuda')
# Perform inference using the model
outputs = model(**inputs)
logits = outputs.logits

# Get the predicted label
predicted_class_id = logits.argmax().item()
print("predicted_class_id",predicted_class_id)
labels = model.config.id2label
print("labels",labels)
predicted_label = labels[predicted_class_id]

# Output the result
print(f"Predicted label: {predicted_label}")
print(f"Model predection is : {label_map[predicted_class_id]}")

