from game_model import *
from game_interface import *

def test_begin_game(capsys):
    begin_game()
    captured = capsys.readouterr()
    assert captured.out.strip() == 
    
    