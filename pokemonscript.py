import requests
import os

# Function to download file from URL
def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

# Read URLs from text.txt and download files
with open('text.txt', 'r') as file:
    for line in file:
        url = line.strip()  # Remove newline characters
        filename = os.path.basename(url)  # Extract filename from URL
        try:
            download_file(url, filename)
            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed to download {filename}: {e}")