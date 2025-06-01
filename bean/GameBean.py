import json
from typing import Dict

class GameBean:
    def __init__(self, name: str, genre: str, platform: str):
        self.name = name
        self.genre = genre
        self.platform = platform

    def to_dict(self) -> Dict[str, str]:
        return {
            'name': self.name,
            'genre': self.genre,
            'platform': self.platform
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'GameBean':
        return cls(name=data['name'], genre=data['genre'], platform=data['platform'])

    @classmethod
    def from_json(cls, json_str: str) -> 'GameBean':
        data = json.loads(json_str)
        return cls.from_dict(data)

# Example usage:
game = GameBean(name="Example Game", genre="Action", platform="PC")
json_str = game.to_json()
print(json_str)

new_game = GameBean.from_json(json_str)
print(new_game.name, new_game.genre, new_game.platform)