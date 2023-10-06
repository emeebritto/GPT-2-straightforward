from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import os


# Load the pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Set the model to evaluation mode
model.eval()

# Prompt for text generation
sequence = input("start with: ")
window_length = 0 # by spaces (0 = all sequence) - experimental

while True:
	# set context length
	context_window = " ".join(sequence.split(" ")[-window_length:])

	# Encode the prompt
	input_ids = tokenizer.encode(context_window, return_tensors="pt")
	attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

	# Generate text
	output = model.generate(
		input_ids,
		max_new_tokens=60,
		num_return_sequences=1,
		no_repeat_ngram_size=2,
		top_k=50,
		top_p=0.95,
		attention_mask=attention_mask,
		pad_token_id=model.config.eos_token_id
	)

	# Decode and print the generated text
	generated_text = tokenizer.decode(
		output[0],
		skip_special_tokens=True
	)

	os.system('clear')
	sequence += generated_text[len(context_window):]
	print(sequence)
