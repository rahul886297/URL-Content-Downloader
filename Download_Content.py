import requests
import os

def download_content(url, output_file):
    """
    Downloads content from a given URL and saves it to a file.
    
    Parameters:
    url (str): The URL to download content from.
    output_file (str): The file path where the content will be saved.
    """
    try:
        print(f"Downloading content from: {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check if the request was successful

        # Write content to file
        with open(output_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Content saved to: {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading content: {e}")

if __name__ == "__main__":
    print("URL Content Downloader")
    
    # Input the URL
    url = input("Enter the URL: ").strip()
    
    # Derive output file name from URL or user input
    filename = input("Enter the output file name (or press Enter to auto-generate): ").strip()
    if not filename:
        filename = os.path.basename(url) or "downloaded_content"
    
    # Call the downloader function
    download_content(url, filename)

