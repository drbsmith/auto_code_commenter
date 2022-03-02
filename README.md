# auto_code_commenter

Scans through python code and scaffolds out the comment blocks used by Doxygen to jump start code documentation and catch missing comment areas.

## Getting Started

## Gotchas: Compatibility

__Multi-lines__: This code base relies on functional single lines of code, and does not play well with multi-line statements (with the '\\' joiner) or multi-statement lines (with ';'). In both cases the parser will create single-statement lines and remove the '\\' and ';' markers. This does not change the function of the code, but will alter the coding style, if the code base uses those patterns.

### Todo:

* auto populate "\__init__.py" files with appropriate @package entries and a list for each included file
* be able to update headers without full erase and replace (to keep anything between the title and the Classes/Functions lists)
* gen Function comment blocks, with @param and @return boilerplate lines
* calculate stats for functions and modules: how many lines (each func), how many other calls, dependencies (functions relied on)
* tease out inline comments to create description?
* tease out TODO comments and put in header of the file
* build library of patterns to describe what each line (or block) does.
* diagnostic tools: scan directory structure and assess missing documentation
* handle ## vs """ comment blocks?
* document global variables!
* scrape for decorators and document in header? or in function doc?