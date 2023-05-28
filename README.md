## :space_invader: About

This code imports modules such as 'os', 'openai', 'sys' and 'dotenv'. It loads sensitive authentication information into the defined environment. This code defines the `create_image()` function that takes in a `description` argument, passes the description into an OpenAI API to generate an image and returns the url of that image. Finally, when the code is executed directly, `sys.argv[1]` is used to extract the first argument passed to the script and is used as the description passed to the `create_image()` function. The resulting image url is printed to the console.

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

python3 script.py "A person walking down a street"

## :raising_hand: Contribution

All contributions are welcome! Please open an issue or submit a pull request.

