#!/usr/bin/env python3

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

"""NanamiLang REPL"""

import os
import sys
import atexit
import readline
import argparse
import traceback
from typing import List, Any
from nanamilang import Program
from nanamilang import datatypes
from nanamilang.builtin import Builtin, BuiltinMacro
from nanamilang import __version_string__, __author__

history_file_path = os.path.join(
    os.path.expanduser("~"), ".nanamilang_history")
try:
    readline.read_history_file(history_file_path)
    readline.set_history_length(1000)
except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, history_file_path)

readline.parse_and_bind("tab: complete")


def complete(t: str, s: int):
    """NanamiLang REPL complete() function for GNU readline"""
    vocabulary = Builtin.completions() + BuiltinMacro.completions()
    results: List[Any] = [x for x in vocabulary if x.startswith(t)] + [None]
    return results[s]


readline.set_completer(complete)


def main():
    """NanamiLang REPL Main function"""

    parser = argparse.ArgumentParser('NanamiLang REPL')
    parser.add_argument('--no-greeting',
                        help='Greeting can be disabled',
                        action='store_true', default=False)
    parser.add_argument('--dumptree',
                        help='Dump tree each time',
                        action='store_true', default=False)
    parser.add_argument('--print-exception',
                        help='Call traceback.print_exc()',
                        action='store_true', default=False)

    args = parser.parse_args()

    p_ver = '.'.join([str(sys.version_info.major),
                      str(sys.version_info.minor),
                      str(sys.version_info.micro)])

    print('NanamiLang', __version_string__, 'by', __author__, 'on Python', p_ver)
    if not args.no_greeting:
        print('Type (doc function-or-macro) to see function-or-macro sample doc')
        print('Type (exit!) or press "Control+D" / "Control+C" to exit the REPL')
        print('History has been read and will be appended to', history_file_path)

    Builtin.install(
        {
            'name': 'exit!', 'type': 'function',
            'sample': '(exit!)', 'docstring': 'Exit NanamiLang REPL'
        },
        lambda _: sys.exit(0)
    )

    while True:
        try:
            inp = input("USER> ")
            # Skip evaluating in case of empty string
            if not inp:
                continue
            try:
                p = Program(inp)
                if args.dumptree:
                    p.dump_tree()
                res = p.evaluate()
                print(res.format())
            except Exception as e:
                if args.print_exception:
                    traceback.print_exc()
                else:
                    print(e)
                print(datatypes.Nil('nil').format())
        except EOFError:
            print("Bye for now!")
            break
        except KeyboardInterrupt:
            print("\b\bBye for now!")
            break

    return 0

    # Return 0 to system and exit NanamiLang REPL script after playing around


if __name__ == "__main__":

    main()
