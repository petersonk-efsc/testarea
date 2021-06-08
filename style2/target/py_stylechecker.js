'use strict';import{AssertionError,AttributeError,BaseException,DeprecationWarning,Exception,IndexError,IterableError,KeyError,NotImplementedError,RuntimeWarning,StopIteration,UserWarning,ValueError,Warning,__JsIterator__,__PyIterator__,__Terminal__,__add__,__and__,__call__,__class__,__envir__,__eq__,__floordiv__,__ge__,__get__,__getcm__,__getitem__,__getslice__,__getsm__,__gt__,__i__,__iadd__,__iand__,__idiv__,__ijsmod__,__ilshift__,__imatmul__,__imod__,__imul__,__in__,__init__,__ior__,__ipow__,
__irshift__,__isub__,__ixor__,__jsUsePyNext__,__jsmod__,__k__,__kwargtrans__,__le__,__lshift__,__lt__,__matmul__,__mergefields__,__mergekwargtrans__,__mod__,__mul__,__ne__,__neg__,__nest__,__or__,__pow__,__pragma__,__pyUseJsNext__,__rshift__,__setitem__,__setproperty__,__setslice__,__sort__,__specialattrib__,__sub__,__super__,__t__,__terminal__,__truediv__,__withblock__,__xor__,abs,all,any,assert,bool,bytearray,bytes,callable,chr,copy,deepcopy,delattr,dict,dir,divmod,enumerate,filter,float,getattr,
hasattr,input,int,isinstance,issubclass,len,list,map,max,min,object,ord,pow,print,property,py_TypeError,py_iter,py_metatype,py_next,py_reversed,py_typeof,range,repr,round,set,setattr,sorted,str,sum,tuple,zip}from"./org.transcrypt.__runtime__.js";import{get_final_grade}from"./py_sc_lib.js";import{get_summary_results}from"./py_sc_lib.js";import{process_one_file}from"./py_sc_lib.js";import{PyFile}from"./py_sc_lib.js";import{PyStyleCheckData}from"./py_sc_lib.js";var __name__="__main__";export var __author__=
"Karen Peterson";export var __date__="4/15/2021";export var read_upload_file=function(src_file,dom_file_obj){src_file.file_text=document.getElementById("dom_file_obj").value};export var do_it=function(event){var style_summ=StyleSummary();style_summ.check_files=[];for(var single_file of document.select("textarea.fileText")){var src_file=PyFile();var __left0__=document.getElementById(single_file.id+"Name").value;src_file.filename=__left0__;var single_file_name=__left0__;read_upload_file(src_file,single_file.id);
process_one_file(src_file);style_summ.check_files.append(src_file)}var output_str="<pre>"+get_summary_results(style_summ,true,true)+"</pre>";document.getElementById("results").innerHTML=output_str};

//# sourceMappingURL=py_stylechecker.map