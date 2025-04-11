from models import LevelData, Move
from typing import List


def play(level_data: LevelData) -> List[Move]:
    moves = []
    own_player = level_data.own_player
    players = level_data.players
    items = level_data.items
    enemies = level_data.enemies
    
    moves.append({"speak": "Hello Botomy!"})

    moves.append({
      "debug_info": {
          "message": "oh hai"
      }
    })
    return moves