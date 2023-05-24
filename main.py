import os
import openai
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


def create_image(description):
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url


# If the script is run directly, execute the main function
if __name__ == "__main__":
    description = sys.argv[1]
    url = create_image(description=description)
    print(url)