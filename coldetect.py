def chack_player_platform_collsion(player_x,player_y,platform_x,platform_y):
    """
    >>> chack_player_platform_collsion(60,60,90,24)
    True

    """
    if platform_x - 36 <= player_x <= platform_x + 36 and player_y - 24  == platform_y + 12 :
        return True
    else:
        return False


        
