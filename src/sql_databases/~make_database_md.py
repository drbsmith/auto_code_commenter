


# make the root, or package, md file for the database:

# TODO: make 'tables' into a md table with space for a brief description of each table (pref auto generated!)


template = """# [DATABASE]

MySQL version: 5.7

## Tables

[TABLES]

@package [SCHEMA]"""



def MakeRootMarkdown(database, schema, tables):
	"""! 
	@param database: (str) name of the database, will be H1 in document
	@param schema: (str) the package name, such as 'public'
	@param tables: (list of str) the name of each table, will become link to that table's doc
	"""

	file = template

	file = file.replace('[DATABASE]', database.title())
	file = file.replace('[SCHEMA]', schema)

	tables_str = ""

	tables.sort() # sort ascending

	for table in tables:
		tables_str += "* [{}](md_{}_tables_{}.html)\n".format(table.title(), database, table)

	file = file.replace('[TABLES]', tables_str)

	return file

def DataFrameToMD(dframe):
	md = "|"
	line = "|"

	for c in dframe.columns:
		md += "{}|".format(c)
		line += "---|"
	md += "\n" + line + "\n"

	for idx, row in dframe.iterrows():
		md += "|"
		for c in dframe.columns:
			md += "{}|".format(row[c])
		md += "\n"

	return md