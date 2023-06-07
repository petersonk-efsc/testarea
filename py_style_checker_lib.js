var pyStyleCheckerCode =
`
def read_upload_file(src_file, dom_file_obj):
    tmp = document.getElementById(dom_file_obj).value
    src_file.lines = tmp
    src_file.lines_list = tmp.split('\\n')
    if src_file.lines_list[-1] == '':
        src_file.lines_list.pop()
    for ind in range(len(src_file.lines_list)):
        src_file.lines_list[ind] += '\\n'
    with open(src_file.filename, 'w') as out_file:
        out_file.write(src_file.lines)

def do_it():
    style_summ = PyStyleSumm()
    if document.getElementById('ignoring').innerHTML != '':
        style_summ.web_pylint_opts = [document.getElementById('ignoring').innerHTML]
    style_summ.files = []

    for single_file in document.getElementsByClassName('fileText'):
        src_file = PyFile()
        src_file.filename = document.getElementById(single_file.id + 'Name').value
        read_upload_file(src_file, single_file.id)
        process_one_file(style_summ, src_file)
        style_summ.files.append(src_file)

    document.getElementById('results').innerHTML = '<pre>' + get_summary_results(style_summ, True, True) + '</pre>'
`;
