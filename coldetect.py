def check_player_platform_collsion(player_x,player_y,platform_x,platform_y):
    """
    >>> check_player_platform_collsion(60,60,90,24)
    True

    >>> check_player_platform_collsion(100,29,34,23)
    False

    """
    if platform_x - 36 <= player_x + 3 <= platform_x + 36 and platform_y + 11 <= player_y - 24  <= platform_y + 12 :
        return True
    else:
        return False


def test_case(sn,stn):
    for i in range(sn,stn):
        print(i)
        if i == 3:
            return i
    else:
        return 0


        
