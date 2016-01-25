'''
Author: Mossein King --Mk--
Using module termcolor
Visit README.md for more information on the module or on how to install the package

'''

from termcolor import colored, cprint

text =colored("Hi, My name is ", 'blue') + colored("Mossein King\n", 'red', attrs=['bold']) + colored("I am your guide to using this module\n", 'yellow', attrs=['dark', 'underline'])
thanks = colored("GIve thanks to the developer of this module\n", 'white', 'on_grey')
info = colored("For more information visit ", 'magenta') + colored("https://pypi.python.org/pypi/termcolor", 'blue', attrs=['bold', 'underline'])
print text + thanks + info

 
