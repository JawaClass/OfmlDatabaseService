INP_DESCR = """
name	odb

table	attpt	attpt.csv	variable_width
fields	10
field	1	odb_name	vstring		delim ; trim hidx link
field	2	name	string	255	delim ; trim
field	3	select	vstring		delim ; trim
field	4	text_idx	uint32		delim ; trim
field	5	x_pos	string	255	delim ; trim
field	6	y_pos	string	255	delim ; trim
field	7	z_pos	string	255	delim ; trim
field	8	direction	string	255	delim ; trim
field	9	rotation	string	255	delim ; trim
field	10	mode	string	255	delim ; trim

table	funcs	funcs.csv	csv
fields	2
field	1	name	string	255	trim  hidx
field	2	body	vstring		trim

table	layer	layer.csv	variable_width
fields	2
field	1	layer_name	vstring		delim ; trim hidx
field	2	attributes	vstring		delim ; trim

table	odb2d	odb2d.csv	csv
fields	10
field	1	odb_name	string	43	trim hidx
field	2	level	uint16		
field	3	visible	string	255	trim
field	4	x_offs	string	255	trim
field	5	y_offs	string	255	trim
field	6	rot	string	255	trim
field	7	x_scale	string	255	trim
field	8	y_scale	string	255	trim
field	9	ctor	vstring		trim
field	10	attrib	vstring		trim

table	odb3d	odb3d.csv	csv
fields	13
field	1	odb_name	string	255	trim  hidx
field	2	obj_name	string	255	trim
field	3	visible	string	255	trim
field	4	x_offs	string	255	trim
field	5	y_offs	string	255	trim
field	6	z_offs	string	255	trim
field	7	x_rot	string	255	trim
field	8	y_rot	string	255	trim
field	9	z_rot	string	255	trim
field	10	ctor	vstring		trim
field	11	mat	vstring		trim
field	12	attrib	vstring		trim
field	13	link	string	255	trim

table	oppattpt	oppattpt.csv	variable_width
fields	5
field	1	odb_name	vstring		delim ; trim hidx link
field	2	select	vstring		delim ; trim
field	3	opposite	string	255	delim ; trim
field	4	direction	string	255	delim ; trim
field	5	att_points	vstring		delim ; trim

table	stdattpt	stdattpt.csv	csv
fields	4
field	1	odb_name	string	255	trim hidx
field	2	has_stdattpts	uint8		trim
field	3	prep_stdattpts	uint8		trim
field	4	stdattpts	vstring		trim
"""