from gridenc import gridenclib as glib

test_grid = glib.init_grid(10,1234)
test_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890"
def test_grid_init():
    assert glib.init_grid(5,1234) == [
        ['\x0c', '%', 'o', 'a', 'm'], ['_', 'f', '7', '\t', 'n'],
        ['r', 'Z', 'K', 'd', 'g'],
        ['e', '$', '\x0b', ' ', '['],
        ['\n', '?', 'C', 'u', 'I'],
        ['y', 'c', '1', '~', 'U'],
        ['s', '}', 't', 'z', '\r'],
        ['l', '&', '`', '(', 'k'],
        [':', 'N', '"', '6', 'R'],
        ['L', 'H', '\\', 'E', '*'],
        ['/', '0', 'h', ';', 'q'],
        ['b', 'Y', 'F', '>', '+'],
        ['J', 'v', 'x', '2', 'P'],
        ['A', 'W', 'Q', 'j', '8'],
        ['X', '|', 'B', '.', 'G'],
        ['3', '!', '<', 'p', '='],
        ['#', 'w', 'T', ',', 'S'],
        ['V', '9', 'M', ']', 'i'],
        ['5', '^', '@', ')', "'"],
        ['4', '{', 'O', 'D', '-']]
    assert glib.init_grid(10,2008) == [
    ['s', '=', 'Y', 'o', 'g', '#', '"', 'Z', 'w', 'U'],
    [':', 'H', 'G', '}', '%', '3', '1', 'z', 'P', 'x'],
    ['>', 'A', ' ', '8', '7', 'D', '?', 'S', '[', 'T'],
    ['i', 'V', 'c', '!', ']', 'b', 'y', 'K', '~', 'k'],
    ['W', ',', '{', 'm', 'e', '(', 'Q', ';', '\x0c', 'J'],
    ['d', '6', 'r', 'q', 'X', '+', 'h', '<', 'l', 'p'],
    ['N', "'", 'a', '*', 'f', '.', '9', 'u', '`', 'R'],
    ['E', '/', '_', '\x0b', '\n', 'I', 'n', '$', 'C', 'j'],
    ['\\', 'B', '2', 't', 'F', 'L', '4', 'M', '|', '-'],
    ['^', 'v', '@', '&', '0', '5', '\t', 'O', '\r', ')']]
def test_enc():
    
    assert glib.grid_enc(test_str , test_grid) == "6 5 7 2 2 2 9 8 4 8 5 7 7 4 4 6 2 4 6 0 1 2 4 5 8 7 4 1 9 7 6 4 6 7 4 4 8 4 8 2 2 9 8 5 6 6 7 0 5 6 1 1 1 8 2 7 6 3 7 5 9 5 9 0 4 3 0 7 6 9 8 6 5 1"
    assert glib.grid_enc(test_str , test_grid , "5 1u 10 2d 14 3r 16 6l") == "6 5 7 2 2 2 9 8 4 8 4 7 6 4 3 6 1 4 5 0 2 2 5 5 9 7 5 1 1 0 7 7 7 4 5 1 9 1 8 9 3 6 9 2 7 3 7 7 6 3 1 8 2 5 3 4 7 0 8 2 0 2 9 7 5 0 1 4 7 6 9 3 5 8"       
def test_dec():
    assert glib.grid_dec(glib.grid_enc(test_str , test_grid) , test_grid) == test_str
    assert glib.grid_dec(glib.grid_enc(test_str , test_grid , "10 6u 23 5l 26 1d 35 9r") , test_grid , "10 6u 23 5l 26 1d 35 9r" ) == test_str      
    