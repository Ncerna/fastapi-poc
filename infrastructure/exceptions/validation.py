from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from application.shared.wappers.response import ApiResponse

async def validation_exception_handler(request: Request, exc: RequestValidationError):

    errors = []

    for err in exc.errors():
        field = ".".join(str(x) for x in err["loc"][1:])  # elimina "body"
        errors.append({
            "field": field,
            "message": err["msg"]
        })

    return JSONResponse(
        status_code=422,
        content=ApiResponse(
            message="Validation error",
            status=False,
            data=errors
        ).to_dict()
    )