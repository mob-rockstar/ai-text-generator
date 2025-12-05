
import sys
import os
from datetime import datetime
from generate import generate_text
from utils.prompt_examples import DEFAULT_PROMPT




def main():
    print("AI Text Generator — Using OpenAI API")
    print("-----------------------------------")


    # Use default prompt if none passed
    prompt = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PROMPT


    print(f"Using prompt: {prompt}\n")


    output = generate_text(prompt)


    print("Generated Output:\n")
    print(output)
    
    # Save to file
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"generated_{timestamp}.txt")
    
    with open(filename, "w") as f:
        f.write(f"Prompt: {prompt}\n")
        f.write("=" * 50 + "\n")
        f.write(output)
    
    print(f"\n✓ Output saved to: {filename}")




if __name__ == "__main__":
    main()