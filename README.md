# Calculator App 🧮

A simple and fast REST API calculator built with FastAPI.

## Features

- ➕ **Addition** - Add two numbers
- ➖ **Subtraction** - Subtract two numbers
- ✖️ **Multiplication** - Multiply two numbers
- ➗ **Division** - Divide two numbers

## Requirements

- Python 3.12+
- FastAPI

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/calculator-app.git
   cd calculator-app
   ```

2. Install dependencies:
   ```bash
   pip install fastapi[standard]
   ```

## Usage

### Start the server

```bash
fastapi dev app/main.py
```

The API will be available at `http://127.0.0.1:8000`

### API Endpoint

#### `GET /calc`

Perform arithmetic operations on two numbers.

**Query Parameters:**

| Parameter | Type   | Required | Default | Description                              |
| --------- | ------ | -------- | ------- | ---------------------------------------- |
| `a`       | float  | Yes      | -       | First number                             |
| `b`       | float  | Yes      | -       | Second number                            |
| `op`      | string | No       | `add`   | Operation: `add`, `sub`, `mul`, or `div` |

**Example Requests:**

```bash
# Addition (default)
curl "http://127.0.0.1:8000/calc?a=10&b=5"

# Subtraction
curl "http://127.0.0.1:8000/calc?a=10&b=5&op=sub"

# Multiplication
curl "http://127.0.0.1:8000/calc?a=10&b=5&op=mul"

# Division
curl "http://127.0.0.1:8000/calc?a=10&b=5&op=div"
```

**Example Response:**

```json
{
  "a": 10,
  "b": 5,
  "opreations": "add",
  "result": 15
}
```

## API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## License

MIT License
