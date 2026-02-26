# ResearchMind AI

A multi-agent LLM system that autonomously researches 
any topic, synthesizes information from multiple sources, 
and generates structured reports with citations.

## Tech Stack
- Python, BeautifulSoup, Scrapy, Selenium
- LangChain, AWS Bedrock, Pinecone
- FastAPI, Streamlit, Docker, AWS

## Setup
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run scraper
python scraper/scraper.py

## Project Status
Week 1 — Building data ingestion pipeline