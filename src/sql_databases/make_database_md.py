


# make the root, or package, md file for the database:

# TODO: make 'tables' into a md table with space for a brief description of each table (pref auto generated!)

# ideal column order: ordinal position, column name, column type, column key or comment, then the specifics (len, precision, scale,)
# in mysql column type wraps up data type and length/precision. Postgres does not have 'column_type' (at least Redshift)


root_template = """# [DATABASE] {#[DATABASE]}

MySQL version: [VERSION]

## Tables

[TABLES]

@package [SCHEMA]"""

table_template = """# [DATABASE]:[TABLE] {#[TABLE]}

# [TITLE] - Table Description

TODOC:

## Columns

[COLUMNS]

@package [DATABASE]/[SCHEMA]
"""

# column_type for postgres, data_type for mysql...
SIMPLE_COLUMN_SET = ['ordinal_position', 'column_name', 'data_type', 'is_nullable', 'column_default']


def MakeRootMarkdown(database, schema, tables, version='unknown'):
	"""! 
	@param database: (str) name of the database, will be H1 in document
	@param schema: (str) the package name, such as 'public'
	@param tables: (list of str) the name of each table, will become link to that table's doc
	"""

	file = root_template

	file = file.replace('[DATABASE]', database.title())
	file = file.replace('[SCHEMA]', schema)
	file = file.replace('[VERSION]', version)

	tables_str = ""

	tables.sort() # sort ascending

	for table in tables:
		tables_str += "* [{}]({}.html)\n".format(table.title(), table)

	file = file.replace('[TABLES]', tables_str)

	return file

def ReorderColumns(column_df):

	col = list(column_df.columns.values)

	# move any CHARACTER columns to the end
	move_col = [c for c in col if 'character' in c]
	col = [c for c in col if not c in move_col]
	col += move_col

	# move any NUMERIC columns to the end
	move_col = [c for c in col if 'numeric' in c]
	col = [c for c in col if not c in move_col]
	col += move_col

	# move any DATETIME columns to the end
	move_col = [c for c in col if 'datetime' in c]
	col = [c for c in col if not c in move_col]
	col += move_col

	# move any UDT columns to the end
	move_col = [c for c in col if 'udt' in c]
	col = [c for c in col if not c in move_col]
	col += move_col

	# strip out any TABLE named columns and move them to the end
	table_col = [c for c in col if 'table' in c]
	col = [c for c in col if not c in table_col]
	col += table_col

	# move any DTD columns to the end
	move_col = [c for c in col if 'dtd' in c]
	col = [c for c in col if not c in move_col]
	col += move_col

	# make ordinal_position first, but then remove the header name later when we build the table
	if "ordinal_position" in col: # unlikely it has both, but ... why not?
		col.remove("ordinal_position")
		col = ["ordinal_position"] + col

	return column_df[col]

def makeSimpleTable(columns, NOTES=None):
	"""!
	@param NOTES: a dictionary with a custom note entry for each row
	"""
	col = list(columns.columns.values)
	reduced_set = [c for c in col if c in SIMPLE_COLUMN_SET] # some might be missing, like column_default in materialized views 
	df = columns[reduced_set]

	# create a dict to insert the notes column
	if not NOTES is None:
		note = []
		for idx, row in df.iterrows():
			if row['column_name'] in NOTES:
				note.append(NOTES[row['column_name']])
			else: note.append('')
		print(note)
		if len(note) > 0:
			df['NOTES'] = note

	md = makeDetailedTable(df)

	return md

def makeDetailedTable(columns):
	import numpy as np

	col = list(columns.columns.values)
	# make the header first
	md = ""
	line2 = ""
	for c in col:
		if c.lower() != 'ordinal_position':
			md += "| {} ".format(c.replace('_',' ').title())   # replace _ with a space, Doxygen formats much better once broken into words.
		else:
			md += "| " # it'll be obvious it's the position, reduce the visual clutter by stripping this header

		line2 += "| ---- "
	md += "|\n"
	md += line2 + "|\n"

	# now make the body for each column
	for idx, row in columns.iterrows():
		for c in col:
			# TODO: if numeric but int = float (aka round number) print with no decimal places. pricision, length, and others get coerced to float by pandas
			if row[c] is None or row[c] == 'nan' or (not type(row[c]) is str and np.isnan(row[c])):
				md += "| "
			elif (type(row[c]) is int or type(row[c]) is float) and int(row[c]) == row[c]:
				md += "| {} ".format(int(row[c]))
			else:
				md += "| {} ".format(row[c])
		md += "|\n"

	return md

def MakeTableMarkdown(database, schema, table, column_df, NOTES=None):
	"""!
	@param columns: (DataFrame) colmns to convert to a MD table """
	import pandas as pd

	file = table_template
	file = file.replace('[DATABASE]', database)
	file = file.replace('[SCHEMA]', schema)
	file = file.replace('[TABLE]', table)
	title = table.replace('_', ' ').title()
	file = file.replace('[TITLE]', title)

	# drop any empty/nan columns
	columns = column_df.dropna(how='all', axis=1)
	columns = ReorderColumns(columns)

	if 'ordinal_position' in columns:
		columns = columns.sort_values(by=['ordinal_position'])

	md = makeSimpleTable(columns, NOTES=NOTES)
	md += '----\n## Detailed Structure\n'
	md += makeDetailedTable(columns)

	file = file.replace('[COLUMNS]', md)

	return file

