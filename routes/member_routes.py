from fastapi import APIRouter,HTTPException
from database.member_db import MemberDB
import logging

logger = logging.getLogger(__name__)

router_members = APIRouter()

members = MemberDB()


@router_members.post("")
def postcreate_member(data:dict):
        logger.info("Request sent to create a new member")
        members.create_member(data)
        logger.info("The request was accepted and a new user was created.")
        return "Member created successfully"

@router_members.get("")
def get_members():
    logger.info("Request sent")
    all = members.get_all_members()
    logger.info("Request accepted")
    return f"all_members :{all}"

@router_members.get("/{id}")
def get_members_id(id:int):
    logger.info("Request sent")
    member = members.get_member_by_id(id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    logger.info("Request accepted")
    return f"member_by_id:{member}"

@router_members.put("/{id}")
def update_member_id(id,data:dict):
    logger.info("Request sent")
    if not members.get_member_by_id(id):
        raise HTTPException(status_code=404, detail="Member not found")
    members.update_member(id, data) 
    logger.info("The server updated the requested fields.")


@router_members.put("/{id}/activate")
def put_activate_member(id):
    logger.info("Request sent")
    if not members.get_member_by_id(id):
        raise HTTPException(status_code=404, detail="Member not found")
    members.activate_member(id)
    logger.info("Changed to the requested user agent")
    return "Member activated"

@router_members.put("/{id}/deactivate")
def put_activate_member(id):
    logger.info("Request sent")
    if not members.get_member_by_id(id):
        raise HTTPException(status_code=404, detail="Member not found")
    members.deactivate_member(id)
    logger.info("CThe change was caught and changed to free.")
    return "Member deactivated"