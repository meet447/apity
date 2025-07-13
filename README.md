# Apity - Unified API Gateway

A FastAPI-based unified API gateway that provides consistent interfaces to multiple external services including weather data, web search, and IP geolocation.

## Project Overview

Apity is designed as a flexible API aggregator that:
- Provides standardized endpoints for common services
- Supports multiple providers for each service type
- Automatically selects providers based on availability/configuration
- Normalizes responses across different providers
- Includes plugin system for response post-processing

## Project Structure

```
apity/
├── adapters/           # Provider-specific implementations
│   ├── ip/            # IP geolocation providers
│   │   ├── ipapi.py
│   │   └── ipinfo.py
│   ├── search/        # Search providers
│   │   ├── duckduckgo.py
│   │   └── google.py
│   └── weather/       # Weather providers
│       ├── openweather.py
│       └── weatherapi.py
├── core/              # Core framework components
├── models/            # Pydantic data models
│   ├── ip.py
│   ├── search.py
│   └── weather.py
├── plugins/           # Response post-processing
├── routes/            # API endpoint definitions
│   ├── ip.py
│   ├── search.py
│   └── weather.py
├── services/          # Business logic services
│   ├── cache.py
│   ├── llm_normalizer.py
│   ├── selector.py
│   └── utils.py
├── tests/             # Test suite
├── config.py          # Configuration management
├── main.py            # FastAPI application entry point
└── requirements.txt   # Python dependencies
```

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd apity
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   Create a `.env` file in the project root with your API keys:
   ```
   WEATHERAPI_KEY=your_weatherapi_key
   OPENWEATHER_KEY=your_openweather_key
   OPENROUTER_KEY=your_openrouter_key
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

## Available APIs

### 1. IP Geolocation API
**Endpoint:** `GET /ip-geolocation`

**Parameters:**
- `ip` (required): IP address to lookup

**Example:**
```
GET /ip-geolocation?ip=8.8.8.8
```

**Supported Providers:**
- IPApi
- IPInfo

### 2. Search API
**Endpoint:** `GET /search`

**Parameters:**
- `q` (required): Search query string

**Example:**
```
GET /search?q=python programming
```

**Supported Providers:**
- DuckDuckGo
- Google Search

### 3. Weather API
**Endpoint:** `GET /weather`

**Parameters:**
- `city` (required): City name for weather lookup

**Example:**
```
GET /weather?city=London
```

**Supported Providers:**
- OpenWeatherMap
- WeatherAPI

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Requests**: HTTP library for API calls
- **python-dotenv**: Environment variable management
- **curl_cffi**: HTTP client with advanced features
- **ddgs**: DuckDuckGo search integration
- **googlesearch-python**: Google search integration

## Features

- **Provider Selection**: Automatic selection of available providers
- **Response Normalization**: Consistent response format across providers
- **Plugin System**: Extensible post-processing capabilities
- **Environment-based Configuration**: Secure API key management
- **Error Handling**: Comprehensive error handling with HTTP status codes
- **Type Safety**: Pydantic models for request/response validation

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

Run the test suite:
```bash
python -m pytest tests/
```

## Architecture

The project follows a modular architecture:

1. **Routes**: Define API endpoints and handle HTTP requests
2. **Services**: Contain business logic and provider selection
3. **Adapters**: Implement provider-specific API integrations
4. **Models**: Define data structures and validation rules
5. **Plugins**: Handle response post-processing and enhancement

## Contributing

1. Follow the existing code structure
2. Add tests for new features
3. Update documentation when adding new APIs
4. Ensure environment variables are properly documented

