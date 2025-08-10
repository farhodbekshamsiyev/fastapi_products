from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers import catalog, product


def create_app() -> FastAPI:
    """Create a FastAPI application."""

    app = FastAPI(
        title="Shop Inventory FastAPI Application",
        description="This is a sample Shop Inventory FastAPI application with CORS enabled.",
        version="1.0.0",
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Set all CORS enabled origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(catalog.router)
    app.include_router(product.router)

    return app


myapp = create_app()
