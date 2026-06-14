from fastapi import APIRouter,HTTPException
from database.member_db import MemberDB
from database.book_db import BOOKDB
import logging

logger = logging.basicConfig(filename='myapp.log', level=logging.INFO,format= "%(asctime)s %(levelname)s %(message)s" )

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
    if genre in ("Fiction","Non-Fiction","Science","History","Other"):
        logger.info("Sending a request")
        count = book.count_by_genre(genre) 
        logger.info("Sending a request")
        return count 
    else:
        raise HTTPException(404,"The request sent is incorrect.")

@router_reports.get("/books/{id}/borrow/{member_id}")
def get_book_id_borrow(id:int,member_id:int):
    count_active_borrows= book.count_active_borrows_by_member(member_id) 
    return count_active_borrows


@router_reports.get("/summary")
def active_members():
    logger.info("Request sent")
    members_acthve = members.count_active_members()
    logger.info("We got the number of users.")
    return members_acthve 

@router_reports.get("/top-member")
def top_member():
     logger.info("Request sent")
     top = members.get_top_member() 
     logger.info("We bring you who is at the top")
