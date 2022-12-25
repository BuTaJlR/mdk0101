from fastapi import APIRouter
from server.sql_base.models import Museum
from server.resolvers import museum

router = APIRouter(prefix='/Museum', tags=['Museum'])

@router.post('/create')
def create(_museum: Museum) -> int:
    new_id = museum.create(_museum)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{museum_id}')
def get(museum_id: int) -> Museum | None:
    return museum.get(museum_id)

@router.get('/')
def get_all() -> list[Museum] | None:
    return museum.get_all()

@router.get('/remove/{museum_id}')
def remove(museum_id: int) -> None:
    return museum.remove(museum_id)


@router.put("/update/{museum_id}")
def update(museum_id: int, new_data: Museum):
    return museum.update(museum_id=museum_id, new_data=new_data)

