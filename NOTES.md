# TODO Notes

## 2022-03-15

* build a graph structure for a package, one file for each module, that describes how classes/functions import or call each other
* what is preferred documentation style for decorators? Does doxygen scrape those automatically? How does it show inheritance for Python?
	* scrape for decorators and document in header? or in function doc?
* add param tag to config. '@param xxx:' for doxygen, ':param xxx:' for sphinx.

## 2022-03-10

* be able to update headers without full erase and replace (to keep anything between the title and the Classes/Functions lists)
* tease out inline comments to create description?
* tease out TODO comments and put in header of the file? but they wouldn't update...maybe not really a documentation job.
* build library of patterns to describe what each line (or block) does.
* handle ## vs """ comment blocks?
* create a subdirectory for each module, keep what each module calls to be able to describe who calls each function

## 2022-03-08
* init_file_creator.py - if retaining text from previous file, drop Package: line and [TODO-DOC] lines.



# Done

* Tweaks to CodeLine/Block parsing. Handle decorators, incorrect indentation if there is a non-functional ';' in the line. Extra \n after codeblocks when printing (casting to str)
	- docstring start/stop inside of a literal break indentation. They aren't actually starting/closing a docstring but the parser thinks they are...
* migrate header_generator to use config.py
* Classes: auto doc 'self' variables-- decided to ignore them, they are obvious to any python reader
* calculate stats for functions and modules: how many lines (each func), how many other calls, dependencies (functions relied on)
* document global variables!
* Refactor header_generator to use Line/Block parsing
* CodeBlock.py: indent is being made part of the set_docstrings block. Why??
		This is happening when the previous block is more than one indentation level deeper when it ends. The next code then becomes part of the preceding block, rather than a new block.
* Refactor directory_check ^
* Refactor function_documentor, function_profiler ^ -- also use config.py for TODO_DOC tags
