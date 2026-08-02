# Academic Support System

An intelligent solution validator that uses Claude's vision and language capabilities to help students learn through guided feedback. The system extracts problems from images and validates student solutions with progressive hints across three attempts.

## Features

- **Image-to-Text Problem Extraction**: Automatically extract problems from images using Claude's vision capabilities
- **Intelligent Solution Validation**: Evaluates student solutions against problem statements
- **Progressive Hints System**: Provides increasingly detailed guidance across 3 attempts:
  - **Attempt 1**: Subtle hints that guide thinking without giving answers
  - **Attempt 2**: Stronger guidance with more specific direction
  - **Attempt 3**: Complete solution with explanation for learning
- **Multi-Subject Support**: Works with math, physics, chemistry, coding, essays, and more
- **User-Friendly Interface**: Clear prompts and formatted output with visual indicators

## Prerequisites

- Python 3.8 or higher
- Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com))
- Internet connection (for Claude API calls)

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Get your Anthropic API key from [console.anthropic.com](https://console.anthropic.com)

3. Set the environment variable:
   
   **On macOS/Linux:**
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   
   **On Windows (Command Prompt):**
   ```cmd
   set ANTHROPIC_API_KEY=your-api-key-here
   ```
   
   **On Windows (PowerShell):**
   ```powershell
   $env:ANTHROPIC_API_KEY="your-api-key-here"
   ```

## Quick Start

1. Run the program:
   ```bash
   python academic_support.py
   ```

2. Enter the path to your problem image when prompted
   ```
   Enter path to problem image (jpg, png, etc.): ./problems/math.jpg
   ```

3. Review the extracted problem text

4. Submit your solution (up to 3 attempts):
   ```
   📝 ATTEMPT 1/3
   Enter your solution: x = 4
   ```

5. Get feedback:
   - ✅ **Correct**: Problem solved, session ends
   - ❌ **Incorrect**: Receive a hint and try again

## How It Works

### 1. Problem Extraction
The system uses Claude's advanced vision capabilities to read and transcribe problems from images, handling various formats, handwriting styles, and equations.

### 2. Solution Validation
Each solution is evaluated by Claude against the problem statement. The validation approach adapts based on attempt number:

- **Attempt 1-2**: Encourage independent problem-solving by providing thoughtful hints
- **Attempt 3**: Provide the complete solution with explanation to prevent frustration

### 3. Progressive Feedback
This three-attempt structure mirrors effective tutoring practices:
- Early attempts encourage critical thinking
- Middle attempts build on reasoning
- Final attempt ensures students understand the correct approach

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- WebP (.webp)

## Example Session

```
============================================================
   ACADEMIC SUPPORT SYSTEM - Solution Validator
============================================================

Enter path to problem image (jpg, png, etc.): problems/algebra.png

Extracting problem from image...

────────────────────────────────────────────────────────────
PROBLEM:
────────────────────────────────────────────────────────────
Solve for x: 2x + 5 = 13
────────────────────────────────────────────────────────────

📝 ATTEMPT 1/3
Enter your solution: x = 3
────────────────────────────────────────────────────────────
❌ Not quite right. Hint: Remember to subtract 5 from both sides first
────────────────────────────────────────────────────────────

You have 2 attempt(s) remaining.

📝 ATTEMPT 2/3
Enter your solution: x = 4
────────────────────────────────────────────────────────────
✅ Correct! Great job!
────────────────────────────────────────────────────────────

🎉 Completed successfully in 2 attempt(s)!
```

## Supported Problem Types

The system works with academic problems across all domains:

- **Math**: Algebra, calculus, geometry, trigonometry, statistics
- **Physics**: Mechanics, thermodynamics, electromagnetism, optics
- **Chemistry**: Stoichiometry, balancing equations, molecular structure
- **Programming**: Code review, debugging, algorithm design
- **Languages**: Translation, grammar, syntax analysis
- **Essays**: Concept questions, analysis, critical thinking
- **Any other academic domain**: The AI can evaluate solutions for virtually any subject

## Tips for Best Results

**Image Quality:**
- Use good lighting and clear focus
- Keep text readable and at reasonable size
- Include all problem details in the frame
- Avoid extreme angles or heavy shadows
- For handwritten problems, use dark pen on light paper

**Solution Format:**
- Be clear and specific in your answer
- Show relevant work or reasoning when appropriate
- Use proper mathematical notation (e.g., "x = 4" not "the answer is 4")

## Customization

To modify the hint strategy, edit the `response_instruction` sections in the `validate_solution()` function in `academic_support.py`. You can adjust:
- Hint difficulty
- Hint format and style
- When to provide complete solutions
- Feedback messages

## Environment Variables

- `ANTHROPIC_API_KEY` (required): Your Anthropic API key for authentication

## Dependencies

- **anthropic** (v0.39.0+): Official Anthropic Python SDK for Claude API access

## Model Information

This system uses Claude Opus 5 (`claude-opus-5`), which provides:
- Advanced vision capabilities for accurate problem extraction
- Strong reasoning for solution validation
- High-quality natural language generation for helpful feedback

## Troubleshooting

**"Error: ANTHROPIC_API_KEY environment variable not set"**
- Ensure you've set the API key environment variable
- Verify the key is valid and active in your Anthropic console
- On some terminals, you may need to restart after setting the variable

**"File not found. Please enter a valid file path."**
- Check the image path is correct (relative or absolute)
- Ensure the file exists and you have read permissions
- Use forward slashes (/) for paths, even on Windows

**"Error evaluating solution"**
- This indicates an issue with API response parsing
- Check your internet connection
- Verify your API key is valid and has sufficient credits
- Try again with clearer problem/solution text
- Ensure the problem image is readable to the AI

**Image extraction produces unclear or incorrect text**
- Improve image quality (lighting, focus, contrast)
- Ensure text is clear and readable
- Take a better photo/screenshot of the problem
- Try cropping the image to focus on just the problem

## Project Structure

```
classmate/
├── academic_support.py    # Main application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Security & Privacy

- Your API key is used only for authentication with Anthropic
- Problem images and solutions are sent to the Claude API for processing
- Data is processed according to Anthropic's privacy policy
- Review [Anthropic's privacy policy](https://www.anthropic.com/privacy) for more details

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions:
- About the Claude API: [support.anthropic.com](https://support.anthropic.com)
- Report bugs: Check the project repository or contact the maintainer
