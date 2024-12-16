from fastapi import APIRouter
from services import player_services
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class Player(BaseModel):
    id: Optional[int]
    name: str
    win: Optional[int]
    lose: Optional[int]
    best_score_id: Optional[int]

@router.get("/players")
def get():
    return player_services.get_players()

@router.post("/player")
def post(player: Player):
    return player_services.add_player()

@router.put("/player")
def put(player: Player):
    return player_services.update_player()

@router.delete("/player/{player_id}")
def delete(player_id: int):
    return player_services.delete_player(player_id)