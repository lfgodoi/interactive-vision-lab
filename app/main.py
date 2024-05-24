# Importing packages and modules
import uvicorn
from fastapi import FastAPI

# Setting app title and description
title = "Interactive Vision Lab"
description = "A full stack project that brings together image processing \
              and analysis techniques through an interactive platform."

# Creating the app
app = FastAPI(
    title=title,
    description=description
)

# Running the app
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)