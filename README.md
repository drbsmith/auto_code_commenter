# auto_code_commenter

Scans through python code and scaffolds out the comment blocks used by Doxygen to jump start code documentation and catch missing comment areas.

## Getting Started

## Gotchas: Compatibility

__Multi-lines__: This code base relies on functional single lines of code, and does not play well with multi-line statements (with the '\\' joiner) or multi-statement lines (with ';'). In both cases the parser will create single-statement lines and remove the '\\' and ';' markers. This does not change the function of the code, but will alter the coding style, if the code base uses those patterns.
__Docstrings__: In Python, docstrings that have the triple quotes more than 2x on one line will cause unpredictable results. Also, if one docstring terminates and another is opened on the same line. It does not play well with mixing single- and double-quote docstrings in one module (this package uses double-quotes by default).

