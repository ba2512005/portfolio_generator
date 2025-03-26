import json
import os
import requests # Import requests library
from docx import Document
import fitz  # PyMuPDF

def parse_docx(file_path):
    """Parse a DOCX file and return its text content"""
    doc = Document(file_path)
    paragraphs = []
    for para in doc.paragraphs:
        paragraphs.append(para.text)
    return "\n".join(paragraphs)

def parse_pdf(file_path):
    """Parse a PDF file and return its text content"""
    text = ""
    with fitz.open(file_path) as doc:
        for page_num, page in enumerate(doc.pages(), 1):
            text += page.get_text("text")
    return text

def main(resume_file):
    # Load API key from config.json
    with open('config.json', 'r') as f:
        config = json.load(f)
        gemini_api_key = config['gemini_api_key']

    # Determine file type and extract text
    if resume_file.endswith('.docx'):
        resume_text = parse_docx(resume_file)
    elif resume_file.endswith('.pdf'):
        resume_text = parse_pdf(resume_file)
    else:
        raise ValueError("Unsupported file format. Only DOCX and PDF are supported.")

    # Call Gemini API for parsing (placeholder - API call logic will be added later)
    print("Calling Gemini API to parse resume...")
    parsed_data_from_api = { # Placeholder response for now
        "name": "Gemini Parsed Name",
        "email": "gemini_parsed_email@example.com",
        "work_experience": [],
        "education": [],
        "skills": []
    } 

    data = parsed_data_from_api # Use placeholder data for now

    # Create basic structure matching portfolio.json format and map data
    resume_data = {
        "name": data.get('name') or "",
        "label": "",  # Not directly available in resume-parser output
        "image_path": "img/default-image.png",
        "contact": {
            "email": data.get('email') or "",
            "phone": "", # Not extracted from placeholder response
            "location": "" # Not extracted from placeholder response
        },
        "summary": "", # Not extracted from placeholder response
        "base_url": "127.0.0.1:5500",
        "social_links": [],
        "work_experience": data.get('work_experience') or [],
        "projects": [], # Not directly parsed by default, needs custom logic
        "volunteer_experience": [], # Not directly parsed by default
        "education": data.get('education') or [],
        "skills": data.get('skills') or [],
        "interests": [], # Not directly parsed by default
        "languages": [], # Not directly parsed by default
        "references": [] # Not directly parsed by default
    }

    # Write to JSON file
    output_filename = f"{os.path.splitext(resume_file)[0]}.json"
    with open(output_filename, 'w') as f:
        json.dump(resume_data, f, indent=2)

if __name__ == "__main__":
    import sys
    print(f"Arguments passed to script: {sys.argv}")  # Debugging line
    if len(sys.argv) != 2:
        print("Usage: python parse_resume.py [resume_file]")
        sys.exit(1)
    main(sys.argv[1])
