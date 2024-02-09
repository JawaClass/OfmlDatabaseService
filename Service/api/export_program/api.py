from flask import Blueprint, jsonify, request
from Service.api.export_program.creator import Creator
from Service.api.export_program.util import CreateProgramApiRequest
from settings import Config

bp = Blueprint("export_program", __name__, url_prefix="/export_program")


@bp.route('/create', methods=["POST"])
def create_program():

    params = CreateProgramApiRequest(**request.json)
    print("create_program", params)
    creator = Creator(params=params)
    creator.run_export_pipeline()
    print("creator export path ::", creator.export_path)
    return jsonify({
        "export_path": str(creator.export_path)
    })
