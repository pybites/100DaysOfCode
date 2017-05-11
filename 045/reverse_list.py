#!python3
#reverse_list.py is a quick script to reverse the order of a list copied to the clipboard

import pyperclip

def paste_from_clipboard():
	text = pyperclip.paste().split("\r")
	return text
	
def copy_to_clipboard(new_list):
	new_list[-1] = '\n' + new_list[-1]
	new_text = ''.join(new_list)
	pyperclip.copy(new_text)
	print("The new string is now copied to the clipboard. Hit CTRL V to paste.")
	
def reverse_list(text_list):
	text_list.reverse()
	return text_list

if __name__ == "__main__":
	new_list = reverse_list(paste_from_clipboard())
	copy_to_clipboard(new_list)
