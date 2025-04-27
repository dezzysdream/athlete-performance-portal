from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from schemas.graphql import schema

app = FastAPI()

# 🛡️ Add this CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all frontend origins (good for dev)
    allow_credentials=True,
    allow_methods=["*"],   # Allow all HTTP methods (OPTIONS, POST, GET, etc)
    allow_headers=["*"],   # Allow all headers
)

# GraphQL Setup
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def root():
    return {"message": "Welcome to Athlete Performance Portal API"}
