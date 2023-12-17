from fastapi import HTTPException
from pydantic import BaseModel
import json
import yaml
from fastapi.responses import StreamingResponse
from . import router


class ConvertRequest(BaseModel):
    swagger_json: str


def convert_json_to_yaml(json_data: str) -> str:
    try:
        data = json.loads(json_data)

        yaml_data = yaml.dump(data, default_flow_style=False)

        return yaml_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error converting JSON to YAML: {str(e)}")


@router.get("/", response_class=StreamingResponse)
async def convert_and_download(request: ConvertRequest):
    try:
        yaml_data = convert_json_to_yaml(request.swagger_json)
        headers = {
            "Content-Disposition": "attachment; filename=schema.yaml",
            "Content-Type": "application/x-yaml",
        }
        yaml_bytes = yaml_data.encode("utf-8")
        return StreamingResponse(iter([yaml_bytes]), headers=headers)

    except HTTPException as e:
        raise e
