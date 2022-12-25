from server.sql_base.models import Ticket
from server.sql_base.dbmanger import DbManager

dbmanager = DbManager(base_path='server/sql_base/museum.db')

def create(_ticket: Ticket) -> int:
    new_id = dbmanager.execute(
        query="insert into Ticket(excursionId, userId, price) values(?, ?, ?)",
        args=(_ticket.excursionId, _ticket.userId, _ticket.price)
    )
    return new_id

def get(ticket_id: int) -> Ticket | None:
    res = dbmanager.execute(
        query='select * from Ticket where id=(?)',
        args=(ticket_id,)
    )

    return None if not res else Ticket(
        id=res[0],
        excursionId=res[1],
        userId=res[2],
        price=res[3]
    )
def get_all() -> list[Ticket]:
    ticket_list = dbmanager.execute(query= "select * from Ticket",many=True)
    res = []

    if ticket_list:
        for ticket in ticket_list:
            res.append(Ticket(
                id=ticket[0],
                excursionId=ticket[1],
                userId=ticket[2],
                price=ticket[3]
            ))

    return res

def remove(ticket_id: int) -> None:
    return dbmanager.execute('delete from Ticket where id=(?)', args=(ticket_id,))

def update(ticket_id: int, new_data: Ticket) -> None:
    return dbmanager.execute(
        query='update Ticket set (excursionId, userId, price) = (?, ?, ?) where id=(?)',
        args=(new_data.excursionId, new_data.userId, new_data.price,ticket_id))

