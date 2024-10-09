# Author  : Jonathan Ramos
# Date    : 10/08/24
# Purpose : Launch a map in the browser given an address

import webbrowser, sys, pyperclip

# Obtain address from CLI
if len(sys.argv) > 1:
  address = ''.join(sys.argv[1:]) 
else:
  address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/' + address)
