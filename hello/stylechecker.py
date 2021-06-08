#!/usr/bin/env python3

"""Style Check a Source File."""

__author__ = 'Karen Peterson'
__date__ = '4/15/2021'

from sc_lib import StyleSummary
from sc_lib import SrcFile
from sc_lib import Line
from sc_lib import detabify
from sc_lib import process_one_file
from sc_lib import get_summary_results
#from browser import document, html


def read_upload_file(src_file, dom_file_obj):
    """TBD."""
    tmp = document.getElementById ('dom_file_obj') .value # document[dom_file_obj].value
    all_lines = tmp.split('\n')
    if all_lines[-1] == '':
        all_lines.pop()
    for line in all_lines:
        one_line = Line()
        line_with_new = line + '\n'
        line_list = list(line_with_new)
        detabify(line_list)
        one_line.orig_line = line_list
        one_line.clean_line = line_list.copy()
        src_file.lines.append(one_line)


def do_it(event):
    style_summ = StyleSummary()
    style_summ.files = []
    
    for single_file in document.getElementsByClassName('textarea.fileText'):        
        src_file = SrcFile()
        src_file.filename = single_file_name = document.getElementById (single_file.id + 'Name').value # document[single_file.id + 'Name'].value
        #  src_file.filename = document['fileSource1Name'].value
        read_upload_file(src_file, single_file.id)        
        process_one_file(src_file)
        style_summ.files.append(src_file)

    output_str = '<pre>' + get_summary_results(style_summ, True, True) + '</pre>'
        
    document.getElementById ('results').innerHTML = output_str
    # document['results'] <= html.P(output_str)

#from browser import document, alert, html
#document['run'].bind('click',do_it)

