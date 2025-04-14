## Project Overview

This project is my attempt at play a bit with the development and deployment of AI agents. 

## How to Run

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/ai-agents.git
    cd ai-agents
    ```

2. **Create .env file with OpenAI API-KEY:**
    ```bash
    cp .env-example .env
    ## update variable in .env file
    ```

### Run directly

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the main application:**
    ```bash
    python main.py
    ```

### Run with Podman

2. **Podman compose:**
    ```bash
    podman-compose up --build
    ```