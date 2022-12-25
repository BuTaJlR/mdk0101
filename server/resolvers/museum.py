from server.sql_base.models import Museum
from server.sql_base.dbmanger import DbManager

dbmanager = DbManager(base_path='server/sql_base/museum.db')

def create(_museum: Museum) -> int:
    new_id = dbmanager.execute(
        query="insert into Museum(name) values(?)",
        args=(_museum.name,)
    )
    return new_id

def get(museum_id: int) -> Museum | None:
    res = dbmanager.execute(
        query='select * from Museum where id=(?)',
        args=(museum_id,)
    )

    return None if not res else Museum(
        id=res[0],
        name=res[1]
    )
def get_all() -> list[Museum]:
    Museum_list = dbmanager.execute(query= "select * from Museum",many=True)
    res = []

    if Museum_list:
        for museum in Museum_list:
            res.append(Museum(
                id=museum[0],
                name=museum[1]
            ))

    return res

def remove(museum_id: int) -> None:
    return dbmanager.execute('delete from Museum where id=(?)', args=(museum_id,))

def update(museum_id: int, new_data: Museum) -> None:
    return dbmanager.execute(
        query='update Museum set (name) = (?) where id=(?)',
        args=(new_data.name, museum_id))

