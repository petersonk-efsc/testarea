#!/usr/bin/env python3

'''Python Style Checker (pylint and pycodestyle).'''

__author__ = 'Karen Peterson'
__date__ = '6/15/2020'

# KP - don't need the following 3 lines when doing html version
#import sys
#sys.path.insert(0, './pycodestyle_lib')
#sys.path.insert(0, './pylint_lib')

import sys
import os
from pathlib import Path
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename
import pycodestyle
# import pylint.epylint as lint #KP
# import web_epylint as lint

def file_len(fname):
    """Count lines in the file."""
    try:
        with open(fname) as file_to_read:
            count = 0
            for _line in file_to_read:
                count = count + 1
        return count
    except OSError:
        return -1
    


def get_config_file():
    """Get config file."""
    ## root = Tk()
    ## filepath = askopenfilename(
    ##     filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    ## )
    ## root.destroy()
    ## if not filepath:
    ##     print('No config file selected - exiting')
    ##     sys.exit(-1)
    ## return filepath
    return ''


def read_config_file():
    """Read and parse config file."""
    total_file_count = 0
    total_line_count = 0
    total_missing = 0

    web_pylint_opts = ' --persistent=n --score=n '
    check_files = []

    filepath = 'config_sc.txt' # KP get_config_file()
    with open(filepath, 'r') as input_file:
        path = Path(filepath).parent.absolute()
        text = input_file.read()
        os.chdir(path)

        lines = text.split('\n')

        for line in lines:
            words = line.split()
            if len(words) >= 2 and words[0] == 'LintIgnore:':
                web_pylint_opts += ' --disable=' + words[1]
            elif len(words) >= 2 and words[0] == 'File:':
                check_files.append(words[1])
                total_file_count += 1
                line_count = file_len(words[1])
                if line_count <= 0:
                    total_missing += 1
                else:
                    total_line_count += line_count
    return total_file_count, total_line_count, total_missing, \
        web_pylint_opts, check_files


class PyFile:
    def __init__(self):
        """Constructor."""
        self.err_count = 0
        self.line_count = 0

        self.web_pylint_opts = ''
        self.filename = ''
        self.file_text = ''
        self.results = ''

        
class PyStyleCheckData:
    def __init__(self):
        """Constructor."""
        self.total_err_count = 0
        self.total_file_count = 0
        self.total_line_count = 0
        self.total_missing = 0

        self.web_pylint_opts = ''
        self.check_files = []
        self.score = 0
        

class WebPyCodeStyleReport(pycodestyle.StandardReport):
    """Reporter class."""
    def get_file_results(self):
        self._deferred_print.sort()
        results = []
        for style_part in self._deferred_print:
            results.append((self.filename, style_part[0],
                            style_part[1]+1, style_part[2],
                            style_part[3], style_part[4]))
        return results


def run_pylint(file_to_check, web_pylint_opts, file_text):
    """Run pylint."""
    output = 'pylint style checker...\n'
    from io import StringIO
    lint_out = StringIO()
    from pylint.lint import Run
    from web_run import WebRun
    # with open('sample.py', 'r') as input_file:
    #   lines = input_file.read()
    WebRun([file_to_check, '--from-stdin'], exit=False, lines=file_text, web_output=lint_out) #lint_out)
    print('KP-done')
    output += lint_out.getvalue()
##    with open('sample.py', 'r') as input_file:
##        lines = input_file.readlines()
##    (pylint_stdout, pylint_stderr) = lint.web_py_run(
##        '--from-stdin ' + web_pylint_opts, lines=lines, return_std=True)
##    print('\n\n\n' + pylint_stdout.getvalue() + '\n\n\n')
##    print('\n\n\n' + pylint_stderr.getvalue() + '\n\n\n')
##    for err in pylint_stderr.getvalue():
##        if (len(err) >= 5):
##            output += err[0] + ':' + err[1] + ':' + err[2] + ': ' + err[3] + ': ' + err[4] + '\n'
##        else:
##            print('KP' + err)
    # output += pylint_stdout.getvalue()
    # output += pylint_stderr.getvalue()    
    return output #KP

    (pylint_stdout, pylint_stderr) = lint.py_run(
        web_pylint_opts, return_std=True)
    output += pylint_stdout.getvalue()
    output += pylint_stderr.getvalue()
    return output


def run_pycodestyle(check_files, file_text):
    """Run pycodestyle."""
    output = '\n\npycodestyle style checker...\n'
    # KP - can call pycodestyle and pass in a list of lines
    #with open('sample.py', 'r') as input_file:
    #    lines = input_file.readlines()
    lines = file_text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i] + '\n'
    style_checker = pycodestyle.Checker(reporter=WebPyCodeStyleReport, lines=lines)
    style_checker.filename = check_files[0]
    result = style_checker.check_all()
    print(result)
    for style_part in result:
        output += '{:s}:{:d}:{:d}: {:s} {:s}\n'.format(
            style_part[0], style_part[1],
            style_part[2], style_part[3],
            style_part[4])
    return output #KP
    # KP - end of new version of pycodestyle
    
    style_checker = pycodestyle.StyleGuide(reporter=WebPyCodeStyleReport)
    result = style_checker.check_files(check_files)
    for style_part in result.get_file_results():
        output += '{:s}:{:d}:{:d}: {:s} {:s}\n'.format(
            style_part[0], style_part[1],
            style_part[2], style_part[3],
            style_part[4])
    return output


def process_one_file(file_to_check):
    print('KP process', file_to_check.filename)
    output = '-------------------------------------------\n'
    output += 'Checking ' + file_to_check.filename + '\n\n'
    output += run_pylint(file_to_check.filename, file_to_check.web_pylint_opts, file_to_check.file_text)
    output += run_pycodestyle([file_to_check.filename], file_to_check.file_text)
    output += '\n-------------------------------------------\n'
    file_to_check.results = output
    file_to_check.err_count = output.count('.py:')
    file_to_check.line_count = file_to_check.file_text.count('\n') + 1 # Do I need + 1?


def get_summary_results(pystyle_data, a, b):
    """Main program."""
    pystyle_data.total_err_count = 0
    pystyle_data.total_file_count = 0
    pystyle_data.total_line_count = 0
    pystyle_data.total_missing = 0

    pystyle_data.web_pylint_opts = ''
    #pystyle_data.check_files = []

    #total_file_count, total_line_count, total_missing, \
    #    web_pylint_opts, check_files = read_config_file()
    
    output = ''
    for file in pystyle_data.check_files:
        pystyle_data.total_err_count += file.err_count
        pystyle_data.total_line_count += file.line_count
        output += file.results

    #total_err_count = output.count('.py:')
    start_score = (pystyle_data.total_line_count - pystyle_data.total_err_count) / pystyle_data.total_line_count * 100
    score = start_score
    missing = ''
    if pystyle_data.total_missing > 0:
        missing_penalty = pystyle_data.total_missing / len(pystyle_data.check_files) * 100
        score -= missing_penalty
        missing = '\n- {:.1f}% for missing files'.format(missing_penalty)

    pystyle_data.score = score
    format_str = "Score: {:.1f}%\n\n" \
        + "Found {:d} errors / {:d} total lines = {:.1f}%{:s}\n{:s}"
    output = format_str.format(
        score, pystyle_data.total_err_count, pystyle_data.total_line_count,
        start_score, missing, output)
    return output
    

def get_final_grade(pystyle_data):
    return pystyle_data.score
