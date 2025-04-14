## Project Overview

This project is my attempt at play a bit with the development and deployment of AI agents. 

## How to Run with Podman

1. **Clone the repository:**
    ```bash
    git clone https://github.com/josequaresma/ai-agents.git
    cd ai-agents
    ```

2. **Create .env file with OpenAI API-KEY:**
    ```bash
    cp .env-example .env
    ## update variable in .env file
    ```

3. **Podman compose:**
    ```bash
    podman-compose up --build
    ```