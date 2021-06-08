// Transcrypt'ed from Python, 2021-06-08 19:49:57
var re = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_re__ from './re.js';
__nest__ (re, '', __module_re__);
var __name__ = 'sc_lib';
export var __author__ = 'Karen Peterson';
export var __date__ = '4/15/2021';
export var SPACES_PER_INDENT = 4;
export var Token =  __class__ ('Token', [object], {
	__module__: __name__,
	NO_TOKEN: 0,
	OP_TOKEN: 1,
	FUNC_ID_TOKEN: 2,
	VAR_ID_TOKEN: 3,
	CLASS_ID_TOKEN: 4,
	STRUCT_ID_TOKEN: 5,
	ENUM_ID_TOKEN: 6,
	ENUM_VALUE_ID_TOKEN: 7,
	CONSTANT_ID_TOKEN: 8,
	NUMBER_TOKEN: 9,
	ID_TOKEN: 10,
	get __init__ () {return __get__ (this, function (self) {
		self.tok_str = '';
		self.line = -(1);
		self.col = -(1);
		self.stmt = -(1);
		self.ind = -(1);
		self.tok_type = Token.NO_TOKEN;
	});}
});
export var Line =  __class__ ('Line', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		self.orig_line = [];
		self.clean_line = [];
		self.first_token = -(1);
		self.last_token = -(1);
		self.issues = [];
		self.issue_types = [];
	});}
});
export var NO_STMT = 0;
export var CONTINUATION = 1;
export var INCLUDE_ANGLE_STMT = 10;
export var INCLUDE_QUOTE_STMT = 11;
export var PREPROCESSOR_STMT = 12;
export var USING_STMT = 13;
export var START_BLOCK_STMT = 20;
export var END_BLOCK_STMT = 21;
export var FOR_STMT = 30;
export var WHILE_STMT = 31;
export var DO_STMT = 32;
export var DO_WHILE_STMT = 33;
export var IF_STMT = 40;
export var ELSE_IF_STMT = 41;
export var ELSE_STMT = 42;
export var SWITCH_STMT = 43;
export var CASE_STMT = 44;
export var DEFAULT_STMT = 45;
export var CONTINUE_STMT = 50;
export var GOTO_STMT = 51;
export var BREAK_STMT = 52;
export var DECLARE_STMT = 60;
export var DECLARE_CONST_STMT = 61;
export var PROTOTYPE_STMT = 70;
export var FUNC_HDR_STMT = 71;
export var CLASS_STMT = 72;
export var ACCESS_STMT = 73;
export var STRUCT_STMT = 74;
export var ENUM_STMT = 75;
export var BLOCK_INTRO_STMT = 76;
export var SEQUENCE_STMT = 80;
export var RETURN_STMT = 81;
export var EMPTY_STMT = 82;
export var END_STMT = 83;
export var Statement =  __class__ ('Statement', [object], {
	__module__: __name__,
	NO_STMT: 0,
	CONTINUATION: 1,
	INCLUDE_ANGLE_STMT: 10,
	INCLUDE_QUOTE_STMT: 11,
	PREPROCESSOR_STMT: 12,
	USING_STMT: 13,
	START_BLOCK_STMT: 20,
	END_BLOCK_STMT: 21,
	FOR_STMT: 30,
	WHILE_STMT: 31,
	DO_STMT: 32,
	DO_WHILE_STMT: 33,
	IF_STMT: 40,
	ELSE_IF_STMT: 41,
	ELSE_STMT: 42,
	SWITCH_STMT: 43,
	CASE_STMT: 44,
	DEFAULT_STMT: 45,
	CONTINUE_STMT: 50,
	GOTO_STMT: 51,
	BREAK_STMT: 52,
	DECLARE_STMT: 60,
	DECLARE_CONST_STMT: 61,
	PROTOTYPE_STMT: 70,
	FUNC_HDR_STMT: 71,
	CLASS_STMT: 72,
	ACCESS_STMT: 73,
	STRUCT_STMT: 74,
	ENUM_STMT: 75,
	BLOCK_INTRO_STMT: 76,
	SEQUENCE_STMT: 80,
	RETURN_STMT: 81,
	EMPTY_STMT: 82,
	END_STMT: 83,
	KEYWORD_DICT: dict ({'using': tuple ([USING_STMT, true, ';', false]), '{': tuple ([START_BLOCK_STMT, false, '', false]), '}': tuple ([END_BLOCK_STMT, false, '', false]), 'for': tuple ([FOR_STMT, true, ')', true]), 'do': tuple ([DO_STMT, false, '', false]), 'if': tuple ([IF_STMT, true, ')', true]), 'switch': tuple ([SWITCH_STMT, true, ')', true]), 'case': tuple ([CASE_STMT, true, ':', false]), 'default': tuple ([DEFAULT_STMT, true, ':', false]), 'continue': tuple ([CONTINUE_STMT, true, ';', false]), 'goto': tuple ([GOTO_STMT, true, ';', false]), 'break': tuple ([BREAK_STMT, true, ';', false]), 'return': tuple ([RETURN_STMT, true, ';', false]), ';': tuple ([EMPTY_STMT, false, '', false])}),
	get __init__ () {return __get__ (this, function (self) {
		self.stmt_type = self.NO_STMT;
		self.first_token = -(1);
		self.last_token = -(1);
	});}
});
export var SrcFile =  __class__ ('SrcFile', [object], {
	__module__: __name__,
	LANG_CPP: 1,
	LANG_JAVA: 2,
	LANG_CSHARP: 3,
	CASE_CAMEL: 1,
	CASE_PASCAL: 2,
	CASE_ALL_UPPER: 3,
	get __init__ () {return __get__ (this, function (self) {
		self.filename = '';
		self.num_functions = 0;
		self.lines = [];
		self.tokens = [];
		self.statements = [];
		self.indent = SPACES_PER_INDENT;
		self.lang = self.LANG_CPP;
		self.curly_same_line = true;
		self.class_name = self.CASE_PASCAL;
		self.func_name = self.CASE_CAMEL;
	});}
});
export var StyleSummary =  __class__ ('StyleSummary', [object], {
	__module__: __name__,
	ERROR_GENERIC: 0,
	ERROR_FILE_NO_COMMENT: 1,
	ERROR_FILE_COMMENT: 2,
	ERROR_FUNCTION_NO_COMMENT: 3,
	ERROR_FUNCTION_COMMENT: 4,
	ERROR_PACKAGE_INCLUDE: 5,
	ERROR_GLOBAL_GOTO: 6,
	ERROR_UPPER_LOWER_CASE: 7,
	ERROR_INDENTATION: 8,
	ERROR_SPACING: 9,
	ERROR_BRACES: 10,
	ERROR_DECLARATIONS: 11,
	ERROR_FUNC_ORDER: 12,
	ERROR_OTHER: 13,
	CATEGORIES: tuple ([tuple ([[ERROR_FILE_NO_COMMENT, ERROR_FILE_COMMENT], 'File Comments']), tuple ([[ERROR_FUNCTION_NO_COMMENT, ERROR_FUNCTION_COMMENT], 'Method/Function Comments']), tuple ([[ERROR_PACKAGE_INCLUDE], 'Package/Includes']), tuple ([[ERROR_GLOBAL_GOTO], 'Globals/continue/breaks']), tuple ([[ERROR_UPPER_LOWER_CASE], 'Proper upper/lowercases']), tuple ([[ERROR_INDENTATION], 'Proper indentation']), tuple ([[ERROR_SPACING], 'Proper spacing']), tuple ([[ERROR_BRACES], 'Proper braces']), tuple ([[ERROR_DECLARATIONS], 'Proper declarations']), tuple ([[ERROR_FUNC_ORDER], 'Proper method/function order']), tuple ([[ERROR_OTHER], 'Other issues'])]),
	get __init__ () {return __get__ (this, function (self) {
		self.files = [];
		self.issues = dict ({});
		self.score = 0;
		self.total = 100;
	});}
});
export var remove_comments_and_strings = function (src_file) {
	var in_quote = false;
	var in_single_quote = false;
	var in_multi_comment = false;
	var in_single_comment = false;
	var prev_char = ' ';
	var set_space = false;
	for (var full_line of src_file.lines) {
		var line = full_line.clean_line;
		var prev_char = '\n';
		var prev_prev_char = '\n';
		for (var ind = 0; ind < len (line); ind++) {
			var set_space = false;
			if (in_quote) {
				if (line [ind] == '"' && (prev_char != '\\' || prev_prev_char == '\\')) {
					var in_quote = false;
				}
				else {
					var set_space = true;
				}
			}
			else if (in_single_quote) {
				if (line [ind] == "'" && (prev_char != '\\' || prev_prev_char == '\\')) {
					var in_single_quote = false;
				}
				else {
					var set_space = true;
				}
			}
			else if (in_multi_comment) {
				if (line [ind] == '/' && prev_char == '*') {
					var in_multi_comment = false;
					line [ind - 1] = ' ';
					var set_space = true;
				}
				else if (line [ind] != '\n') {
					var set_space = true;
				}
			}
			else if (in_single_comment) {
				if (line [ind] == '\n') {
					var in_single_comment = false;
				}
				else {
					var set_space = true;
				}
			}
			else if (line [ind] == '"') {
				var in_quote = true;
			}
			else if (line [ind] == "'") {
				var in_single_quote = true;
			}
			else if (line [ind] == '*' && prev_char == '/') {
				var in_multi_comment = true;
				line [ind - 1] = ' ';
				var set_space = true;
			}
			else if (line [ind] == '/' && prev_char == '/') {
				var in_single_comment = true;
				line [ind - 1] = ' ';
				var set_space = true;
			}
			var prev_prev_char = prev_char;
			var prev_char = line [ind];
			if (set_space) {
				line [ind] = ' ';
			}
		}
	}
};
export var detabify = function (line) {
	var ind = 0;
	while (ind < len (line)) {
		if (line [ind] == '\t') {
			line [ind] = ' ';
			var leftover = (SPACES_PER_INDENT - 1) - __mod__ (ind, SPACES_PER_INDENT);
			for (var _ = 0; _ < leftover; _++) {
				line.insert (ind, ' ');
			}
			ind += leftover;
		}
		ind++;
	}
};
export var tokenize_stmts = function (src_file) {
	var token_cnt = 0;
	var token_start = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ';
	var token_middle = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ0123456789';
	var long_op_tokens = ['::', '++', '--', '->', '.*', '<<', '>>', '<=', '>=', '==', '!=', '&&', '||', '*=', '/=', '+=', '-=', '&=', '^=', '|='];
	for (var line_num = 0; line_num < len (src_file.lines); line_num++) {
		var line = src_file.lines [line_num].clean_line;
		src_file.lines [line_num].first_token = token_cnt;
		var line_len = len (line);
		var col_num = 0;
		var tok_chars = [];
		while (col_num < line_len) {
			if (__in__ (line [col_num], token_start)) {
				var new_tok = Token ();
				var tok_chars = [];
				new_tok.line = line_num;
				new_tok.col = col_num;
				new_tok.ind = token_cnt;
				new_tok.tok_type = Token.ID_TOKEN;
				while (__in__ (line [col_num], token_middle)) {
					tok_chars.append (line [col_num]);
					col_num++;
				}
				new_tok.tok_str = ''.join (tok_chars);
				src_file.tokens.append (new_tok);
				token_cnt++;
			}
			else if (line [col_num].isspace ()) {
				col_num++;
			}
			else if (__in__ (line [col_num], '.0123456789')) {
				var new_tok = Token ();
				var tok_chars = [];
				new_tok.line = line_num;
				new_tok.col = col_num;
				new_tok.ind = token_cnt;
				new_tok.tok_type = Token.NUMBER_TOKEN;
				tok_chars.append (line [col_num]);
				col_num++;
				while (__in__ (line [col_num], '.0123456789')) {
					tok_chars.append (line [col_num]);
					col_num++;
				}
				new_tok.tok_str = ''.join (tok_chars);
				src_file.tokens.append (new_tok);
				token_cnt++;
			}
			else {
				var new_tok = Token ();
				var tok_chars = [];
				tok_chars.append (line [col_num]);
				new_tok.line = line_num;
				new_tok.col = col_num;
				new_tok.tok_type = Token.OP_TOKEN;
				new_tok.ind = token_cnt;
				if (__in__ (line [col_num] + line [col_num + 1], long_op_tokens)) {
					tok_chars.append (line [col_num + 1]);
					col_num++;
				}
				col_num++;
				new_tok.tok_str = ''.join (tok_chars);
				src_file.tokens.append (new_tok);
				token_cnt++;
			}
		}
		src_file.lines [line_num].last_token = token_cnt;
	}
};
export var get_next_token = function (tokens, token_ind) {
	if (token_ind >= 0 && token_ind + 1 < len (tokens)) {
		token_ind++;
		return tokens [token_ind];
	}
	return Token ();
};
export var get_prev_token = function (tokens, token_ind) {
	if (token_ind > 0 && token_ind - 1 < len (tokens)) {
		token_ind--;
		return tokens [token_ind];
	}
	return Token ();
};
export var find_next_token = function (tokens, tok_ind, find_char) {
	var next_tok = Token ();
	while (tok_ind < len (tokens) && tokens [tok_ind].tok_str != find_char) {
		tok_ind++;
	}
	if (tok_ind < len (tokens)) {
		var next_tok = tokens [tok_ind];
	}
	return next_tok;
};
export var continue_till_char = function (tokens, tok_ind, end_char, match, forward) {
	if (typeof match == 'undefined' || (match != null && match.hasOwnProperty ("__kwargtrans__"))) {;
		var match = false;
	};
	if (typeof forward == 'undefined' || (forward != null && forward.hasOwnProperty ("__kwargtrans__"))) {;
		var forward = true;
	};
	var count = 0;
	var start_char = '';
	if (match) {
		var match_char_dict = dict ({'(': ')', ')': '(', '{': '}', '}': '{', '[': ']', ']': '[', '<': '>', '>': '>'});
		if (__in__ (end_char, match_char_dict)) {
			var start_char = match_char_dict [end_char];
		}
	}
	var move_to_next_tok = 1;
	if (!(forward)) {
		move_to_next_tok *= -(1);
	}
	var done = false;
	while (!(done)) {
		if (match) {
			if (tokens [tok_ind].tok_str == start_char) {
				count++;
			}
			else if (tokens [tok_ind].tok_str == end_char) {
				count--;
			}
		}
		if (tokens [tok_ind].tok_str == end_char && count == 0) {
			var done = true;
		}
		else if (tok_ind + move_to_next_tok >= 0 && tok_ind + move_to_next_tok < len (tokens)) {
			tok_ind += move_to_next_tok;
		}
		else {
			var done = true;
		}
	}
	return tok_ind;
};
export var find_smallest = function (tok1, tok2) {
	if (tok1.line == -(1)) {
		return tok2;
	}
	else if (tok2.line == -(1)) {
		return tok1;
	}
	else if (tok1.line < tok2.line) {
		return tok1;
	}
	else if (tok2.line < tok1.line) {
		return tok2;
	}
	else if (tok1.col < tok2.col) {
		return tok1;
	}
	return tok2;
};
export var classify_tokens = function (src_file) {
	src_file.num_functions = 0;
	var tokens = src_file.tokens;
	src_file.statements = [];
	var tok_ind = 0;
	while (tok_ind < len (tokens)) {
		var curr_tok = tokens [tok_ind];
		var curr_tok_str = curr_tok.tok_str;
		var new_stmt = Statement ();
		new_stmt.first_token = tok_ind;
		if (__in__ (curr_tok_str, Statement.KEYWORD_DICT)) {
			var key_info = Statement.KEYWORD_DICT [curr_tok_str];
			new_stmt.stmt_type = key_info [0];
			if (key_info [1]) {
				var tok_ind = continue_till_char (tokens, tok_ind, key_info [2], key_info [3]);
			}
		}
		else if (curr_tok_str == '#') {
			var next_tok = get_next_token (tokens, tok_ind);
			if (next_tok.tok_str == 'include') {
				var next2_tok = get_next_token (tokens, next_tok.ind);
				if (next2_tok.tok_str == '<') {
					new_stmt.stmt_type = Statement.INCLUDE_ANGLE_STMT;
					var end_char = '>';
				}
				else {
					new_stmt.stmt_type = Statement.INCLUDE_QUOTE_STMT;
					var end_char = '"';
				}
				var tok_ind = next2_tok.ind + 1;
				var tok_ind = continue_till_char (tokens, tok_ind, end_char);
			}
			else {
				new_stmt.stmt_type = Statement.PREPROCESSOR_STMT;
			}
		}
		else if (curr_tok.tok_str == 'while') {
			new_stmt.stmt_type = Statement.WHILE_STMT;
			var tmp_tok = get_prev_token (tokens, tok_ind);
			var tok_ind = continue_till_char (tokens, tok_ind, ')', true);
			if (tmp_tok.tok_str == '}') {
				var tmp2_tok = get_next_token (tokens, tok_ind);
				if (tmp2_tok.tok_str == ';') {
					new_stmt.stmt_type = Statement.DO_WHILE_STMT;
					var tok_ind = tmp2_tok.ind;
				}
			}
		}
		else if (curr_tok.tok_str == 'else') {
			var tmp_tok = get_next_token (tokens, tok_ind);
			if (tmp_tok.tok_str == 'if') {
				var tok_ind = continue_till_char (tokens, tok_ind, ')', true);
				new_stmt.stmt_type = Statement.ELSE_IF_STMT;
			}
			else {
				new_stmt.stmt_type = Statement.ELSE_STMT;
			}
		}
		else if (__in__ (curr_tok.tok_str, ['private', 'public', 'protected']) && tok_ind + 1 < len (tokens) && tokens [tok_ind + 1].tok_str == ':') {
			new_stmt.stmt_type = Statement.ACCESS_STMT;
			var tok_ind = continue_till_char (tokens, tok_ind, ':', false);
		}
		else {
			var left_paren_tok = find_next_token (tokens, tok_ind, '(');
			var semi_tok = find_next_token (tokens, tok_ind, ';');
			var left_curly_tok = find_next_token (tokens, tok_ind, '{');
			var equal_tok = find_next_token (tokens, tok_ind, '=');
			var small_tok = find_smallest (find_smallest (left_paren_tok, semi_tok), find_smallest (left_curly_tok, equal_tok));
			var small_tok_str = small_tok.tok_str;
			if (__in__ (small_tok_str, ['=', ';'])) {
				new_stmt.stmt_type = Statement.SEQUENCE_STMT;
				if (curr_tok.tok_type == Token.ID_TOKEN) {
					var found_const = false;
					var var_type = Token.VAR_ID_TOKEN;
					for (var ind = curr_tok.ind; ind < small_tok.ind; ind++) {
						if (tokens [ind].tok_str == 'const') {
							var var_type = Token.CONSTANT_ID_TOKEN;
							var found_const = true;
						}
					}
					var next_tok = get_next_token (tokens, tok_ind);
					var next_tok_ind = next_tok.ind;
					while (__in__ (next_tok.tok_str, ['<', '['])) {
						if (next_tok.tok_str == '<') {
							var end_char = '>';
						}
						else {
							var end_char = ']';
						}
						var next_tok_ind = continue_till_char (tokens, next_tok_ind, end_char, __kwargtrans__ ({match: true}));
						var next_tok = get_next_token (tokens, next_tok_ind);
						var next_tok_ind = next_tok.ind;
					}
					if (next_tok.tok_type == Token.ID_TOKEN) {
						if (found_const) {
							new_stmt.stmt_type = Statement.DECLARE_CONST_STMT;
						}
						else {
							new_stmt.stmt_type = Statement.DECLARE_STMT;
						}
						var finding_vars = true;
						var tmp_ind = curr_tok.ind;
						while (tmp_ind < semi_tok.ind) {
							if (tokens [tmp_ind + 1].tok_type == Token.ID_TOKEN) {
								// pass;
							}
							else if (tokens [tmp_ind + 1].tok_str == '<') {
								var tmp_ind = continue_till_char (tokens, tmp_ind, '>', __kwargtrans__ ({match: true}));
							}
							else if (tokens [tmp_ind + 1].tok_str == '[') {
								tokens [tmp_ind].tok_type = var_type;
								var tmp_ind = continue_till_char (tokens, tmp_ind, ']', __kwargtrans__ ({match: true}));
								while (tmp_ind < semi_tok.ind && !__in__ (tokens [tmp_ind + 1].tok_str, tuple ([',', ';']))) {
									if (tokens [tmp_ind + 1].tok_str == '(') {
										var tmp_ind = continue_till_char (tokens, tmp_ind, ')', __kwargtrans__ ({match: true}));
									}
									else if (tokens [tmp_ind + 1].tok_str == '[') {
										var tmp_ind = continue_till_char (tokens, tmp_ind, ']', __kwargtrans__ ({match: true}));
									}
									else if (tokens [tmp_ind + 1].tok_str == '{') {
										var tmp_ind = continue_till_char (tokens, tmp_ind, '}', __kwargtrans__ ({match: true}));
									}
									tmp_ind++;
								}
							}
							else if (tokens [tmp_ind + 1].tok_str == '=') {
								tokens [tmp_ind].tok_type = var_type;
								while (tmp_ind < semi_tok.ind && !__in__ (tokens [tmp_ind + 1].tok_str, tuple ([',', ';']))) {
									if (tokens [tmp_ind + 1].tok_str == '(') {
										var tmp_ind = continue_till_char (tokens, tmp_ind, ')', __kwargtrans__ ({match: true}));
									}
									else if (tokens [tmp_ind + 1].tok_str == '[') {
										var tmp_ind = continue_till_char (tokens, tmp_ind, ']', __kwargtrans__ ({match: true}));
									}
									else if (tokens [tmp_ind + 1].tok_str == '{') {
										var tmp_ind = continue_till_char (tokens, tmp_ind, '}', __kwargtrans__ ({match: true}));
									}
									tmp_ind++;
								}
							}
							else if (__in__ (tokens [tmp_ind + 1].tok_str, tuple ([',', ';']))) {
								tokens [tmp_ind].tok_type = var_type;
							}
							tmp_ind++;
						}
					}
				}
				var tok_ind = continue_till_char (tokens, tok_ind, ';');
			}
			else if (small_tok_str == '(') {
				var fun_name_tok = get_prev_token (tokens, left_paren_tok.ind);
				if (fun_name_tok.tok_type == Token.ID_TOKEN) {
					src_file.num_functions++;
					new_stmt.stmt_type = Statement.FUNC_HDR_STMT;
					fun_name_tok.tok_type = Token.FUNC_ID_TOKEN;
				}
				else {
					new_stmt.stmt_type = Statement.SEQUENCE_STMT;
				}
				var tok_ind = continue_till_char (tokens, tok_ind, ')', true);
				var tmp_tok = get_next_token (tokens, tok_ind);
				if (tmp_tok.tok_str != '{') {
					new_stmt.stmt_type = Statement.SEQUENCE_STMT;
					var tok_ind = continue_till_char (tokens, tok_ind, ';');
				}
			}
			else {
				var tok_ind = continue_till_char (tokens, tok_ind, '{', false);
				var tok_ind = get_prev_token (tokens, tok_ind).ind;
				var tmp_ind = new_stmt.first_token;
				var done = false;
				var stmt_type = Statement.BLOCK_INTRO_STMT;
				var tok_type = Token.ID_TOKEN;
				while (tmp_ind < tok_ind && !(done)) {
					if (tokens [tmp_ind].tok_str == 'class') {
						var stmt_type = Statement.CLASS_STMT;
						var tok_type = Token.CLASS_ID_TOKEN;
						var done = true;
					}
					else if (tokens [tmp_ind].tok_str == 'struct') {
						var stmt_type = Statement.STRUCT_STMT;
						var tok_type = Token.STRUCT_ID_TOKEN;
						var done = true;
					}
					else if (tokens [tmp_ind].tok_str == 'enum') {
						var stmt_type = Statement.ENUM_STMT;
						var tok_type = Token.ENUM_ID_TOKEN;
						var tok_ind = continue_till_char (tokens, tok_ind, ';', false);
						for (var tmp_ind = small_tok.ind; tmp_ind < tok_ind; tmp_ind++) {
							if (src_file.tokens [tmp_ind].tok_type == Token.ID_TOKEN) {
								src_file.tokens [tmp_ind].tok_type = Token.ENUM_VALUE_ID_TOKEN;
							}
						}
						var done = true;
					}
					tmp_ind++;
				}
				new_stmt.stmt_type = stmt_type;
				var var_tok = get_prev_token (tokens, left_curly_tok.ind);
				var_tok.tok_type = tok_type;
			}
		}
		tok_ind++;
		new_stmt.last_token = tok_ind;
		for (var ind = new_stmt.first_token; ind < new_stmt.last_token; ind++) {
			tokens [ind].stmt = len (src_file.statements);
		}
		src_file.statements.append (new_stmt);
	}
};
export var check_capitalization = function (src_file) {
	for (var tok of src_file.tokens) {
		if (tok.tok_type == Token.FUNC_ID_TOKEN) {
			if (('A' <= tok.tok_str [0] && tok.tok_str [0] <= 'Z')) {
				src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_UPPER_LOWER_CASE, ('Function name must start with lowercase letter (' + tok.tok_str) + ')']));
			}
		}
		else if (tok.tok_type == Token.VAR_ID_TOKEN) {
			if (('A' <= tok.tok_str [0] && tok.tok_str [0] <= 'Z')) {
				src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_UPPER_LOWER_CASE, ('Variable name must start with lowercase letter (' + tok.tok_str) + ')']));
			}
		}
		else if (tok.tok_type == Token.CLASS_ID_TOKEN) {
			if (('a' <= tok.tok_str [0] && tok.tok_str [0] <= 'z')) {
				src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_UPPER_LOWER_CASE, ('Class name must start with uppercase letter (' + tok.tok_str) + ')']));
			}
		}
		else if (tok.tok_type == Token.STRUCT_ID_TOKEN) {
			if (('a' <= tok.tok_str [0] && tok.tok_str [0] <= 'z')) {
				src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_UPPER_LOWER_CASE, ('Struct name must start with uppercase letter (' + tok.tok_str) + ')']));
			}
		}
		else if (tok.tok_type == Token.ENUM_ID_TOKEN) {
			if (('a' <= tok.tok_str [0] && tok.tok_str [0] <= 'z')) {
				src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_UPPER_LOWER_CASE, ('Enum name must start with uppercase letter (' + tok.tok_str) + ')']));
			}
		}
		else if (__in__ (tok.tok_type, [Token.CONSTANT_ID_TOKEN, Token.ENUM_VALUE_ID_TOKEN])) {
			var msg = 'Constant name must be all uppercase';
			if (tok.tok_type == Token.ENUM_VALUE_ID_TOKEN) {
				var msg = 'Enum value must be all uppercase';
			}
			var all_upper = true;
			for (var let of tok.tok_str) {
				if (('a' <= let && let <= 'z')) {
					var all_upper = false;
				}
			}
			if (!(all_upper)) {
				src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_UPPER_LOWER_CASE, ((msg + ' (') + tok.tok_str) + ')']));
			}
		}
	}
};
export var check_spacing = function (src_file) {
	var prev_tok = Token ();
	var next_tok = Token ();
	var prev_after = -(1);
	for (var tok of src_file.tokens) {
		if (tok.tok_type == Token.OP_TOKEN) {
			var tok_str = tok.tok_str;
			var need_space_before = false;
			var need_space_before_check = false;
			var need_space_after = false;
			var need_space_after_check = false;
			if (__in__ (tok_str, ['++', '--'])) {
				if (prev_tok.tok_type == Token.OP_TOKEN) {
					var need_space_after = false;
					var need_space_after_check = true;
				}
				else {
					var need_space_before = false;
					var need_space_before_check = true;
				}
			}
			else if (__in__ (tok_str, ['<<', '>>', '<=', '>=', '==', '!=', '&&', '||', '*=', '/=', '+=', '-=', '&=', '^=', '|=', '%=', '+', '/', '%:', '='])) {
				var need_space_before = true;
				var need_space_before_check = true;
				var need_space_after = true;
				var need_space_after_check = true;
			}
			else if (__in__ (tok_str, ['::', '->', '.', '['])) {
				var need_space_before = false;
				var need_space_before_check = true;
				var need_space_after = false;
				var need_space_after_check = true;
			}
			else if (__in__ (tok_str, [':'])) {
				if (__in__ (src_file.statements [tok.stmt].stmt_type, tuple ([Statement.CASE_STMT, Statement.DEFAULT_STMT, Statement.ACCESS_STMT]))) {
					var need_space_before = false;
					var need_space_before_check = true;
					var need_space_after = true;
					var need_space_after_check = true;
				}
				else {
					var need_space_before = true;
					var need_space_before_check = true;
					var need_space_after = true;
					var need_space_after_check = true;
				}
			}
			else if (__in__ (tok_str, ['?', ','])) {
				var need_space_before = false;
				var need_space_before_check = true;
				var need_space_after = true;
				var need_space_after_check = true;
			}
			else if (tok_str == '(') {
				if (prev_tok.tok_type == Token.FUNC_ID_TOKEN) {
					var need_space_before = false;
					var need_space_before_check = true;
				}
				else if (__in__ (prev_tok.tok_str, ['if', 'for', 'while', 'switch'])) {
					var need_space_before = true;
					var need_space_before_check = true;
				}
			}
			else if (tok_str == '*') {
				if (!__in__ (prev_tok.tok_str, ['(', '['])) {
					var need_space_before = true;
					var need_space_before_check = true;
				}
			}
			else if (tok_str == '-') {
				if (!__in__ (prev_tok.tok_str, ['(', '['])) {
					var need_space_before = true;
					var need_space_before_check = true;
				}
				var next_tok = get_next_token (src_file.tokens, tok.ind);
				if (next_tok.tok_type == Token.NUMBER_TOKEN) {
					var need_space_after = false;
					var need_space_before_check = true;
				}
				else {
					var need_space_after = true;
					var need_space_before_check = true;
				}
			}
			else if (tok_str == '<') {
				var next_tok = get_next_token (src_file.tokens, tok.ind);
				var next_next_tok = get_next_token (src_file.tokens, next_tok.ind);
				if (__in__ (next_next_tok.tok_str, [',', '>'])) {
					var need_space_after = false;
					var need_space_after_check = true;
				}
				else if (src_file.statements [tok.stmt].stmt_type == Statement.INCLUDE_ANGLE_STMT) {
					var need_space_before = true;
					var need_space_before_check = true;
					var need_space_after = false;
					var need_space_after_check = true;
				}
				else {
					var need_space_before = true;
					var need_space_before_check = true;
					var need_space_after = true;
					var need_space_after_check = true;
				}
			}
			else if (tok_str == '>') {
				var prev_prev_tok = get_prev_token (src_file.tokens, prev_tok.ind);
				if (__in__ (prev_prev_tok.tok_str, [',', '<'])) {
					var need_space_before = false;
					var need_space_before_check = true;
				}
				else if (src_file.statements [tok.stmt].stmt_type == Statement.INCLUDE_ANGLE_STMT) {
					var need_space_before = false;
					var need_space_before_check = true;
					var need_space_after = true;
					var need_space_after_check = true;
				}
				else {
					var need_space_before = true;
					var need_space_before_check = true;
					var need_space_after = true;
					var need_space_after_check = true;
				}
			}
			if (need_space_before_check) {
				var end_col = len (prev_tok.tok_str) + prev_tok.col;
				if (tok.line == prev_tok.line) {
					if (end_col < tok.col && !(need_space_before)) {
						src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_SPACING, 'No space before ' + tok_str]));
					}
					else if (end_col >= tok.col && need_space_before) {
						if (prev_tok.ind != prev_after) {
							src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_SPACING, 'Missing space before ' + tok_str]));
						}
					}
				}
			}
			if (need_space_after_check) {
				var next_tok = get_next_token (src_file.tokens, tok.ind);
				var end_col = len (tok.tok_str) + tok.col;
				if (tok.line == next_tok.line) {
					if (end_col < next_tok.col && !(need_space_after)) {
						src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_SPACING, 'No space after ' + tok_str]));
					}
					else if (end_col >= next_tok.col && need_space_after) {
						var prev_after = tok.ind;
						src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_SPACING, 'Missing space after ' + tok_str]));
					}
				}
			}
		}
		var prev_tok = tok;
	}
};
export var check_indentation = function (src_file) {
	var indent_stack = [['', 0]];
	var stmt_ind = 0;
	var prev_stmt = Statement ();
	for (var line of src_file.lines) {
		if (line.last_token > line.first_token) {
			var stmt_ind = src_file.tokens [line.first_token].stmt;
			if (src_file.statements [stmt_ind].stmt_type == Statement.END_BLOCK_STMT) {
				if (indent_stack [-(1)] [0] == ':') {
					indent_stack.py_pop ();
				}
				indent_stack.py_pop ();
			}
			else if (__in__ (src_file.statements [stmt_ind].stmt_type, [Statement.CASE_STMT, Statement.DEFAULT_STMT, Statement.ACCESS_STMT])) {
				if (indent_stack [-(1)] [0] == ':') {
					indent_stack.py_pop ();
				}
			}
			if (line.first_token > src_file.statements [stmt_ind].first_token) {
				if (src_file.tokens [line.first_token].col < indent_stack [-(1)] [1]) {
					line.issues.append (tuple ([StyleSummary.ERROR_INDENTATION, ('Indentation for continued line is not correct - should be at least ' + str (indent_stack [-(1)] [1])) + ' spaces']));
				}
			}
			else {
				var tmp_indent = indent_stack [-(1)] [1];
				if (stmt_ind > 0 && src_file.statements [stmt_ind].stmt_type != Statement.START_BLOCK_STMT && __in__ (src_file.statements [stmt_ind - 1].stmt_type, [Statement.FOR_STMT, Statement.WHILE_STMT, Statement.DO_STMT, Statement.IF_STMT, Statement.ELSE_IF_STMT, Statement.ELSE_STMT])) {
					var last_tok_prev_stmt = src_file.tokens [src_file.statements [stmt_ind - 1].last_token - 1];
					if (last_tok_prev_stmt.line != src_file.tokens [line.first_token].line) {
						tmp_indent += SPACES_PER_INDENT;
					}
				}
				if (src_file.tokens [line.first_token].col != tmp_indent) {
					line.issues.append (tuple ([StyleSummary.ERROR_INDENTATION, ('Improper indentation - should be ' + str (indent_stack [-(1)] [1])) + ' spaces']));
				}
			}
			for (var tok_ind = line.first_token; tok_ind < line.last_token; tok_ind++) {
				var tmp_stmt_type = src_file.statements [src_file.tokens [tok_ind].stmt].stmt_type;
				if (tmp_stmt_type == Statement.END_BLOCK_STMT && tok_ind != line.first_token) {
					indent_stack.py_pop ();
				}
				else if (tmp_stmt_type == Statement.START_BLOCK_STMT) {
					indent_stack.append (['{', indent_stack [-(1)] [1] + SPACES_PER_INDENT]);
				}
			}
			if (__in__ (src_file.statements [stmt_ind].stmt_type, [Statement.CASE_STMT, Statement.DEFAULT_STMT, Statement.ACCESS_STMT])) {
				indent_stack.append ([':', indent_stack [-(1)] [1] + SPACES_PER_INDENT]);
			}
		}
	}
};
export var check_blank_lines = function (src_file) {
	var num_blank = 0;
	var checking = true;
	for (var line of src_file.lines) {
		if (''.join (line.orig_line).strip () == '') {
			num_blank++;
		}
		else {
			var num_blank = 0;
			var checking = true;
		}
		if (checking && num_blank > 1) {
			var checking = false;
			line.issues.append (tuple ([StyleSummary.ERROR_SPACING, 'Too many blank lines - at most one blank line between sections']));
		}
	}
};
export var check_multiple_stmts = function (src_file) {
	var ind = 0;
	var prev_line = -(1);
	while (ind < len (src_file.statements)) {
		var start_line = src_file.tokens [src_file.statements [ind].first_token].line;
		var end_line = src_file.tokens [src_file.statements [ind].last_token - 1].line;
		if (start_line == prev_line) {
			var only_one = false;
			if (src_file.statements [ind].stmt_type == Statement.EMPTY_STMT) {
				if (ind > 0) {
					var prev_stmt = src_file.statements [ind - 1];
					if (prev_stmt.stmt_type == Statement.END_BLOCK_STMT) {
						var start_block_ind = continue_till_char (src_file.tokens, prev_stmt.first_token, '{', true, false);
						var prev_tok = get_prev_token (src_file.tokens, start_block_ind);
						if (!(__in__ (src_file.statements [prev_tok.stmt].stmt_type, [Statement.CLASS_STMT, Statement.STRUCT_STMT]))) {
							var only_one = true;
						}
					}
					else {
						var only_one = true;
					}
				}
				ind++;
			}
			else if (src_file.statements [ind].stmt_type == Statement.START_BLOCK_STMT) {
				if (ind > 0) {
					var prev_stmt = src_file.statements [ind - 1];
					if (!__in__ (prev_stmt.stmt_type, [Statement.FOR_STMT, Statement.WHILE_STMT, Statement.DO_STMT, Statement.IF_STMT, Statement.ELSE_IF_STMT, Statement.ELSE_STMT, Statement.SWITCH_STMT, Statement.FUNC_HDR_STMT, Statement.CLASS_STMT, Statement.STRUCT_STMT, Statement.ENUM_STMT, Statement.BLOCK_INTRO_STMT])) {
						var only_one = true;
					}
				}
				ind++;
			}
			else {
				var only_one = src_file.statements [ind].stmt_type != Statement.DO_WHILE_STMT;
				while (ind < len (src_file.statements) && prev_line == src_file.tokens [src_file.statements [ind].first_token].line) {
					ind++;
				}
			}
			if (only_one) {
				src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_OTHER, 'Only one statement per line']));
			}
		}
		else {
			ind++;
		}
		var prev_line = end_line;
	}
};
export var check_token_use = function (src_file) {
	var ind = 0;
	while (ind < len (src_file.tokens)) {
		var tok = src_file.tokens [ind];
		var tok_str = tok.tok_str;
		if (__in__ (tok_str, ['==', '!='])) {
			var prev_tok = get_prev_token (src_file.tokens, tok.ind);
			var next_tok = get_next_token (src_file.tokens, tok.ind);
			if (__in__ (next_tok.tok_str, ['true', 'false'])) {
				src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_OTHER, '==/!= true or false is unnecessary']));
			}
			else if (__in__ (prev_tok.tok_str, ['true', 'false'])) {
				src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_OTHER, '==/!= true or false is unnecessary']));
			}
		}
		else if (tok_str == 'NULL' && src_file.lang == SrcFile.LANG_CPP) {
			src_file.lines [tok.line].issues.append (tuple ([StyleSummary.ERROR_OTHER, 'Use nullptr not NULL']));
		}
		ind++;
	}
};
export var get_comment = function (src_file, start_com_line, start_com_col, end_com_line, end_com_col) {
	var comment = '';
	if (start_com_line != end_com_line) {
		for (var char of src_file.lines [start_com_line].orig_line.__getslice__ (start_com_col, null, 1)) {
			comment += char;
		}
		for (var line of src_file.lines.__getslice__ (start_com_line + 1, end_com_line, 1)) {
			for (var char of line.orig_line) {
				comment += char;
			}
		}
		var start_com_col = 0;
	}
	for (var char of src_file.lines [end_com_line].orig_line.__getslice__ (start_com_col, end_com_col, 1)) {
		comment += char;
	}
	var comment = comment.strip ();
	if (comment.endswith ('*/')) {
		var trim_to = comment.rfind ('/*');
		if (trim_to != -(1)) {
			var comment = comment.__getslice__ (trim_to, null, 1);
		}
	}
	return comment;
};
export var check_comments = function (src_file) {
	if (len (src_file.tokens) == 0) {
		return ;
	}
	var com_opening = re.compile ('\\/\\*[ \\n]*\\* \\S[\\s\\S]*\\*[ \\n]*\\* Name:[ \\t]+\\S[\\s\\S]*\\* Date:[ \\t]+\\S[\\s\\S]*\\*\\/');
	var end_com_line = src_file.tokens [0].line;
	var end_com_col = src_file.tokens [0].col;
	var comment = get_comment (src_file, 0, 0, end_com_line, end_com_col);
	if (len (comment) == 0) {
		src_file.lines [0].issues.append (tuple ([StyleSummary.ERROR_FILE_NO_COMMENT, 'Missing comment at top of file']));
	}
	else {
		var result = com_opening.match (comment);
		if (result === null) {
			src_file.lines [0].issues.append (tuple ([StyleSummary.ERROR_FILE_COMMENT, 'Comment at top of file is not in the correct format']));
		}
	}
};
export var check_other_stuff = function (src_file) {
	var blocks = [[false]];
	var found_include_quote = false;
	var found_func = false;
	var prev_stmt = Statement ();
	var com_with_param = re.compile ('\\/\\*[ \\n]*\\* \\S[\\s\\S]*\\*[ \\n]*\\* Parameter:[ \\t]+\\S[\\s\\S]*\\* Return:[ \\t]+\\S[\\s\\S]*\\*\\/');
	var com_without_param = re.compile ('\\/\\*[ \\n]*\\* \\S[\\s\\S]*\\*[ \\n]*\\* Return:[ \\t]+\\S[\\s\\S]*\\*\\/');
	for (var stmt_ind = 0; stmt_ind < len (src_file.statements); stmt_ind++) {
		var stmt = src_file.statements [stmt_ind];
		var start_line = src_file.tokens [stmt.first_token].line;
		if (stmt.stmt_type == Statement.INCLUDE_QUOTE_STMT) {
			var found_include_quote = true;
		}
		else if (stmt.stmt_type == Statement.INCLUDE_ANGLE_STMT) {
			if (found_include_quote) {
				src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_PACKAGE_INCLUDE, '<> includes should be before "" includes']));
			}
		}
		else if (stmt.stmt_type == Statement.START_BLOCK_STMT) {
			blocks.append ([false]);
		}
		else if (stmt.stmt_type == Statement.END_BLOCK_STMT) {
			blocks.py_pop ();
		}
		else if (stmt.stmt_type == Statement.DECLARE_STMT) {
			if (len (blocks) == 1) {
				src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_GLOBAL_GOTO, 'No global variables']));
			}
			var tok_ind = stmt.first_token;
			var num_vars = 0;
			while (tok_ind < stmt.last_token) {
				if (__in__ (src_file.tokens [tok_ind].tok_type, tuple ([Token.VAR_ID_TOKEN, Token.CONSTANT_ID_TOKEN]))) {
					num_vars++;
				}
				else if (src_file.tokens [tok_ind].tok_str == '[') {
					var only_nums = true;
					var bracket_cnt = 1;
					tok_ind++;
					var tok_cnt = 0;
					while (tok_ind < stmt.last_token && bracket_cnt > 0) {
						var tok_str = src_file.tokens [tok_ind].tok_str;
						if (tok_str == ']') {
							bracket_cnt--;
						}
						else if (tok_str == '[') {
							bracket_cnt++;
						}
						else if (tok_str != ',') {
							tok_cnt++;
							if (!(__in__ (src_file.tokens [tok_ind].tok_type, [Token.OP_TOKEN, Token.NUMBER_TOKEN]))) {
								var only_nums = false;
							}
						}
						tok_ind++;
					}
					if (only_nums && tok_cnt > 0) {
						src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_OTHER, 'Cannot hard-code number when creating array']));
					}
				}
				tok_ind++;
			}
			if (num_vars > 1) {
				src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_DECLARATIONS, 'May only declare 1 variable per statement']));
			}
			blocks [-(1)] [0] = true;
		}
		else if (stmt.stmt_type == Statement.DECLARE_CONST_STMT) {
			if (blocks [-(1)] [0]) {
				src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_DECLARATIONS, 'Declare constants before other variables']));
			}
		}
		else if (stmt.stmt_type == Statement.CONTINUE_STMT) {
			src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_GLOBAL_GOTO, 'May not use continue']));
		}
		else if (stmt.stmt_type == Statement.GOTO_STMT) {
			src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_GLOBAL_GOTO, 'May not use goto']));
		}
		else if (stmt.stmt_type == Statement.BREAK_STMT) {
			var tmp_stmt_ind = stmt_ind - 1;
			var done = false;
			var check_for_comment = false;
			while (tmp_stmt_ind > 0 && !(done)) {
				if (src_file.statements [tmp_stmt_ind].stmt_type == Statement.END_BLOCK_STMT) {
					while (tmp_stmt_ind > 0 && src_file.statements [tmp_stmt_ind].stmt_type != Statement.START_BLOCK_STMT) {
						tmp_stmt_ind--;
					}
					if (tmp_stmt_ind > 0 && __in__ (src_file.statements [tmp_stmt_ind - 1].stmt_type, [Statement.FOR_STMT, Statement.WHILE_STMT, Statement.DO_STMT])) {
						tmp_stmt_ind--;
					}
				}
				else if (__in__ (src_file.statements [tmp_stmt_ind].stmt_type, [Statement.CASE_STMT, Statement.DEFAULT_STMT])) {
					var done = true;
				}
				else if (__in__ (src_file.statements [tmp_stmt_ind].stmt_type, [Statement.FOR_STMT, Statement.WHILE_STMT, Statement.DO_STMT])) {
					var done = true;
					var check_for_comment = true;
				}
				tmp_stmt_ind--;
			}
			if (check_for_comment) {
				var start_com_line = src_file.tokens [prev_stmt.last_token - 1].line;
				var start_com_col = src_file.tokens [prev_stmt.last_token - 1].col;
				start_com_col += len (src_file.tokens [prev_stmt.last_token - 1].tok_str);
				var end_com_line = src_file.tokens [stmt.first_token].line;
				var end_com_col = src_file.tokens [stmt.first_token].col;
				var comment = get_comment (src_file, start_com_line, start_com_col, end_com_line, end_com_col);
				if (comment == '') {
					var start_com_line = src_file.tokens [stmt.last_token - 1].line;
					var start_com_col = src_file.tokens [stmt.last_token - 1].col;
					start_com_col += len (src_file.tokens [stmt.last_token - 1].tok_str);
					var next_token = get_next_token (src_file.tokens, stmt.last_token - 1);
					var end_com_line = next_token.line;
					var end_com_col = next_token.col;
					var comment = get_comment (src_file, start_com_line, start_com_col, end_com_line, end_com_col);
					if (comment == '') {
						src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_GLOBAL_GOTO, 'break in loop must have comment on this line or previous line explaining purpose']));
					}
				}
			}
		}
		else if (stmt.stmt_type == Statement.FUNC_HDR_STMT) {
			var is_main = false;
			var func_name = '';
			for (var token of src_file.tokens.__getslice__ (stmt.first_token, stmt.last_token, 1)) {
				if (token.tok_type == Token.FUNC_ID_TOKEN) {
					var func_name = token.tok_str;
					if (func_name == 'main') {
						var is_main = true;
					}
				}
			}
			if (is_main && found_func) {
				src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_FUNC_ORDER, 'main() should be first function/method in file']));
			}
			var found_func = true;
			var start_com_line = src_file.tokens [prev_stmt.last_token - 1].line;
			var start_com_col = src_file.tokens [prev_stmt.last_token - 1].col;
			start_com_col += len (src_file.tokens [prev_stmt.last_token - 1].tok_str);
			var end_com_line = src_file.tokens [stmt.first_token].line;
			var end_com_col = src_file.tokens [stmt.first_token].col;
			var comment = get_comment (src_file, start_com_line, start_com_col, end_com_line, end_com_col);
			if (len (comment) == 0) {
				src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_FUNCTION_NO_COMMENT, ('Missing comment before function/method (' + func_name) + ')']));
			}
			else {
				var result = null;
				var prev_tok = get_prev_token (src_file.tokens, stmt.last_token - 1);
				if (prev_tok.tok_str == '(') {
					var result = com_without_param.match (comment);
				}
				else {
					var result = com_with_param.match (comment);
				}
				if (result === null) {
					src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_FUNCTION_COMMENT, ('Function/method comment is not correct format (' + func_name) + ')']));
				}
			}
		}
		if (__in__ (stmt.stmt_type, [Statement.FUNC_HDR_STMT, Statement.FOR_STMT, Statement.WHILE_STMT, Statement.DO_STMT, Statement.IF_STMT, Statement.IF_STMT, Statement.ELSE_IF_STMT, Statement.ELSE_STMT, Statement.SWITCH_STMT, Statement.CLASS_STMT])) {
			var next_tok = get_next_token (src_file.tokens, stmt.last_token - 1);
			if (next_tok.tok_str != '{') {
				src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_BRACES, 'Missing opening {']));
			}
			else if (next_tok.line == src_file.tokens [stmt.last_token - 1].line) {
				src_file.lines [start_line].issues.append (tuple ([StyleSummary.ERROR_BRACES, '{ must be on the following line']));
			}
		}
		var prev_stmt = stmt;
	}
};
export var get_cat_score = function (style_summ, cat_num) {
	var score = 10;
	var max = 10;
	if (__in__ (StyleSummary.ERROR_FILE_COMMENT, cat_num)) {
		if (len (style_summ.files) == 1) {
			if (style_summ.issues [StyleSummary.ERROR_FILE_NO_COMMENT] >= 1) {
				var score = 0;
			}
			else if (style_summ.issues [StyleSummary.ERROR_FILE_COMMENT] >= 1) {
				var score = 7;
			}
		}
		else if (style_summ.issues [StyleSummary.ERROR_FILE_NO_COMMENT] >= 2) {
			var score = 0;
		}
		else if (style_summ.issues [StyleSummary.ERROR_FILE_NO_COMMENT] == 1) {
			if (style_summ.issues [StyleSummary.ERROR_FILE_COMMENT] >= 2) {
				var score = 0;
			}
			else {
				var score = 4;
			}
		}
		else if (style_summ.issues [StyleSummary.ERROR_FILE_COMMENT] >= 2) {
			var score = 4;
		}
		else if (style_summ.issues [StyleSummary.ERROR_FILE_COMMENT] >= 1) {
			var score = 7;
		}
	}
	else if (__in__ (StyleSummary.ERROR_FUNCTION_COMMENT, cat_num)) {
		var total_functions = 0;
		for (var src_file of style_summ.files) {
			total_functions += src_file.num_functions;
		}
		if (total_functions == 1) {
			if (style_summ.issues [StyleSummary.ERROR_FUNCTION_NO_COMMENT] >= 1) {
				var score = 0;
			}
			else if (style_summ.issues [StyleSummary.ERROR_FUNCTION_COMMENT] >= 1) {
				var score = 7;
			}
		}
		else if (style_summ.issues [StyleSummary.ERROR_FUNCTION_NO_COMMENT] >= 2) {
			var score = 0;
		}
		else if (style_summ.issues [StyleSummary.ERROR_FUNCTION_NO_COMMENT] == 1) {
			if (style_summ.issues [StyleSummary.ERROR_FUNCTION_COMMENT] >= 2) {
				var score = 0;
			}
			else {
				var score = 4;
			}
		}
		else if (style_summ.issues [StyleSummary.ERROR_FUNCTION_COMMENT] >= 2) {
			var score = 4;
		}
		else if (style_summ.issues [StyleSummary.ERROR_FUNCTION_COMMENT] >= 1) {
			var score = 7;
		}
	}
	else if (__in__ (StyleSummary.ERROR_PACKAGE_INCLUDE, cat_num)) {
		var max = 5;
		var score = 5;
		if (style_summ.issues [StyleSummary.ERROR_PACKAGE_INCLUDE] > 0) {
			var score = 0;
		}
	}
	else if (__in__ (StyleSummary.ERROR_FUNC_ORDER, cat_num)) {
		var max = 5;
		var score = 5;
		if (style_summ.issues [StyleSummary.ERROR_FUNC_ORDER] > 0) {
			var score = 0;
		}
	}
	else if (__in__ (StyleSummary.ERROR_GLOBAL_GOTO, cat_num)) {
		if (style_summ.issues [StyleSummary.ERROR_GLOBAL_GOTO] > 1) {
			var score = 0;
		}
		else if (style_summ.issues [StyleSummary.ERROR_GLOBAL_GOTO] > 0) {
			var score = 5;
		}
	}
	else if (style_summ.issues [cat_num [0]] >= 3) {
		var score = 0;
	}
	else if (style_summ.issues [cat_num [0]] == 2) {
		var score = 4;
	}
	else if (style_summ.issues [cat_num [0]] == 1) {
		var score = 7;
	}
	return tuple ([score, max]);
};
export var print_category_results = function (style_summ, cat_num, cat_str) {
	var __left0__ = get_cat_score (style_summ, cat_num);
	var score = __left0__ [0];
	var max = __left0__ [1];
	style_summ.total += max;
	style_summ.score += score;
	print (cat_str, ' --> ', score, '/', max);
	for (var src_file of style_summ.files) {
		for (var stmt_ind = 0; stmt_ind < len (src_file.lines); stmt_ind++) {
			for (var issue of src_file.lines [stmt_ind].issues) {
				if (__in__ (issue [0], cat_num)) {
					print ('    ', src_file.filename, ' (', '{:3d}'.format (stmt_ind + 1), ') ', issue [1], __kwargtrans__ ({sep: ''}));
				}
			}
		}
	}
};
export var print_summary_results = function (style_summ) {
	for (var ind = 0; ind < StyleSummary.ERROR_OTHER + 1; ind++) {
		style_summ.issues [ind] = 0;
	}
	style_summ.total = 0;
	style_summ.score = 0;
	for (var src_file of style_summ.files) {
		for (var stmt of src_file.lines) {
			for (var issue of stmt.issues) {
				style_summ.issues [issue [0]]++;
			}
		}
	}
	for (var cat of StyleSummary.CATEGORIES) {
		print_category_results (style_summ, cat [0], cat [1]);
	}
	print ('------------------------------');
	print ('Style Score:', style_summ.score, '/', style_summ.total);
	print ();
	for (var src_file of style_summ.files) {
		print ('******************************');
		print (src_file.filename);
		print ('******************************');
		if (len (src_file.lines) == 0) {
			print ('MISSING FILE!!!');
		}
		else if (len (src_file.tokens) == 0) {
			print ('BLANK FILE!!!');
		}
		else {
			for (var stmt of src_file.lines) {
				for (var issue of stmt.issues) {
					print ('// STYLE CHECK:', issue [1]);
				}
				print (''.join (stmt.orig_line), __kwargtrans__ ({end: ''}));
			}
		}
	}
};
export var get_category_results = function (style_summ, cat_num, cat_str) {
	var cat_text = '';
	var __left0__ = get_cat_score (style_summ, cat_num);
	var score = __left0__ [0];
	var max = __left0__ [1];
	style_summ.total += max;
	style_summ.score += score;
	cat_text += ((((cat_str + ' --> ') + str (score)) + '/') + str (max)) + '\n';
	for (var src_file of style_summ.files) {
		for (var stmt_ind = 0; stmt_ind < len (src_file.lines); stmt_ind++) {
			for (var issue of src_file.lines [stmt_ind].issues) {
				if (__in__ (issue [0], cat_num)) {
					cat_text += ((((('    ' + src_file.filename) + ' (') + str (stmt_ind + 1)) + ') ') + issue [1]) + '\n';
				}
			}
		}
	}
	return cat_text;
};
export var get_summary_results = function (style_summ, replace_less, span_color) {
	if (typeof replace_less == 'undefined' || (replace_less != null && replace_less.hasOwnProperty ("__kwargtrans__"))) {;
		var replace_less = false;
	};
	if (typeof span_color == 'undefined' || (span_color != null && span_color.hasOwnProperty ("__kwargtrans__"))) {;
		var span_color = false;
	};
	var summ_text = '';
	for (var ind = 0; ind < StyleSummary.ERROR_OTHER + 1; ind++) {
		style_summ.issues [ind] = 0;
	}
	style_summ.total = 0;
	style_summ.score = 0;
	for (var src_file of style_summ.files) {
		for (var stmt of src_file.lines) {
			for (var issue of stmt.issues) {
				style_summ.issues [issue [0]]++;
			}
		}
	}
	for (var cat of StyleSummary.CATEGORIES) {
		summ_text += get_category_results (style_summ, cat [0], cat [1]);
	}
	var final_grade = (style_summ.score / style_summ.total) * 100;
	var summ_text = (((((('Style Score: ' + str (style_summ.score)) + '/') + str (style_summ.total)) + '\n') + '------------------------------\n') + summ_text) + '\n';
	for (var src_file of style_summ.files) {
		summ_text += '******************************\n';
		summ_text += src_file.filename + '\n';
		summ_text += '******************************\n';
		if (len (src_file.lines) == 0) {
			summ_text += 'MISSING FILE!!!\n';
		}
		else if (len (src_file.tokens) == 0) {
			summ_text += 'BLANK FILE!!!\n';
		}
		else {
			for (var stmt of src_file.lines) {
				for (var issue of stmt.issues) {
					if (span_color) {
						summ_text += '<span style="background-color: pink">';
					}
					summ_text += ('// STYLE CHECK: ' + issue [1]) + '\n';
					if (span_color) {
						summ_text += '</span>';
					}
				}
				if (replace_less) {
					summ_text += ''.join (stmt.orig_line).py_replace ('<', '&lt;');
				}
				else {
					summ_text += ''.join (stmt.orig_line);
				}
			}
		}
	}
	return summ_text;
};
export var get_final_grade = function (style_summ) {
	return (style_summ.score / style_summ.total) * 100;
};
export var process_one_file = function (src_file) {
	remove_comments_and_strings (src_file);
	tokenize_stmts (src_file);
	classify_tokens (src_file);
	check_indentation (src_file);
	check_capitalization (src_file);
	check_spacing (src_file);
	check_blank_lines (src_file);
	check_multiple_stmts (src_file);
	check_token_use (src_file);
	check_comments (src_file);
	check_other_stuff (src_file);
};

//# sourceMappingURL=sc_lib.map