To use this script simply copy some text (doesn't matter how much) to the clipboard.

Once copied, run the script and you'll be asked to specify which text you want to REPLACE.

You'll then be asked for the text you'd like to replace this with.

After hitting enter, the replacement will be carried out and the new block of text will be copied back to your clipboard automatically.

EXAMPLE:

Original Text: Bob is the best!

$ python text_replacer.py 
What would you like to replace? Bob
And what would you like to replace it with? Julian
The new string is now copied to the clipboard. Hit CTRL V to paste.

New Text: Julian is the best!


USE CASE:

There are many use cases, especially at work where a hostname might change and you have to update a document etc.

One other situation that came in handy recently was to remove all spaces in a string. This would be done by simply entering a SPACE when choosing what to replace then not entering anything at all at the replacement prompt.
