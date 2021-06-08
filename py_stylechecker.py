#!/usr/bin/env python3

"""Style Check a Source File."""

__author__ = 'Karen Peterson'
__date__ = '4/15/2021'

from py_sc_lib import PyStyleCheckData
from py_sc_lib import PyFile
from py_sc_lib import process_one_file
from py_sc_lib import get_summary_results
from py_sc_lib import get_final_grade
from browser import document, html


def read_upload_file(src_file, dom_file_obj):
    """TBD."""
    tmp = document[dom_file_obj].value
    src_file.file_text = tmp


def do_it(event):
    style_summ = StyleSummary()
    style_summ.check_files = []
    
    for single_file in document.select('textarea.fileText'):        
        src_file = PyFile()
        src_file.filename = single_file_name = document[single_file.id + 'Name'].value
        #  src_file.filename = document['fileSource1Name'].value
        read_upload_file(src_file, single_file.id)        
        process_one_file(src_file)
        style_summ.check_files.append(src_file)

    output_str = '<pre>' + get_summary_results(style_summ, True, True) + '</pre>'
        
    document['results'].text = ''
    document['results'] <= html.P(output_str)

from browser import document, alert, html
document['run'].bind('click',do_it)

