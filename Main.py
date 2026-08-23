#Main.py
from Extractor.Extractor import Extractor
from sender.sender import sender
import os
import tkinter
from tkinter import Tk, filedialog
directory = None
resume_path = []
extracted_text = None
results = None
def on_submit(rp):
    global extracted_text, results
    ext = Extractor(rp)
    texts = ext.worker()
    extracted_text = dict(zip(rp, texts))
    API_Key = Input1.get().strip()
    Jobdesc = Job_desc.get("1.0",tkinter.END).strip()
    results = sender(API_Key,extracted_text,Jobdesc)
    Output.delete("1.0", tkinter.END)
    for path, raw_response in results.items():
        parsed = parse_result(raw_response)
        if parsed:
            name, score = parsed
            Output.insert(tkinter.END, f"{name}: {score}\n")
    print(resume_path)
    print(results)
    print(extracted_text)
def select_folder():
    global directory,resume_path
    directory = filedialog.askdirectory()
    resume_path = [os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(".pdf")]
    return resume_path
root = Tk()
Api_Key = tkinter.Label(root,text="Grok_Api_key")
Input1 = tkinter.Entry(root, width=50)
Input1.pack()
Api_Key.pack()
Desc = tkinter.Label(root,text="Job Description")
Desc.pack()
Job_desc = tkinter.Text(root, height = 10, width = 50)
Job_desc.pack()
Folder = tkinter.Button(root, text = "Select Folder", command = lambda: select_folder())
Folder.pack()
Button = tkinter.Button(root, text="Submit", command = lambda: on_submit(resume_path))
Button.pack()
Output = tkinter.Text(root, height = 10, width = 50)
Output.pack()
def parse_result(text):
    text = text.strip()
    if text == "SKIP" or "|" not in text:
        return None
    name_part, score_part = text.split("|")
    name = name_part.replace("Name:", "").strip()
    score = score_part.replace("Score:", "").strip()
    return name, score
root.mainloop()