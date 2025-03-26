from resume_parser.resumeparse import resumeparse

try:
    parser = resumeparse()
    print("ResumeParser instantiated successfully!")
except Exception as e:
    print(f"Error instantiating ResumeParser: {e}")
