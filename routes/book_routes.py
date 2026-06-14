from fastapi import APIRouter,HTTPException
from database.book_db import BOOKDB
from database.member_db import MemberDB
import logging

router_book = APIRouter()

logger = logging.basicConfig(filename='myapp.log', level=logging.INFO,format= "%(asctime)s %(levelname)s %(message)s" )

logger = logging.getLogger(__name__)


members = MemberDB()

book = BOOKDB()

@router_book.post("")
def creat_book(titel:str,author:str,genre:str,):
    logger.info("Sending a request")
    book.create_book(titel,author,genre)
    logger.info("The new book was created")

@router_book.get("")
def get_all():
    logger.info("Sending a request")
    all_book = book.get_all_books()
    logger.info("The request was accepted.")
    return all_book

@router_book.get("/{id}")
def get_book_id(id:int):
    logger.info("Sending a request")
    book_id = book.get_book_by_id(id)
    logger.info("Sending a request")
    return book_id


@router_book.put("/{id}")
def up_book(id, data:dict):
    logger.info("Sending a request")
    book.update_book(id,data)
    logger.info("The request sent is incorrect.")


@router_book.put("/{id}/return/{member_id}")
def set_available_return(id:int , member_id:int):
    logger.info("Sending a request")
    book.set_available(id, "return", member_id)
    logger.info("The request sent is incorrect.") 
    
@router_book.put("/{id}/borrow/{member_id}")
def increment_borrows_book(id):
    logger.info("Request sent")
    members.increment_borrows(id)
    logger.info("The number of books borrowed increased by one.")
