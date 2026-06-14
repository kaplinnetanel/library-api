from database.db_connection import create_tables
from fastapi import FastAPI
from routes import member_routes,book_routes,report_routes
import uvicorn
create_tables()

app = FastAPI()

app.include_router(book_routes.router_book,prefix="/books",tags=["books"])
app.include_router(member_routes.router_members,prefix="/members",tags=["members"])
app.include_router(report_routes.router_reports,prefix="/reports",tags=["reports"])


if "name" == "__main__":
    uvicorn.run("main:app",port=8000,host="127,0,0,1",reload=True)