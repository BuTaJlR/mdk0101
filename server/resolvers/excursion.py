from server.sql_base.models import Excursion
from server.sql_base.dbmanger import DbManager

dbmanager = DbManager(base_path='server/sql_base/museum.db')

def create(_excursion: Excursion) -> int:
    new_id = dbmanager.execute(
        query="insert into Excursion(presonalId, museumId) values(?, ?)",
        args=(_excursion.presonalId, _excursion.museumId)
    )
    return new_id

def get(excursion_id: int) -> Excursion | None:
    res = dbmanager.execute(
        query='select * from Excursion where id=(?)',
        args=(excursion_id,)
    )

    return None if not res else Excursion(
        id=res[0],
        presonalId=res[1],
        museumId=res[2]
    )
def get_all() -> list[Excursion]:
    Excursion_list = dbmanager.execute(query= "select * from Excursion",many=True)
    res = []

    if Excursion_list:
        for excursion in Excursion_list:
            res.append(Excursion(
                id=excursion[0],
                presonalId=excursion[1],
                museumId=excursion[2]
            ))

    return res

def remove(excursion_id: int) -> None:
    return dbmanager.execute('delete from Excursion where id=(?)', args=(excursion_id,))

def update(excursion_id: int, new_data: Excursion) -> None:
    return dbmanager.execute(
        query='update Excursion set (presonalId, museumId) = (?, ?) where id=(?)',
        args=(new_data.presonalId, new_data.museumId, excursion_id))

