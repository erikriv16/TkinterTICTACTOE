from tkinter import *
from tkinter import messagebox

BLUE = "#27374D"
BLUE_GRAY = "#526D82"
LIGHT_BLUE_GRAY = "#9DB2BF"
LIGHT_GRAY = "#DDE6ED"
RED = "#B70404"
BLACK ="#080202"





class TicTacToe:
    def __init__(self):
        self.master = Tk()
        self.master.title("TicTacToe")
        self.master.geometry("720x720")
        self.master.config(bg=BLUE)

        self.labelStart = self.createInitalLabel()

        self.TICTACTOEFrame = self.createTICframe()

        self.create3x3grid()

        self.playerButtonCount = 0
        
        self.TIC_TAC_TOE = [

            [None, None, None],
            [None, None, None],
            [None, None, None]

        ]






    def createTICframe(self):      #creating and adding frame that will hold 3x3 buttons for game
        frame = LabelFrame(self.master, background="white", width=360, height=360)
        frame.pack(pady=50)
        return frame
    
    def createInitalLabel(self):   #creating and adding label that says tictactoe at top of screen 
        label = Label(self.master, text="TicTacToe", bg=BLUE, fg=LIGHT_GRAY, font=("Arial", 25), pady=20)
        label.pack()
        return label

    def create3x3grid(self):
        self.button1 = Button(self.TICTACTOEFrame, text="0", width=120, height=120, bg="white", command=lambda:self.buttonOnePress(0, 0))
        self.button1.place(x=0, y=0)
        self.button2 = Button(self.TICTACTOEFrame, text="0", width=120, height=120, bg="white", command=lambda:self.buttonTwoPress(0, 1))
        self.button2.place(x=120, y=0)
        self.button3 = Button(self.TICTACTOEFrame, text="0", width=120, height=120, bg="white", command=lambda:self.buttonThreePress(0, 2))
        self.button3.place(x=240, y=0)
        self.button4 = Button(self.TICTACTOEFrame, text="0", width=120, height=120, bg="white", command=lambda:self.buttonFourPress(1, 0))
        self.button4.place(x=0, y=120)
        self.button5 = Button(self.TICTACTOEFrame, text="0", width=120, height=120, bg="white", command=lambda:self.buttonFivePress(1, 1))
        self.button5.place(x=120, y=120)
        self.button6 = Button(self.TICTACTOEFrame, text="0", width=120, height=120, bg="white", command=lambda:self.buttonSixPress(1, 2))
        self.button6.place(x=240, y=120)
        self.button7 = Button(self.TICTACTOEFrame, text="0", width=120, height=120, bg="white", command=lambda:self.buttonSevenPress(2, 0))
        self.button7.place(x=0, y=240)
        self.button8 = Button(self.TICTACTOEFrame, text="0", width=120, height=120, bg="white", command=lambda:self.buttonEightPress(2, 1))
        self.button8.place(x=120, y=240)
        self.button9 = Button(self.TICTACTOEFrame, text="0", width=120, height=120, bg="white", command=lambda:self.buttonNinePress(2, 2))
        self.button9.place(x=240, y=240)


    def buttonOnePress(self, x, y):
        if self.button1.cget("bg") == "white":
            if self.playerButtonCount % 2 == 0:
                self.button1.config(bg=RED)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 1)
                self.playerOneCheck()
                self.tie()

            else:
                self.button1.config(bg=BLACK)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 2)
                self.playerTwoCheck()
                self.tie()

    def buttonTwoPress(self, x, y):
        if self.button2.cget("bg") == "white":
            if self.playerButtonCount % 2 == 0:
                self.button2.config(bg=RED)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 1)
                self.playerOneCheck()
                self.tie()

            else:
                self.button2.config(bg=BLACK)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 2)
                self.playerTwoCheck()
                self.tie()

    def buttonThreePress(self, x, y):
        if self.button3.cget("bg") == "white":
            if self.playerButtonCount % 2 == 0:
                self.button3.config(bg=RED)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 1)
                self.playerOneCheck()
                self.tie()

            else:
                self.button3.config(bg=BLACK)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 2)
                self.playerTwoCheck()
                self.tie()

    def buttonFourPress(self, x, y):
        if self.button4.cget("bg") == "white":
            if self.playerButtonCount % 2 == 0:
                self.button4.config(bg=RED)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 1)
                self.playerOneCheck()
                self.tie()

            else:
                self.button4.config(bg=BLACK)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 2)
                self.playerTwoCheck()
                self.tie()

    def buttonFivePress(self, x, y):
        if self.button5.cget("bg") == "white":
            if self.playerButtonCount % 2 == 0:
                self.button5.config(bg=RED)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 1)
                self.playerOneCheck()
                self.tie()

            else:
                self.button5.config(bg=BLACK)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 2)
                self.playerTwoCheck()
                self.tie()

    def buttonSixPress(self, x, y):
        if self.button6.cget("bg") == "white":
            if self.playerButtonCount % 2 == 0:
                self.button6.config(bg=RED)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 1)
                self.playerOneCheck()
                self.tie()

            else:
                self.button6.config(bg=BLACK)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 2)
                self.playerTwoCheck()
                self.tie()

    def buttonSevenPress(self, x, y):
        if self.button7.cget("bg") == "white":
            if self.playerButtonCount % 2 == 0:
                self.button7.config(bg=RED)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 1)
                self.playerOneCheck()
                self.tie()

            else:
                self.button7.config(bg=BLACK)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 2)
                self.playerTwoCheck()
                self.tie()

    def buttonEightPress(self, x, y):
        if self.button8.cget("bg") == "white":
            if self.playerButtonCount % 2 == 0:
                self.button8.config(bg=RED)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 1)
                self.playerOneCheck()
                self.tie()

            else:
                self.button8.config(bg=BLACK)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 2)
                self.playerTwoCheck()
                self.tie()

    def buttonNinePress(self, x, y):
        if self.button9.cget("bg") == "white":
            if self.playerButtonCount % 2 == 0:
                self.button9.config(bg=RED)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 1)
                self.playerOneCheck()
                self.tie()

            else:
                self.button9.config(bg=BLACK)
                self.playerButtonCount += 1
                self.update2Darray(x, y, 2)
                self.playerTwoCheck()
                self.tie()


    def tie(self):
        if self.playerButtonCount >= 9:
            self.master.quit()


    def update2Darray(self, x, y, playerNum):
        self.TIC_TAC_TOE[x][y] = playerNum
        print(self.TIC_TAC_TOE)


    def playerOneCheck(self):
        playerOneWins = False
        if self.equals3(self.TIC_TAC_TOE[0][0], self.TIC_TAC_TOE[0][1], self.TIC_TAC_TOE[0][2]):
            playerOneWins = True
        
        elif self.equals3(self.TIC_TAC_TOE[1][0], self.TIC_TAC_TOE[1][1], self.TIC_TAC_TOE[1][2]):
            playerOneWins = True

        elif self.equals3(self.TIC_TAC_TOE[2][0], self.TIC_TAC_TOE[2][1], self.TIC_TAC_TOE[2][2]):
            playerOneWins = True

        elif self.equals3(self.TIC_TAC_TOE[0][0], self.TIC_TAC_TOE[1][0], self.TIC_TAC_TOE[2][0]):
            playerOneWins = True

        elif self.equals3(self.TIC_TAC_TOE[0][1], self.TIC_TAC_TOE[1][1], self.TIC_TAC_TOE[2][1]):
            playerOneWins = True

        elif self.equals3(self.TIC_TAC_TOE[0][2], self.TIC_TAC_TOE[1][2], self.TIC_TAC_TOE[2][2]):
            playerOneWins = True

        elif self.equals3(self.TIC_TAC_TOE[0][0], self.TIC_TAC_TOE[1][1], self.TIC_TAC_TOE[2][2]):
            playerOneWins = True

        elif self.equals3(self.TIC_TAC_TOE[0][2], self.TIC_TAC_TOE[1][1], self.TIC_TAC_TOE[2][0]):
            playerOneWins = True

        if playerOneWins == True:
            self.resetGame()
            print(self.TIC_TAC_TOE)
            messagebox.showinfo("Winner!", "Player 1 wins!")
                


    def playerTwoCheck(self):
        playerTwoWins = False
        if self.equals3(self.TIC_TAC_TOE[0][0], self.TIC_TAC_TOE[0][1], self.TIC_TAC_TOE[0][2]):
            playerTwoWins = True
        
        elif self.equals3(self.TIC_TAC_TOE[1][0], self.TIC_TAC_TOE[1][1], self.TIC_TAC_TOE[1][2]):
            playerTwoWins = True

        elif self.equals3(self.TIC_TAC_TOE[2][0], self.TIC_TAC_TOE[2][1], self.TIC_TAC_TOE[2][2]):
            playerTwoWins = True

        elif self.equals3(self.TIC_TAC_TOE[0][0], self.TIC_TAC_TOE[1][0], self.TIC_TAC_TOE[2][0]):
            playerTwoWins = True

        elif self.equals3(self.TIC_TAC_TOE[0][1], self.TIC_TAC_TOE[1][1], self.TIC_TAC_TOE[2][1]):
            playerTwoWins = True

        elif self.equals3(self.TIC_TAC_TOE[0][2], self.TIC_TAC_TOE[1][2], self.TIC_TAC_TOE[2][2]):
            playerTwoWins = True

        elif self.equals3(self.TIC_TAC_TOE[0][0], self.TIC_TAC_TOE[1][1], self.TIC_TAC_TOE[2][2]):
            playerTwoWins = True

        elif self.equals3(self.TIC_TAC_TOE[0][2], self.TIC_TAC_TOE[1][1], self.TIC_TAC_TOE[2][0]):
            playerTwoWins = True 

        if playerTwoWins == True:
            self.resetGame()
            print(self.TIC_TAC_TOE)
            messagebox.showinfo("Winner!", "Player 2 wins!")

                


    def resetGame(self):
        for i in range(3):
            for j in range(3):
                self.TIC_TAC_TOE[i][j] = None

        self.button1.config(bg="white")
        self.button2.config(bg="white")
        self.button3.config(bg="white")
        self.button4.config(bg="white")
        self.button5.config(bg="white")
        self.button6.config(bg="white")
        self.button7.config(bg="white")
        self.button8.config(bg="white")
        self.button9.config(bg="white")

        self.playerButtonCount = 0


    def equals3(self, a, b, c):
        if isinstance(a, int):
            return (a == b and b == c)


    def run(self):
        self.master.mainloop()




tictactoe1 = TicTacToe()
tictactoe1.run()
