from fastapi import APIRouter
from server.sql_base.models import Ticket
from server.resolvers import ticket

router = APIRouter(prefix='/Ticket', tags=['Ticket'])

#ticket = Ticket | ticket_id = ticket_id | Ticket = Ticket

@router.post('/create')
def create(_ticket: Ticket) -> int:
    new_id = ticket.create(_ticket)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{ticket_id}')
def get(ticket_id: int) -> Ticket | None:
    return ticket.get(ticket_id)

@router.get('/')
def get_all() -> list[Ticket] | None:
    return ticket.get_all()

@router.get('/remove/{ticket_id}')
def remove(ticket_id: int) -> None:
    return ticket.remove(ticket_id)


@router.put("/update/{ticket_id}")
def update(ticket_id: int, new_data: Ticket):
    return ticket.update(ticket_id=ticket_id, new_data=new_data)

