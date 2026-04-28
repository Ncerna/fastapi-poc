# shared/middleware/response_middleware.py
import json
from fastapi import Request
from fastapi.responses import JSONResponse
from  application.shared.wappers.response   import ApiResponse

async def response_middleware(request: Request, call_next):
    response = await call_next(request)

    if isinstance(response, JSONResponse):
        try:
            body = json.loads(response.body)

            # evitar doble envoltura
            if isinstance(body, dict) and "status" in body:
                return response

            wrapped = ApiResponse(data=body)

            return JSONResponse(
                status_code=response.status_code,
                content=wrapped.model_dump()
            )
        except:
            return response

    return response