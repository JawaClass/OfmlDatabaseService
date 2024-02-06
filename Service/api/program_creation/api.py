from flask import Blueprint, jsonify, request
from Service.api.program_creation.creator import Creator
from Service.api.program_creation.util import CreateProgramApiRequest
from settings import Config

bp = Blueprint("program_creation", __name__, url_prefix="/program_creation")


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
