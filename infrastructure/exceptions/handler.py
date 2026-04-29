from fastapi import Request
from fastapi.responses import JSONResponse
from application.errors.app_exception import AppException
from application.shared.wappers.response import ApiResponse

async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ApiResponse(
            message=exc.message,
            status=False,
            data=exc.data
        ).to_dict()
    )