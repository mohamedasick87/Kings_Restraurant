from tkinter import * 
import subprocess
root = Tk()
root.geometry("400x400")
root.title("MAK RESTRAURANT")

def main():

	subprocess.call(["python","Final_Project.py"])

Button(root,text="Click here",command = main).grid(row=1,column = 5)

root.mainloop()

# 1. Blockchain - 6 weeks
# 2. Android app using kotlin - 8 weeks
# 3. Html - 8 weeks
# 4. Advanced c++ - 4 weeks
# 5. English Grammer for Employability - 4 weeks
# 6. git - 6 weeks
