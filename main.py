import logging
import random
import customtkinter as ctk
import colors as clr


log = logging.getLogger(__name__)
logging.basicConfig(filename='log.log', level=logging.INFO,)

fluff = clr.clrs

frost_fox = random.choices(clr.clrs, weights=clr.wet, k=1)[0]

colorCount = [
    0, #red
    0, #orange
    0, #yellow
    0, #green
    0, #blue
    0, #purple
    0, #brown
    0, #white
    0, #black
]

print(colorCount)


class Main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x720")
        try:

            self.bluecolorcount = 0
            self.purplecolorcount = 0
            self.browncolorcount = 0

            self.rainbowframe = ctk.CTkFrame(master=self.root, bg_color='black', fg_color=frost_fox, width=500, height=500)
            self.rainbowframe.pack(fill="both", expand=True)


            self.secondFrame = ctk.CTkFrame(master=self.root, bg_color="black", fg_color="black", width=500, height=500)
            self.secondFrame.pack(fill="both", expand=True)


            self.sideone = ctk.CTkLabel(master=self.secondFrame, bg_color="black", width=300, height=100, fg_color="black",text="")
            self.sideone.pack(side = "left", expand=False)

            self.textbox = ctk.CTkTextbox(master=self.secondFrame, corner_radius=0, text_color="white", fg_color="black", width=300, height=100)
            self.textbox.pack(side = "left", expand=True)

            self.sidetwo = ctk.CTkLabel(master=self.secondFrame, bg_color="black", width=300, height=100, fg_color="black",text="")
            self.sidetwo.pack(side = "left", expand=False)

            self.side03 = ctk.CTkLabel(master=self.root, bg_color="black", width=10, height=10, fg_color="green",text="")
            self.side03.pack(fill = "both", expand=True)

            self.button = ctk.CTkButton(master=self.root,command=self.colorchange,width=100,height=100, fg_color="blue", text_color="white", text=frost_fox, state="normal", border_width=2, border_color="light blue")
            self.button.pack(fill='both', expand=False)

            self.side04 = ctk.CTkLabel(master=self.root, bg_color="black", width=10, height=10, fg_color="green",text="")
            self.side04.pack(fill = "both", expand=True)

            self.colorsframe = ctk.CTkFrame(master=self.root, bg_color = "black", fg_color= "black", width=900, height=100)
            self.colorsframe.pack(fill="both", expand=False)

            self.redframe = ctk.CTkFrame(master=self.colorsframe, bg_color="black", fg_color="black", width=100, height=100)
            self.redframe.pack(side="left", expand=False)
            self.redlabel = ctk.CTkLabel(master=self.redframe, bg_color="red", fg_color="red", text_color="black", text = f'\n{colorCount[0]}', width=50, height=5)
            self.redlabel.pack(fill="both", expand=True)
            self.orangeframe = ctk.CTkFrame(master=self.colorsframe, bg_color="black", fg_color="black", width=100, height=100)
            self.orangeframe.pack(side="left", expand=False)
            self.orangelabel = ctk.CTkLabel(master=self.orangeframe, bg_color="orange", fg_color="orange", text_color="black", text = f'\n{colorCount[1]}', width=50, height=5)
            self.orangelabel.pack(fill="both", expand=True)
            self.yellowframe = ctk.CTkFrame(master=self.colorsframe, bg_color="black", fg_color="black", width=100, height=100)
            self.yellowframe.pack(side="left", expand=False)
            self.yellowlabel = ctk.CTkLabel(master=self.yellowframe, bg_color="yellow", fg_color="yellow", text_color="black", text = f'\n{colorCount[2]}', width=50, height=5)
            self.yellowlabel.pack(fill="both", expand=True)
            self.greenframe = ctk.CTkFrame(master=self.colorsframe, bg_color="black", fg_color="black", width=100, height=100)
            self.greenframe.pack(side="left", expand=False)
            self.greenlabel = ctk.CTkLabel(master=self.greenframe, bg_color="green", fg_color="green", text_color="black", text = f'\n{colorCount[3]}', width=50, height=5)
            self.greenlabel.pack(fill="both", expand=True)
            self.blueframe = ctk.CTkFrame(master=self.colorsframe, bg_color="black", fg_color="black", width=100, height=100)
            self.blueframe.pack(side="right", expand=False)
            self.bluelabel = ctk.CTkLabel(master=self.blueframe, bg_color="blue", fg_color="blue", text_color="black", text = f'\n{self.bluecolorcount}', width=50, height=5)
            self.bluelabel.pack(fill="both", expand=True)
            self.purpleframe = ctk.CTkFrame(master=self.colorsframe, bg_color="black", fg_color="black", width=100, height=100)
            self.purpleframe.pack(side="right", expand=False)
            self.purplelabel = ctk.CTkLabel(master=self.purpleframe, bg_color="purple", fg_color="purple", text_color="black", text = f'\n{self.purplecolorcount}', width=50, height=5)
            self.purplelabel.pack(fill="both", expand=True)
            self.brownframe = ctk.CTkFrame(master=self.colorsframe, bg_color="black", fg_color="black", width=100, height=100)
            self.brownframe.pack(side="right", expand=False)
            self.brownlabel = ctk.CTkLabel(master=self.brownframe, bg_color="brown", fg_color="brown", text_color="black", text = f'\n{self.browncolorcount}', width=50, height=5)
            self.brownlabel.pack(fill="both", expand=True)
            self.blackframe = ctk.CTkFrame(master=self.colorsframe, bg_color="black", fg_color="black", width=100, height=100)
            self.blackframe.pack(side="right", expand=False)
            self.blacklabel = ctk.CTkLabel(master=self.blackframe, bg_color="black", fg_color="black", text_color="white", text = f'\n{colorCount[8]}', width=50, height=5)
            self.blacklabel.pack(fill="both", expand=True)
            self.whiteframe = ctk.CTkFrame(master=self.colorsframe, bg_color="black", fg_color="black", width=100, height=100)
            self.whiteframe.pack(side="right", expand=False)
            self.whitelabel = ctk.CTkLabel(master=self.whiteframe, bg_color="white", fg_color="white", text_color="black", text = f'\n{colorCount[7]}', width=50, height=5,)
            self.whitelabel.pack(fill="both", expand=True)

            self.finalFrame = ctk.CTkFrame(master=self.root, bg_color = "black", fg_color= "black", width=100, height=100)
            self.finalFrame.pack(fill="both", expand=True)

        except Exception as e:
            log.info(f'self.__init__: {e}')
            print(f'self.__init__: {e}')


    def colorchange(self):

        try:
            self.button.configure(state='disabled',text_color_disabled=frost_fox, )
            somefluff = self.rainbowframe.cget('fg_color')

            if fluff[0] == somefluff:
                colorCount[8] -= 3

                print(colorCount)
                colorCount[0] += 4
                print(f'\n colorcount = {colorCount[0]}')
                print(colorCount)
                print(f'\n WAS RED. RED COLOR COUNT = {colorCount[0]}')
                self.button.configure(text="red", )
                self.redlabel.configure(text=f'{colorCount[0]}', )
                self.blacklabel.configure(text=colorCount[8], )
                self.textbox.insert("0.0", F'\n WAS RED. RED COLOR COUNT = {colorCount[0]}')
            else:
                if fluff[1] == somefluff:
                    colorCount[1] += 4
                    colorCount[8] -= 3
                    print(f'\n WAS ORANGE. ORANGE COLOR COUNT = {colorCount[1]}')
                    self.button.configure(text="orange", )
                    self.orangelabel.configure(text=colorCount[1], )
                    self.blacklabel.configure(text=colorCount[8], )
                    self.textbox.insert("0.0", F'\n WAS ORANGE. ORANGE COLOR COUNT = {colorCount[1]}')

                else:
                    if fluff[2] == somefluff:
                        colorCount[2] += 4
                        colorCount[8] -= 3
                        print(F'\n WAS YELLOW. YELLOW COLOR COUNT = {colorCount[2]}')
                        self.button.configure( text="yellow", )
                        self.yellowlabel.configure(text=colorCount[2], )
                        self.blacklabel.configure(text=colorCount[8], )
                        self.textbox.insert("0.0", F'\n WAS YELLOW. YELLOW COLOR COUNT = {colorCount[2]}')
                    else:
                        if fluff[3] == somefluff:
                            colorCount[3] += 4
                            colorCount[8] -= 3
                            print(F'\n WAS GREEN. GREEN COLOR COUNT = {colorCount[3]}')
                            self.button.configure(text="green", )
                            self.greenlabel.configure(text=colorCount[3], )
                            self.blacklabel.configure(text=colorCount[8], )
                            self.textbox.insert("0.0", F'\n WAS GREEN. GREEN COLOR COUNT = {colorCount[3]}')
                        else:
                            if fluff[4] == somefluff:
                                self.bluecolorcount += 4
                                colorCount[8] -= 3
                                print(F'\n WAS BLUE. BLUE COLOR COUNT = {self.bluecolorcount}')
                                self.button.configure(text="blue", )
                                self.bluelabel.configure(text=self.bluecolorcount, )
                                self.blacklabel.configure(text=colorCount[8], )
                                self.textbox.insert("0.0", F'\n WAS BLUE. BLUE COLOR COUNT = {self.bluecolorcount}')
                            else:
                                if fluff[5] == somefluff:
                                    self.purplecolorcount += 4
                                    colorCount[8] -= 3
                                    print(F'\n WAS PURPLE. PURPLE COLOR COUNT = {self.purplecolorcount}')
                                    self.button.configure(text="purple", )
                                    self.purplelabel.configure(text=self.purplecolorcount, )
                                    self.blacklabel.configure(text=colorCount[8], )
                                    self.textbox.insert("0.0", F'\n WAS PURPLE. PURPLE COLOR COUNT = {self.purplecolorcount}')
                                else:
                                    if fluff[6] == somefluff:
                                        self.browncolorcount += 4
                                        colorCount[8] -= 3
                                        print(F'\n WAS BROWN. BROWN COLOR COUNT = {self.browncolorcount}')
                                        self.button.configure(text="brown", )
                                        self.brownlabel.configure(text=self.browncolorcount, )
                                        self.blacklabel.configure(text=colorCount[8], )
                                        self.textbox.insert("0.0", F'\n WAS BROWN. BROWN COLOR COUNT = {self.browncolorcount}')
                                    else:
                                        print('boop')

                                        if fluff[7] == somefluff:
                                            colorCount[8] += 8
                                            colorCount[0] -= 4
                                            colorCount[1] -= 4
                                            colorCount[2] -= 4
                                            colorCount[3] -= 4
                                            self.bluecolorcount -= 4
                                            self.purplecolorcount -= 4
                                            self.browncolorcount -= 4

                                            colorCount[7] -= 4
                                            self.textbox.insert("0.0", F'\n WAS BLACK. BLACK COLOR COUNT = {colorCount[8]}')


                                            self.redlabel.configure(text=colorCount[0], )
                                            self.orangelabel.configure(text=colorCount[1], )
                                            self.yellowlabel.configure(text=colorCount[2], )
                                            self.greenlabel.configure(text=colorCount[3], )
                                            self.bluelabel.configure(text=self.bluecolorcount, )
                                            self.purplelabel.configure(text=self.purplecolorcount, )
                                            self.brownlabel.configure(text=self.browncolorcount, )

                                            self.blacklabel.configure(text=colorCount[8], )
                                            self.whitelabel.configure(text=colorCount[7], )

                                            print(F'\n WAS BLACK. BLACK COLOR COUNT = {colorCount[8]}')
                                            self.button.configure(text="black", )

                                        else:
                                            if fluff[8] == somefluff:
                                                colorCount[7] += 4
                                                colorCount[8] -= 3

                                                print(F'\n WAS WHITE. WHITE COLOR COUNT = {colorCount[7]}')
                                                self.button.configure(text="white", )
                                                self.whitelabel.configure(text=colorCount[7], )
                                                self.blacklabel.configure(text=colorCount[8], )
                                                self.textbox.insert("0.0",F'\n WAS WHITE. WHITE COLOR COUNT = {colorCount[7]}')
                                            else:
                                                print('f')
                                            print(somefluff)
                                            self.changingGuard()
                                            print(f'\n NOW = {self.rainbowframe.cget('fg_color')}')
            self.changingGuard()
            self.chancerising()
        except Exception as e:
            log.info(f'self.colorchange: {e}')
            print(f'self.colorchange: {e}')
        self.root.after(1000, self.colorchange)


    def changingGuard(self):
        try:
            self.rainbowframe.configure(fg_color=random.choice(clr.clrs))
        except Exception as e:
            log.info(f'self.changingGuard: {e}')
            print(f'self.changingGuard: {e}')


    def chancerising(self):
        try:
            if colorCount[8] <= -100:
                colorCount[8] = 0
                colorCount[0] = 0
                colorCount[1] = 0
                colorCount[2] = 0
                colorCount[3] = 0
                self.bluecolorcount = 0
                self.purplecolorcount = 0
                self.browncolorcount = 0
                colorCount[7] = 0
                self.redlabel.configure(text=colorCount[0], )
                self.orangelabel.configure(text=colorCount[1], )
                self.yellowlabel.configure(text=colorCount[2], )
                self.greenlabel.configure(text=colorCount[3], )
                self.bluelabel.configure(text=self.bluecolorcount, )
                self.purplelabel.configure(text=self.purplecolorcount, )
                self.brownlabel.configure(text=self.browncolorcount, )
                self.blacklabel.configure(text=colorCount[8], )
                self.whitelabel.configure(text=colorCount[7], )
            else:
                print('f')
        except Exception as e:
            log.info(f'self.chancerising: {e}')
            print(f'self.chancerising: {e}')
        self.root.after(1000, self.chancerising)

if __name__ == "__main__":
    root = ctk.CTk()
    app = Main(root)
    root.mainloop()
