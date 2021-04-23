def remove_comments_and_strings(whole_file):
    """TBD.

    Args:
        TBD

    Returns:
        TBD
    """
    in_quote = False
    in_single_quote = False
    in_multi_comment = False
    in_single_comment = False
    prev_char = ' '
    set_space = False
    for line in whole_file:
        prev_char = '\n'
        for ind in range(len(line)):
            set_space = False
            if in_quote:
                if line[ind] == '"' and prev_char != '\\':
                    in_quote = False
                else:
                    set_space = True
            elif in_single_quote:
                if line[ind] == '\'' and prev_char != '\\':
                    in_single_quote = False
                else:
                    set_space = True
            elif in_multi_comment:
                if line[ind] == '/' and prev_char == '*':
                    in_multi_comment = False
                    line[ind-1] = ' '
                    set_space = True
                elif line[ind] != '\n':
                    set_space = True
            elif in_single_comment:
                if line[ind] == '\n':
                    in_single_comment = False
                else:
                    set_space = True
            elif line[ind] == '"':
                in_quote = True
            elif line[ind] == '\'':
                in_single_quote = True
            elif line[ind] == '*' and prev_char == '/':
                in_multi_comment = True
                line[ind-1] = ' '
                set_space = True
            elif line[ind] == '/' and prev_char == '/':
                in_single_comment = True
                line[ind-1] = ' '
                set_space = True
            prev_char = line[ind]
            if set_space:
                line[ind] = ' '


def detabify(whole_file):
    """TBD.

    Args:
        TBD

    Returns:
        TBD
    """
    for line in whole_file:
        line_len = len(line)
        ind = 0
        while ind < line_len:
            if line[ind] == '\t':
                line[ind] = ' '
                leftover = 3 - (ind % 4)
                for _ in range(leftover):
                    line.insert(ind, ' ')
                ind += leftover
            ind += 1


from browser import document, html

def do_it(event):
    tmp = document['file1Text'].value
    alert('****\n' + tmp + '\n****')
    whole_file = []
    for line in tmp.split('\n'):
        tmp2 = list(line)
        tmp2.append('\n')
        if line.find('/' + '*') >= 0:
            alert(line + ' -- ' + str(tmp2))    
        whole_file.append(tmp2)
	tmp_str = str(whole_file)
    
	remove_comments_and_strings(whole_file)
	detabify(whole_file)

	output_str = '<pre><code>' + tmp_str + '\n'
	for line in whole_file:
		output_str += "".join(line)
	for line in whole_file:
		output_str += "".join(line).replace('<', '&lt;')
	output_str += '</code></pre>'	
    document['results'].text = ''
    document['results'] <= html.P(output_str)

from browser import document, alert, html
document['run'].bind('click',do_it)

