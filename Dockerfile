
CMD ["bash", "-c", "uvicorn taskman.main:app --host 0.0.0.0 --port ${PORT}"]