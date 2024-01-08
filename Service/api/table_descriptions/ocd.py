INP_DESCR = """
name	pdata

table	ocd_artbase	ocd_artbase.csv	mscsv
fields	4
field	1	article_nr	vstring		delim ; hidx link
field	2	prop_class	vstring		delim ;
field	3	property	vstring		delim ;
field	4	prop_value	vstring		delim ;

table	ocd_article	ocd_article.csv	mscsv
fields	11
field	1	article_nr	vstring		delim ; hidx
field	2	art_type	vstring		delim ;
field	3	manufacturer	vstring		delim ;
field	4	series	vstring		delim ;
field	5	short_textnr	vstring		delim ;
field	6	long_textnr	vstring		delim ;
field	7	rel_obj	uint32		delim ;
field	8	fast_supply	uint16		delim ;
field	9	discountable	uint8		delim ;
field	10	order_unit	vstring		delim ;
field	11	scheme_id	vstring		delim ;
index	btree	manufacturer series
index	btree	manufacturer

table	ocd_articletaxes	ocd_articletaxes.csv	mscsv
fields	4
field	1	article_nr	vstring		delim ; hidx link
field	2	tax_id	vstring		delim ;
field	3	date_from	vstring		delim ;
field	4	date_to	vstring		delim ;

table	ocd_artlongtext	ocd_artlongtext.csv	mscsv
fields	5
field	1	textnr	vstring		delim ; hidx link
field	2	language	vstring		delim ;
field	3	line_nr	uint8		delim ;
field	4	line_fmt	vstring		delim ;
field	5	text	vstring		delim ;

table	ocd_artshorttext	ocd_artshorttext.csv	mscsv
fields	5
field	1	textnr	vstring		delim ; hidx link
field	2	language	vstring		delim ;
field	3	line_nr	uint8		delim ;
field	4	line_fmt	vstring		delim ;
field	5	text	vstring		delim ;

table	ocd_codescheme	ocd_codescheme.csv	mscsv
fields	10
field	1	scheme_id	vstring		delim ; hidx link
field	2	scheme	vstring		delim ;
field	3	varcode_sep	vstring		delim ;
field	4	value_sep	vstring		delim ;
field	5	visibility	vstring		delim ;
field	6	invisible_char	vstring		delim ;
field	7	unselect_char	vstring		delim ;
field	8	trim	uint8		delim ;
field	9	mo_sep	vstring		delim ;
field	10	mo_bracket	vstring		delim ;

table	ocd_packaging	ocd_packaging.csv	mscsv
fields	13
field	1	article_nr	vstring		delim ; hidx link
field	2	var_cond	vstring		delim ;
field	3	width	vstring		delim ;
field	4	height	vstring		delim ;
field	5	depth	vstring		delim ;
field	6	measure_unit	vstring		delim ;
field	7	volume	vstring		delim ;
field	8	volume_unit	vstring		delim ;
field	9	tara_weight	vstring		delim ;
field	10	net_weight	vstring		delim ;
field	11	weight_unit	vstring		delim ;
field	12	items_per_unit	vstring		delim ;
field	13	pack_units	vstring		delim ;
index	btree	article_nr var_cond

table	ocd_price	ocd_price.csv	mscsv
fields	13
field	1	article_nr	vstring		delim ; hidx link
field	2	var_cond	vstring		delim ;
field	3	price_type	vstring		delim ;
field	4	price_level	vstring		delim ;
field	5	price_rule	vstring		delim ;
field	6	price_textnr	vstring		delim ;
field	7	price	float64		delim ;
field	8	is_fix	uint8		delim ;
field	9	currency	vstring		delim ;
field	10	date_from	vstring		delim ;
field	11	date_to	vstring		delim ;
field	12	scale_quantity	uint16		delim ;
field	13	rounding_id	vstring		delim ;
index	btree	article_nr var_cond price_type price_level

table	ocd_pricetext	ocd_pricetext.csv	mscsv
fields	5
field	1	textnr	vstring		delim ; hidx link
field	2	language	vstring		delim ;
field	3	line_nr	uint8		delim ;
field	4	line_fmt	vstring		delim ;
field	5	text	vstring		delim ;

table	ocd_propclasstext	ocd_propclasstext.csv	mscsv
fields	5
field	1	textnr	vstring		delim ; hidx link
field	2	language	vstring		delim ;
field	3	line_nr	uint8		delim ;
field	4	line_fmt	vstring		delim ;
field	5	text	vstring		delim ;

table	ocd_property	ocd_property.csv	mscsv
fields	15
field	1	prop_class	vstring		delim ; hidx link
field	2	property	vstring		delim ;
field	3	pos_prop	uint16		delim ;
field	4	prop_textnr	vstring		delim ;
field	5	rel_obj	uint32		delim ;
field	6	prop_type	vstring		delim ;
field	7	digits	uint16		delim ;
field	8	dec_digits	uint8		delim ;
field	9	need_input	uint8		delim ;
field	10	add_values	uint8		delim ;
field	11	restrictable	uint8		delim ;
field	12	multi_option	uint8		delim ;
field	13	scope	vstring		delim ;
field	14	txt_control	vstring		delim ;
field	15	hint_text_id	vstring		delim ;
index	btree	prop_class property

table	ocd_propertyclass	ocd_propertyclass.csv	mscsv
fields	5
field	1	article_nr	vstring		delim ; hidx link
field	2	pos_class	uint16		delim ;
field	3	prop_class	vstring		delim ;
field	4	textnr	vstring		delim ;
field	5	rel_obj	uint32		delim ;

table	ocd_propertytext	ocd_propertytext.csv	mscsv
fields	5
field	1	textnr	vstring		delim ; hidx link
field	2	language	vstring		delim ;
field	3	line_nr	uint8		delim ;
field	4	line_fmt	vstring		delim ;
field	5	text	vstring		delim ;

table	ocd_propertyvalue	ocd_propertyvalue.csv	mscsv
fields	12
field	1	prop_class	vstring		delim ;
field	2	property	vstring		delim ;
field	3	pos_pval	uint16		delim ;
field	4	pval_textnr	vstring		delim ;
field	5	rel_obj	uint32		delim ;
field	6	is_default	uint8		delim ;
field	7	suppress_txt	uint8		delim ;
field	8	op_from	vstring		delim ;
field	9	value_from	vstring		delim ;
field	10	op_to	vstring		delim ;
field	11	value_to	vstring		delim ;
field	12	raster	vstring		delim ;
index	btree	prop_class property
index	btree	prop_class property value_from

table	ocd_prophinttext	ocd_prophinttext.csv	mscsv
fields	5
field	1	textnr	vstring		delim ; hidx link
field	2	language	vstring		delim ;
field	3	line_nr	uint8		delim ;
field	4	line_fmt	vstring		delim ;
field	5	text	vstring		delim ;

table	ocd_propvaluetext	ocd_propvaluetext.csv	mscsv
fields	5
field	1	textnr	vstring		delim ; hidx link
field	2	language	vstring		delim ;
field	3	line_nr	uint8		delim ;
field	4	line_fmt	vstring		delim ;
field	5	text	vstring		delim ;

table	ocd_relation	ocd_relation.csv	mscsv
fields	3
field	1	rel_name	vstring		delim ; hidx link
field	2	rel_blocknr	uint16		delim ;
field	3	rel_block	vstring		delim ;

table	ocd_relationobj	ocd_relationobj.csv	mscsv
fields	5
field	1	rel_obj	uint32		delim ;
field	2	position	uint16		delim ;
field	3	rel_name	vstring		delim ;
field	4	rel_type	vstring		delim ;
field	5	rel_domain	vstring		delim ;
index	btree	rel_obj

table	ocd_rounding	ocd_rounding.csv	mscsv
fields	8
field	1	id	vstring		delim ; hidx link
field	2	nr	uint16		delim ;
field	3	min	vstring		delim ;
field	4	max	vstring		delim ;
field	5	type	vstring		delim ;
field	6	precision	float64		delim ;
field	7	add_before	float64		delim ;
field	8	add_after	float64		delim ;

table	ocd_taxscheme	ocd_taxscheme.csv	mscsv
fields	6
field	1	tax_id	vstring		delim ;
field	2	country	vstring		delim ;
field	3	region	vstring		delim ;
field	4	number	uint16		delim ;
field	5	tax_type	vstring		delim ;
field	6	tax_category	vstring		delim ;
index	btree	tax_id country
index	btree	tax_id country region

table	ocd_version	ocd_version.csv	mscsv
fields	10
field	1	format_version	vstring		delim ;
field	2	rel_coding	vstring		delim ;
field	3	data_version	vstring		delim ;
field	4	date_from	vstring		delim ;
field	5	date_to	vstring		delim ;
field	6	region	vstring		delim ;
field	7	varcond_var	vstring		delim ;
field	8	placeholder_on	uint8		delim ;
field	9	tables	vstring		delim ;
field	10	comment	vstring		delim ;

table   optproperty_dat optproperty_dat.csv    mscsv
fields  3
field   1       prop_class      string  9999
field   2       property        string  9999
field   3       prop_textnr     string  9999
index	hash	prop_class

table    optpropvalue_txt    optpropvalue_txt.csv    mscsv
fields   5
field    1    textnr        string    9999
field    2    language      string    9999
field    3    line_nr       uint8
field    4    line_fmt      vstring
field    5    text          string    9999
index    hash    textnr
"""