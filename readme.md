# CrewAI LinkedIn Content Team App

## Overview

The CrewAI LinkedIn Content Team App is an open-source, template-driven application for generating LinkedIn-ready content using a structured workflow. The app is designed to help teams research, create, and refine engaging social media content, emphasizing high-quality output and collaborative teamwork. This project is built to be deployed on [Replit](https://replit.com), allowing users to explore its capabilities easily.

## Features

- **Automated Research**: Uses tools to fetch and analyze the latest articles and trends about a specific subject focus.
- **Content Creation**: Develops LinkedIn posts tailored to a professional, tech-savvy audience.
- **Editorial Review**: Refines and ensures the quality and brand alignment of all content.
- **Output Management**: Automatically saves outputs into well-organized files and directories.

## Workflow

The app leverages **CrewAI**'s agents and tasks to execute a sequential process:

1. **Research Phase**:
   - Agent: `Senior Research Analyst`
   - Task: Collect, analyze, and summarize relevant articles about the specified subject focus.
   - Output: A markdown report with article summaries, key quotes, and analysis.

2. **Content Writing Phase**:
   - Agent: `Social Media Content Writer`
   - Task: Create LinkedIn posts based on research findings, aligning with a specific style and voice.
   - Output: Drafted LinkedIn posts.

3. **Editing Phase**:
   - Agent: `Senior Editor`
   - Task: Review and finalize social media posts for quality, brand alignment, and accuracy.
   - Output: Finalized LinkedIn content and a report summarizing the process.

## Requirements

Before running the app, ensure you have the following:

1. **API Keys**:
   - **OpenAI API Key**: Required for generating content and facilitating agent workflows.
   - **SerperDev API Key**: Required for search and web scraping functionality.
   - Add these keys as environment variables or directly configure them in the script.

2. **Python Packages**:
   - Install the required Python packages:
     ```bash
     pip install crewai crewai_tools
     ```

3. **Access to Replit** (optional but recommended):
   - Easily deploy and test the app in a cloud-based environment.

## How to Use

### Step 1: Clone the App
- **On Replit**:
  - Fork or clone the repository directly in Replit for a ready-to-run environment.
- **On Another Python IDE**:
  - Clone the repository to your local machine using:
    ```bash
    git clone https://github.com/your-repo/crewai-linkedin-template.git
    ```
  - Open the project in your preferred Python IDE.

### Step 2: Add Your API Keys
- Create a `.env` file in the project root or set environment variables with your API keys:
  ```env
  OPENAI_API_KEY=your_openai_api_key
  SERPER_API_KEY=your_serperdev_api_key```

### Step 3: Customize the App
- Edit the agent prompts in the script to suit your needs:
- Define the topic of focus.
- Specify the style of writing for LinkedIn posts.
- Add your company context (e.g., what your company does, offerings, target audience).

Step 4: Run the App
- Execute the script:
```
python app.py
```


### Step 5: Retrieve Outputs
- The results, including research reports and finalized LinkedIn posts, will be saved in the outputs/ folder with timestamps for easy organization.

## Customization

The app is highly flexible:
- Adjust agents’ roles and backstories to reflect your team structure and goals.
- Modify task descriptions and expected outputs to tailor content creation workflows.
- Integrate additional tools or APIs for enhanced functionality.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Credits

This template is powered by [CrewAI](https://crewai.com) and was built using [Replit](https://replit.com).

Start creating professional LinkedIn content effortlessly with this intuitive template! 🚀

