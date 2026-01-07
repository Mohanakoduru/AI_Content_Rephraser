# AI Content Rephraser

AI Content Rephraser is a Streamlit-based web application that converts a single caption into multiple high-quality rewritten versions using large language models. It is built for content creators, marketers, freelancers, and agencies who need fast, consistent content variations.

## Features

- Rewrites one input into multiple styles:
  - Viral version
  - Short version
  - Emotional version
  - SEO-friendly version
  - Niche / trend-based version
- Simple and clean Streamlit interface
- Option to use your own Groq API key
- Download individual outputs or all versions together
- Lightweight and fast execution

## Tech Stack

- Python
- Streamlit
- Groq LLM API
- python-dotenv

## Project Structure

ai_content_rephraser/
├── app.py
├── groq_client.py
├── prompt_engine.py
├── .env
├── requirements.txt
└── README.md

## Setup Instructions

1. Clone the repository
git clone https://github.com/your-username/ai-content-rephraser.git
cd ai-content-rephraser

2. Create and activate a virtual environment (optional)
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Add environment variables
Create a .env file in the root directory:
GROQ_API_KEY=your_groq_api_key_here

## Run the Application

streamlit run app.py

The application will open in your default browser.

## How It Works

1. User enters a caption or short text
2. A structured prompt is generated
3. The prompt is sent to the Groq LLM
4. The response is split into multiple content styles
5. Outputs are displayed and available for download

## Use Cases

- Social media captions
- YouTube Shorts and Reels content
- Marketing copy rewriting
- SEO content optimization
- Freelancing and agency workflows

## Future Enhancements

- Bulk content rephrasing
- Brand tone memory
- User authentication
- Usage limits and analytics
- Export to DOCX and CSV formats

## Author

Built by Mohan Koduru  
Year: 2026
