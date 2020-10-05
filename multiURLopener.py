"""
Simple module that utilizes a text file with links 
"""


import webbrowser

webbrowser.register('brave',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//BraveSoftware//Brave-Browser//Application//brave.exe"))
def multiURLopener(txt):
    f= open(txt, "r")
    for x in f:
        webbrowser.get("brave").open_new_tab(x)