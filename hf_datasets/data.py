import os
import csv
from datasets import load_dataset

# Set Hugging Face datasets cache path to D:
os.environ["HF_DATASETS_CACHE"] = "D:/Shepherd OS/hf_datasets"

# Load the dataset
ds = load_dataset("DatadudeDev/Bible")

# Define the file path to save the CSV file
output_file_path = "D:/Shepherd OS/hf_datasets/bible.csv"

# Open the CSV file in write mode
with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["Citation", "Book", "Chapter", "Verse", "Text"])

    # Iterate through the dataset and extract relevant data
    for entry in ds['train']:
        book = entry['book']
        chapter = entry['chapter']
        verse = entry['verse']
        text = entry['text']
        
        # Create the citation in the format "Genesis 1:1"
        citation = f"{book} {chapter}:{verse}"
        
        # Write the data to the CSV file
        writer.writerow([citation, book, chapter, verse, text])

print(f"Data has been successfully written to {output_file_path}")
