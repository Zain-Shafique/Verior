import argparse
import json
import random

def generate_response(prompt):
    """Simulate AI processing and generate structured JSON response"""
    if not prompt.strip():
        return {
            "error": "Empty input",
            "details": "Prompt cannot be blank",
            "success": False
        }
    
    responses = [
        f"I analyzed: '{prompt}'. Interesting topic!",
        f"Regarding '{prompt}': Here's what I think...",
        f"Response to '{prompt}': This is a simulated insight."
    ]
    
    return {
        "response": random.choice(responses),
        "model": "simulated-ai-v1",
        "tokens_used": len(prompt.split()) + random.randint(5, 25),
        "success": True
    }

def main():
    parser = argparse.ArgumentParser(description='Mock AI API CLI')
    parser.add_argument('prompt', type=str, help='Input text for AI processing')
    parser.add_argument('--pretty', action='store_true', help='Pretty-print JSON output')
    args = parser.parse_args()
    
    result = generate_response(args.prompt)
    print(json.dumps(result, indent=4 if args.pretty else None))

if __name__ == "__main__":
    main()
