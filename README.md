# AI Text Generator

An AI-powered text generation tool using OpenAI's API to generate content based on custom prompts.

## Features

- Generate AI text using OpenAI's GPT-4o-mini model
- Use default prompts or provide custom ones via command line
- Automatically save generated output to timestamped `.txt` files
- Clean, organized output with prompt and generated text

## Prerequisites

- Python 3.7+
- OpenAI API key

## Installation

1. **Clone or download the project**

2. **Install dependencies**:
```powershell
pip install -r requirements.txt
```

3. **Set up your OpenAI API key**:
   - Create a `.env` file in the project root
   - Add your API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
   
   Or set it as an environment variable:
   ```powershell
   $env:OPENAI_API_KEY = "your-api-key-here"
   ```

## Usage

### Run with default prompt:
```powershell
python main.py
```

### Run with custom prompt:
```powershell
python main.py "Your custom prompt here"
```

## Output

Generated text is automatically saved to the `output/` directory with a timestamp:
- `output/generated_20251205_143022.txt`

Each file contains:
- The prompt used
- A separator line
- The generated text

## Project Structure

```
.
├── main.py                 # Main entry point
├── generate.py             # Text generation logic
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API key)
├── config/
│   └── settings.py         # Configuration and OpenAI client setup
├── utils/
│   └── prompt_examples.py  # Default prompts
└── output/                 # Generated output files
```

## Dependencies

- `python-dotenv` - Load environment variables from `.env` file
- `openai` - OpenAI Python client library

## Configuration

Modify the model in `generate.py`:
```python
def generate_text(prompt: str, model: str = "gpt-4o-mini") -> str:
```

Change `model` parameter to use a different OpenAI model (e.g., `"gpt-3.5-turbo"`, `"gpt-4"`).

## Error Handling

Common issues:
- **API Key Error**: Ensure your `.env` file has a valid `OPENAI_API_KEY`
- **Rate Limit**: OpenAI may limit requests based on your account tier
- **No Output Directory**: The script auto-creates the `output/` folder if it doesn't exist

## License

Open source - feel free to modify and use for your needs
