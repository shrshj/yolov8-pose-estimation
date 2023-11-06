import os
import requests
from bs4 import BeautifulSoup
from glob import glob

# Function to fetch image URLs based on a search query
def get_image_urls(search_query):
    # Define the base URL and query parameters for Google Image search.
    base_url = "https://www.google.com/search"
    params = {
        "q": search_query,
        "tbm": "isch",
    }

    # Define headers to mimic a web browser.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Send an HTTP request to Google Image search.
    response = requests.get(base_url, params=params, headers=headers)
    response.raise_for_status()

    # Parse the HTML response using BeautifulSoup.
    soup = BeautifulSoup(response.content, "html.parser")
    image_urls = []

    # Extract image URLs from the HTML response.
    for img in soup.select(".rg_i"):
        img_url = img.get("data-src") or img.get("data-iurl")
        if img_url:
            image_urls.append(img_url)

    return image_urls

# Function to download and save images
def download_images(image_urls, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    saved_images_url = []  # List to store saved image URLs

    for i, img_url in enumerate(image_urls):
        try:
            response = requests.get(img_url)
            response.raise_for_status()

            if img_url in saved_images_url:
                print(f"Skipping duplicate image {img_url}")
                continue  # Skip saving if it's a duplicate
            saved_images_url.append(img_url)  # Add the URL to the already saved list

            img_data = response.content

            # Generate the filename based on the image URL
            filename = img_url.split(':')[-1].split('=')[0] + ".jpg"

            # Save the image to the output folder.
            with open(os.path.join(output_folder, filename), "wb") as img_file:
                img_file.write(img_data)

        except Exception as e:
            print(f"Error downloading image {img_url}: {e}")

# Function to rename images in a folder
def rename_images(img_root_folder):
    img_paths = glob(img_root_folder + '/*')

    for i, path in enumerate(img_paths):
        # Create a new filename based on the index 'i'
        new_filename = f"image_{i+1}.jpg"

        # Rename the image file
        new_path = os.path.join(img_root_folder, new_filename)
        os.rename(path, new_path)

if __name__ == "__main__":
    # Defining the query list keywords
    query_list = ["violin", 'violinist ', 'play violin', 'violin instrument']

    # Folder to save downloaded images in
    output_folder = 'images'

    # Searching image URLs for each keyword
    for q in query_list:
        search_query = q

        # Get image URLs based on the search query.
        image_urls = get_image_urls(search_query)

        # Download and save the images to the output folder.
        download_images(image_urls, output_folder)

        print(f"Downloading images for '{search_query}' keyword to '{output_folder}' folder is DONE.")

    # Renaming the downloaded images with better names
    rename_images(output_folder)
