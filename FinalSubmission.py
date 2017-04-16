# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 18:15:37 2016

@author: pi
"""

import binascii #to convert file to hex code 
import matplotlib.pyplot as plt #for matplotlib 
import numpy as np 
import Tkinter as tk #to make the window
from scipy.stats import gaussian_kde #to get the frequency of the points 
from pyknon.genmidi import Midi #convert the numbers to notes 
import pygame as pg #midi player 
from pyknon.music import NoteSeq #takes notes and forms sequences 

class Example(tk.Frame):
    def __init__(self, parent): 
        tk.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.prompt = tk.Label(self, text="Enter a file ", anchor="w")
        self.entry = tk.Entry(self)
        self.submit = tk.Button(self, text="Submit", command = self.visualize)

        self.play = tk.Button(self, text="Play Audio",command = self.quit)
        self.output = tk.Label(self, text="")

        # lay the widgets out on the screen.
        self.prompt.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x", padx=20)
        self.output.pack(side="top", fill="x", expand=True)
		
        self.output.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="right")
        self.play.pack
    def visualize(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation

		ig = str(self.entry.get())
		while(ig != "x" or "X"):
				try:
					with open(ig, 'rb') as f:
						content = f.read()
					s = binascii.hexlify(content) #turn file to binary
					s = list(s) #lists the binary




					for n,i in enumerate(s): #turn the number to individual characters
						if i=='a': #turn the numbers from hex to regular
							s[n]='10'
						if i=='b':
							s[n]='11'
						if i=='c':
							s[n]='12'
						if i=='d':
							s[n]='13'
						if i=='e':
							s[n]='14'
						if i=='f':
							s[n]='15'
						if i=='g':
							s[n]='16'
					l =[] #make 2 lists
					e = []
					s = map(int, s)
					for x in range (0,len(s)/2): #add all the numbers in the list from 0 to half to list l
						l.extend([s[x]])
					for x in range (len(s)/2,len(s)): #add all the numbers in the list from 0 to half to list e
						e.extend([s[x]])

        				le = np.vstack([l,e])
        				z = gaussian_kde(le)(le)
        				fig, ax = plt.subplots()



					plt.axis([-1, 17, -1, 17]) #set limits


					ax.scatter(l, e, c = z, edgecolor = '')
#

					plt.show()
					s1 = map(str,s)

					notes = []

					for n in s:
						n = str(n)
						if n == "0" or n == "1":
							notes.append("C")
						if n == '2' or n == '3':
							notes.append("D")
						if n == '4' or n == '5':
							notes.append("E")
						if n == '6' or n == '7':
							notes.append("F")
						if n == '8' or n == '9':
							notes.append("G")
						if n == '10' or n == '11':
							notes.append("A")
						if n == '12' or n == '13':
							notes.append("B")
						if n == '14' or n == '15' or n == '16' :
							notes.append("C")


					midi1 = " ".join(notes)
					#midi1 = "A B C D "
					notes1 = NoteSeq(midi1)
					midi = Midi(1, tempo=200)
					midi.seq_notes(notes1, track=0)
					midi.write("demo.mid")
					def play_music(music_file):

				#    stream music with mixer.music module in blocking manner
				#    this will stream the sound from disk while playing

						clock = pg.time.Clock()
						try:
							pg.mixer.music.load(music_file)
							print("Music file {} loaded!".format(music_file))
						except pygame.error:
							print("File {} not found! {}".format(music_file, pg.get_error()))
							return
						pg.mixer.music.play()
				    # check if playback has finished
						while pg.mixer.music.get_busy():
							clock.tick(30)
				# pick a midi or MP3 music file you have in the working folder
				# or give full pathname
					music_file = "demo.mid"
				#music_file = "Drumtrack.mp3"
					freq = 44100    # audio CD quality
					bitsize = -16   # unsigned 16 bit
					channels = 2    # 1 is mono, 2 is stereo
					buffer = 2048   # number of samples (experiment to get right sound)
					pg.mixer.init(freq, bitsize, channels, buffer)
				# optional volume 0 to 1.0
					pg.mixer.music.set_volume(0.8)
					try:
						play_music(music_file)
					except KeyboardInterrupt:
				    # if user hits Ctrl/C then exit
				    # (works only in console mode)
						pg.mixer.music.fadeout(1000)
						pg.mixer.music.stop()
						raise SystemExit

					break;

				except(IOError):
					self.output.configure("Try again")
				self.output.configure(text=ig)




# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
