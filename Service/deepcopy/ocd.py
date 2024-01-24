from flask import Blueprint

bp = Blueprint("deepcopy", __name__, url_prefix="/deepcopy")

# params: program_name: str, articles: list[(article_nr, program)]
# copy ocd from

