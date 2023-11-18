last_distance_x = 0

def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    '''return "up" or "down", depending on which way the paddle should go to
    align its centre with the centre of the ball, assuming the ball will
    not be moving
    
    Arguments:
    paddle_frect: a rectangle representing the coordinates of the paddle
                  paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                  corner of the rectangle. 
                  paddle_frect.size[0], paddle_frect.size[1] are the dimensions
                  of the paddle along the x and y axis, respectively
    
    other_paddle_frect:
                  a rectangle representing the opponent paddle. It is formatted
                  in the same way as paddle_frect
    ball_frect:   a rectangle representing the ball. It is formatted in the 
                  same way as paddle_frect
    table_size:   table_size[0], table_size[1] are the dimensions of the table,
                  along the x and the y axis respectively
    
    The coordinates look as follows:
    
     0             x
     |------------->
     |
     |             
     |
 y   v
    '''          
    global last_distance_x
    paddle_center_x = paddle_frect.pos[0] + paddle_frect.size[0] / 2
    ball_center_x = ball_frect.pos[0] + 15 / 2
    distance_x = ball_center_x - paddle_center_x

    if last_distance_x > distance_x:
        direction = 'towards'
    else:
        direction = 'away'

    last_distance_x = distance_x

    # if direction == 'towards':
    #     if paddle_frect.pos[1]+paddle_frect.size[1]/2 < ball_frect.pos[1]+ball_frect.size[1]/2:
    #         return "down"
    #     else:
    #         return "up"
        
    if paddle_frect.pos[1]+paddle_frect.size[1]/2 < ball_frect.pos[1]+ball_frect.size[1]/2:
        return "down"
    else:
        return "up"  
    
