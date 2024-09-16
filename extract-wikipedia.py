import requests
from bs4 import BeautifulSoup

# Replace with the Wikipedia URL of your chosen actor
url = "https://en.wikipedia.org/wiki/Tom_Cruise"  # Example: Tom Cruise

def scrape_wikipedia(url):
    # User-Agent to mimic a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    # Fetch the content from the URL
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all paragraph tags in the document
        paragraphs = soup.find_all('p')

        # Filter out paragraphs that are empty or just have metadata
        meaningful_paragraphs = [p.get_text() for p in paragraphs if p.get_text().strip()]

        # Debugging: Print the number of meaningful paragraphs found
        print(f"Found {len(meaningful_paragraphs)} meaningful paragraphs.")

        # Write the text to wikipedia.txt
        with open('wikipedia.txt', 'w', encoding='utf-8') as f:
            for paragraph in meaningful_paragraphs:
                f.write(paragraph + "\n\n")
            
        print("Wikipedia content saved to wikipedia.txt")
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

# Call the function
scrape_wikipedia(url)