
# Dark Pattern Recognition Extension

This project is a browser extension designed to identify and classify dark patterns on websites. It leverages a fine-tuned BERT model to detect whether content is a dark pattern or not. Additionally, another model is used to categorize the type of dark pattern detected.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Downloading the Fine-Tuned BERT Model](#downloading-the-fine-tuned-bert-model)
- [Usage](#usage)
- [Extension Functionality](#extension-functionality)


## Features

- **Dark Pattern Detection**: Identifies dark patterns on web pages using a fine-tuned BERT model.
- **Pattern Classification**: Classifies the detected dark patterns into specific types.
- **Browser Extension**: Easy-to-use browser extension interface for real-time analysis.
- **Customizable Models**: Fine-tune the models with custom datasets to improve performance.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.6+** and **pip** installed on your machine.
- **Node.js** and **npm** installed on your machine.
- **CUDA Toolkit**: Installed and configured if using GPU for model training.

## Installation

To install the project, follow these steps:

### Backend (Python)

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/dark-pattern-recognition.git
    cd dark-pattern-recognition/backend
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Frontend (Browser Extension)

1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```

2. Install the dependencies:
    ```bash
    npm install
    ```

3. Build the extension:
    ```bash
    npm run build
    ```

4. Load the extension in your browser (e.g., Chrome, Firefox):
    - Open the browser and go to the extensions page.
    - Enable "Developer mode" (Chrome) or "Debug mode" (Firefox).
    - Click "Load unpacked" (Chrome) or "Load Temporary Add-on" (Firefox).
    - Select the `build` directory from the `frontend` folder.

## Downloading the Fine-Tuned BERT Model

To download the fine-tuned BERT model:

1. Visit the following link: [Fine-Tuned BERT Model](https://drive.google.com/drive/folders/1KKfP0-sfA6D-XwqH0mjQOghQA69TLeJw?usp=sharing)

2. Download the model files from the Google Drive folder.

3. Place the downloaded model files inside the `backend/api` directory.

    The structure should look like this:
    ```plaintext
    backend/
    ├── api/
    │   ├── bert_model/     # The fine-tuned BERT model directory
    │   │   ├── config.json
    │   │   ├── pytorch_model.bin
    │   │   ├── tokenizer_config.json
    │   │   └── vocab.txt
    ├── dataset/
    ├── train.py
    ├── requirements.txt
    └── app.py
    ```

## Usage

### Detecting Dark Patterns

1. Activate the extension in your browser.
2. Navigate to a website you want to analyze.
3. Click on the extension icon in the browser toolbar.
4. The extension will scan the page and highlight detected dark patterns, providing a classification for each.

## Extension Functionality

The browser extension performs the following tasks:

- **Content Analysis**: Scrapes text content from the current webpage.
- **Dark Pattern Detection**: Uses the fine-tuned BERT model to identify dark patterns.
- **Pattern Classification**: Classifies detected dark patterns into predefined categories.
- **User Feedback**: Highlights dark patterns and displays information to the user.
