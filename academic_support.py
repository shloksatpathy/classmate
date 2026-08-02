#!/usr/bin/env python3
"""
Academic Support System - Solution Validator with Hints
Takes problem images, extracts text, validates solutions with 3 attempts
"""

import anthropic
import base64
import json
import os
import sys
from pathlib import Path


def encode_image(image_path: str) -> str:
    """Encode image to base64 for Claude API"""
    with open(image_path, "rb") as img_file:
        return base64.standard_b64encode(img_file.read()).decode("utf-8")


def get_image_media_type(image_path: str) -> str:
    """Determine media type from file extension"""
    ext = Path(image_path).suffix.lower()
    media_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp"
    }
    return media_types.get(ext, "image/jpeg")


def extract_problem_from_image(client: anthropic.Anthropic, image_path: str) -> str:
    """Extract problem text from image using Claude vision"""
    image_data = encode_image(image_path)
    media_type = get_image_media_type(image_path)

    message = client.messages.create(
        model="claude-opus-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Extract and clearly transcribe the problem/question shown in this image. Include all relevant details, equations, or instructions. Just provide the problem text, nothing else."
                    }
                ],
            }
        ],
    )

    return message.content[0].text


def validate_solution(client: anthropic.Anthropic, problem: str, solution: str, attempt: int) -> dict:
    """
    Validate solution and generate response based on attempt number
    Returns: {is_correct: bool, message: str}
    """

    if attempt == 1:
        response_instruction = """If the solution is CORRECT, respond with: {"correct": true, "message": "Correct! Well done!"}

If INCORRECT, respond with ONLY valid JSON: {"correct": false, "message": "Not quite right. Hint: [provide a subtle hint that guides thinking without giving the answer]"}"""

    elif attempt == 2:
        response_instruction = """If the solution is CORRECT, respond with: {"correct": true, "message": "Correct! Great job!"}

If INCORRECT, respond with ONLY valid JSON: {"correct": false, "message": "Still not right. Here's a stronger hint: [provide more specific guidance while still requiring thought]"}"""

    else:  # attempt == 3
        response_instruction = """If the solution is CORRECT, respond with: {"correct": true, "message": "Correct! Excellent work!"}

If INCORRECT, respond with ONLY valid JSON: {"correct": false, "message": "The correct solution is: [provide the complete correct answer with brief explanation]"}"""

    prompt = f"""You are an academic support tutor. Evaluate if the student's solution is correct.

PROBLEM:
{problem}

STUDENT'S SOLUTION:
{solution}

{response_instruction}

Respond ONLY with valid JSON, no other text."""

    message = client.messages.create(
        model="claude-opus-5",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    response_text = message.content[0].text

    try:
        result = json.loads(response_text)
        return {
            "is_correct": result.get("correct", False),
            "message": result.get("message", "Unable to evaluate solution")
        }
    except json.JSONDecodeError:
        return {
            "is_correct": False,
            "message": "Error evaluating solution. Please try again."
        }


def run_academic_support():
    """Main function to run the academic support system"""

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    print("\n" + "="*60)
    print("   ACADEMIC SUPPORT SYSTEM - Solution Validator")
    print("="*60)

    # Get problem image path
    while True:
        image_path = input("\nEnter path to problem image (jpg, png, etc.): ").strip()
        if os.path.isfile(image_path):
            break
        print("File not found. Please enter a valid file path.")

    # Extract problem from image
    print("\nExtracting problem from image...")
    problem = extract_problem_from_image(client, image_path)
    print(f"\n{'─'*60}")
    print("PROBLEM:")
    print(f"{'─'*60}")
    print(problem)
    print(f"{'─'*60}\n")

    # Solution validation loop (3 attempts)
    for attempt in range(1, 4):
        print(f"\n📝 ATTEMPT {attempt}/3")

        while True:
            solution = input("Enter your solution: ").strip()
            if solution:
                break
            print("Please enter a solution.")

        result = validate_solution(client, problem, solution, attempt)

        print(f"\n{'─'*60}")
        if result["is_correct"]:
            print("✅ " + result["message"])
            print(f"{'─'*60}")
            print(f"\n🎉 Completed successfully in {attempt} attempt(s)!")
            return
        else:
            print(f"❌ {result['message']}")
            if attempt < 3:
                print(f"\nYou have {3 - attempt} attempt(s) remaining.")
            print(f"{'─'*60}")

    print("\n" + "="*60)
    print("You've used all 3 attempts. Review the correct solution above.")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_academic_support()
