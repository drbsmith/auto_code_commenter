# TODO Notes

## 2022-03-07

* Tweaks to CodeLine/Block parsing. Handle decorators, incorrect indentation if there is a non-functional ';' in the line. Extra \n after codeblocks when printing (casting to str)
	- docstring start/stop inside of a literal break indentation. They aren't actually starting/closing a docstring but the parser thinks they are...
* Refactor header_generator to use Line/Block parsing
* Refactor directory_check ^
* Refactor function_documentor, function_profiler ^ -- also use config.py for TODO_DOC tags
