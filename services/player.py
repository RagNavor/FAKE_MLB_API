from schemas.schemas_player import UpdatePlayer
from models.player import Player
from datetime import datetime


class PlayerService():
    def __init__(self, db) -> None:
        self.db = db
    def get_all_players(self):
        result = self.db.query(Player).all()
        return result
    
    def get_players_by_team(self, id:int):
        result = self.db.query(Player).filter(Player.team_id == id).all()
        print(result)
        return result
    
    def get_players_starting_pitchers(self):
        result = self.db.query(Player).filter(Player.pos == 'SP').all()
        print(result)
        return result
    
    def get_players_relief_pitchers(self):
        result = self.db.query(Player).filter(Player.pos == 'RP').all()
        print(result)
        return result
    
    def get_players_catchers(self):
        result = self.db.query(Player).filter(Player.pos == 'C').all()
        print(result)
        return result
    
    def get_players_shortstops(self):
        result = self.db.query(Player).filter(Player.pos == 'SS').all()
        print(result)
        return result
    
    def get_players_first_basemen(self):
        result = self.db.query(Player).filter(Player.pos == '1B').all()
        print(result)
        return result
    
    def get_players_second_basemen(self):
        result = self.db.query(Player).filter(Player.pos == '2B').all()
        print(result)
        return result
    
    def get_players_third_basemen(self):
        result = self.db.query(Player).filter(Player.pos == '3B').all()
        print(result)
        return result
    
    def get_players_left_fielders(self):
        result = self.db.query(Player).filter(Player.pos == 'LF').all()
        print(result)
        return result
    
    def get_players_right_fielders(self):
        result = self.db.query(Player).filter(Player.pos == 'RF').all()
        print(result)
        return result
    
    def get_players_center_fielders(self):
        result = self.db.query(Player).filter(Player.pos == 'CF').all()
        print(result)
        return result
    
    def get_players_designated_hitter(self):
        result = self.db.query(Player).filter(Player.pos == 'DH').all()
        print(result)
        return result
    
    
    def get_players_bat_right(self):
        result = self.db.query(Player).filter(Player.bat == 'R').all()
        print(result)
        return result
    
    
    def get_players_bat_left(self):
        result = self.db.query(Player).filter(Player.bat == 'L').all()
        print(result)
        return result
    
    
    def get_players_throw_right(self):
        result = self.db.query(Player).filter(Player.thw == 'R').all()
        print(result)
        return result
    
    
    def get_players_throw_left(self):
        result = self.db.query(Player).filter(Player.pos == 'L').all()
        print(result)
        return result
    