#!/usr/bin/env python3

"""Style Check a Source File."""

__author__ = 'Karen Peterson'
__date__ = '4/15/2021'

import pathlib
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
    EMPTY_STMT = 81
    END_STMT = 82

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
                    ';': (EMPTY_STMT, False, '', False)
                    }

    def __init__(self):
        """Constructor."""
        self.stmt_type = self.NO_STMT
        self.first_token = -1
        self.last_token = -1


class Comment:
    """TBD."""
    def __init__(self):
        """Constructor."""
        self.start_line = -1
        self.start_col = -1
        self.end_line = -1
        self.end_col = -1


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
    # KP - should I move these here instead of in line
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

    CATEGORIES = (([Line.ERROR_FILE_NO_COMMENT, Line.ERROR_FILE_COMMENT], 'File Comments'),
                  ([Line.ERROR_FUNCTION_NO_COMMENT, Line.ERROR_FUNCTION_COMMENT], 'Function Comments'),
                  ([Line.ERROR_PACKAGE_INCLUDE], 'Package/Includes'),
                  ([Line.ERROR_GLOBAL_GOTO], 'Globals, continue, goto, break'),
                  ([Line.ERROR_UPPER_LOWER_CASE], 'Using proper case'),
                  ([Line.ERROR_INDENTATION], 'Indentation issues'),
                  ([Line.ERROR_SPACING], 'Spacing issues'),
                  ([Line.ERROR_BRACES], 'Brace formatting'),
                  ([Line.ERROR_DECLARATIONS], 'Declarations'),
                  ([Line.ERROR_FUNC_ORDER], 'Function order'),
                  ([Line.ERROR_OTHER], 'Other issues'))

    def __init__(self):
        """Constructor."""
        self.files = []
        self.issues = {}
        self.score = 0
        self.total = 100


def read_source_file(src_file):
    """TBD."""
    if pathlib.Path(src_file.filename).exists():
        with open(src_file.filename, 'r') as in_file:
            for line in in_file:
                one_line = Line()
                line = list(line)
                detabify(line)
                one_line.orig_line = line
                one_line.clean_line = line.copy()
                src_file.lines.append(one_line)


def remove_comments_and_strings(src_file):
    """TBD."""
    in_quote = False
    in_single_quote = False
    in_multi_comment = False
    in_single_comment = False
    prev_char = ' '
    set_space = False
    # line_ind = 0
    for full_line in src_file.lines:  # line_ind in range(len(src_file.lines)): # KP: for stmt in lines:
        # line = src_file.lines[line_ind].clean_line
        line = full_line.clean_line
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
    # '->*' may need to account for this in C++

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


def token_to_string2(token): #KP - can remove this function
    """TBD."""
    return token.tok_str  # ''.join(token.tok)


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
    # tokens = src_file.tokens
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
        elif curr_tok.tok_str in 'while':
            new_stmt.stmt_type = Statement.WHILE_STMT
            tmp_tok = get_prev_token(tokens, tok_ind)
            tok_ind = continue_till_char(tokens, tok_ind, ')', True)
            # KP - Assumes that } while (...); is end of a do-while
            if tmp_tok.tok_str == '}':
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
        # need this, but need to make sure next token is : before labeling it an ACCESS_STMT
        elif (curr_tok.tok_str in ['private', 'public', 'protected']
              and tok_ind + 1 < len(tokens) and tokens[tok_ind + 1].tok_str == ':'):
            new_stmt.stmt_type = Statement.ACCESS_STMT
            # tok_ind = continue_till_char(tokens, tok_ind, ':', True)
            tok_ind = continue_till_char(tokens, tok_ind, ':', False)
        else:
            left_paren_tok = find_next_token(tokens, tok_ind, '(')
            semi_tok = find_next_token(tokens, tok_ind, ';')
            left_curly_tok = find_next_token(tokens, tok_ind, '{')
            equal_tok = find_next_token(tokens, tok_ind, '=')
            # test to find smallest
            # if ( then function header or prototype or call
            # if ; then regular Line - possibly declare
            # if { then class or random block? or array declaration with initialization
            # NOTE - need to check for = for assignment with ( )
            small_tok = find_smallest(find_smallest(left_paren_tok, semi_tok),
                                      find_smallest(left_curly_tok, equal_tok))
            small_tok_str = small_tok.tok_str
            if small_tok_str in ['=', ';']:
                # NOTE - need to separate sequence from declaration
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
                        var_tok_ind = small_tok.ind
                        while finding_vars:
                            var_tok = get_prev_token(tokens, var_tok_ind)
                            while var_tok.tok_str == ']':
                                var_tok_ind = continue_till_char(tokens,
                                                                 var_tok_ind,
                                                                 '[',
                                                                 match=True,
                                                                 forward=False)
                                var_tok = get_prev_token(tokens, var_tok_ind)
                                var_tok_ind = var_tok.ind
                            var_tok.tok_type = var_type # Token.VAR_ID_TOKEN
                            var_tok = get_prev_token(tokens, var_tok_ind)
                            var_tok_ind = var_tok.ind
                            finding_vars = var_tok.tok_str == ','
                tok_ind = continue_till_char(tokens, tok_ind, ';')
            elif small_tok_str == '(':
                # KP - is the following note still true - are prototypes falling in this elif?
                # NOTE - these could be function calls or prototypes or void function call
                # -- need to get matching ) and then look at next token { for function def versus something else
                src_file.num_functions += 1
                new_stmt.stmt_type = Statement.FUNC_HDR_STMT
                fun_name_tok = get_prev_token(tokens, left_paren_tok.ind)
                fun_name_tok.tok_type = Token.FUNC_ID_TOKEN
                tok_ind = continue_till_char(tokens, tok_ind, ')', True)
                tmp_tok = get_next_token(tokens, tok_ind)
                if tmp_tok.tok_str != '{':
                    new_stmt.stmt_type = Statement.SEQUENCE_STMT
                    tok_ind = continue_till_char(tokens, tok_ind, ';')
                """ KP - do not care if line is a function prototype
                if tmp_tok.tok_str in ['=', ';']:
                    new_stmt.stmt_type = Statement.PROTOTYPE_STMT
                    tok_ind = continue_till_char(tokens, tok_ind, ';')
                elif tmp_tok.tok_str != '{':
                    new_stmt.stmt_type = Statement.SEQUENCE_STMT
                    tok_ind = continue_till_char(tokens, tok_ind, ';')
                """
            elif small_tok_str == '{':
                # need to check for array declaration and verify if public/private/static before class is included here
                # tok_ind = continue_till_char(tokens, tok_ind, '{', True)
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
                            print('KP', src_file.tokens[tmp_ind].tok_str, src_file.tokens[tmp_ind].tok_type)
                            if src_file.tokens[tmp_ind].tok_type == Token.ID_TOKEN:
                                src_file.tokens[tmp_ind].tok_type = Token.ENUM_VALUE_ID_TOKEN
                        # tok_ind = get_next_token(tokens, tok_ind).ind
                        done = True
                    tmp_ind += 1
                new_stmt.stmt_type = stmt_type
                var_tok = get_prev_token(tokens, left_curly_tok.ind)
                var_tok.tok_type = tok_type
            else:
                pass # curr_tok.Statement = Statement.CONTINUATION
        tok_ind += 1 #, curr_tok = get_next_token(src_file, tok_ind)
        new_stmt.last_token = tok_ind
        for ind in range(new_stmt.first_token, new_stmt.last_token):
            tokens[ind].stmt = len(src_file.statements)
        src_file.statements.append(new_stmt)


def check_capitalization(src_file):
    """TBD."""
    for tok in src_file.tokens:
        if tok.tok_type == Token.FUNC_ID_TOKEN:
            if tok.tok_str[0].isupper():
                src_file.lines[tok.line].issues.append((Line.ERROR_UPPER_LOWER_CASE,
                                                        'Function name must start with lowercase letter'))
        elif tok.tok_type == Token.VAR_ID_TOKEN:
            if tok.tok_str[0].isupper():
                src_file.lines[tok.line].issues.append((Line.ERROR_UPPER_LOWER_CASE,
                                                       'Variable name must start with lowercase letter'))
        elif tok.tok_type == Token.CLASS_ID_TOKEN:
            if tok.tok_str[0].islower():
                src_file.lines[tok.line].issues.append((Line.ERROR_UPPER_LOWER_CASE,
                                                        'Class name must start with uppercase letter'))
        elif tok.tok_type == Token.STRUCT_ID_TOKEN:
            if tok.tok_str[0].islower():
                src_file.lines[tok.line].issues.append((Line.ERROR_UPPER_LOWER_CASE,
                                                        'Struct name must start with uppercase letter'))
        elif tok.tok_type == Token.ENUM_ID_TOKEN:
            if tok.tok_str[0].islower():
                src_file.lines[tok.line].issues.append((Line.ERROR_UPPER_LOWER_CASE,
                                                        'Enum name must start with uppercase letter'))
        elif tok.tok_type in [Token.CONSTANT_ID_TOKEN, Token.ENUM_VALUE_ID_TOKEN]:
            msg = 'Constant name must be all uppercase letters'
            if tok.tok_type == Token.ENUM_VALUE_ID_TOKEN:
                msg = 'Enum value must be all uppercase letters'
            all_upper = True
            for let in tok.tok_str:
                if let.islower():
                    all_upper = False
            if not all_upper:
                src_file.lines[tok.line].issues.append((Line.ERROR_UPPER_LOWER_CASE,
                                                        msg + ' (' + tok.tok_str + ')'))


def check_spacing(src_file):
    """TBD."""
    prev_tok = Token()
    next_tok = Token()
    for tok in src_file.tokens:
        if tok.tok_type == Token.OP_TOKEN:
            tok_str = tok.tok_str
            need_space_before = False
            need_space_before_check = False
            need_space_after = False
            need_space_after_check = False
            if tok_str in ['++', '--']:
                # check either before or after is an id, no space
                pass
            elif tok_str in ['<<', '>>',
                             '<=', '>=', '==', '!=', '&&', '||',
                             '*=', '/=', '+=', '-=', '&=', '^=', '|=']:
                need_space_before = True
                need_space_before_check = True
                need_space_after = True
                need_space_after_check = True
            elif tok_str == '(' and prev_tok.tok_type == Token.FUNC_ID_TOKEN:
                need_space_before = False
                need_space_before_check = True
            """
                ['::', '++', '--', '->', '.*', '<<', '>>',
                      '<=', '>=', '==', '!=', '&&', '||',
                      '*=', '/=', '+=', '-=', '&=', '^=', '|=']"""
            if need_space_before_check:
                end_col = len(prev_tok.tok_str) + prev_tok.col
                if tok.line == prev_tok.line:
                    if end_col < tok.col and (not need_space_before):
                        src_file.lines[tok.line].issues.append((Line.ERROR_SPACING,
                                                                'No space before ' + tok_str))
                    elif end_col >= tok.col and need_space_before:
                        src_file.lines[tok.line].issues.append((Line.ERROR_SPACING,
                                                                'Need space before ' + tok_str))
            if need_space_after_check:
                next_tok = get_next_token(src_file.tokens, tok.ind)
                end_col = len(tok.tok_str) + tok.col
                if tok.line == next_tok.line:
                    if end_col < next_tok.col and (not need_space_after):
                        src_file.lines[tok.line].issues.append((Line.ERROR_SPACING,
                                                               'No space after ' + tok_str))
                    elif end_col >= next_tok.col and need_space_after:
                        src_file.lines[tok.line].issues.append((Line.ERROR_SPACING,
                                                                'Need space after ' + tok_str))
        prev_tok = tok


def check_indentation(src_file):
    """TBD."""
    # KP - not handling {} (inline functions) in :'s properly - I think this part is fixed
    indent_stack = [['', 0]]
    stmt_ind = 0
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
                    line.issues.append((Line.ERROR_INDENTATION,
                                        'Indentation for continued line is not correct - should be at least ' + str(indent_stack[-1][1]) + ' spaces'))
            elif src_file.tokens[line.first_token].col != indent_stack[-1][1]:
                line.issues.append((Line.ERROR_INDENTATION,
                                    'Indentation is not correct - should be ' + str(indent_stack[-1][1]) + ' spaces'))
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
    for line in src_file.lines:
        if ''.join(line.orig_line).strip() == '':
            num_blank += 1
        else:
            num_blank = 0
        if num_blank > 1:
            line.issues.append((Line.ERROR_SPACING,
                                'Too many blank lines'))


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
                        src_file.lines[start_line].issues.append((Line.ERROR_OTHER,
                                                                  'Only one statement per line'))
                ind += 1
            else:
                only_one = src_file.statements[ind].stmt_type != Statement.DO_WHILE_STMT  # KP - True
                while ind < len(src_file.statements) and prev_line == src_file.tokens[src_file.statements[ind].first_token].line:
                    ind += 1
            if only_one:
                src_file.lines[start_line].issues.append((Line.ERROR_OTHER,
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
                src_file.lines[tok.line].issues.append((Line.ERROR_OTHER,
                                                        '==/!= true or false is unnecessary'))
            elif prev_tok.tok_str in ['true', 'false']:
                src_file.lines[tok.line].issues.append((Line.ERROR_OTHER,
                                                        '==/!= true or false is unnecessary'))
        elif tok_str == 'NULL' and src_file.lang == SrcFile.LANG_CPP:
            src_file.lines[tok.line].issues.append((Line.ERROR_OTHER,
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
    return comment


def check_comments(src_file):
    """TBD."""
    if len(src_file.tokens) == 0:
        return
    com_opening = re.compile(r'\/\*[ \n]*\* \S[\s\S]*\*[ \n]*\* Name: \S[\s\S]*\* Date: \S[\s\S]*\*\/')
    end_com_line = src_file.tokens[0].line
    end_com_col = src_file.tokens[0].col
    comment = get_comment(src_file, 0, 0, end_com_line, end_com_col)
    if len(comment) == 0:
        src_file.lines[0].issues.append((Line.ERROR_FILE_NO_COMMENT,
                                                 'Missing comment at top of file'))
    else:
        result = com_opening.match(comment)
        if result is None:
            src_file.lines[0].issues.append((Line.ERROR_FILE_COMMENT,
                                             'Comment at top of file is not in the correct format'))


def check_other_stuff(src_file):
    """TBD."""
    blocks = [[False]]
    found_include_quote = False
    found_func = False
    prev_stmt = Statement()
    com_with_param = re.compile(r'\/\*[ \n]*\* \S[\s\S]*\*[ \n]*\* Parameter: \S[\s\S]*\* Return: \S[\s\S]*\*\/')
    com_without_param = re.compile(r'\/\*[ \n]*\* \S[\s\S]*\*[ \n]*\* Return: \S[\s\S]*\*\/')
    #prog = re.compile('[\s\S]*Parameter: [\s\S]*')
    for stmt_ind in range(len(src_file.statements)):
        stmt = src_file.statements[stmt_ind]
        start_line = src_file.tokens[stmt.first_token].line
        if stmt.stmt_type == Statement.INCLUDE_QUOTE_STMT:
            found_include_quote = True
        elif stmt.stmt_type == Statement.INCLUDE_ANGLE_STMT: # KP - only need for C++
            if found_include_quote:
                src_file.lines[start_line].issues.append((Line.ERROR_PACKAGE_INCLUDE,
                                                          '<> includes should be before "" includes'))
        elif stmt.stmt_type == Statement.START_BLOCK_STMT:
            blocks.append([False])
        elif stmt.stmt_type == Statement.END_BLOCK_STMT:
            blocks.pop()
        elif stmt.stmt_type == Statement.DECLARE_STMT:
            if len(blocks) == 1:
                src_file.lines[start_line].issues.append((Line.ERROR_GLOBAL_GOTO,
                                                          'No global variables'))
            tok_ind = stmt.first_token
            while tok_ind < stmt.last_token:
                if src_file.tokens[tok_ind].tok_str == '[':
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
                        src_file.lines[start_line].issues.append((Line.ERROR_OTHER,
                                                                  'Cannot hard-code number when creating array'))
                tok_ind += 1
            blocks[-1][0] = True
        elif stmt.stmt_type == Statement.DECLARE_CONST_STMT:
            if blocks[-1][0]:
                src_file.lines[start_line].issues.append((Line.ERROR_DECLARATIONS,
                                                          'Declare constants before other variables'))
        elif stmt.stmt_type == Statement.CONTINUE_STMT:
            src_file.lines[start_line].issues.append((Line.ERROR_GLOBAL_GOTO,
                                                      'May not use continue'))
        elif stmt.stmt_type == Statement.GOTO_STMT:
            src_file.lines[start_line].issues.append((Line.ERROR_GLOBAL_GOTO,
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
                        src_file.lines[start_line].issues.append((Line.ERROR_GLOBAL_GOTO,
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
                src_file.lines[start_line].issues.append((Line.ERROR_FUNC_ORDER,
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
                src_file.lines[start_line].issues.append((Line.ERROR_FUNCTION_NO_COMMENT,
                                                         'Missing comment before function/method'))
            else:
                result = None
                prev_tok = get_prev_token(src_file.tokens, stmt.last_token-1)
                if prev_tok.tok_str == '(':
                    result = com_with_param.match(comment)
                else:
                    result = com_without_param.match(comment)
                if result is None:
                    src_file.lines[start_line].issues.append((Line.ERROR_FUNCTION_COMMENT,
                                                              'Function/method comment is not correct format'))
        if stmt.stmt_type in [Statement.FUNC_HDR_STMT,
                              Statement.FOR_STMT, Statement.WHILE_STMT,
                              Statement.DO_STMT, Statement.IF_STMT,
                              Statement.IF_STMT, Statement.ELSE_IF_STMT,
                              Statement.ELSE_STMT, Statement.SWITCH_STMT,
                              Statement.CLASS_STMT]:
            next_tok = get_next_token(src_file.tokens, stmt.last_token-1)
            if next_tok.tok_str != '{':
                src_file.lines[start_line].issues.append((Line.ERROR_BRACES,
                                                         'Missing opening {'))
            elif next_tok.line == src_file.tokens[stmt.last_token-1].line:
                src_file.lines[start_line].issues.append((Line.ERROR_BRACES,
                                                          '{ must be on the following line'))
        prev_stmt = stmt


def get_cat_score(style_summ, cat_num):
    """TBD."""
    score = 10
    max = 10
    if Line.ERROR_FILE_COMMENT in cat_num:
        if len(style_summ.files) == 1:
            if style_summ.issues[Line.ERROR_FILE_NO_COMMENT] >= 1:
                score = 0
            elif style_summ.issues[Line.ERROR_FILE_COMMENT] >= 1:
                score  = 7
        else:
            if style_summ.issues[Line.ERROR_FILE_NO_COMMENT] >= 2:
                score = 0
            elif style_summ.issues[Line.ERROR_FILE_NO_COMMENT] == 1:
                score  = 4
            elif style_summ.issues[Line.ERROR_FILE_COMMENT] >= 2:
                score  = 4
            elif style_summ.issues[Line.ERROR_FILE_COMMENT] >= 1:
                score  = 7
    elif Line.ERROR_FUNCTION_COMMENT in cat_num:
        total_functions = 0
        for src_file in style_summ.files:
            total_functions += src_file.num_functions
        if total_functions == 1:
            if style_summ.issues[Line.ERROR_FUNCTION_NO_COMMENT] >= 1:
                score = 0
            elif style_summ.issues[Line.ERROR_FUNCTION_COMMENT] >= 1:
                score  = 7
        else:
            if style_summ.issues[Line.ERROR_FUNCTION_NO_COMMENT] >= 2:
                score = 0
            elif style_summ.issues[Line.ERROR_FUNCTION_NO_COMMENT] == 1:
                score  = 4
            elif style_summ.issues[Line.ERROR_FUNCTION_COMMENT] >= 2:
                score  = 4
            elif style_summ.issues[Line.ERROR_FUNCTION_COMMENT] >= 1:
                score  = 7        
    elif Line.ERROR_PACKAGE_INCLUDE in cat_num:
        max = 5
        score = 5
        if style_summ.issues[Line.ERROR_PACKAGE_INCLUDE] > 0:
            score = 0
    elif Line.ERROR_FUNC_ORDER in cat_num:
        max = 5
        score = 5
        if style_summ.issues[Line.ERROR_FUNC_ORDER] > 0:
            score = 0
    elif Line.ERROR_GLOBAL_GOTO in cat_num:
        if style_summ.issues[Line.ERROR_GLOBAL_GOTO] > 0:
            score = 0
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
                    print('    ', src_file.filename, ' (', stmt_ind + 1, ') ', issue[1], sep='')


def print_summary_results(style_summ):
    for ind in range(Line.ERROR_OTHER+1):
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
    for ind in range(Line.ERROR_OTHER+1):
        style_summ.issues[ind] = 0
    style_summ.total = 0
    style_summ.score = 0
    for src_file in style_summ.files:
        for stmt in src_file.lines:
            for issue in stmt.issues:
                style_summ.issues[issue[0]] += 1
    for cat in StyleSummary.CATEGORIES:
        summ_text += get_category_results(style_summ, cat[0], cat[1])
    summ_text += '------------------------------\n'
    summ_text += 'Style Score:' + str(style_summ.score) + '/' + str(style_summ.total) + '\n\n'

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


from browser import document, html


def read_upload_file(src_file, dom_file_obj):
    """TBD."""
    tmp = document[dom_file_obj].value
    all_lines = tmp.split('\n')
    for line in all_lines:
        one_line = Line()
        line_with_new = line + '\n'
        line_list = list(line_with_new)
        detabify(line_list)
        one_line.orig_line = line_list
        one_line.clean_line = line_list.copy()
        src_file.lines.append(one_line)


def do_it(event):
    tmp_msg = ''
    for x in document.select('textarea.fileText'):
        tmp_msg += x.id + '\n'
    alert(tmp_msg)
    
    style_summ = StyleSummary()
    style_summ.files = []
    
    src_file = SrcFile()
    src_file.filename = document['fileName1'].value
    read_upload_file(src_file, 'fileSource1')
        
    process_one_file(src_file)
    
    style_summ.files.append(src_file)

    output_str = '<pre>' + get_summary_results(style_summ, True, True) + '</pre>'
        
    document['results'].text = ''
    document['results'] <= html.P(output_str)

from browser import document, alert, html
document['run'].bind('click',do_it)

