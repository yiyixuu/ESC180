import math

last_distance_x = 0
last_ball_center_x = 0.001
last_ball_center_y = 0.001

def predict_ball_position(ball_pos, ball_velocity, paddle_x, table_size):
    if ball_velocity[0] != 0:
        m = ball_velocity[1] / ball_velocity[0] # slope
        c = -ball_pos[0] * m + ball_pos[1] # y-intercept
        val = (m * paddle_x + c) % (2 * table_size[1])
        return min(val, 2 * table_size[1] - val)
    return ball_pos[1]

def get_y_for_angle(paddle_frect, angle):
    center = paddle_frect.size[1] / 2
    sign = 1 - 2 * (angle < 0)
    rel_dist_from_c = sign * angle / paddle_frect.size[1] * 180 / math.pi
    rel_dist_from_c = min(0.5, rel_dist_from_c)
    rel_dist_from_c = max(-0.5, rel_dist_from_c)
    print(f'rel_dist_from_c: {rel_dist_from_c:.2f}')
    return center + rel_dist_from_c * paddle_frect.size[1]

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
    global last_ball_center_x
    global last_ball_center_y

    # Calculate the center of the paddle and the ball
    paddle_center_y = paddle_frect.pos[1] + paddle_frect.size[1] / 2
    paddle_center_x = paddle_frect.pos[0] + paddle_frect.size[0] / 2

    other_paddle_center_y = other_paddle_frect.pos[1] + other_paddle_frect.size[1] / 2
    other_paddle_center_x = other_paddle_frect.pos[0] + other_paddle_frect.size[0] / 2

    ball_center_y = ball_frect.pos[1] + 15 / 2
    ball_center_x = ball_frect.pos[0] + 15 / 2

    


    
    # Calculate the distance between the centers of the paddle and the ball
    distance_y = ball_center_y - paddle_center_y
    distance_x = ball_center_x - paddle_center_x

    if last_distance_x < distance_x:
        direction = 'towards'
    else:
        direction = 'away'

    # print(f'direction: {direction} y dist: {distance_y} x dist: {distance_x} dist: {math.sqrt(distance_y**2+distance_x**2)}')

    
    # If the ball is moving away from the paddle, don't move
    # if ball_center < table_size[0] / 2:
    #     return None
    ball_v_x = ball_center_x - last_ball_center_x
    ball_v_y = ball_center_y - last_ball_center_y

    last_distance_x = distance_x
    
    if direction == 'towards':
        predicted_y = predict_ball_position((ball_center_x, ball_center_y), (ball_v_x, ball_v_y), paddle_center_x, table_size)
    else:
        predicted_y_away = predict_ball_position((ball_center_x, ball_center_y), (ball_v_x, ball_v_y), other_paddle_center_x, table_size)
        predicted_y = predict_ball_position((other_paddle_center_x, predicted_y_away), (-ball_v_x, ball_v_y), paddle_center_x, table_size)
    
    # print(f'direction: {direction}, v_x: {ball_v_x:.2f}, v_y: {ball_v_y:.2f}, predicted_y: {predicted_y:.2f}, paddle_center_y: {paddle_center_y:.2f}, distance {abs(predicted_y - paddle_center_y):.2f}')


    last_ball_center_x = ball_center_x
    last_ball_center_y = ball_center_y


    # # move center to predicted y if ball is moving towards paddle, otherwise move to center
    # if direction == 'towards':
    #     if paddle_center_y > predicted_y:
    #         print('up')
    #         return 'up'
    #     elif paddle_center_y < predicted_y:
    #         print('down')
    #         return 'down'
    #     else:
    #         return None
    # else:
    #     if paddle_center_y > table_size[1] / 2:
    #         print('up')
    #         return 'up'
    #     elif paddle_center_y < table_size[1] / 2:
    #         print('down')
    #         return 'down'
    #     else:
    #         return None
    
    # # always move edge of paddle to predicted y
    # if other_paddle_center_y < table_size[1] / 2:
    #     if paddle_frect.pos[1] > predicted_y:
    #         return 'up'
    #     elif paddle_frect.pos[1] < predicted_y:
    #         return 'down'
    #     else:
    #         return None
    # else:
    #     if paddle_frect.pos[1] + paddle_frect.size[1]> predicted_y:
    #         return 'up'
    #     elif paddle_frect.pos[1] + paddle_frect.size[1] < predicted_y:
    #         return 'down'
    #     else:
    #         return None

    # # Calculate the angle between the ball and the paddle
    # if other_paddle_center_y > table_size[1] / 2:
    #     angle = math.atan2(predicted_y, paddle_center_x)
    # else:
    #     angle = math.atan2(table_size[1] - predicted_y, paddle_center_x)

    # print(f'angle: {angle:.2f}')
    

    # # Calculate the y coordinate where the ball will hit the paddle
    # hit_y = get_y_for_angle(paddle_frect, angle)
    # print(f'hit_y: {hit_y:.2f}')

    # # Move the paddle to hit the ball at the calculated y coordinate
    # print(f'paddle_frect.pos[1] + hit_y: {paddle_frect.pos[1] + hit_y:.2f} predicted_y: {predicted_y:.2f}')
    # if paddle_frect.pos[1] + hit_y > predicted_y:
    #     return 'down'
    # elif paddle_frect.pos[1] + hit_y < predicted_y:
    #     return 'up'
    # else:
    #     return None

    # always move center of paddle to predicted y
    if paddle_center_y > predicted_y:
        # print('up')
        return 'up'
    elif paddle_center_y < predicted_y:
        # print('down')
        return 'down'
    else:
        return None
