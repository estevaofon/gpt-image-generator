## :space_invader: About

This code is a Python script that uses the OpenAI API to generate an image based on a given text prompt. It imports necessary libraries, sets up the OpenAI API, creates a function "create_image" that takes in a string "description" as a prompt and returns an image URL. Finally, it runs the "create_image" function if the script is run directly and prints the resulting image URL. 

## :wrench: Requirements

The following Python libraries are required:

- os
- openai
- sys
- dotenv


## :rocket: OpenAI API

This application uses the OpenAI API. You will need to obtain an API key from the [OpenAI website](https://openai.com/), and add it to your environment variables or a .env file in the project root with the key `OPENAI_API_KEY`.

## :shipit: Environment Variables

This application uses the following environment variables, which need to be added to a .env file in the project root:

- OPENAI_API_KEY


## :runner:  Usage

python filename.py "description"

## :raising_hand: Contribution

All contributions are welcome! Please open an issue or submit a pull request.

