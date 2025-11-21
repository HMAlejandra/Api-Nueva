#!/usr/bin/env python3
"""
Script para ejecutar la aplicación
"""
import uvicorn
from api.app.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "api.app.main:app",
        host=settings.host,
        port=settings.port,
        reload=True
    )

