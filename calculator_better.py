import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title("Calculator")
        self.resultFR, self.num_comps_buttons = self.create_Frames()
        (self.num1, self.num2, self.num3, self.num4, self.num5,
        self.num6, self.num7, self.num8, self.num9, self.num0,
        self.btnplusminus, self.btnequals, self.btnpercent, self.btnfloat, 
        self.btnsqrroot, self.btnclear, self.btnplus, self.btnminus, 
        self.btntimes, self.btndivide) = self.create_BTNS()
        self.resultLabel = self.create_resLabel()
        self.part1_typed = "0"
        self.part2_typed = "0"
        self.part1_cleared = ""
        self.part2_cleared = ""
        self.equation = "0"
        self.result = ""
        self.oper_symbol = ""
        self.counter = {"add_btn": 0, "sub_btn": 0, "times_btn": 0, "div_btn": 0}

    def create_Frames(self):
        resultFR = ttk.Frame(self.window, height=50, width=5, relief="ridge")
        resultFR.grid(row=0, column=0, padx = 5, pady = 5, ipadx=5, ipady=5)
        resultFR.grid_columnconfigure(0, weight=1)
        resultFR.grid_rowconfigure(0, weight=1)

        num_comps_buttons = ttk.Frame(self.window)
        num_comps_buttons.grid(row=1, column=0, padx=5, pady=5)

        return resultFR, num_comps_buttons
    
    def create_resLabel(self):
        resultLabel = tk.Label(self.resultFR, height=2, width=40, 
                               background="WHITE", anchor="e", text="0", font=(20))
        resultLabel.grid(row=0, column=0)

        return resultLabel
    
    def create_BTNS(self):
        num1 = tk.Button(self.num_comps_buttons, text="1", height=3, width=12, command=lambda:self.num1_func())
        num1.grid(row=3, column=0)

        num2 = tk.Button(self.num_comps_buttons, text="2", height=3, width=12, command=lambda:self.num2_func())
        num2.grid(row=3, column=1)

        num3 = tk.Button(self.num_comps_buttons, text="3", height=3, width=12, command=lambda:self.num3_func())
        num3.grid(row=3, column=2)

        num4 = tk.Button(self.num_comps_buttons, text="4", height=3, width=12, command=lambda:self.num4_func())
        num4.grid(row=2, column=0)

        num5 = tk.Button(self.num_comps_buttons, text="5", height=3, width=12, command=lambda:self.num5_func())
        num5.grid(row=2, column=1)

        num6 = tk.Button(self.num_comps_buttons, text="6", height=3, width=12, command=lambda:self.num6_func())
        num6.grid(row=2, column=2)

        num7 = tk.Button(self.num_comps_buttons, text="7", height=3, width=12, command=lambda:self.num7_func())
        num7.grid(row=1, column=0)

        num8 = tk.Button(self.num_comps_buttons, text="8", height=3, width=12, command=lambda:self.num8_func())
        num8.grid(row=1, column=1)

        num9 = tk.Button(self.num_comps_buttons, text="9", height=3, width=12, command=lambda:self.num9_func())
        num9.grid(row=1, column=2)

        num0 = tk.Button(self.num_comps_buttons, text="0", height=3, width=12, command=lambda:self.num0_func())
        num0.grid(row=4, column=1)

        btnplusminus = tk.Button(self.num_comps_buttons, text="+/-", height=3, width=12, command=lambda:self.btnplusminus_func())
        btnplusminus.grid(row=4, column=0)

        btnequals = tk.Button(self.num_comps_buttons, text="=", height=3, width=12, command=lambda:self.btnequals_func())
        btnequals.grid(row=4,column=3)

        btnpercent = tk.Button(self.num_comps_buttons, text="%", height=3, width=12, command=lambda:self.btnpercent_func())
        btnpercent.grid(row=0, column=2)

        btnfloat = tk.Button(self.num_comps_buttons, text=".", height=3, width=12, command=lambda:self.btnfloat_func())
        btnfloat.grid(row=4, column=2)

        btnsqrroot = tk.Button(self.num_comps_buttons, text="√x", height=3, width=12, command=lambda:self.btnsqrroot_func())
        btnsqrroot.grid(row=0, column=1)

        btnclear = tk.Button(self.num_comps_buttons, text="C", height=3, width=12, command=lambda:self.btnclear_func())
        btnclear.grid(row=0, column=0)

        btnplus = tk.Button(self.num_comps_buttons, text="+", height=3, width=12, command=lambda:self.btnplus_func())
        btnplus.grid(row=3, column=3)

        btnminus = tk.Button(self.num_comps_buttons, text="-", height=3, width=12, command=lambda:self.btnminus_func())
        btnminus.grid(row=2, column=3)

        btntimes = tk.Button(self.num_comps_buttons, text="x", height=3, width=12, command=lambda:self.btntimes_func())
        btntimes.grid(row=1, column=3)

        btndivide = tk.Button(self.num_comps_buttons, text="/", height=3, width=12, command=lambda:self.btndivide_func())
        btndivide.grid(row=0, column=3)

        return (num0, num1, num2, num3, num4, num5, num6, num7, num8, num9, btnplusminus, btnequals, btnpercent, btnfloat, btnsqrroot, 
                btnclear, btnplus, btnminus, btntimes, btndivide)
    
    def assign_and_display(self):
        self.invalid_calc()
        if self.oper_symbol == "":
            self.part1_typed = self.equation[:]
            self.resultLabel.config(text=self.part1_typed)
        else:
            self.part2_typed = self.equation[:]
            self.resultLabel.config(text=(self.part1_typed + self.oper_symbol + self.part2_typed))
        if self.result != "":
            if "." in self.result:
                idx = self.result.find(".")
                if (len(self.result[(idx+1):]) == 1) and (self.result[-1] == "0"):
                    self.result = self.result[:-2]
            temp_store = self.result
            self.btnclear_func()
            self.part1_typed = temp_store
            self.resultLabel.config(text=self.part1_typed)

    def has_number(self, var):
        return any(char.isdigit() for char in var if not char.isalpha())

    def invalid_calc(self):
        if "%" in self.equation and self.equation[-1:] != "%":
            self.btnclear_func()
        if (self.oper_symbol == " / ") and (self.part2_cleared == 0):
            self.btnclear_func()
        if (self.oper_symbol != "") and (self.part1_typed != "0"):
            check_valid = self.has_number(self.part1_typed)
            if check_valid is not True:
                self.btnclear_func()
        elif (self.oper_symbol != "") and (self.part2_typed != "0"):
            check_valid = self.has_number(self.part2_typed)
            if check_valid is not True:
                self.btnclear_func()

    def num0_func(self):
        if self.equation != "0" and len(self.equation) < 16:
            self.equation += "0"
            self.assign_and_display()

    def num1_func(self):
        if self.equation == "0":
            self.equation = "1"
            self.assign_and_display()
        elif self.equation != "0" and len(self.equation) < 16:
            self.equation += "1"
            self.assign_and_display()

    def num2_func(self):
        if self.equation == "0":
            self.equation = "2"
            self.assign_and_display()
        elif self.equation != "0" and len(self.equation) < 16:
            self.equation += "2"
            self.assign_and_display()

    def num3_func(self):
        if self.equation == "0":
            self.equation = "3"
            self.assign_and_display()
        elif self.equation != "0" and len(self.equation) < 16:
            self.equation += "3"
            self.assign_and_display()

    def num4_func(self):
        if self.equation == "0":
            self.equation = "4"
            self.assign_and_display()
        elif self.equation != "0" and len(self.equation) < 16:
            self.equation += "4"
            self.assign_and_display()

    def num5_func(self):
        if self.equation == "0":
            self.equation = "5"
            self.assign_and_display()
        elif self.equation != "0" and len(self.equation) < 16:
            self.equation += "5"
            self.assign_and_display()


    def num6_func(self):
        if self.equation == "0":
            self.equation = "6"
            self.assign_and_display()
        elif self.equation != "0" and len(self.equation) < 16:
            self.equation += "6"
            self.assign_and_display()

    def num7_func(self):
        if self.equation == "0":
            self.equation = "7"
            self.assign_and_display()
        elif self.equation != "0" and len(self.equation) < 16:
            self.equation += "7"
            self.assign_and_display()


    def num8_func(self):
        if self.equation == "0":
            self.equation = "8"
            self.assign_and_display()
        elif self.equation != "0" and len(self.equation) < 16:
            self.equation += "8"
            self.assign_and_display()

    def num9_func(self):
        if self.equation == "0":
            self.equation = "9"
            self.assign_and_display()
        elif self.equation != "0" and len(self.equation) < 16:
            self.equation += "9"
            self.assign_and_display()

    def btnclear_func(self):
        self.part1_typed = "0"
        self.part2_typed = "0"
        self.part1_cleared = ""
        self.part2_cleared = ""
        self.result = ""
        self.equation = "0"
        self.oper_symbol = ""
        self.resultLabel.config(text=self.part1_typed)

    def btnfloat_func(self):
        if "." not in self.equation:
            if self.equation == "√" or self.equation == "-":
                self.equation += "0" + "."
                self.assign_and_display()
            else:
                self.equation += "."
                self.assign_and_display()

    def btnplusminus_func(self):
        if "-" not in self.equation:
            if self.equation == "0":
                self.equation = ""
            self.equation = "-" + self.equation
            self.assign_and_display()
        else:
            if self.equation == "-":
                self.equation = "0"
                self.assign_and_display()
            else:
                self.equation = self.equation[1:]
                self.assign_and_display()

    def btnsqrroot_func(self):
        if "√" not in self.equation:
            if self.equation == "0":
                self.equation = ""
            if len(self.equation) == 1 and self.equation[0] == "-":
                self.equation += "√"
                self.assign_and_display()
            elif len(self.equation) > 1 and self.equation[0] == "-" :
                self.equation = self.equation[0] + "√" + self.equation[1:]
                self.assign_and_display()
            else:
                self.equation = "√" + self.equation
                self.assign_and_display()

    def btnpercent_func(self):
        if "%" not in self.equation:
            self.equation = self.equation + "%"
            self.assign_and_display()

    def change_var_type(self, type_switch):
        assert type_switch != ""
        if "." in type_switch:
            type_switch = float(type_switch)
        else:
            type_switch = int(type_switch)
        return type_switch
    
    def strip_symbols(self, og):
        changed = og
        if "-" in changed:
            changed = changed[1:]
        changed = self.calculate_root_and_percent(changed)
        if "-" in og:
            changed = "-" + changed
        return changed
    
    def calculate_root_and_percent(self, eq_part):
        assert eq_part != ""
        if "√" in eq_part and "%" in eq_part:
            eq_part = eq_part[1:-1]
            part_stripped = eq_part
            eq_part = self.change_var_type(eq_part)
            eq_part = eq_part ** (1/2)
            if str(part_stripped) == self.part1_typed[(((len(self.part1_typed)-(len(str(part_stripped)))))-1):-1]:
                eq_part = eq_part / 100
                return str(eq_part)
            else:
                part1perc = self.change_var_type(self.part1_cleared)
                eq_part = part1perc * (eq_part / 100)
                return str(eq_part)
        elif "√" in eq_part:
            eq_part = eq_part[1:]
            eq_part = self.change_var_type(eq_part)
            eq_part = eq_part ** (1/2)
            return str(eq_part)
        elif "%" in eq_part:
            eq_part = eq_part[:-1]
            eq_part = self.change_var_type(eq_part)
            if str(eq_part) == self.part1_typed[(((len(self.part1_typed)-(len(str(eq_part)))))-1):-1]:
                eq_part = eq_part / 100
                return str(eq_part)
            else:
                part1perc = self.change_var_type(self.part1_cleared)
                eq_part = part1perc * (eq_part / 100)
                return str(eq_part)
        else:
            return str(eq_part)
    
    def consecutive_comps(self, comp):
        if self.result == "":
            self.btnequals_func()
        if self.part1_typed == "0" and self.part2_typed == "0":
            self.btnclear_func()
        else:
            temp_save = self.part1_typed
            self.btnclear_func()
            self.part1_typed = temp_save
            self.oper_symbol = comp
            self.assign_and_display()

    def btnplus_func(self):
        if (self.oper_symbol == "") or (self.oper_symbol != " + " and self.part2_typed == "0"):
            self.counter["add_btn"] = 1
            self.oper_symbol = " + "
            self.equation = "0"
            self.assign_and_display()
        elif (self.counter["add_btn"] >= 1) or (self.oper_symbol != " + "):
            self.counter["add_btn"] += 1
            self.consecutive_comps(" + ")

    def btnminus_func(self):
        if (self.oper_symbol == "") or (self.oper_symbol != " - " and self.part2_typed == "0"):
            self.counter["sub_btn"] = 1
            self.oper_symbol = " - "
            self.equation = "0"
            self.assign_and_display()
        elif (self.counter["sub_btn"] >= 1) or (self.oper_symbol != " - "):
            self.counter["sub_btn"] += 1
            self.consecutive_comps(" - ")
    
    def btntimes_func(self):
        if (self.oper_symbol == "") or (self.oper_symbol != " * " and self.part2_typed == "0"):
            self.counter["times_btn"] = 1
            self.oper_symbol = " * "
            self.equation = "0"
            self.assign_and_display()
        elif (self.counter["times_btn"] >= 1) or (self.oper_symbol != " * "):
            self.counter["times_btn"] += 1
            self.consecutive_comps(" * ")
    
    def btndivide_func(self):
        if (self.oper_symbol == "") or (self.oper_symbol != " / " and self.part2_typed == "0"):
            self.counter["div_btn"] = 1
            self.oper_symbol = " / "
            self.equation = "0"
            self.assign_and_display()
        elif (self.counter["div_btn"] >= 1) or (self.oper_symbol != " / "):
            self.counter["div_btn"] += 1
            self.consecutive_comps(" / ")
    
    def btnequals_func(self):
        self.part1_cleared = self.strip_symbols(self.part1_typed)
        self.part2_cleared = self.strip_symbols(self.part2_typed)
        self.part1_cleared = self.change_var_type(self.part1_cleared)
        self.part2_cleared = self.change_var_type(self.part2_cleared)
        if self.oper_symbol == " + ":
            self.result = str(self.part1_cleared + self.part2_cleared)[:16]
            self.assign_and_display()
        elif self.oper_symbol == " - ":
            self.result = str(self.part1_cleared - self.part2_cleared)[:16]
            self.assign_and_display()
        elif self.oper_symbol == " * ":
            self.result = str(self.part1_cleared * self.part2_cleared)[:16]
            self.assign_and_display()
        elif self.oper_symbol == " / ":
            try:
                self.result = str(self.part1_cleared / self.part2_cleared)[:16]
                self.assign_and_display()
            except ZeroDivisionError:
                self.invalid_calc()

if __name__ == "__main__":
    program = Calculator()
    program.window.mainloop()