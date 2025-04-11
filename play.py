from models import LevelData, Move
from typing import List


def play(level_data: LevelData) -> List[Move]:
  moves = []
  moves.append({"speak": "Hello Botomy!"})

  moves.append({
      "debug_info": {
          "message": "oh hai"
      }
  })
  return moves