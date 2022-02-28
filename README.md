# auto_code_commenter

Scans through python code and scaffolds out the comment blocks used by Doxygen to jump start code documentation and catch missing comment areas.

Todo:

* auto populate "\__init__.py" files with appropriate @package entries and a list for each included file
* be able to update headers without full erase and replace (to keep anything between the title and the Classes/Functions lists)
* gen Function comment blocks, with @param and @return boilerplate lines