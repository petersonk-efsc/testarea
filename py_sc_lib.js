var pyScLibCode =
`import sys
import os
import pycodestyle
# import pylint.epylint as lint #KP
# import web_epylint as lint

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


def run_pylint(web_pylint_opts, filename, lines):
    """Run pylint."""
    output = '***** pylint *****\\n'
    from io import StringIO
    lint_out = StringIO()
    #with open('sample.py', 'r') as input_file:
    #    lines = input_file.read()
    wb = WebRun([filename, '--from-stdin', '--persistent=n', '--score=n'], exit=False, lines=lines, web_output=lint_out) #lint_out)
    # print('XXX', wb.linter.reporter.out.getvalue())
    output += lint_out.getvalue()
    return output #KP


def run_pycodestyle(filename, lines_list):
    """Run pycodestyle."""
    output = '***** pycodestyle *****\\n'
    # KP - can call pycodestyle and pass in a list of lines
    #with open('sample.py', 'r') as input_file:
    #    lines = input_file.readlines()
    style_checker = pycodestyle.Checker(reporter=WebPyCodeStyleReport, lines=lines_list)
    style_checker.filename = filename
    result = style_checker.check_all()
    for style_part in result:
        output += '{:s}:{:d}:{:d}: {:s} {:s}\\n'.format(
            style_part[0], style_part[1],
            style_part[2], style_part[3],
            style_part[4])
    return output #KP


class PyFile:
    """TBD."""
    def __init__(self):
        """Constructor."""
        self.filename = ''
        self.lines_list = []
        self.lines = ''
        self.errors = ''
        self.error_dict = {}
        self.err_count = 0


class PyStyleSumm:
    def __init__(self):
        """Constructor."""
        self.total_err_count = 0
        self.total_file_count = 0
        self.total_line_count = 0
        self.total_missing = 0
        self.web_pylint_opts = ''
        self.files = []
        self.score = 0
        self.total = 100


def get_summary_results(style_summ, replace_less=False, span_color=False):
    """Main program."""
    summ_text = ''
    for file_to_check in style_summ.files:
        summ_text += file_to_check.filename + ':\\n'
        summ_text += file_to_check.errors
        summ_text += '\\n'

    start_score = (style_summ.total_line_count - style_summ.total_err_count) / style_summ.total_line_count * 100
    style_summ.score = start_score
    missing = ''
    if style_summ.total_missing > 0:
        missing_penalty = style_summ.total_missing / style_summ.total_file_count * 100
        style_summ.score -= missing_penalty
        missing = '\\n- {:.1f}% for missing files'.format(missing_penalty)

    if style_summ.score < 0:
        style_summ.score = 0
    format_str = "Found {:d} errors / {:d} total lines = {:.1f}%{:s}\\n\\n{:s}"
    summ_text = format_str.format(
        style_summ.total_err_count, style_summ.total_line_count,
        start_score, missing, summ_text)
    
    summ_text = 'Style Score: ' + str(round(style_summ.score, 1)) + '/' + str(style_summ.total) + '\\n' \
                + '------------------------------\\n' + summ_text

    for src_file in style_summ.files:
        summ_text += '\\n******************************\\n'
        summ_text += src_file.filename + '\\n'
        summ_text += '******************************\\n'
        if len(src_file.lines_list) == 0:
            summ_text += 'MISSING FILE!!!\\n'
        else:
            for line_ind in range(len(src_file.lines_list)):
                line = src_file.lines_list[line_ind]
                if line_ind in src_file.error_dict:
                    for issue in src_file.error_dict[line_ind]:
                        if span_color:
                            summ_text += '<span style="background-color: pink">'
                        summ_text += '## STYLE CHECK: ' + issue + '\\n'
                        if span_color:
                            summ_text += '</span>'
                if replace_less:
                    summ_text += ''.join(line).replace('<', '&lt;')
                else:
                    summ_text += ''.join(line)
    return summ_text


def get_final_grade(style_summ):
    return style_summ.score / style_summ.total * 100


def extract_errors(src_file, messages, linter):
    for tmp in messages.split('\\n'):
        if '.py:' in tmp:
            src_file.err_count += 1
            line_num = int(tmp.split(':')[1]) - 1
            if line_num in src_file.error_dict:
                src_file.error_dict[line_num].append(linter + tmp)
            else:
                src_file.error_dict[line_num] = [linter +  tmp]

                    
def process_one_file(style_summ, src_file):
    """TBD."""
    style_summ.total_file_count += 1
    style_summ.total_line_count += len(src_file.lines_list)
    if len(src_file.lines_list) > 0:
        output1 = run_pylint(style_summ.web_pylint_opts, src_file.filename, src_file.lines)
        extract_errors(src_file, output1, '(pylint) ')
        output2 = run_pycodestyle(src_file.filename, src_file.lines_list)
        extract_errors(src_file, output2, '(pycodestyle) ')
        style_summ.total_err_count += src_file.err_count
        src_file.errors = output1 + '\\n' + output2
    else:
        style_summ.total_missing += 1
`;
