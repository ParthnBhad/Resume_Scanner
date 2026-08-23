#Extractor
import pdfplumber
from concurrent.futures import ThreadPoolExecutor
class Extractor:
    def __init__(self,resume_path):
        self.resume_path = resume_path
    def Extract(self,Path):
        try:
            with pdfplumber.open(Path) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            print("Error")
            return f"[could not read this file: {e}]"
    def worker(self):
        with ThreadPoolExecutor(max_workers=5) as ex:
            results = ex.map(self.Extract, self.resume_path)
            return results
