## :space_invader: About

This code imports necessary libraries and sets up an API key for OpenAI. There is a function called "create_image" that takes in a description, sends it to OpenAI, and returns the URL of the generated image. The main function takes a user input description and calls the "create_image" function with the input as a parameter and prints the resulting URL.

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

python <filename>.py "Description of the image you want to create"

## :raising_hand: Contribution

All contributions are welcome! Please open an issue or submit a pull request.

