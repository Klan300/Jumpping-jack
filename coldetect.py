import time


def check_player_platform_collsion(player_x,player_y,platform_x,platform_y):

    """
    >>> check_player_platform_collsion(60,60,90,24)
    True

    >>> check_player_platform_collsion(100,29,34,23)
    False

    """
    if platform_x - 36 <= player_x + 3 <= platform_x + 36 and (platform_y + 9<= player_y - 23 <= platform_y + 12):
        return True
    else:
        return False


def check_time(time_str):
    end_time = time.time()
    return end_time - time_str




    


        
