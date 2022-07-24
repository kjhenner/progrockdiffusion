from tkinter import *
import os
import json
import threading
from threading import Timer
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk,Image

json_set = json.load(open('settings.json'))
# args = [steps_text, height_text, width_text, clip_guidance_scale_text, skip_steps_text, skip_steps_ratio_text, use_secondary_model, vitb32, vitb16, vitl14, vitl14_336, rn101, rn50, rn50x4, rn50x16, rn50x64]

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

def save_text():
    x = steps_text.get()
    json_set['steps'] = int(x)
    x = height_text.get()
    json_set['height'] = int(x)
    x = width_text.get()
    json_set['width'] = int(x)
    x = clip_guidance_scale_text.get()
    if x != 'auto':
        json_set['clip_guidance_scale'] = int(x)
    else:
        json_set['clip_guidance_scale'] = x
    x = skip_steps_text.get()
    json_set['skip_steps'] = int(x)
    x = skip_steps_ratio_text.get()
    json_set['skip_steps_ratio'] = float(x)
    x = use_secondary_model_text.get()
    json_set['use_secondary_model'] = x
    x = vitb32_text.get()
    json_set['ViTB32'] = float(x)
    x = vitb16_text.get()
    json_set['ViTB16'] = float(x)
    x = vitl14_text.get()
    json_set['ViTL14'] = float(x)
    x = vitl14_336_text.get()
    json_set['ViTL14_336'] = float(x)
    x = rn101_text.get()
    json_set['RN101'] = float(x)
    x = rn50_text.get()
    json_set['RN50'] = float(x)
    x = rn50x4_text.get()
    json_set['RN50x4'] = float(x)
    x = rn50x16_text.get()
    json_set['RN50x16'] = float(x)
    x = rn50x64_text.get()
    json_set['RN50x64'] = float(x)
    x = eta_text.get()
    json_set['eta'] = x
    x = sampling_mode_text.get()
    
    json_set['sampling_mode'] = x
    x = set_seed_text.get()
    json_set['set_seed'] = float(x)
    x = display_rate_text.get()
    json_set['display_rate'] = float(x)
    # x = diffusion_model_text.get()
    # json_set['diffusion_model'] = x
    json_set['text_prompts']['0'][0] = prompt_text.get()
    with open("settings.json", "w") as outfile: 
        json.dump(json_set, outfile)

def run_thread():
    save_text()
    runThread = threading.Thread(target=do_run)
    runThread.start()

def do_run():
    show_image()
    os.system('python prd.py -s settings.json')

def show_image():
    print('shit should print')
    image_window = Toplevel()
    global canvas
    canvas = Canvas(image_window, height=1024, width=1024)
    global img
    global image_container
    img = PhotoImage(file="progress.png")
    image_container = canvas.create_image(0,0, anchor="nw",image=img)
    canvas.pack()
    updater()   

def updater():
    window.after(1000, refresh_image)

def refresh_image():
    updater()
    global img
    global image_container
    global canvas
    img = PhotoImage(file="progress.png")
    canvas.itemconfig(image_container, image = img)

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

eta = Label(frame1, text='ETA:')
eta.grid(row=3, column=0, pady=5, padx=2, sticky=NW)

eta_text = Entry(frame1, textvariable=get_text('eta'), width=8)
eta_text.grid(row=3, column=1, pady=5, padx=2, sticky=NW)

use_secondary_model = Label(frame1, text='Use Secondary Model:')
use_secondary_model.grid(row=3, column=2, pady=5, padx=2, sticky=NW)

use_secondary_model_text = Entry(frame1, textvariable=get_text('use_secondary_model'), width=8)
use_secondary_model_text.grid(row=3, column=3, pady=5, padx=2, sticky=NW)

display_rate = Label(frame1, text='Display Rate:')
display_rate.grid(row=3, column=4, pady=5, padx=2, sticky=NW)

display_rate_text = Entry(frame1, textvariable=get_text('display_rate'), width=8)
display_rate_text.grid(row=3, column=5, pady=5, padx=2, sticky=NW)

vitb32 = Label(frame1, text='VitB32:')
vitb32.grid(row=4, column=0, pady=5, padx=2, sticky=NW)

vitb32_text = Entry(frame1, textvariable=get_text('ViTB32'), width=8)
vitb32_text.grid(row=4, column=1, pady=5, padx=2, sticky=NW)

vitb16 = Label(frame1, text='VitB16:')
vitb16.grid(row=4, column=2, pady=5, padx=2, sticky=NW)

vitb16_text = Entry(frame1, textvariable=get_text('ViTB16'), width=8)
vitb16_text.grid(row=4, column=3, pady=5, padx=2, sticky=NW)

vitl14 = Label(frame1, text='VitL14:')
vitl14.grid(row=5, column=0, pady=5, padx=2, sticky=NW)

vitl14_text = Entry(frame1, textvariable=get_text('ViTL14'), width=8)
vitl14_text.grid(row=5, column=1, pady=5, padx=2, sticky=NW)

vitl14_336 = Label(frame1, text='VitL14 336:')
vitl14_336.grid(row=5, column=2, pady=5, padx=2, sticky=NW)

vitl14_336_text = Entry(frame1, textvariable=get_text('ViTL14_336'), width=8)
vitl14_336_text.grid(row=5, column=3, pady=5, padx=2, sticky=NW)

rn101 = Label(frame1, text='RN101:')
rn101.grid(row=6, column=0, pady=5, padx=2, sticky=NW)

rn101_text = Entry(frame1, textvariable=get_text('RN101'), width=8)
rn101_text.grid(row=6, column=1, pady=5, padx=2, sticky=NW)

rn50 = Label(frame1, text='RN50:') 
rn50.grid(row=7, column=0, pady=5, padx=2, sticky=NW)

rn50_text = Entry(frame1, textvariable=get_text('RN50'), width=8)
rn50_text.grid(row=7, column=1, pady=5, padx=2, sticky=NW)

rn50x4 = Label(frame1, text='RN50x4:')
rn50x4.grid(row=7, column=2, pady=5, padx=2, sticky=NW)

rn50x4_text = Entry(frame1, textvariable=get_text('RN50x4'), width=8)
rn50x4_text.grid(row=7, column=3, pady=5, padx=2, sticky=NW)

rn50x16 = Label(frame1, text='RN50x16:')
rn50x16.grid(row=8, column=0, pady=5, padx=2, sticky=NW)

rn50x16_text = Entry(frame1, textvariable=get_text('RN50x16'), width=8)
rn50x16_text.grid(row=8, column=1, pady=5, padx=2, sticky=NW)

rn50x64 = Label(frame1, text='RN50x64:')
rn50x64.grid(row=8, column=2, pady=5, padx=2, sticky=NW)

rn50x64_text = Entry(frame1, textvariable=get_text('RN50x64'), width=8)
rn50x64_text.grid(row=8, column=3, pady=5, padx=2, sticky=NW)

sampling_mode = Label(frame1, text='Sampling Mode:')
sampling_mode.grid(row=9, column=0, pady=5, padx=2, sticky=NW)

sampling_mode_text = Entry(frame1, textvariable=get_text('sampling_mode'), width=8)
sampling_mode_text.grid(row=9, column=1, pady=5, padx=2, sticky=NW)

set_seed = Label(frame1, text='Set Seed:')
set_seed.grid(row=9, column=2, pady=5, padx=2, sticky=NW)

set_seed_text = Entry(frame1, textvariable=get_text('set_seed'), width=8)
set_seed_text.grid(row=9, column=3, pady=5, padx=2, sticky=NW)

save = Button(frame1,text='Save Settings', command=save_text).grid(row=1000, column=0)

run = Button(frame1,text='Run', command=run_thread).grid(row=1000, column=1)

window.title('ProgRockDiffusion (PRD): '+json_set['batch_name'])

window.mainloop()
