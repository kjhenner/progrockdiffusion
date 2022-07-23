from tkinter import *
import os
import json
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk,Image




json_set = json.load(open('settings.json'))

def get_text(derp):
    for key in json_set.items():
        text = StringVar()
        text.set(json_set[derp])
        return text

def get_prompt():
    for key in json_set.items():
        json_set['text_prompts']['0'][0] = json_set['text_prompts']['0'][0].replace('{','')
        text = StringVar()
        text.set(json_set['text_prompts']['0'][0])
        print(json_set['text_prompts']['0'][0])
        return text

path = './'

def writeToJSONFile(path, fileName, data):
    with open(path + fileName + '.json', 'w') as f:
        json.dump(data, f)


def save_text():
    for key, value in json_set.items():
        json_set['text_prompts']['0'][0] = prompt_text.get()
        files = [('JSON File', '*.json')]
        fileName='Derp'
        filepos = asksaveasfile(filetypes = files,defaultextension = json,initialfile='Derp')
        writeToJSONFile(filepos, fileName, json_set)
        
def do_run():
    os.system('python prd.py -s settings.json')

def callback():
    img2 = ImageTk.PhotoImage(Image.open("progress.png"))
    image_window.image = img2

window = Tk()

master_frame = Frame(bg='Light Blue', bd=3, relief=RIDGE)
master_frame.grid(sticky=NSEW)
master_frame.columnconfigure(0, weight=1)

frame1 = Frame(master_frame, bg='Light Green', bd=2, relief=FLAT)
frame1.grid(row=1, column=0, sticky=NW)

frame2 = Frame(master_frame, bg='Red', bd=2, relief=FLAT)
frame2.grid(row=4, column=0, sticky=NW) 

prompt = Label(frame2, text='Prompt:')
prompt.grid(row=1, column=0, pady=5, padx=2, sticky=NW)

prompt_text = Entry(frame2, textvariable=get_prompt(), width=150)
prompt_text.grid(row=2, column=0, pady=5, padx=2, sticky=NW)

steps = Label(frame1, text='Steps:')
steps.grid(row=1, column=0, pady=5, padx=2, sticky=NW)

steps_text = Entry(frame1, textvariable=get_text('steps'), width=8)
steps_text.grid(row=1, column=1, pady=5, padx=2, sticky=NW)

height = Label(frame1, text='Height:')
height.grid(row=1, column=2, pady=5, padx=2, sticky=NW)

height_text = Entry(frame1, textvariable=get_text('height'), width=8)
height_text.grid(row=1, column=3, pady=5, padx=2, sticky=NW)

width = Label(frame1, text='Width:')
width.grid(row=1, column=4, pady=5, padx=2, sticky=NW)

width_text = Entry(frame1, textvariable=get_text('width'), width=8)
width_text.grid(row=1, column=5, pady=5, padx=2, sticky=NW)

clip_guidance_scale = Label(frame1, text='Clip Guidance Scale:')
clip_guidance_scale.grid(row=2, column=0, pady=5, padx=2, sticky=NW)

clip_guidance_scale_text = Entry(frame1, textvariable=get_text('clip_guidance_scale'), width=8)
clip_guidance_scale_text.grid(row=2, column=1, pady=5, padx=2, sticky=NW)

skip_steps = Label(frame1, text='Skip Steps:')
skip_steps.grid(row=2, column=2, pady=5, padx=2, sticky=NW)

skip_steps_text = Entry(frame1, textvariable=get_text('skip_steps'), width=8)
skip_steps_text.grid(row=2, column=3, pady=5, padx=2, sticky=NW)

skip_steps_ratio = Label(frame1, text='Skip Steps Ratio:')
skip_steps_ratio.grid(row=2, column=4, pady=5, padx=2, sticky=NW)

skip_steps_ratio_text = Entry(frame1, textvariable=get_text('skip_steps_ratio'), width=8)
skip_steps_ratio_text.grid(row=2, column=5, pady=5, padx=2, sticky=NW)

save = Button(window,text='Save Settings', command=save_text).grid(row=1000, column=0)

run = Button(window,text='Run', command=do_run).grid(row=0, column=1)

refresh = Button(window,text='Refresh', command=callback).grid(row=1, column=1)

image_window = Toplevel()

canvas = Canvas(image_window, height=1024, width=1024)  
img = ImageTk.PhotoImage(Image.open("progress.png"))  
canvas.create_image(20, 20, anchor=NW, image=img) 
canvas.pack()

window.title('ProgRockDiffusion (PRD): '+json_set['batch_name'])

window.mainloop()
