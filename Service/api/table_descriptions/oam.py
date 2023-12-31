INP_DESCR = """
name	oam

table	oam_article2odbparams	oam_article2odbparams.csv	csv
fields	4
field	1	article	vstring		trim hidx link
field	2	vc_type	vstring		trim
field	3	varcode	vstring		trim
field	4	params	vstring		trim

table	oam_article2ofml	oam_article2ofml.csv	csv
fields	4
field	1	article	vstring		delim ; trim hidx
field	2	ofml_type	vstring		delim ; trim hidx link
field	3	odb_name	vstring		delim ; trim hidx link
field	4	params	vstring		delim ; trim hidx

table	oam_property2mat	oam_property2mat.csv	csv
fields	5
field	1	article	vstring		trim
field	2	property	vstring		trim
field	3	prop_value	vstring		trim
field	4	mat_layer	vstring		trim
field	5	material	vstring		trim
index	btree	article
"""