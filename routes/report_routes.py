from fastapi import APIRouter,HTTPException
from database.member_db import MemberDB
from database.book_db import BOOKDB
import logging

logger = logging.getLogger(__name__)


router_reports = APIRouter()

book = BOOKDB()
members = MemberDB()

@router_reports.get("/summary")
def get_summary():
    total_book = book.count_total_books()
    is_available_True = book.count_available_books()
    is_available_False = book.count_borrowed_books()
    return f"total_book : {total_book}, is_available_True: {is_available_True},is_available_False :{is_available_False} "

@router_reports.get("/books-by-genre") 
def get_books_by_genre(genre:str):
    logger.info(f"Request to count books by genre: {genre}")
    valid_genres = ("Fiction", "Non-Fiction", "Science", "History", "Other")
    if genre not in valid_genres:
        logger.error("Invalid genre provided")
        raise HTTPException(status_code=400, detail="Invalid genre provided")    
    count = book.count_by_genre(genre)
    return {"genre": genre, "count": count}

@router_reports.get("/top-member")
def top_member():
    logger.info("Fetching top member report")
    top = members.get_top_member()
    if not top:
        logger.info({"message": "No data available"})
        return {"message": "No data available"}
    return top