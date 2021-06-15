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


def do_it():
    style_summ = PyStyleSumm()
    style_summ.files = []

    for single_file in document.getElementsByClassName('fileText'):
        src_file = PyFile()
        src_file.filename = document.getElementById(single_file.id + 'Name').value
        read_upload_file(src_file, single_file.id)
        process_one_file(style_summ, src_file)
        style_summ.files.append(src_file)

    document.getElementById('results').innerHTML = '<pre>' + get_summary_results(style_summ, True, True) + '</pre>'
`;
