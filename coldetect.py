import time


def check_player_platform_collsion(player_x,player_y,platform_x,platform_y):

    """
    >>> check_player_platform_collsion(60,60,90,24)
    True

    >>> check_player_platform_collsion(100,29,34,23)
    False

    """
    if platform_x - 36 <= player_x + 3 <= platform_x + 36 and (platform_y + 7 < player_y - 24 < platform_y + 16 ):
        return True
    else:

        return False


def check_time(time_str):
    end_time = time.time()
    return end_time - time_str


def test(dex):
    count = 0
    for i in range(len(dex)):
        if dex[i-count] % 2:
            dex.pop(i-count)
            count += 1
    return dex




        
