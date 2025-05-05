from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from schemas.graphql import schema

app = FastAPI()

# ✅ Add CORS Middleware (this allows your frontend to talk to the backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later you can change this to your Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Mount the GraphQL API at /graphql
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# Optional: Root route for health check or info
@app.get("/")
def root():
    return {"message": "Welcome to Athlete Performance Portal API"}
