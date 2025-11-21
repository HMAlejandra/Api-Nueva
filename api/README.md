# SoulTrip Backend API

API REST construida con FastAPI y Python 3.12 para el sistema de gestión de museo.

## Características

- **FastAPI**: Framework moderno y rápido para construir APIs
- **SQLAlchemy**: ORM para gestión de base de datos
- **PostgreSQL**: Base de datos relacional
- **Pydantic**: Validación de datos y serialización
- **Gemini AI**: Integración con Google Gemini para comentarios generados por IA

## Estructura del Proyecto

```
api/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Aplicación principal FastAPI
│   ├── config.py               # Configuración de la aplicación
│   ├── database.py             # Configuración de base de datos
│   ├── models/                 # Modelos SQLAlchemy
│   │   ├── artwork.py
│   │   └── painting.py
│   ├── schemas/                # Schemas Pydantic
│   │   ├── artwork.py
│   │   ├── painting.py
│   │   └── emotion.py
│   ├── repositories/           # Capa de acceso a datos
│   │   ├── artwork_repository.py
│   │   └── painting_repository.py
│   ├── services/               # Lógica de negocio
│   │   ├── artwork_service.py
│   │   ├── painting_service.py
│   │   ├── gemini_service.py
│   │   └── emotion_service.py
│   ├── routers/                # Endpoints FastAPI
│   │   ├── artworks.py
│   │   ├── paintings.py
│   │   ├── gemini.py
│   │   ├── emotions.py
│   │   ├── health.py
│   │   └── root.py
│   └── config/
│       └── data_loader.py      # Carga de datos iniciales
├── requirements.txt
├── .env.example
└── README.md
```

## Instalación

1. **Clonar el repositorio y navegar a la carpeta api:**
```bash
cd api
```

2. **Crear un entorno virtual:**
```bash
python3.12 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno:**
```bash
cp .env.example .env
# Editar .env con tus credenciales
```

## Configuración

El archivo `.env` debe contener:

```env
DATABASE_URL=postgresql://usuario:password@host:puerto/database
GEMINI_ENDPOINT=https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent
GEMINI_API_KEY=tu_api_key_aqui
HOST=0.0.0.0
PORT=8080
```

## Ejecución

### Desarrollo
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

### Producción
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## Endpoints

### Health Check
- `GET /health` - Verificar estado del servidor

### Root
- `GET /` - Mensaje de bienvenida

### Artworks
- `GET /api/artworks` - Obtener todas las obras
- `GET /api/artworks/{id}` - Obtener obra por ID
- `POST /api/artworks` - Crear nueva obra
- `DELETE /api/artworks/{id}` - Eliminar obra

### Paintings
- `GET /api/paintings` - Obtener todas las pinturas
- `GET /api/paintings/{id}` - Obtener pintura por ID
- `POST /api/paintings` - Crear nueva pintura
- `DELETE /api/paintings/{id}` - Eliminar pintura

### Gemini AI
- `GET /api/ia/comentario?estado={estado}&obra={obra}` - Generar comentario con IA

### Emotions
- `POST /api/emotions` - Generar comentario basado en emociones

## Documentación

Una vez que el servidor esté corriendo, puedes acceder a:
- **Swagger UI**: http://localhost:8080/docs
- **ReDoc**: http://localhost:8080/redoc

## Buenas Prácticas Implementadas

1. **Separación de responsabilidades**: Capas separadas (routers, services, repositories, models)
2. **Type hints**: Uso completo de type hints en Python
3. **Validación de datos**: Pydantic schemas para validación
4. **Manejo de errores**: HTTPException apropiadas
5. **Dependency Injection**: Uso de Depends() de FastAPI
6. **CORS configurado**: Middleware para permitir requests cross-origin
7. **Configuración centralizada**: Variables de entorno con pydantic-settings
8. **Código limpio**: Docstrings y comentarios descriptivos

## Tecnologías

- Python 3.12
- FastAPI 0.109.0
- SQLAlchemy 2.0.25
- PostgreSQL (psycopg2-binary)
- Pydantic 2.5.3
- httpx 0.26.0

## Licencia

Este proyecto es parte de SoulTrip.

