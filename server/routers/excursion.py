from fastapi import APIRouter
from server.sql_base.models import Excursion
from server.resolvers import excursion

router = APIRouter(prefix='/Excursion', tags=['Excursion'])

#excursion = Excursion | excursion_id = excursion_id | Excursion = Excursion

@router.post('/create')
def create(_Excursion: Excursion) -> int:
    new_id = excursion.create(_Excursion)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{excursion_id}')
def get(excursion_id: int) -> Excursion | None:
    return excursion.get(excursion_id)

@router.get('/')
def get_all() -> list[Excursion] | None:
    return excursion.get_all()

@router.get('/remove/{excursion_id}')
def remove(excursion_id: int) -> None:
    return excursion.remove(excursion_id)


@router.put("/update/{excursion_id}")
def update(excursion_id: int, new_data: Excursion):
    return excursion.update(excursion_id=excursion_id, new_data=new_data)

