# LinkedIn Post Generator

A Streamlit-based application that generates LinkedIn posts using AI, powered by LangChain and Groq LLM.

## Features

- **Multiple Post Lengths**: Generate short (1-3 lines), medium (4-6 lines), or long (7-10 lines) posts
- **Language Support**: Create posts in English or Hinglish
- **Topic-Based Generation**: Select from various predefined topics/tags
- **Few-Shot Learning**: Uses example posts to improve generated content quality
- **Interactive UI**: Built with Streamlit for an easy-to-use interface

## Project Structure

```
.
├── main.py                 # Streamlit app entry point
├── post_generator.py       # Core post generation logic
├── llm_helper.py          # LLM configuration and setup
├── few_shot.py            # Few-shot learning examples
├── preprocess.py          # Data preprocessing utilities
├── requirements.txt       # Python dependencies
└── data/
    ├── raw_posts.json     # Original post data
    └── processed_posts.json # Processed post data
```

## Requirements

- Python 3.8+
- Streamlit
- LangChain
- Groq API access

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd linkedin-posts
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Groq API key**:
   Create a `.env` file in the project root and add:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

Run the Streamlit application:

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

### Steps to Generate a Post:

1. **Select Post Length**: Choose between Short, Medium, or Long
2. **Select Language**: Pick English or Hinglish
3. **Select Topic**: Choose a topic/tag from the available options
4. **Click "Generate Post"**: The AI will generate a LinkedIn post based on your selections

## File Descriptions

- **main.py**: Streamlit UI with dropdowns for post customization and generation button
- **post_generator.py**: Contains the `generate_post()` function that interfaces with the LLM
- **llm_helper.py**: Initializes and configures the Groq LLM
- **few_shot.py**: Manages few-shot examples to guide post generation
- **preprocess.py**: Utilities for processing raw post data

## Dependencies

| Package | Version |
|---------|---------|
| streamlit | 1.35.0 |
| langchain | 0.2.14 |
| langchain-core | 0.2.39 |
| langchain-community | 0.2.12 |
| langchain_groq | 0.1.9 |
| pandas | >=2.2.2 |
| pillow | >=10.4.0 |

## Future Enhancements

- Save generated posts to file
- Post scheduling integration
- Custom topic creation
- Hashtag suggestions
- Performance metrics tracking

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]
