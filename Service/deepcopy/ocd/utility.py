from pydantic import BaseModel


class DeepcopyRequest(BaseModel):
    name: str
    owner_id: int
    is_public: bool
    article_input: str
    articlenumbers_and_programs: list[tuple[str, str]]


WEB_OCD_TABLES = f"""
    web_ocd_artbase           
    web_ocd_article           
    web_ocd_articletaxes      
    web_ocd_artlongtext       
    web_ocd_artshorttext      
    web_ocd_codescheme        
    web_ocd_identification    
    web_ocd_identification_csv
    web_ocd_packaging         
    web_ocd_price             
    web_ocd_pricetext         
    web_ocd_propclasstext     
    web_ocd_property          
    web_ocd_propertyclass     
    web_ocd_propertytext      
    web_ocd_propertyvalue     
    web_ocd_prophinttext      
    web_ocd_propvaluetext     
    web_ocd_relation          
    web_ocd_relationobj       
    web_ocd_rounding          
    web_ocd_set_csv           
    web_ocd_taxscheme         
    web_ocd_usermessage       
    web_ocd_usermessage_csv   
    web_ocd_version           
    web_optproperty_dat       
    web_optpropvalue_txt      
        """.split()


def make_delete_statement(web_program_name: str):
    return "\n".join([f"DELETE FROM  {table} WHERE web_program_name = \"{web_program_name}\"; " for table in WEB_OCD_TABLES])


def make_select_statement(web_program_name: str):
    return "\n".join([f"SELECT * FROM  {table} WHERE web_program_name = \"{web_program_name}\"; " for table in WEB_OCD_TABLES])


#
# body2 = {
#         "name": "test",
#         "owner_id": 1,
#         "is_public": True,
#         "article_input": "todo .....",
#         "articlenumbers_and_programs": [
#             ("TLTN16880A", "talos"),
#             ("TLESBF1440W1", "talos"),
#             ("TLESBF164050W1", "talos"),
#             ("TLESBF1640W", "talos"),
#             ("TLESBF1640W1", "talos"),
#             ("Q3HO1SE", "quick3"),
#             ("PNESBFI30W", "screens"),
#             ("S6SLV108750A", "s6"),
#             ("S6AP6120B2", "s6"),
#             ("S6AP6323F1", "s6"),
#             ("S6AP6600A", "s6"),
#             ("S6AP6600B2", "s6"),
#             ("S6AP6800A", "s6"),
#             ("WPAPTN", "workplace"),
#             ("WPAPPBEE", "workplace"),
#             ("WPAPPBEF", "workplace"),
#             ("WPAPPDB", "workplace"),
#             ("WPAPPFR", "workplace"),
#             ("WPAPPN", "workplace"),
#             ("WPAPPRA", "workplace"),
#             ("OTDBG1218", "activet"),
#             ("S8ETGEIV11003RB2", "s8"),
#             ("S8ETGEIV11004LA", "s8"),
#             ("S8ETGEIV11004LB2", "s8"),
#             ("S8GTV11KR6455A1", "s8"),
#             ("S8GTV11KR6456A", "s8"),
#             ("S8GTV11KR6456A1", "s8"),
#             ("S8SF04", "locker"),
#             ("S8SF08", "locker"),
#             ("S8SFM08", "locker"),
#             ("S8ZAKL20", "locker"),
#             ("S8ZAKL200", "locker"),
#             ("S8ZBAB", "locker"),
#         ]
#     }