from main import hello

def test_hello():
    assert hello() == "Hello, GitHub Actions!"
```
This **tests** your function. It imports `hello()` and checks if it returns the right thing. If it does → test passes. If not → test fails.

### File 3 — `requirements.txt` (your dependencies)
```
pytest