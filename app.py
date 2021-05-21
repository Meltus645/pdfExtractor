import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root =tk.Tk()
canvas =tk.Canvas(root, width=600,height=300)
canvas.grid(columnspan =3,rowspan =3)
#commands
def open_file():
    browse_txt.set('Loading ...')
    file =askopenfile(parent =root, mode ='rb', title ='Choose a file', filetype =[('Pdf file','*.pdf')])
    if file:
        read_pdf =PyPDF2.PdfFileReader(file)
        page =read_pdf.getPage(0)
        page_content =page.extractText()

        # text box
        text_box =tk.Text(root, height =10, width =50, padx =15,pady =15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure('center', justify ='center')
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(row =3, column =1)
        browse_txt.set('Browse')
        
# logo
logo =Image.open('logo.png')
logo =ImageTk.PhotoImage(logo)
logo_label =tk.Label(image =logo)
logo_label.image =logo
logo_label.grid(row =0,column =1)

# instructions
instructions =tk.Label(root, text ='Select a pdf file from your system', font ='Raleway')
instructions.grid(row =1,column =0, columnspan =3)

# action button
browse_txt =tk.StringVar()
browse_btn =tk.Button(root, textvariable =browse_txt,font ='Raleway',bg='purple', fg='#f9f9f9', height=2, width=15, command =open_file)
browse_txt.set('Browse')
browse_btn.grid(row =2,column =1)

canvas =tk.Canvas(root, width=600,height=300)
canvas.grid(columnspan =3)
root.mainloop()
