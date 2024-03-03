import argparse
import csv

# Set up argument parsing
parser = argparse.ArgumentParser(description='Create Python files with Furhat API interaction code.')
parser.add_argument('--character', type=str, default='Rania', help='Character name for Furhat set_face method')
parser.add_argument('--input_csv', type=str, required=True, help='Path to the input CSV file')
args = parser.parse_args()

template = """
import time
from furhat_remote_api import FurhatRemoteAPI

def run_action(ip: str):
    furhat = FurhatRemoteAPI(ip)
    furhat.set_face(mask="adult", character="{character}")
    
    url_list = {url_list}

    for url in url_list:
        furhat.say(url=url, lipsync=True)
"""

def create_file(filename, urls, character):
    """Create a Python file with the specified content."""
    content = template.format(url_list=urls, character=character)
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Created {filename} with specified content")

def read_and_process_file(input_filename, character):
    """Read the input file and process each row to create Python files."""
    current_filename = ""
    accumulated_urls = []

    with open(input_filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Check if the row has a new filename
            if row[1].strip():
                # Process the previous filename if there are accumulated URLs
                if accumulated_urls:
                    urls_list_repr = str(accumulated_urls).replace("'", '"')
                    create_file(current_filename, urls_list_repr, character)
                    accumulated_urls = []  # Reset the URLs list
                
                current_filename = row[1].strip()  # Update the current filename
            
            # Accumulate URLs
            if row[2].strip():  # Ensure there is a URL to add
                accumulated_urls.append(row[2].strip())
        
        # Process the last set of accumulated URLs if any
        if accumulated_urls:
            urls_list_repr = str(accumulated_urls).replace("'", '"')
            create_file(current_filename, urls_list_repr, character)

# Main execution
if __name__ == "__main__":
    read_and_process_file(args.input_csv, args.character)
