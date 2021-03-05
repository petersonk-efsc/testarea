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
        for ind in range(len(line)):
            set_space= False
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
	whole_file = [['/', '*', '\n'], [' ', '*', ' ', 'h', 'f', 'h', 'f', 'k', 'd', 's', '\n'], [' ', '*', '/', '\n'], ['\n'], ['#', 'i', 'n', 'c', 'l', 'u', 'd', 'e', ' ', '<', 'i', 'o', 's', 't', 'r', 'e', 'a', 'm', '>', '\n'], ['#', 'i', 'n', 'c', 'l', 'u', 'd', 'e', ' ', '<', 's', 't', 'r', 'i', 'n', 'g', '>', '\n'], ['u', 's', 'i', 'n', 'g', ' ', 'n', 'a', 'm', 'e', 's', 'p', 'a', 'c', 'e', ' ', 's', 't', 'd', ';', '\n'], ['i', 'n', 't', ' ', 'm', 'a', 'i', 'n', '(', ')', '\n'], ['{', '\n'], ['\t', 'i', 'n', 't', ' ', 's', '1', ',', ' ', 's', '2', ',', ' ', 's', '3', ',', ' ', 's', '4', ';', '\n'], ['\t', 'd', 'o', 'u', 'b', 'l', 'e', ' ', 'a', 'v', 'g', ';', '\n'], ['\n'], ['\t', 'c', 'o', 'u', 't', ' ', '<', '<', ' ', '"', 'S', 'c', 'o', 'r', 'e', 's', '?', ' ', '"', ';', '\n'], ['\t', 'c', 'i', 'n', ' ', '>', '>', ' ', 's', '1', ' ', '>', '>', ' ', 's', '2', ' ', '>', '>', ' ', 's', '3', ' ', '>', '>', ' ', 's', '4', ';', '\n'], ['\t', 'c', 'o', 'u', 't', ' ', '<', '<', ' ', 'e', 'n', 'd', 'l', ';', '\n'], ['\n'], ['\t', 'a', 'v', 'g', ' ', '=', ' ', '(', 's', '1', ' ', '+', ' ', 's', '2', ' ', '+', ' ', 's', '3', ' ', '+', ' ', 's', '4', ')', ' ', '/', ' ', '4', '.', '0', ';', '\n'], ['\n'], ['\t', '\t', 'c', 'o', 'u', 't', ' ', '<', '<', ' ', 's', '1', ' ', '<', '<', ' ', '"', ':', ' ', '"', ' ', '<', '<', ' ', 's', '1', ' ', '/', ' ', '1', '0', ' ', '<', '<', ' ', 'e', 'n', 'd', 'l', ';', '\n'], ['\t', ' ', '\t', 'c', 'o', 'u', 't', ' ', '<', '<', ' ', 's', '2', ' ', '<', '<', ' ', '"', ':', ' ', '"', ' ', '<', '<', ' ', 's', '2', ' ', '/', ' ', '1', '0', ' ', '<', '<', ' ', 'e', 'n', 'd', 'l', ';', '\n'], ['\t', ' ', ' ', '\t', 'c', 'o', 'u', 't', ' ', '<', '<', ' ', 's', '3', ' ', '<', '<', ' ', '"', ':', ' ', '"', ' ', '<', '<', ' ', 's', '3', ' ', '/', ' ', '1', '0', ' ', '<', '<', ' ', 'e', 'n', 'd', 'l', ';', '\n'], ['\t', ' ', ' ', ' ', '\t', 'c', 'o', 'u', 't', ' ', '<', '<', ' ', 's', '4', ' ', '<', '<', ' ', '"', ':', ' ', '"', ' ', '<', '<', ' ', 's', '4', ' ', '/', ' ', '1', '0', ' ', '<', '<', ' ', 'e', 'n', 'd', 'l', ';', '\n'], ['\t', 'c', 'o', 'u', 't', ' ', '<', '<', ' ', 'e', 'n', 'd', 'l', ' ', '<', '<', ' ', '"', 'A', 'v', 'g', ' ', '=', ' ', '"', ' ', '<', '<', ' ', 'a', 'v', 'g', ' ', '<', '<', ' ', 'e', 'n', 'd', 'l', ';', '\n'], ['\n'], ['\t', 'c', 'i', 'n', '.', 'i', 'g', 'n', 'o', 'r', 'e', '(', '1', '0', '0', ',', ' ', "'", '\\', 'n', "'", ')', ';', '\n'], ['\t', 'c', 'i', 'n', '.', 'g', 'e', 't', '(', ')', ';', '\t', '/', '/', 's', 'y', 's', 't', 'e', 'm', '(', '"', 'P', 'A', 'U', 'S', 'E', '"', ')', ';', '\n'], ['\t', 'r', 'e', 't', 'u', 'r', 'n', ' ', '0', ';', '\n'], ['}', '\n']]
			
	remove_comments_and_strings(whole_file)
	detabify(whole_file)

	output_str = '<pre>'
	for line in whole_file:
		output_str += "".join(line)
	output_str += '</pre>'	
	document <= html.P(output_str)

from browser import document, html
document['run'].bind('click',do_it)
