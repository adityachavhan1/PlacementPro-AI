import uvicorn

if __name__ == "__main__":
    print("Starting PlacementPro AI Backend on http://127.0.0.1:8000...")
    print("Interactive Swagger API Documentation: http://127.0.0.1:8000/docs")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
