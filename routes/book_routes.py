from fastapi import APIRouter,HTTPException
from database.book_db import BOOKDB
from database.member_db import MemberDB
import logging

router_book = APIRouter()

logger = logging.getLogger(__name__)


members = MemberDB()

book = BOOKDB()

@router_book.post("")
def creat_book(titel:str,author:str,genre:str,):
    logger.info("Sending a request")
    book.create_book(titel,author,genre)
    logger.info("The new book was created")
    return "Book created"

@router_book.get("")
def get_all():
    logger.info("Sending a request")
    all_book = book.get_all_books()
    logger.info("The request was accepted.")
    return all_book

@router_book.get("/{id}")
def get_book_id(id:int):
    logger.info("Sending a request")
    result = book.get_book_by_id(id)
    if not result:
        logger.error("Book not found")
        raise HTTPException(status_code=404, detail="Book not found")
    logger.info("Sending a request")
    return result


@router_book.put("/{id}")
def up_book(id, data:dict):
    logger.info("Sending a request")
    if not book.get_book_by_id(id):
        logger.error("Book not found")
        raise HTTPException(status_code=404, detail="Book not found")
    book.update_book(id,data)
    logger.info("The request sent is incorrect.")
    return "Book updated"

@router_book.put("/{id}/return/{member_id}")
def set_available_return(id:int , member_id:int):
    logger.info("Sending a request")
    book_data = book.get_book_by_id(id)
    if not book_data:
        logger.error("Book not found")
        raise HTTPException(status_code=404, detail="Book not found")
    if book_data['is_available']:
        logger.error("Book is already available")
        raise HTTPException(status_code=400, detail="Book is already available")
    book.set_available(id,"return", member_id)
    logger.info("The request sent is incorrect.") 
    return "Book returned"


    
@router_book.put("/{id}/borrow/{member_id}")
def increment_borrows_book(id:int,member_id:int):
    logger.info("Request sent")
    book_data = book.get_book_by_id(id)
    member_data = members.get_member_by_id(member_id)
    if not book_data:
        logger.error("book not found")
        raise HTTPException(status_code=404, detail="Book not found")
    if not member_data:
        logger.error("Member not found")
        raise HTTPException(status_code=404, detail="Member not found")
    if not book_data['is_available']:
        logger.error("Book is not available")
        raise HTTPException(status_code=400, detail="Book is not available")
    if not member_data['is_active']:
        logger.error("Member is not active")
        raise HTTPException(status_code=400, detail="Member is not active")
    if member_data['total_borrows'] >= 4:
        logger.error("Member has reached maximum borrows")
        raise HTTPException(status_code=400, detail="Member has reached maximum borrows")
    book.set_available(id, "borrow", member_id)
    members.increment_borrows(member_id)
    logger.info(f"Book {id} borrowed successfully")
    return f"Book {id} borrowed successfully"