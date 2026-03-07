# LLM Projects

This repository is a collection of mini-projects, notebooks, and experiments focused on Large Language Models (LLMs). It covers various topics including LangChain, Llama models, and integration with services like Together AI and OpenAI.

## Table of Contents

- [Project Structure](#project-structure)
  - [LangChain Notebooks](#langchain-notebooks)
  - [Llama Notebooks (DeepLearning.AI)](#llama-notebooks)
  - [Other Notebooks](#other-notebooks)
  - [ML Application](#ml-application)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [Resources](#resources)
- [License](#license)

## Project Structure

### LangChain Notebooks
These notebooks follow the LangChain for LLM Application Development course and cover:
- `langchain-Model_prompt_parser.ipynb`: Introduction to Models, Prompts, and Output Parsers.
- `langchain-Chains.ipynb`: Working with different types of chains (Simple, Sequential).
- `langchain-Memory.ipynb`: Implementing memory in LLM applications.
- `langchain-QnA.ipynb`: Question and Answering over documents.
- `langchain-Evaluation.ipynb`: Evaluating LLM applications.
- `langchain-Agents.ipynb`: Using LLMs as reasoning engines to take actions.

### Llama Notebooks
A series of notebooks focused on Llama models, inspired by DeepLearning.AI's "Prompt Engineering with Llama 2/3" course:
- `deeplearning_ai_getting_started_llama.ipynb`: Basic interactions with Llama.
- `deeplearning_ai_prompt_engineering_techniques_llama.ipynb`: Advanced prompting strategies.
- `deeplearning_ai_code_llama.ipynb`: Using Llama for code generation and analysis.
- `deeplearning_ai_multi_turn_conversations_llama.ipynb`: Building conversational interfaces.
- `deeplearning_ai_comparing_llama_models.ipynb`: Comparing different Llama model sizes and versions.
- `deeplearning_ai_llama_guard.ipynb`: Implementing safety guardrails.
- `deeplearning_ai_walkthrough_helper_function.ipynb`: Utility functions for Llama API calls.

### Other Notebooks
- `together_ai_service_setup.ipynb`: Setting up and using the Together AI API.
- `tokenise_test_gpt2.ipynb`: Testing tokenization with GPT-2.

### ML Application
- `ml_app/`: A standalone Flask application for image classification.
  - `app.py`: Flask API using MobileNetV2 (TensorFlow/Keras).
  - Includes sample images for testing.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ppant/llm-projects.git
   cd llm-projects
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   The notebooks require several packages. You can install them using:
   ```bash
   pip install langchain openai together python-dotenv tensorflow flask pillow numpy
   ```

## Environment Variables

Some notebooks require API keys from OpenAI or Together AI. Create a `.env` file in the root directory and add your keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
TOGETHER_API_KEY=your_together_api_key_here
```

## Resources

- [DeepLearning.AI - Prompt Engineering with Llama 2](https://learn.deeplearning.ai/courses/prompt-engineering-with-llama-2)
- [Together AI API Documentation](https://api.together.xyz/docs)
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
