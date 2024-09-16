import fandom

# Set the wiki name
wiki_name = "Jojo"

# Set the character based on student ID (Dio Brando for last digit 2)
character_name = "Dio Brando"

def scrape_fandom_character(character_name):
    try:
        # Search for the character in the Jojo wiki
        page = fandom.page(title=character_name, wiki=wiki_name)
        
        # Check the content type and structure
        content = page.content
        print(f"Content Type: {type(content)}")
        print(f"Content: {content}")

        # If content is a dict, extract relevant information
        if isinstance(content, dict):
            content = content.get('sections', 'No content available')  # Example key: change based on structure

        # Convert the content to string if needed
        if isinstance(content, list):
            content = "\n\n".join([section.get('content', '') for section in content if 'content' in section])

        # Save the character's data to fanwiki.txt
        with open('fanwiki.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fandom content for {character_name} saved to fanwiki.txt")
    except Exception as e:
        print(f"Error fetching data for {character_name}: {e}")

# Call the function
scrape_fandom_character(character_name)
