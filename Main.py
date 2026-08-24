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
            name, score, justification = parsed
            Output.insert(tkinter.END, f"{name}: {score} - {justification}\n")
    print(resume_path)
    print(results)
    print(extracted_text)
def select_folder():
    global directory,resume_path
    directory = filedialog.askdirectory()
    resume_path = [os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(".pdf")]
    return resume_path
root = Tk()
root.rowconfigure(3, weight=1)
root.rowconfigure(5, weight=1)
root.columnconfigure(0, weight=1)
Api_Key = tkinter.Label(root, text="Grok_Api_key")
Api_Key.grid(row=0, column=0, sticky="w")
Input1 = tkinter.Entry(root, width=50)
Input1.grid(row=1, column=0, sticky="ew")
Desc = tkinter.Label(root, text="Job Description")
Desc.grid(row=2, column=0, sticky="w")
Job_desc = tkinter.Text(root, height=10, width=50)
Job_desc.grid(row=3, column=0, sticky="nsew")
Folder = tkinter.Button(root, text="Select Folder", command=lambda: select_folder())
Folder.grid(row=4, column=0, sticky="w")
Button = tkinter.Button(root, text="Submit", command=lambda: on_submit(resume_path))
Button.grid(row=4, column=0, sticky="e")
Output = tkinter.Text(root, height=10, width=50)
Output.grid(row=5, column=0, sticky="nsew")
def parse_result(text):
    text = text.strip()
    if text == "SKIP" or "|" not in text:
        return None
    parts = text.split("|")
    if len(parts) != 3:
        return None  # didn't follow format — safer to skip than guess
    name = parts[0].replace("Name:", "").strip()
    score = parts[1].replace("Score:", "").strip()
    justification = parts[2].replace("Justification:", "").strip()
    return name, score, justification
root.mainloop()