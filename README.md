
# Streamlit Chatbot Project

This repository contains the code for a chatbot application with a backend powered by a Google API key and a frontend built using Streamlit.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Introduction

This project is a chatbot application that leverages Google's APIs for natural language processing and other AI functionalities. The frontend is built using Streamlit, making it easy to interact with the chatbot via a web interface.

## Features

- **Natural Language Processing:** Powered by Google's APIs.
- **Interactive UI:** Built with Streamlit for a smooth user experience.
- **Customizable:** Easily configurable to suit different use cases.

## Tech Stack

- **Backend:** Google API Key
- **Frontend:** Streamlit

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/chatbot-project.git
   cd chatbot-project
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Google API Key:**
   - Obtain an API key from [Google Cloud](https://console.cloud.google.com/).
   - Set the API key in your environment variables:
     ```bash
     export GOOGLE_API_KEY='your-api-key-here'
     ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Interact with the chatbot:**
   - Open the URL provided by Streamlit in your browser.
   - Start chatting with the bot!

## Configuration

- **Google API Key:** Ensure your API key is correctly set in the environment variable `GOOGLE_API_KEY`.
- **Streamlit Configuration:** Modify `app.py` as needed to adjust the chatbot's behavior or UI elements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
