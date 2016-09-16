import winsound
from tkinter import *
from tkinter import filedialog





class App:
	

	def __init__(self, master):
		field_button_name = StringVar()
		field_button_dir = StringVar()

		dict = {}

		frame_main = Frame(master)
		frame_main.grid(row = 0)
		
		frame_buttons = Frame(master)
		frame_buttons.grid(row = 1)
		
		
		label_name_entry = Label(frame_main, text = "Button Name:")
		label_name_entry.grid(row = 0, column = 0)
			
		button_find_song = Button(frame_main, text = "Select Song",command = lambda : sound_directory())
		button_find_song.grid(row = 1, column = 0)	
			
		entry_name_button = Entry(frame_main, textvariable = field_button_name, width = 40)              ##Field for files
		entry_name_button.grid(row = 0, column = 1)
			
		entry_dir_song = Entry(frame_main, textvariable = field_button_dir, width = 40)
		entry_dir_song.grid(row = 1, column = 1)
		
		button_make_button = Button(frame_main, text = "Make Button", command = lambda : make_new_button())
		button_make_button.grid(row = 0, rowspan =2, column = 2)

		def sound_directory():
			dirName = filedialog.askopenfilename()
			if dirName:
				field_button_dir.set(dirName)
				
		def make_new_button():
			button_new_made = Button(frame_buttons, text = field_button_name.get(), command = lambda : play_sound(dict [field_button_name.get()]))
			button_new_made.pack()
			dict [field_button_name.get()] = field_button_dir.get()
			dict [field_button_name.get()]
		
		def play_sound(sound_name):
			winsound.PlaySound(sound_name, winsound.SND_FILENAME)
			
	
			
root = Tk()

app = App(root)


root.mainloop()


