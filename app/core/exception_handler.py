from fastapi.responses import JSONResponse


def business_exception_handler(request, exc):
    return JSONResponse(
        status_code==exc.code,
        content=
    )