# Smart Resume Screener

A desktop tool that helps HR teams quickly screen resumes against a job description using an LLM. Select a folder of resumes, paste in a job description, and get back a ranked list of candidate names and fit scores.

## How It Works

1. User selects a folder containing candidate resumes (PDF).
2. The tool extracts text from each resume in parallel.
3. Each resume, along with the job description, is sent to the Grok API for evaluation.
4. The model returns a fit score (1–10) and candidate name for each resume.
5. Results are displayed directly in the app.

## Features

- Simple GUI built with Tkinter
- Bulk folder upload — screen many resumes in one run
- Parallel resume extraction using a thread pool for faster processing
- LLM-based scoring and candidate name extraction via the Grok API
- Bring-your-own API key — no shared or hardcoded credentials

## Tech Stack

- **Language:** Python
- **GUI:** Tkinter
- **PDF Extraction:** pdfplumber
- **Concurrency:** ThreadPoolExecutor
- **LLM:** Grok API (xAI)

## Project Structure

```
Smart_Resume_Scanner/
├── Main.py            # GUI and application entry point
├── sender.py           # Handles requests to the Grok API
├── Extractor/
│   ├── __init__.py
│   └── Extractor.py    # Resume text extraction logic
```

## Setup

1. Clone the repository.
2. Install dependencies:
   ```
   pip install pdfplumber requests
   ```
3. Run the app:
   ```
   python Main.py
   ```
4. Enter your Grok API key, paste a job description, select a resume folder, and submit.

## Why Bring Your Own API Key

Resume screening volume varies a lot between users, and API usage has a real cost. Rather than embedding a shared key (which raises both cost and security concerns), the tool lets each user supply their own key. This keeps the tool provider-agnostic, avoids unbounded API costs on one account, and avoids shipping credentials inside the application.

## Currently Available options
Groq : get your api key from console.groq.com

## Status

This is a working prototype. Planned improvements include support for more file formats (DOCX), better error handling for corrupted or unreadable files, and a more polished output view.
## Known Issues

Frontend is basic: The current Tkinter GUI is functional but static and not visually polished. Layout and styling improvements are planned.
Groq API rate limiting: The Groq endpoint can return a 413 error under certain conditions, tied to the account's tokens-per-minute limit rather than the size of any single request. This can interrupt processing when screening many resumes in one run.

## Video Demo


https://github.com/user-attachments/assets/eaa88a60-8293-4f1f-b42a-de62070a1da4



