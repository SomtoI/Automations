import tkinter as tk
import pyttsx3, PyPDF2, os
from tkinter import filedialog

folder_path = "C:\\Users\\HP\\Music\\Pdfconversions"


def select_files():
    file_paths = filedialog.askopenfilenames(
        title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")]
    )
    for file_path in file_paths:
        # Add your logic here to handle each file path
        print("Selected File:", file_path)
        # Example: Pass the file path to your conversion code
        convert_file(file_path)


def convert_file(file_path):
    # TODO: Add your conversion code here
    pdfreader = PyPDF2.PdfReader(open(file_path, "rb"))
    speaker = pyttsx3.init()

    for page_num in range(len(pdfreader.pages)):
        text = pdfreader.pages[page_num].extract_text()
        clean_text = text.strip().replace("\n", " ")

    file_name = os.path.splitext(os.path.basename(file_path))[0]
    save_path = os.path.join(folder_path, f"{file_name}.mp3")

    speaker.say(f"Processing and saving {file_name} ...")
    speaker.save_to_file(clean_text, save_path)
    speaker.say(f"Done")

    speaker.runAndWait()


# Create the main window
window = tk.Tk()

# Create a label
label = tk.Label(window, text="PDF Converter")
label.pack(pady=10)

# Create a button to select files
select_button = tk.Button(window, text="Select Files", command=select_files)
select_button.pack(pady=5)

# Create a button to start conversion
convert_button = tk.Button(window, text="Convert", command=convert_file)
convert_button.pack(pady=5)

# Run the main event loop
window.mainloop()
