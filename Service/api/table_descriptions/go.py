INP_DESCR = """
# GO III (MT) Input Description, Version 1.17
# Copyright (C) 2002-2013 EasternGraphics.

name    go_tables

table   go_types	go_types.csv		csv
fields  6
field   1  id		vstring		delim ; trim hidx link
field   2  name		vstring		delim ; trim hidx link
field   3  format	vstring		delim ; trim
field   4  default	vstring		delim ; trim
field   5  mode		uint16          trim
field   6  filter	vstring		delim ; trim
index btree id name

table   go_articles	go_articles.csv		csv
fields  6
field   1  id		vstring		delim ; trim hidx link
field   2  manufacturer	vstring		delim ; trim
field   3  program	vstring		delim ; trim
field   4  article_nr	vstring		delim ; trim hidx link
field   5  prm_key	vstring		delim ; trim hidx link
field   6  chprm_key	vstring		delim ; trim

table   go_properties	go_properties.csv	csv
fields  6
field   1  id		vstring		delim ; trim hidx link
field   2  key		vstring		delim ; trim hidx link
field   3  name		vstring		delim ; trim hidx link
field   4  value	vstring		delim ; trim
field   5  variant_code	vstring		delim ; trim
field   6  variant_value	vstring	delim ; trim
index btree name value
index btree id name
index btree id name value

table	go_setup	go_setup.csv		csv
fields	3
field	1 id		vstring		delim ;	trim hidx link
field	2 key		vstring		delim ; trim 
field	3 value		vstring		delim ; trim 
"""