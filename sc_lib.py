#!/usr/bin/env python3

"""Style Check a Source File."""

__author__ = 'Karen Peterson'
__date__ = '4/15/2021'

import re

SPACES_PER_INDENT = 4


class Token:
    """TBD."""
    NO_TOKEN = 0
    OP_TOKEN = 1
    FUNC_ID_TOKEN = 2
    VAR_ID_TOKEN = 3
    CLASS_ID_TOKEN = 4
    STRUCT_ID_TOKEN = 5
    ENUM_ID_TOKEN = 6
    ENUM_VALUE_ID_TOKEN = 7
    CONSTANT_ID_TOKEN = 8
    NUMBER_TOKEN = 9
    ID_TOKEN = 10

    def __init__(self):
        """Constructor."""
        self.tok_str = ''
        self.line = -1
        self.col = -1
        self.stmt = -1
        self.ind = -1
        self.tok_type = Token.NO_TOKEN


class Line:
    """TBD."""
    def __init__(self):
        """Constructor."""
        self.orig_line = []
        self.clean_line = []
        self.first_token = -1
        self.last_token = -1
        self.issues = []
        self.issue_types = []


class Statement:
    """TBD."""
    NO_STMT = 0
    CONTINUATION = 1

    INCLUDE_ANGLE_STMT = 10
    INCLUDE_QUOTE_STMT = 11
    PREPROCESSOR_STMT = 12
    USING_STMT = 13

    START_BLOCK_STMT = 20
    END_BLOCK_STMT = 21

    FOR_STMT = 30
    WHILE_STMT = 31
    DO_STMT = 32
    DO_WHILE_STMT = 33

    IF_STMT = 40
    ELSE_IF_STMT = 41
    ELSE_STMT = 42
    SWITCH_STMT = 43
    CASE_STMT = 44
    DEFAULT_STMT = 45

    CONTINUE_STMT = 50
    GOTO_STMT = 51
    BREAK_STMT = 52

    DECLARE_STMT = 60
    DECLARE_CONST_STMT = 61

    PROTOTYPE_STMT = 70
    FUNC_HDR_STMT = 71
    CLASS_STMT = 72
    ACCESS_STMT = 73
    STRUCT_STMT = 74
    ENUM_STMT = 75
    BLOCK_INTRO_STMT = 76  # namespace, something like func header, but not function

    SEQUENCE_STMT = 80
    RETURN_STMT = 81
    EMPTY_STMT = 82
    END_STMT = 83

    KEYWORD_DICT = {'using': (USING_STMT, True, ';', False),
                    '{': (START_BLOCK_STMT, False, '', False),
                    '}': (END_BLOCK_STMT, False, '', False),
                    'for': (FOR_STMT, True, ')', True),
                    'do': (DO_STMT, False, '', False),
                    'if': (IF_STMT, True, ')', True),
                    'switch': (SWITCH_STMT, True, ')', True),
                    'case': (CASE_STMT, True, ':', False),
                    'default': (DEFAULT_STMT, True, ':', False),
                    'continue': (CONTINUE_STMT, True, ';', False),
                    'goto': (GOTO_STMT, True, ';', False),
                    'break': (BREAK_STMT, True, ';', False),
                    'return': (RETURN_STMT, True, ';', False),
                    ';': (EMPTY_STMT, False, '', False)
                    }

    def __init__(self):
        """Constructor."""
        self.stmt_type = self.NO_STMT
        self.first_token = -1
        self.last_token = -1


class SrcFile:
    """TBD."""
    LANG_CPP = 1
    LANG_JAVA = 2
    LANG_CSHARP = 3

    CASE_CAMEL = 1
    CASE_PASCAL = 2
    CASE_ALL_UPPER = 3

    def __init__(self):
        """Constructor."""
        self.filename = ''
        self.num_functions = 0
        self.lines = []
        self.tokens = []
        self.statements = []
        self.indent = SPACES_PER_INDENT
        self.lang = self.LANG_CPP
        self.curly_same_line = True
        self.class_name = self.CASE_PASCAL
        self.func_name = self.CASE_CAMEL


class StyleSummary:
    """TBD."""
    ERROR_GENERIC = 0;
    ERROR_FILE_NO_COMMENT = 1;
    ERROR_FILE_COMMENT = 2;
    ERROR_FUNCTION_NO_COMMENT = 3;
    ERROR_FUNCTION_COMMENT = 4;
    ERROR_PACKAGE_INCLUDE = 5;
    ERROR_GLOBAL_GOTO = 6;
    ERROR_UPPER_LOWER_CASE = 7;
    ERROR_INDENTATION = 8;
    ERROR_SPACING = 9;
    ERROR_BRACES = 10;
    ERROR_DECLARATIONS = 11;
    ERROR_FUNC_ORDER = 12;
    ERROR_OTHER = 13;

    CATEGORIES = (([ERROR_FILE_NO_COMMENT, ERROR_FILE_COMMENT], 'File Comments'),
                  ([ERROR_FUNCTION_NO_COMMENT, ERROR_FUNCTION_COMMENT], 'Method/Function Comments'),
                  ([ERROR_PACKAGE_INCLUDE], 'Package/Includes'),
                  ([ERROR_GLOBAL_GOTO], 'Globals/continue/breaks'),
                  ([ERROR_UPPER_LOWER_CASE], 'Proper upper/lowercases'),
                  ([ERROR_INDENTATION], 'Proper indentation'),
                  ([ERROR_SPACING], 'Proper spacing'),
                  ([ERROR_BRACES], 'Proper braces'),
                  ([ERROR_DECLARATIONS], 'Proper declarations'),
                  ([ERROR_FUNC_ORDER], 'Proper method/function order'),
                  ([ERROR_OTHER], 'Other issues'))

    def __init__(self):
        """Constructor."""
        self.files = []
        self.issues = {}
        self.score = 0
        self.total = 100


def remove_comments_and_strings(src_file):
    """TBD."""
    in_quote = False
    in_single_quote = False
    in_multi_comment = False
    in_single_comment = False
    prev_char = ' '
    set_space = False
    for full_line in src_file.lines:
        line = full_line.clean_line
        prev_char = '\n'
        prev_prev_char = '\n'
        for ind in range(len(line)):
            set_space = False
            if in_quote:
                if line[ind] == '"' and (prev_char != '\\' or prev_prev_char == '\\'):
                    in_quote = False
                else:
                    set_space = True
            elif in_single_quote:
                if line[ind] == '\'' and (prev_char != '\\' or prev_prev_char == '\\'):
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
            prev_prev_char = prev_char
            prev_char = line[ind]
            if set_space:
                line[ind] = ' '


def detabify(line):
    """TBD."""
    ind = 0
    while ind < len(line):
        if line[ind] == '\t':
            line[ind] = ' '
            leftover = (SPACES_PER_INDENT - 1) - (ind % SPACES_PER_INDENT)
            for _ in range(leftover):
                line.insert(ind, ' ')
            ind += leftover
        ind += 1


def tokenize_stmts(src_file):
    """TBD."""
    token_cnt = 0
    token_start = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ'
    token_middle = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ0123456789'
    long_op_tokens = ['::', '++', '--', '->', '.*', '<<', '>>',
                      '<=', '>=', '==', '!=', '&&', '||',
                      '*=', '/=', '+=', '-=', '&=', '^=', '|=']
    # C++, may need to account for '->*'

    for line_num in range(len(src_file.lines)):
        line = src_file.lines[line_num].clean_line
        src_file.lines[line_num].first_token = token_cnt
        line_len = len(line)
        col_num = 0
        tok_chars = []
        while col_num < line_len:
            if line[col_num] in token_start:
                new_tok = Token()
                tok_chars = []
                new_tok.line = line_num
                new_tok.col = col_num
                new_tok.ind = token_cnt
                new_tok.tok_type = Token.ID_TOKEN
                while line[col_num] in token_middle:
                    tok_chars.append(line[col_num])
                    col_num += 1
                new_tok.tok_str = ''.join(tok_chars)
                src_file.tokens.append(new_tok)
                token_cnt += 1
            elif line[col_num].isspace():
                col_num += 1
            elif line[col_num] in '.0123456789':
                new_tok = Token()
                tok_chars = []
                new_tok.line = line_num
                new_tok.col = col_num
                new_tok.ind = token_cnt
                new_tok.tok_type = Token.NUMBER_TOKEN
                tok_chars.append(line[col_num])
                col_num += 1
                while line[col_num] in '.0123456789':
                    tok_chars.append(line[col_num])
                    col_num += 1
                new_tok.tok_str = ''.join(tok_chars)
                src_file.tokens.append(new_tok)
                token_cnt += 1
            else:
                new_tok = Token()
                tok_chars = []
                tok_chars.append(line[col_num])
                new_tok.line = line_num
                new_tok.col = col_num
                new_tok.tok_type = Token.OP_TOKEN
                new_tok.ind = token_cnt
                if line[col_num] + line[col_num + 1] in long_op_tokens:
                    tok_chars.append(line[col_num + 1])
                    col_num += 1
                col_num += 1
                new_tok.tok_str = ''.join(tok_chars)
                src_file.tokens.append(new_tok)
                token_cnt += 1
        src_file.lines[line_num].last_token = token_cnt


def get_next_token(tokens, token_ind):
    """TBD."""
    if token_ind >= 0 and (token_ind + 1) < len(tokens):
        token_ind += 1
        return tokens[token_ind]
    return Token()


def get_prev_token(tokens, token_ind):
    """TBD."""
    if token_ind > 0 and (token_ind - 1) < len(tokens):
        token_ind -= 1
        return tokens[token_ind]
    return Token()


def find_next_token(tokens, tok_ind, find_char):
    """TBD."""
    next_tok = Token()
    while tok_ind < len(tokens) and tokens[tok_ind].tok_str != find_char:
        tok_ind += 1
    if tok_ind < len(tokens):
        next_tok = tokens[tok_ind]
    return next_tok


def continue_till_char(tokens, tok_ind, end_char, match=False, forward=True):
    """TBD."""
    count = 0
    start_char = ''
    if match:
        match_char_dict = { '(': ')', ')': '(',
                            '{': '}', '}': '{',
                            '[': ']', ']': '[',
                            '<': '>', '>': '>' }
        if end_char in match_char_dict:
            start_char = match_char_dict[end_char]
    move_to_next_tok = 1
    if not forward:
        move_to_next_tok *= -1
    done = False
    while not done:
        if match:
            if tokens[tok_ind].tok_str == start_char:
                count += 1
            elif tokens[tok_ind].tok_str == end_char:
                count -= 1
        if tokens[tok_ind].tok_str == end_char and count == 0:
            done = True
        elif tok_ind + move_to_next_tok >= 0 and tok_ind + move_to_next_tok < len(tokens):
            tok_ind += move_to_next_tok
        else:
            done = True
    return tok_ind


def find_smallest(tok1, tok2):
    """TBD."""
    if tok1.line == -1:
        return tok2
    elif tok2.line == -1:
        return tok1
    elif tok1.line < tok2.line:
        return tok1
    elif tok2.line < tok1.line:
        return tok2
    elif tok1.col < tok2.col:
        return tok1
    return tok2


def classify_tokens(src_file):
    """TBD."""
    src_file.num_functions = 0
    tokens = src_file.tokens
    src_file.statements = []
    tok_ind = 0
    while tok_ind < len(tokens):
        curr_tok = tokens[tok_ind]
        curr_tok_str = curr_tok.tok_str
        new_stmt = Statement()
        new_stmt.first_token = tok_ind
        if curr_tok_str in Statement.KEYWORD_DICT:
            key_info = Statement.KEYWORD_DICT[curr_tok_str]
            new_stmt.stmt_type = key_info[0]
            if key_info[1]:
                tok_ind = continue_till_char(tokens, tok_ind, key_info[2], key_info[3])
        elif curr_tok_str == '#':
            next_tok = get_next_token(tokens, tok_ind)
            if next_tok.tok_str == 'include':
                next2_tok = get_next_token(tokens, next_tok.ind)
                if next2_tok.tok_str == '<':
                    new_stmt.stmt_type = Statement.INCLUDE_ANGLE_STMT
                    end_char = '>'
                else:
                    new_stmt.stmt_type = Statement.INCLUDE_QUOTE_STMT
                    end_char = '"'
                tok_ind = next2_tok.ind + 1
                tok_ind = continue_till_char(tokens, tok_ind, end_char)
            else:
                new_stmt.stmt_type = Statement.PREPROCESSOR_STMT
        elif curr_tok.tok_str == 'while':
            new_stmt.stmt_type = Statement.WHILE_STMT
            tmp_tok = get_prev_token(tokens, tok_ind)
            tok_ind = continue_till_char(tokens, tok_ind, ')', True)
            if tmp_tok.tok_str == '}':  # } while (...); is end of a do-while
                tmp2_tok = get_next_token(tokens, tok_ind)
                if tmp2_tok.tok_str == ';':
                    new_stmt.stmt_type = Statement.DO_WHILE_STMT
                    tok_ind = tmp2_tok.ind
        elif curr_tok.tok_str == 'else':
            tmp_tok = get_next_token(tokens, tok_ind)
            if tmp_tok.tok_str == 'if':
                tok_ind = continue_till_char(tokens, tok_ind, ')', True)
                new_stmt.stmt_type = Statement.ELSE_IF_STMT
            else:
                new_stmt.stmt_type = Statement.ELSE_STMT
        elif (curr_tok.tok_str in ['private', 'public', 'protected']
              and tok_ind + 1 < len(tokens) and tokens[tok_ind + 1].tok_str == ':'):
            new_stmt.stmt_type = Statement.ACCESS_STMT
            tok_ind = continue_till_char(tokens, tok_ind, ':', False)
        else:
            left_paren_tok = find_next_token(tokens, tok_ind, '(')
            semi_tok = find_next_token(tokens, tok_ind, ';')
            left_curly_tok = find_next_token(tokens, tok_ind, '{')
            equal_tok = find_next_token(tokens, tok_ind, '=')
            # if ( then function header or prototype or call
            # if =, ; then regular line - possibly declare
            # if { then class or random block or array declaration with initialization
            small_tok = find_smallest(find_smallest(left_paren_tok, semi_tok),
                                      find_smallest(left_curly_tok, equal_tok))
            small_tok_str = small_tok.tok_str
            if small_tok_str in ['=', ';']:
                new_stmt.stmt_type = Statement.SEQUENCE_STMT
                # if 2 tokens before =, then declaration, last non [] token before = is variable name
                if curr_tok.tok_type == Token.ID_TOKEN:
                    found_const = False
                    var_type = Token.VAR_ID_TOKEN
                    for ind in range(curr_tok.ind, small_tok.ind):
                        if tokens[ind].tok_str == 'const':
                            var_type = Token.CONSTANT_ID_TOKEN
                            found_const = True
                    next_tok = get_next_token(tokens, tok_ind)
                    next_tok_ind = next_tok.ind
                    while next_tok.tok_str in ['<', '[']:
                        if next_tok.tok_str == '<':
                            end_char = '>'
                        else:
                            end_char = ']'
                        next_tok_ind = continue_till_char(tokens, next_tok_ind,
                                                          end_char, match=True)
                        next_tok = get_next_token(tokens, next_tok_ind)
                        next_tok_ind = next_tok.ind
                    if next_tok.tok_type == Token.ID_TOKEN:
                        if found_const:
                            new_stmt.stmt_type = Statement.DECLARE_CONST_STMT
                        else:
                            new_stmt.stmt_type = Statement.DECLARE_STMT
                        finding_vars = True
                        tmp_ind = curr_tok.ind
                        while tmp_ind < semi_tok.ind:
                            if tokens[tmp_ind+1].tok_type == Token.ID_TOKEN:
                                pass
                            elif tokens[tmp_ind+1].tok_str == '<':
                                tmp_ind = continue_till_char(tokens, tmp_ind, '>', match=True)
                            elif tokens[tmp_ind+1].tok_str == '[':
                                tokens[tmp_ind].tok_type = var_type
                                tmp_ind = continue_till_char(tokens, tmp_ind, ']', match=True)
                                while tmp_ind < semi_tok.ind and tokens[tmp_ind+1].tok_str not in (',', ';'):
                                    if tokens[tmp_ind+1].tok_str == '(':
                                        tmp_ind = continue_till_char(tokens, tmp_ind, ')', match=True)
                                    elif tokens[tmp_ind+1].tok_str == '[':
                                        tmp_ind = continue_till_char(tokens, tmp_ind, ']', match=True)
                                    elif tokens[tmp_ind+1].tok_str == '{':
                                        tmp_ind = continue_till_char(tokens, tmp_ind, '}', match=True)
                                    tmp_ind += 1
                            elif tokens[tmp_ind+1].tok_str == '=':
                                tokens[tmp_ind].tok_type = var_type
                                while tmp_ind < semi_tok.ind and tokens[tmp_ind+1].tok_str not in (',', ';'):
                                    if tokens[tmp_ind+1].tok_str == '(':
                                        tmp_ind = continue_till_char(tokens, tmp_ind, ')', match=True)
                                    elif tokens[tmp_ind+1].tok_str == '[':
                                        tmp_ind = continue_till_char(tokens, tmp_ind, ']', match=True)
                                    elif tokens[tmp_ind+1].tok_str == '{':
                                        tmp_ind = continue_till_char(tokens, tmp_ind, '}', match=True)
                                    tmp_ind += 1
                            elif tokens[tmp_ind+1].tok_str in (',', ';'):
                                tokens[tmp_ind].tok_type = var_type
                            tmp_ind += 1
                tok_ind = continue_till_char(tokens, tok_ind, ';')

            elif small_tok_str == '(':
                fun_name_tok = get_prev_token(tokens, left_paren_tok.ind)
                if fun_name_tok.tok_type == Token.ID_TOKEN:
                    src_file.num_functions += 1
                    new_stmt.stmt_type = Statement.FUNC_HDR_STMT
                    fun_name_tok.tok_type = Token.FUNC_ID_TOKEN
                else:
                    new_stmt.stmt_type = Statement.SEQUENCE_STMT
                tok_ind = continue_till_char(tokens, tok_ind, ')', True)
                tmp_tok = get_next_token(tokens, tok_ind)
                if tmp_tok.tok_str != '{':
                    new_stmt.stmt_type = Statement.SEQUENCE_STMT
                    tok_ind = continue_till_char(tokens, tok_ind, ';')
            else:  # small_tok_str == '{':
                tok_ind = continue_till_char(tokens, tok_ind, '{', False)
                tok_ind = get_prev_token(tokens, tok_ind).ind
                
                tmp_ind = new_stmt.first_token
                done = False
                stmt_type = Statement.BLOCK_INTRO_STMT
                tok_type = Token.ID_TOKEN
                while tmp_ind < tok_ind and not done:
                    if tokens[tmp_ind].tok_str == 'class':
                        stmt_type = Statement.CLASS_STMT
                        tok_type = Token.CLASS_ID_TOKEN
                        done = True
                    elif tokens[tmp_ind].tok_str == 'struct':
                        stmt_type = Statement.STRUCT_STMT
                        tok_type = Token.STRUCT_ID_TOKEN
                        done = True
                    elif tokens[tmp_ind].tok_str == 'enum':
                        stmt_type = Statement.ENUM_STMT
                        tok_type = Token.ENUM_ID_TOKEN
                        tok_ind = continue_till_char(tokens, tok_ind, ';', False)
                        for tmp_ind in range(small_tok.ind, tok_ind):
                            if src_file.tokens[tmp_ind].tok_type == Token.ID_TOKEN:
                                src_file.tokens[tmp_ind].tok_type = Token.ENUM_VALUE_ID_TOKEN
                        done = True
                    tmp_ind += 1
                new_stmt.stmt_type = stmt_type
                var_tok = get_prev_token(tokens, left_curly_tok.ind)
                var_tok.tok_type = tok_type
        tok_ind += 1
        new_stmt.last_token = tok_ind
        for ind in range(new_stmt.first_token, new_stmt.last_token):
            tokens[ind].stmt = len(src_file.statements)
        src_file.statements.append(new_stmt)


def check_capitalization(src_file):
    """TBD."""
    for tok in src_file.tokens:
        if tok.tok_type == Token.FUNC_ID_TOKEN:
            if tok.tok_str[0].isupper():
                src_file.lines[tok.line].issues.append((StyleSummary.ERROR_UPPER_LOWER_CASE,
                                                        'Function name must start with lowercase letter (' + tok.tok_str + ')'))
        elif tok.tok_type == Token.VAR_ID_TOKEN:
            if tok.tok_str[0].isupper():
                src_file.lines[tok.line].issues.append((StyleSummary.ERROR_UPPER_LOWER_CASE,
                                                       'Variable name must start with lowercase letter (' + tok.tok_str + ')'))
        elif tok.tok_type == Token.CLASS_ID_TOKEN:
            if tok.tok_str[0].islower():
                src_file.lines[tok.line].issues.append((StyleSummary.ERROR_UPPER_LOWER_CASE,
                                                        'Class name must start with uppercase letter (' + tok.tok_str + ')'))
        elif tok.tok_type == Token.STRUCT_ID_TOKEN:
            if tok.tok_str[0].islower():
                src_file.lines[tok.line].issues.append((StyleSummary.ERROR_UPPER_LOWER_CASE,
                                                        'Struct name must start with uppercase letter (' + tok.tok_str + ')'))
        elif tok.tok_type == Token.ENUM_ID_TOKEN:
            if tok.tok_str[0].islower():
                src_file.lines[tok.line].issues.append((StyleSummary.ERROR_UPPER_LOWER_CASE,
                                                        'Enum name must start with uppercase letter (' + tok.tok_str + ')'))
        elif tok.tok_type in [Token.CONSTANT_ID_TOKEN, Token.ENUM_VALUE_ID_TOKEN]:
            msg = 'Constant name must be all uppercase'
            if tok.tok_type == Token.ENUM_VALUE_ID_TOKEN:
                msg = 'Enum value must be all uppercase'
            all_upper = True
            for let in tok.tok_str:
                if let.islower():
                    all_upper = False
            if not all_upper:
                src_file.lines[tok.line].issues.append((StyleSummary.ERROR_UPPER_LOWER_CASE,
                                                        msg + ' (' + tok.tok_str + ')'))


def check_spacing(src_file):
    """TBD."""
    prev_tok = Token()
    next_tok = Token()
    prev_after = -1
    for tok in src_file.tokens:
        if tok.tok_type == Token.OP_TOKEN:
            tok_str = tok.tok_str
            need_space_before = False
            need_space_before_check = False
            need_space_after = False
            need_space_after_check = False
            if tok_str in ['++', '--']:
                if prev_tok.tok_type == Token.OP_TOKEN:
                    need_space_after = False
                    need_space_after_check = True
                else:                    
                    need_space_before = False
                    need_space_before_check = True
            elif tok_str in ['<<', '>>',
                             '<=', '>=', '==', '!=', '&&', '||',
                             '*=', '/=', '+=', '-=', '&=', '^=', '|=', '%=',
                             '+', '/', '%'
                             ':', '=']:
                need_space_before = True
                need_space_before_check = True
                need_space_after = True
                need_space_after_check = True
            elif tok_str in ['::', '->', '.', '[']:
                need_space_before = False
                need_space_before_check = True
                need_space_after = False
                need_space_after_check = True
            elif tok_str in [':']:
                if src_file.statements[tok.stmt].stmt_type in (Statement.CASE_STMT, Statement.DEFAULT_STMT, Statement.ACCESS_STMT):
                    need_space_before = False
                    need_space_before_check = True
                    need_space_after = True
                    need_space_after_check = True
                else:
                    need_space_before = True
                    need_space_before_check = True
                    need_space_after = True
                    need_space_after_check = True
            elif tok_str in ['?', ',']:
                need_space_before = False
                need_space_before_check = True
                need_space_after = True
                need_space_after_check = True
            elif tok_str == '(':
                if prev_tok.tok_type == Token.FUNC_ID_TOKEN:
                    need_space_before = False
                    need_space_before_check = True
                elif prev_tok.tok_str in ['if', 'for', 'while', 'switch']:
                    need_space_before = True
                    need_space_before_check = True
            elif tok_str == '*':
                if prev_tok.tok_str not in ['(', '[']:
                    need_space_before = True
                    need_space_before_check = True
            elif tok_str == '-':
                if prev_tok.tok_str not in ['(', '[']:
                    need_space_before = True
                    need_space_before_check = True
                next_tok = get_next_token(src_file.tokens, tok.ind)
                if next_tok.tok_type == Token.NUMBER_TOKEN:
                    need_space_after = False
                    need_space_before_check = True
                else:
                    need_space_after = True
                    need_space_before_check = True 
            elif tok_str == '<':
                next_tok = get_next_token(src_file.tokens, tok.ind)
                next_next_tok = get_next_token(src_file.tokens, next_tok.ind)
                if next_next_tok.tok_str in [',', '>']:
                    need_space_after = False
                    need_space_after_check = True
                elif src_file.statements[tok.stmt].stmt_type == Statement.INCLUDE_ANGLE_STMT:
                    need_space_before = True
                    need_space_before_check = True
                    need_space_after = False
                    need_space_after_check = True
                else:
                    need_space_before = True
                    need_space_before_check = True
                    need_space_after = True
                    need_space_after_check = True
            elif tok_str == '>':
                prev_prev_tok = get_prev_token(src_file.tokens, prev_tok.ind)
                if prev_prev_tok.tok_str in [',', '<']:
                    need_space_before = False
                    need_space_before_check = True
                elif src_file.statements[tok.stmt].stmt_type == Statement.INCLUDE_ANGLE_STMT:
                    need_space_before = False
                    need_space_before_check = True
                    need_space_after = True
                    need_space_after_check = True
                else:
                    need_space_before = True
                    need_space_before_check = True
                    need_space_after = True
                    need_space_after_check = True
            if need_space_before_check:
                end_col = len(prev_tok.tok_str) + prev_tok.col
                if tok.line == prev_tok.line:
                    if end_col < tok.col and (not need_space_before):
                        src_file.lines[tok.line].issues.append((StyleSummary.ERROR_SPACING,
                                                                'No space before ' + tok_str))
                    elif end_col >= tok.col and need_space_before:
                        if prev_tok.ind != prev_after:
                            src_file.lines[tok.line].issues.append((StyleSummary.ERROR_SPACING,
                                                                    'Missing space before ' + tok_str))
            if need_space_after_check:
                next_tok = get_next_token(src_file.tokens, tok.ind)
                end_col = len(tok.tok_str) + tok.col
                if tok.line == next_tok.line:
                    if end_col < next_tok.col and (not need_space_after):
                        src_file.lines[tok.line].issues.append((StyleSummary.ERROR_SPACING,
                                                               'No space after ' + tok_str))
                    elif end_col >= next_tok.col and need_space_after:
                        prev_after = tok.ind
                        src_file.lines[tok.line].issues.append((StyleSummary.ERROR_SPACING,
                                                                'Missing space after ' + tok_str))
        prev_tok = tok


def check_indentation(src_file):
    """TBD."""
    indent_stack = [['', 0]]
    stmt_ind = 0
    prev_stmt = Statement()
    for line in src_file.lines:
        if line.last_token > line.first_token:
            stmt_ind = src_file.tokens[line.first_token].stmt
            if src_file.statements[stmt_ind].stmt_type == Statement.END_BLOCK_STMT:
                if indent_stack[-1][0] == ':':
                    indent_stack.pop()
                indent_stack.pop()
            elif src_file.statements[stmt_ind].stmt_type in [Statement.CASE_STMT, Statement.DEFAULT_STMT, Statement.ACCESS_STMT]:
                if indent_stack[-1][0] == ':':
                    indent_stack.pop()
            if line.first_token > src_file.statements[stmt_ind].first_token:
                if src_file.tokens[line.first_token].col < indent_stack[-1][1]:
                    line.issues.append((StyleSummary.ERROR_INDENTATION,
                                        'Indentation for continued line is not correct - should be at least ' + str(indent_stack[-1][1]) + ' spaces'))
            else:
                tmp_indent = indent_stack[-1][1]
                if stmt_ind > 0 \
                    and src_file.statements[stmt_ind].stmt_type != Statement.START_BLOCK_STMT \
                    and src_file.statements[stmt_ind - 1].stmt_type in [Statement.FOR_STMT,
                                                                        Statement.WHILE_STMT,
                                                                        Statement.DO_STMT,
                                                                        Statement.IF_STMT,
                                                                        Statement.ELSE_IF_STMT,
                                                                        Statement.ELSE_STMT]:
                    last_tok_prev_stmt = src_file.tokens[src_file.statements[stmt_ind - 1].last_token - 1]
                    if last_tok_prev_stmt.line != src_file.tokens[line.first_token].line:
                        tmp_indent += SPACES_PER_INDENT
                if src_file.tokens[line.first_token].col != tmp_indent:
                    line.issues.append((StyleSummary.ERROR_INDENTATION,
                                    'Improper indentation - should be ' + str(indent_stack[-1][1]) + ' spaces'))
            for tok_ind in range(line.first_token, line.last_token):
                tmp_stmt_type = src_file.statements[src_file.tokens[tok_ind].stmt].stmt_type
                if tmp_stmt_type == Statement.END_BLOCK_STMT and tok_ind != line.first_token:
                    indent_stack.pop()
                elif tmp_stmt_type == Statement.START_BLOCK_STMT:
                    indent_stack.append(['{', indent_stack[-1][1] + SPACES_PER_INDENT])
            if src_file.statements[stmt_ind].stmt_type in [Statement.CASE_STMT, Statement.DEFAULT_STMT, Statement.ACCESS_STMT]:
                indent_stack.append([':', indent_stack[-1][1] + SPACES_PER_INDENT])


def check_blank_lines(src_file):
    """TBD."""
    num_blank = 0
    checking = True
    for line in src_file.lines:
        if ''.join(line.orig_line).strip() == '':
            num_blank += 1
        else:
            num_blank = 0
            checking = True
        if checking and num_blank > 1:
            checking = False
            line.issues.append((StyleSummary.ERROR_SPACING,
                                'Too many blank lines - at most one blank line between sections'))


def check_multiple_stmts(src_file):
    """TBD."""
    ind = 0
    prev_line = -1
    while ind < len(src_file.statements):
        start_line = src_file.tokens[src_file.statements[ind].first_token].line
        end_line = src_file.tokens[src_file.statements[ind].last_token-1].line
        if start_line == prev_line:
            only_one = False
            if src_file.statements[ind].stmt_type == Statement.EMPTY_STMT:
                if ind > 0:
                    prev_stmt = src_file.statements[ind - 1]
                    if prev_stmt.stmt_type == Statement.END_BLOCK_STMT:
                        start_block_ind = continue_till_char(src_file.tokens, prev_stmt.first_token, '{', True, False)
                        prev_tok = get_prev_token(src_file.tokens, start_block_ind)
                        if not src_file.statements[prev_tok.stmt].stmt_type in [Statement.CLASS_STMT, Statement.STRUCT_STMT]:
                            only_one = True
                    else:
                        only_one = True
                ind += 1
            elif src_file.statements[ind].stmt_type == Statement.START_BLOCK_STMT:
                if ind > 0:
                    prev_stmt = src_file.statements[ind - 1]
                    if prev_stmt.stmt_type not in [Statement.FOR_STMT,
                                                   Statement.WHILE_STMT,
                                                   Statement.DO_STMT,
                                                   Statement.IF_STMT,
                                                   Statement.ELSE_IF_STMT,
                                                   Statement.ELSE_STMT,
                                                   Statement.SWITCH_STMT,
                                                   Statement.FUNC_HDR_STMT,
                                                   Statement.CLASS_STMT,
                                                   Statement.STRUCT_STMT,
                                                   Statement.ENUM_STMT,
                                                   Statement.BLOCK_INTRO_STMT]:
                        only_one = True
                ind += 1
            else:    
                only_one = src_file.statements[ind].stmt_type != Statement.DO_WHILE_STMT
                while ind < len(src_file.statements) and prev_line == src_file.tokens[src_file.statements[ind].first_token].line:
                    ind += 1
            if only_one:
                src_file.lines[start_line].issues.append((StyleSummary.ERROR_OTHER,
                                                          'Only one statement per line'))           
        else:
            ind += 1
        prev_line = end_line


def check_token_use(src_file):
    """TBD."""
    ind = 0
    while ind < len(src_file.tokens):
        tok = src_file.tokens[ind]
        tok_str = tok.tok_str
        if tok_str in ['==', '!=']:
            prev_tok = get_prev_token(src_file.tokens, tok.ind)
            next_tok = get_next_token(src_file.tokens, tok.ind)
            if next_tok.tok_str in ['true', 'false']:
                src_file.lines[tok.line].issues.append((StyleSummary.ERROR_OTHER,
                                                        '==/!= true or false is unnecessary'))
            elif prev_tok.tok_str in ['true', 'false']:
                src_file.lines[tok.line].issues.append((StyleSummary.ERROR_OTHER,
                                                        '==/!= true or false is unnecessary'))
        elif tok_str == 'NULL' and src_file.lang == SrcFile.LANG_CPP:
            src_file.lines[tok.line].issues.append((StyleSummary.ERROR_OTHER,
                                                    'Use nullptr not NULL'))
        ind += 1


def get_comment(src_file, start_com_line, start_com_col, end_com_line, end_com_col):
    """TBD."""
    comment = ''
    if start_com_line != end_com_line:
        for char in src_file.lines[start_com_line].orig_line[start_com_col:]:
            comment += char
        for line in src_file.lines[start_com_line+1:end_com_line]:
            for char in line.orig_line:
                comment += char
        start_com_col = 0
    for char in src_file.lines[end_com_line].orig_line[start_com_col:end_com_col]:
        comment += char
    comment = comment.strip()
    if comment.endswith('*/'):
        trim_to = comment.rfind('/*')
        if trim_to != -1:
            comment = comment[trim_to:]
    return comment


def check_comments(src_file):
    """TBD."""
    if len(src_file.tokens) == 0:
        return
    com_opening = re.compile(r'\/\*[ \n]*\* \S[\s\S]*\*[ \n]*\* Name:[ \t]+\S[\s\S]*\* Date:[ \t]+\S[\s\S]*\*\/')
    end_com_line = src_file.tokens[0].line
    end_com_col = src_file.tokens[0].col
    comment = get_comment(src_file, 0, 0, end_com_line, end_com_col)
    if len(comment) == 0:
        src_file.lines[0].issues.append((StyleSummary.ERROR_FILE_NO_COMMENT,
                                                 'Missing comment at top of file'))
    else:
        result = com_opening.match(comment)
        if result is None:
            src_file.lines[0].issues.append((StyleSummary.ERROR_FILE_COMMENT,
                                             'Comment at top of file is not in the correct format'))


def check_other_stuff(src_file):
    """TBD."""
    blocks = [[False]]
    found_include_quote = False
    found_func = False
    prev_stmt = Statement()
    com_with_param = re.compile(r'\/\*[ \n]*\* \S[\s\S]*\*[ \n]*\* Parameter:[ \t]+\S[\s\S]*\* Return:[ \t]+\S[\s\S]*\*\/')
    com_without_param = re.compile(r'\/\*[ \n]*\* \S[\s\S]*\*[ \n]*\* Return:[ \t]+\S[\s\S]*\*\/')
    for stmt_ind in range(len(src_file.statements)):
        stmt = src_file.statements[stmt_ind]
        start_line = src_file.tokens[stmt.first_token].line
        if stmt.stmt_type == Statement.INCLUDE_QUOTE_STMT:
            found_include_quote = True
        elif stmt.stmt_type == Statement.INCLUDE_ANGLE_STMT: # Only need for C++
            if found_include_quote:
                src_file.lines[start_line].issues.append((StyleSummary.ERROR_PACKAGE_INCLUDE,
                                                          '<> includes should be before "" includes'))
        elif stmt.stmt_type == Statement.START_BLOCK_STMT:
            blocks.append([False])
        elif stmt.stmt_type == Statement.END_BLOCK_STMT:
            blocks.pop()
        elif stmt.stmt_type == Statement.DECLARE_STMT:
            if len(blocks) == 1:
                src_file.lines[start_line].issues.append((StyleSummary.ERROR_GLOBAL_GOTO,
                                                          'No global variables'))
            tok_ind = stmt.first_token
            num_vars = 0
            while tok_ind < stmt.last_token:
                if src_file.tokens[tok_ind].tok_type in (Token.VAR_ID_TOKEN, Token.CONSTANT_ID_TOKEN):
                    num_vars += 1
                elif src_file.tokens[tok_ind].tok_str == '[':
                    only_nums = True
                    bracket_cnt = 1
                    tok_ind += 1
                    tok_cnt = 0
                    while tok_ind < stmt.last_token and bracket_cnt > 0:
                        tok_str = src_file.tokens[tok_ind].tok_str
                        if tok_str == ']':
                            bracket_cnt -= 1
                        elif tok_str == '[':
                            bracket_cnt += 1
                        elif tok_str != ',':
                            tok_cnt += 1
                            if not (src_file.tokens[tok_ind].tok_type in [Token.OP_TOKEN, Token.NUMBER_TOKEN]):
                                only_nums = False
                        tok_ind += 1
                    if only_nums and tok_cnt > 0:
                        src_file.lines[start_line].issues.append((StyleSummary.ERROR_OTHER,
                                                                  'Cannot hard-code number when creating array'))
                tok_ind += 1
            if num_vars > 1:
                src_file.lines[start_line].issues.append((StyleSummary.ERROR_DECLARATIONS,
                                                          'May only declare 1 variable per statement'))
            blocks[-1][0] = True
        elif stmt.stmt_type == Statement.DECLARE_CONST_STMT:
            if blocks[-1][0]:
                src_file.lines[start_line].issues.append((StyleSummary.ERROR_DECLARATIONS,
                                                          'Declare constants before other variables'))
        elif stmt.stmt_type == Statement.CONTINUE_STMT:
            src_file.lines[start_line].issues.append((StyleSummary.ERROR_GLOBAL_GOTO,
                                                      'May not use continue'))
        elif stmt.stmt_type == Statement.GOTO_STMT:
            src_file.lines[start_line].issues.append((StyleSummary.ERROR_GLOBAL_GOTO,
                                                      'May not use goto'))
        elif stmt.stmt_type == Statement.BREAK_STMT:
            tmp_stmt_ind = stmt_ind - 1
            done = False
            check_for_comment = False
            while tmp_stmt_ind > 0 and not done:
                if src_file.statements[tmp_stmt_ind].stmt_type == Statement.END_BLOCK_STMT:
                    while tmp_stmt_ind > 0 and src_file.statements[tmp_stmt_ind].stmt_type != Statement.START_BLOCK_STMT:
                        tmp_stmt_ind -= 1
                    if tmp_stmt_ind > 0 and src_file.statements[tmp_stmt_ind - 1].stmt_type in [Statement.FOR_STMT, Statement.WHILE_STMT, Statement.DO_STMT]:
                        tmp_stmt_ind -= 1
                else:
                    if src_file.statements[tmp_stmt_ind].stmt_type in [Statement.CASE_STMT, Statement.DEFAULT_STMT]:
                        done = True
                    elif src_file.statements[tmp_stmt_ind].stmt_type in [Statement.FOR_STMT, Statement.WHILE_STMT, Statement.DO_STMT]:
                        done = True
                        check_for_comment = True
                tmp_stmt_ind -= 1
            if check_for_comment:
                start_com_line = src_file.tokens[prev_stmt.last_token-1].line
                start_com_col = src_file.tokens[prev_stmt.last_token-1].col
                start_com_col += len(src_file.tokens[prev_stmt.last_token-1].tok_str)
                end_com_line = src_file.tokens[stmt.first_token].line
                end_com_col = src_file.tokens[stmt.first_token].col
                comment = get_comment(src_file, start_com_line, start_com_col,
                                      end_com_line, end_com_col)
                if comment == '':
                    start_com_line = src_file.tokens[stmt.last_token-1].line
                    start_com_col = src_file.tokens[stmt.last_token-1].col
                    start_com_col += len(src_file.tokens[stmt.last_token-1].tok_str)
                    next_token = get_next_token(src_file.tokens, stmt.last_token-1)
                    end_com_line = next_token.line
                    end_com_col = next_token.col
                    comment = get_comment(src_file,
                                          start_com_line, start_com_col,
                                          end_com_line, end_com_col)
                    if comment == '':
                        src_file.lines[start_line].issues.append((StyleSummary.ERROR_GLOBAL_GOTO,
                                                                 'break in loop must have comment on this line or previous line explaining purpose'))
        elif stmt.stmt_type == Statement.FUNC_HDR_STMT:
            is_main = False
            func_name = ''
            for token in src_file.tokens[stmt.first_token:stmt.last_token]:
                if token.tok_type == Token.FUNC_ID_TOKEN:
                    func_name = token.tok_str
                    if func_name == 'main':
                        is_main = True
            if is_main and found_func:
                src_file.lines[start_line].issues.append((StyleSummary.ERROR_FUNC_ORDER,
                                                         'main() should be first function/method in file'))
            found_func = True

            start_com_line = src_file.tokens[prev_stmt.last_token-1].line
            start_com_col = src_file.tokens[prev_stmt.last_token-1].col
            start_com_col += len(src_file.tokens[prev_stmt.last_token-1].tok_str)
            end_com_line = src_file.tokens[stmt.first_token].line
            end_com_col = src_file.tokens[stmt.first_token].col
            comment = get_comment(src_file, start_com_line, start_com_col,
                                  end_com_line, end_com_col)
            if len(comment) == 0:
                src_file.lines[start_line].issues.append((StyleSummary.ERROR_FUNCTION_NO_COMMENT,
                                                         'Missing comment before function/method (' + func_name + ')'))
            else:
                result = None
                prev_tok = get_prev_token(src_file.tokens, stmt.last_token-1)
                if prev_tok.tok_str == '(':
                    result = com_without_param.match(comment)
                else:
                    result = com_with_param.match(comment)
                if result is None:
                    src_file.lines[start_line].issues.append((StyleSummary.ERROR_FUNCTION_COMMENT,
                                                              'Function/method comment is not correct format (' + func_name + ')'))
        if stmt.stmt_type in [Statement.FUNC_HDR_STMT,
                              Statement.FOR_STMT, Statement.WHILE_STMT,
                              Statement.DO_STMT, Statement.IF_STMT,
                              Statement.IF_STMT, Statement.ELSE_IF_STMT,
                              Statement.ELSE_STMT, Statement.SWITCH_STMT,
                              Statement.CLASS_STMT]:
            next_tok = get_next_token(src_file.tokens, stmt.last_token-1)
            if next_tok.tok_str != '{':
                src_file.lines[start_line].issues.append((StyleSummary.ERROR_BRACES,
                                                         'Missing opening {'))
            elif next_tok.line == src_file.tokens[stmt.last_token-1].line:
                src_file.lines[start_line].issues.append((StyleSummary.ERROR_BRACES,
                                                          '{ must be on the following line'))
        prev_stmt = stmt


def get_cat_score(style_summ, cat_num):
    """TBD."""
    score = 10
    max = 10
    if StyleSummary.ERROR_FILE_COMMENT in cat_num:
        if len(style_summ.files) == 1:
            if style_summ.issues[StyleSummary.ERROR_FILE_NO_COMMENT] >= 1:
                score = 0
            elif style_summ.issues[StyleSummary.ERROR_FILE_COMMENT] >= 1:
                score  = 7
        else:
            if style_summ.issues[StyleSummary.ERROR_FILE_NO_COMMENT] >= 2:
                score = 0
            elif style_summ.issues[StyleSummary.ERROR_FILE_NO_COMMENT] == 1:
                if style_summ.issues[StyleSummary.ERROR_FILE_COMMENT] >= 2:
                    score  = 0
                else:
                    score  = 4
            elif style_summ.issues[StyleSummary.ERROR_FILE_COMMENT] >= 2:
                score  = 4
            elif style_summ.issues[StyleSummary.ERROR_FILE_COMMENT] >= 1:
                score  = 7
    elif StyleSummary.ERROR_FUNCTION_COMMENT in cat_num:
        total_functions = 0
        for src_file in style_summ.files:
            total_functions += src_file.num_functions
        if total_functions == 1:
            if style_summ.issues[StyleSummary.ERROR_FUNCTION_NO_COMMENT] >= 1:
                score = 0
            elif style_summ.issues[StyleSummary.ERROR_FUNCTION_COMMENT] >= 1:
                score  = 7
        else:
            if style_summ.issues[StyleSummary.ERROR_FUNCTION_NO_COMMENT] >= 2:
                score = 0
            elif style_summ.issues[StyleSummary.ERROR_FUNCTION_NO_COMMENT] == 1:
                if style_summ.issues[StyleSummary.ERROR_FUNCTION_COMMENT] >= 2:
                    score  = 0
                else:
                    score = 4
            elif style_summ.issues[StyleSummary.ERROR_FUNCTION_COMMENT] >= 2:
                score  = 4
            elif style_summ.issues[StyleSummary.ERROR_FUNCTION_COMMENT] >= 1:
                score  = 7        
    elif StyleSummary.ERROR_PACKAGE_INCLUDE in cat_num:
        max = 5
        score = 5
        if style_summ.issues[StyleSummary.ERROR_PACKAGE_INCLUDE] > 0:
            score = 0
    elif StyleSummary.ERROR_FUNC_ORDER in cat_num:
        max = 5
        score = 5
        if style_summ.issues[StyleSummary.ERROR_FUNC_ORDER] > 0:
            score = 0
    elif StyleSummary.ERROR_GLOBAL_GOTO in cat_num:
        if style_summ.issues[StyleSummary.ERROR_GLOBAL_GOTO] > 1:
            score = 0
        elif style_summ.issues[StyleSummary.ERROR_GLOBAL_GOTO] > 0:
            score = 5
    else:
        if style_summ.issues[cat_num[0]] >= 3:
            score = 0
        elif style_summ.issues[cat_num[0]] == 2:
            score = 4
        elif style_summ.issues[cat_num[0]] == 1:
            score = 7
    return score, max


def print_category_results(style_summ, cat_num, cat_str):
    """TBD."""
    score, max = get_cat_score(style_summ, cat_num)
    style_summ.total += max
    style_summ.score += score
    print(cat_str, ' --> ', score, '/', max)
    for src_file in style_summ.files:
        for stmt_ind in range(len(src_file.lines)):
            for issue in src_file.lines[stmt_ind].issues:
                if issue[0] in cat_num:
                    print('    ', src_file.filename, ' (', '{:3d}'.format(stmt_ind + 1), ') ', issue[1], sep='')


def print_summary_results(style_summ):
    for ind in range(StyleSummary.ERROR_OTHER+1):
        style_summ.issues[ind] = 0
    style_summ.total = 0
    style_summ.score = 0
    for src_file in style_summ.files:
        for stmt in src_file.lines:
            for issue in stmt.issues:
                style_summ.issues[issue[0]] += 1
    for cat in StyleSummary.CATEGORIES:
        print_category_results(style_summ, cat[0], cat[1])
    print('------------------------------')
    print('Style Score:', style_summ.score, '/', style_summ.total)
    print()
    for src_file in style_summ.files:
        print('******************************')
        print(src_file.filename)
        print('******************************')
        if len(src_file.lines) == 0:
            print('MISSING FILE!!!')
        elif len(src_file.tokens) == 0:
            print('BLANK FILE!!!')
        else:
            for stmt in src_file.lines:
                for issue in stmt.issues:
                    print('// STYLE CHECK:', issue[1])
                print(''.join(stmt.orig_line), end='')


def get_category_results(style_summ, cat_num, cat_str):
    """TBD."""
    cat_text = ''
    score, max = get_cat_score(style_summ, cat_num)
    style_summ.total += max
    style_summ.score += score
    cat_text += cat_str + ' --> ' + str(score) + '/' + str(max) + '\n'
    for src_file in style_summ.files:
        for stmt_ind in range(len(src_file.lines)):
            for issue in src_file.lines[stmt_ind].issues:
                if issue[0] in cat_num:
                    cat_text += '    ' + src_file.filename + ' (' + str(stmt_ind + 1) + ') ' + issue[1] + '\n'
    return cat_text


def get_summary_results(style_summ, replace_less=False, span_color=False):
    summ_text = ''
    for ind in range(StyleSummary.ERROR_OTHER+1):
        style_summ.issues[ind] = 0
    style_summ.total = 0
    style_summ.score = 0
    for src_file in style_summ.files:
        for stmt in src_file.lines:
            for issue in stmt.issues:
                style_summ.issues[issue[0]] += 1
    for cat in StyleSummary.CATEGORIES:
        summ_text += get_category_results(style_summ, cat[0], cat[1])
    final_grade = style_summ.score / style_summ.total * 100
    summ_text = 'Style Score:' + str(style_summ.score) + '/' + str(style_summ.total) + '\n' \
                + '------------------------------\n' + summ_text + "\n"

    for src_file in style_summ.files:
        summ_text += '******************************\n'
        summ_text += src_file.filename + '\n'
        summ_text += '******************************\n'
        if len(src_file.lines) == 0:
            summ_text += 'MISSING FILE!!!\n'
        elif len(src_file.tokens) == 0:
            summ_text += 'BLANK FILE!!!\n'
        else:
            for stmt in src_file.lines:
                for issue in stmt.issues:
                    if span_color:
                        summ_text += '<span style="background-color: pink">'
                    summ_text += '// STYLE CHECK: ' + issue[1] + '\n'
                    if span_color:
                        summ_text += '</span>'
                if replace_less:
                    summ_text += ''.join(stmt.orig_line).replace('<', '&lt;')
                else:
                    summ_text += ''.join(stmt.orig_line)
    return summ_text


def get_final_grade(style_summ):
    return style_summ.score / style_summ.total * 100


def process_one_file(src_file):
    """TBD."""
    remove_comments_and_strings(src_file)
    tokenize_stmts(src_file)
    classify_tokens(src_file)

    check_indentation(src_file)
    check_capitalization(src_file)
    check_spacing(src_file)
    check_blank_lines(src_file)
    check_multiple_stmts(src_file)
    check_token_use(src_file)
    check_comments(src_file)
    check_other_stuff(src_file)
