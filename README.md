## About

This code uses the OpenAI API to create a new image based on a provided text prompt. It begins by importing required modules, including the OpenAI API and dotenv library for loading environment variables.

Next, the code loads the OpenAI API key from an environment variable using load_dotenv(). Then it creates a function that takes a text description as input and generates an image corresponding to it using the OpenAI Image.create() method.

Finally, the code checks if the script is being run directly or imported as a module, and if it is being run directly, it takes a text description as a command line argument and prints the generated image URL.

## Requirements

The following Python libraries are required:
- openai
- dotenv


## Usage

python filename.py "Write a description of the image you want to generate"

## Contribuition

All contributions are welcome! Please open an issue or submit a pull request.

