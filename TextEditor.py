import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry("1200x800")
main_application.title("Text editor")

######################## Main Menu ############################# 
main_menu    =  tk.Menu()

#file Icons

new_icon     =  tk.PhotoImage(file='icons2/new.png')
open_icon    =  tk.PhotoImage(file='icons2/open.png')
save_icon    =  tk.PhotoImage(file='icons2/save.png')
save_as_icon =  tk.PhotoImage(file='icons2/save_as.png')
exit_icon    =  tk.PhotoImage(file='icons2/exit.png')

file         =  tk.Menu(main_menu , tearoff=False )



#-------------------------------------------------------------------------------------

#edit icons
copy_icon      = tk.PhotoImage(file='icons2/copy.png')
paste_icon     = tk.PhotoImage(file='icons2/paste.png')
cut_icon       = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon      = tk.PhotoImage(file='icons2/find.png')



edit         =  tk.Menu(main_menu , tearoff=False)


#----------------------------------------------------------------------------------------
#View icons
tool_bar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='icons2/status_bar.png')


view =  tk.Menu(main_menu , tearoff=False)



#-----------------------------------------------------------------------------------
#color icons
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon    = tk.PhotoImage(file='icons2/light_plus.png')
monokai_icon       = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon    = tk.PhotoImage(file='icons2/night_blue.png')
red_icon           = tk.PhotoImage(file='icons2/red.png')
dark_icon          = tk.PhotoImage(file='icons2/dark.png')

color_theme  =  tk.Menu(main_menu , tearoff=False)


theme_choice=tk.StringVar()

color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

color_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red': ('#2d2d2d','#ffe8e8'),
    'Monokai' :('#d3b774','#474747'),
    'Night Blue' :('#ededed','#6b9dc2')
    }

#----------------------------------------------------------------------------------------


#cascade
main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Color", menu=color_theme)


#----------------------- End Main Menu --------------------------

######################## toolbar #############################

tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

#font box

font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#size box
size_var=tk.IntVar()
font_box=ttk.Combobox(tool_bar,width=12,textvariable=size_var,state='readonly')
font_box['values']=tuple(range(8,81))
font_box.current(4)
font_box.grid(row=0,column=1,padx=5)


#Bold button
bold_icon=tk.PhotoImage(file='icons2/bold.png')
bold_button=ttk.Button(tool_bar,image=bold_icon)
bold_button.grid(row=0,column=2,padx=5)

#talics button
italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_button=ttk.Button(tool_bar,image=italic_icon)
italic_button.grid(row=0,column=3,padx=5)

#underline button
underline_icon=tk.PhotoImage(file='icons2/underline.png')
underline_button=ttk.Button(tool_bar,image=underline_icon)
underline_button.grid(row=0,column=4,padx=5)

#font color button
font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
font_color_button=ttk.Button(tool_bar,image=font_color_icon)
font_color_button.grid(row=0,column=5,padx=5)

#align left
align_left_icon=tk.PhotoImage(file='icons2/align_left.png')
align_left_button=ttk.Button(tool_bar,image=align_left_icon)
align_left_button.grid(row=0,column=6,padx=5)

#align centre
align_center_icon=tk.PhotoImage(file='icons2/align_center.png')
align_center_button=ttk.Button(tool_bar,image=align_center_icon)
align_center_button.grid(row=0,column=7,padx=5)

#align right
align_right_icon=tk.PhotoImage(file='icons2/align_right.png')
align_right_button=ttk.Button(tool_bar,image=align_right_icon)
align_right_button.grid(row=0,column=8,padx=5)


#----------------------- End toolbar --------------------------

######################## editor #############################

text_editor =tk.Text(event=None)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and functionality

current_font_family='Arial'
current_font_size=12

def change_font(event=None):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_fontsize(main_application):
    global currrent_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))



font_box.bind("<<ComboboxSelected>>",change_font)
font_box.bind("<<ComboboxSelected>>",change_fontsize)




##Buttons Functionality

#Bold
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))

    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

bold_button.configure(command=change_bold)    

#italic
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))

    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

italic_button.configure(command=change_italic)

#underline
def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']== 0 :
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))

    if text_property.actual()['underline']== 1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_button.configure(command=change_underline)   


#text_editor.configure(font=('Arial',12))

#change font color function

def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
    

font_color_button.configure(command=change_font_color)


#alignment


def align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_button.configure(command=align_left)


def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_button.configure(command=align_right)


def align_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_button.configure(command=align_center)


#----------------------- End editor --------------------------

######################## Main status bar #############################

status_bar=ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False

def changed(Event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c'))  #.replace(' ','') can be used to not count spaces as characters
        status_bar.configure(text=f'characters:{characters}   Words:{words}')
    text_editor.edit_modified(False)
    

        
text_editor.bind('<<Modified>>',changed)




#----------------------- End Main status bar --------------------------


######################## Main menu function #############################

#new Function

url=''

def new(event=None):
    global url
    url =''
    text_editor.delete(1.0,tk.END)
    

#open function

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select file',filetypes=(('Text File','*txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())

    except FileNotFoundError:
            return
    except:
            return
    main_application.title(os.path.basename(url))
       

# Save file

def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w','utf-8') as fw:
                fw.write(content)

        else:
            url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*txt'),('All Files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()

    except:
        return

#save as
def save_as(event=None):
    global url
    try:
        content2=text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*txt'),('All Files','*.*')))
        url.write(content2)
        url.close()

    except:
        return
    

#exit
    
def exit_fuction(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save the fle?')

            if mbox is  True:
                if url:
                    content=text_editorr.get(1.0,tk.END)
                    with open(url,'w',encode='utf-8') as fw:
                        fw.write(content)
                        main_application.close()
                else:
                    content2= text_editor.get(1.0,tk.END)
                    url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()

            elif mbox is False:
                main_application.destroy()

        else:
            main_application.destroy()

    except:
        return



                    

#file commands
file.add_command(label='New' , image=new_icon , compound=tk.LEFT, accelerator="CTRL+N",command=new)
file.add_command(label='Open' , image=open_icon , compound=tk.LEFT, accelerator="CTRL+O",command=open_file)
file.add_command(label='Save' , image=save_icon , compound=tk.LEFT, accelerator="CTRL+S",command=save_file)
file.add_command(label='Save as' , image=save_as_icon , compound=tk.LEFT, accelerator="CTRL+Alt+S",command=save_as)
file.add_command(label='exit' , image=exit_icon , compound=tk.LEFT,accelerator='Ctlr+Q',command=exit_fuction)



#edit Functions

#find


def find_func(evenet=None):

    def find():
        pass

    def replace():
        pass

    
    find_dialog=tk.Toplevel()
    find_dialog.geometry("480x200+500+200")
    find_dialog.title("Find")
    find_dialog.resizable(0,0)


    #frame
    find_frame=ttk.LabelFrame(find_dialog,text="find/replace")
    find_frame.pack(pady=20)

    #label
    text_find_label=ttk.Label(find_frame,text='Find:')
    text_replace_label=ttk.Label(find_frame,text='Replace:')
    
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
    

    #entry
    find_entry=ttk.Entry(find_frame,width=30)
    replace_entry=ttk.Entry(find_frame,width=30)
    
    find_entry.grid(row=0,column=1,padx=4,pady=4)
    replace_entry.grid(row=1,column=1,padx=4,pady=4)
    

    #button
    find_button=ttk.Button(find_frame,text="Find",command=find)
    replace_button=ttk.Button(find_frame,text="Replace",command=replace)

    find_button.grid(row=0,column=3,padx=4,pady=4)
    replace_button.grid(row=1,column=3,padx=4,pady=4)
    
    

#edit commands
edit.add_command(label='Copy' , image=copy_icon,compound=tk.LEFT ,accelerator="Ctrl+C",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste' , image=paste_icon,compound=tk.LEFT ,accelerator="Ctrl+V",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut' , image=cut_icon,compound=tk.LEFT ,accelerator="Ctrl+X",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All' , image=clear_all_icon,compound=tk.LEFT ,accelerator="Ctrl+Alt+C",command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='Find' , image=find_icon,compound=tk.LEFT ,accelerator="Ctrl+F",command=find_func)

#View Functions

#tool bar
#status bar


#view commands
view.add_checkbutton(label='Tool Bar' ,image=tool_bar_icon,compound=tk.LEFT)
view.add_checkbutton(label='Status Bar', image=status_bar_icon,compound=tk.LEFT)

#color theme functions

#select theme

#color theme commands
count=0
for i in color_dict:
    color_theme.add_checkbutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT)
    count +=1


#----------------------- End Main Menu function --------------------------

main_application.config(menu=main_menu)

main_application.mainloop()
