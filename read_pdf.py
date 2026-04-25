import sys
import subprocess

try:
    from pypdf import PdfReader
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    from pypdf import PdfReader

reader = PdfReader(r"c:\GitHub\ar-sayeem\demo\asset\Final_Project_Brief.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

with open(r"c:\GitHub\ar-sayeem\demo\pdf_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("PDF text extracted to pdf_text.txt")