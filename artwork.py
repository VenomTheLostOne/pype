from colorama import Fore, Back, Style


line1 = " ____  _  _  ____  ____    ____  _  _   __   ____  ____ "
line2 = "(  _ \( \/ )(  _ \(  __)  / ___)/ )( \ / _\ (  _ \(  __)"
line3 = " ) __/ )  /  ) __/ ) _)   \___ \) __ (/    \ )   / ) _) "
line4 = "(__)  (__/  (__)  (____)  (____/\_)(_/\_/\_/(__\_)(____)"

line5 = " ____ ____ ____ ____ _________ ____ ____ _________ ____ ____ ____ ____ ____ "
line6 = "||M |||a |||d |||e |||       |||b |||y |||       |||V |||e |||n |||o |||m ||"
line7 = "||__|||__|||__|||__|||_______|||__|||__|||_______|||__|||__|||__|||__|||__||"
line8 = "|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|"



#printing the lines with different colors
# print(Fore.RED + line1)
# print(Fore.GREEN + line2)
# print(Fore.YELLOW + line3)
# print(Fore.BLUE + line4)
# print(Style.RESET_ALL)



class artwork():
    def print(self):
        print(Fore.RED + line1)
        print(Fore.GREEN + line2)
        print(Fore.YELLOW + line3)
        print(Fore.BLUE + line4)
        print(Style.RESET_ALL)
        print("----------------------------------------------")
        print(Fore.RED + line5)
        print(Fore.GREEN + line6)
        print(Fore.YELLOW + line7)
        print(Fore.BLUE + line8)
        print(Style.RESET_ALL)
        print("----------------------------------------------")
        
        
        
        

