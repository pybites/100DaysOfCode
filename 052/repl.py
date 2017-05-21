# code from PyCon talk 'Awesome Commandline Tools by Amjith'
# https://speakerdeck.com/amjith/awesome-commandline-tools
# by https://twitter.com/amjithr
import sys

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
from pygments.lexers.sql import SqlLexer

SQLCompleter = WordCompleter(['select', 'show', 'from', 'insert', 'update',
                              'delete', 'drop', 'where'], ignore_case=True)

while 1:
    try:
        user_input = prompt(u'SQL>',
                        history=FileHistory('history.txt'),
                        auto_suggest=AutoSuggestFromHistory(),
                        completer=SQLCompleter,
                        lexer=SqlLexer,
                        )
        print(user_input)
    except (EOFError, KeyboardInterrupt):
        print('Goodbye!')
        sys.exit()
