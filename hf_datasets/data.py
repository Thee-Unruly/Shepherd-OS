import os
from datasets import load_dataset

# Set Hugging Face datasets cache path to D:
os.environ["HF_DATASETS_CACHE"] = "D:/Shepherd OS/hf_datasets"

# Load the dataset
ds = load_dataset("DatadudeDev/Bible")

# Define the file path to save the text file
output_file_path = "D:/Shepherd OS/hf_datasets/bible.txt"

# Open the file in write mode
with open(output_file_path, 'w', encoding='utf-8') as file:
    # Iterate through the dataset and extract relevant data
    for entry in ds['train']:
        book = entry['book']
        chapter = entry['chapter']
        verse = entry['verse']
        text = entry['text']
        
        # Write the data to the text file in the desired format
        file.write(f"Citation: {book} {chapter}:{verse}\n")
        file.write(f"String Lengths: {len(text)} characters\n")
        file.write(f"Text: {text}\n")
        file.write("-" * 80 + "\n")

print(f"Data has been successfully written to {output_file_path}")
