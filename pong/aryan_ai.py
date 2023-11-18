ball_Xs = []
ball_Ys = []

def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
#   return "up" or "down", depending on which way the paddle should go to
#   align its centre with the centre of the ball, assuming the ball will
#   not be moving
#   
#   Arguments:
#   paddle_frect: a rectangle representing the coordinates of the paddle
#                 paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
#                 corner of the rectangle. 
#                 paddle_frect.size[0], paddle_frect.size[1] are the dimensions
#                 of the paddle along the x and y axis, respectively
#   
#   other_paddle_frect:
#                 a rectangle representing the opponent paddle. It is formatted
#                 in the same way as paddle_frect
#   ball_frect:   a rectangle representing the ball. It is formatted in the 
#                 same way as paddle_frect
#   table_size:   table_size[0], table_size[1] are the dimensions of the table,
#                 along the x and the y axis respectively
#   
#   The coordinates look as follows:
#   
#    0             x
#    |------------->
#    |
#    |             
#    |
#y   |

    global ball_Xs
    global ball_Ys

    ytravel = 0

    ballX = ball_frect.pos[0]+ball_frect.size[0]/2
    ballY = ball_frect.pos[1]+ball_frect.size[1]/2

    paddleX = paddle_frect.pos[0]+paddle_frect.size[0]/2
    paddleY = paddle_frect.pos[1]+paddle_frect.size[1]/2
    half_v_paddleSize = paddle_frect.size[1]/2

    oPaddleX = other_paddle_frect.pos[0]+other_paddle_frect.size[0]/2
    oPaddleY = other_paddle_frect.pos[1]+other_paddle_frect.size[1]/2

    tableX = table_size[0]
    tableY = table_size[1]

    leftB = min(paddle_frect.pos[0]+paddle_frect.size[0], other_paddle_frect.pos[0]+other_paddle_frect.size[0]) + ball_frect.size[0]/2
    rightB = max(paddle_frect.pos[0], other_paddle_frect.pos[0]) - ball_frect.size[0]/2
    topB = ball_frect.size[1]/2
    bottomB = tableY - ball_frect.size[1]/2

    bounds = (leftB, rightB, topB, bottomB)
    
    store_pos(ballX, ballY)
    dx = find_dx(ball_Xs)
    dy = find_dy(ball_Ys)
    
    if dy != "undef" and dx != "undef":
        bounces = get_bounces(ballX, ballY, dx, dy, bounds)
        if bounces != []:
            finalBx, finalBy = bounces[-1]
        else:
            finalBx, finalBy = (ballX, ballY)
        
        if len(bounces) % 2 == 1:
            dy = -dy

        if dx > 0: #right
            x_dist = rightB - finalBx  
            ytravel = (x_dist/dx) * dy
        if dx < 0: #left
            x_dist = finalBx - leftB  
            ytravel = abs(x_dist/dx) * dy 
        
        targetY = finalBy + ytravel
    else: 
        targetY = ballY
    
    #print(f"left bound: {leftB}, right bound: {rightB}, top bound: {topB}, bottom bound: {bottomB}")
    #print(f"dx: {dx}, dy: {dy}")
    #print(f"{numBounces} bounces @ {bounces}")
    #print(f"finalX: {str(finalBx)[:5]}, finalY: {str(finalBy)[:5]}, target: {str(targetY)[:5]}")

    # try to hit where other paddle isnt
    # hit upwards if paddle is below
    # hit downwards if paddle is above

    #if oPaddleY > targetY: #other paddle below
     #   targetY -= half_v_paddleSize + ball_frect.size[1]//2 - 2 # put top of my paddle @ ball
    #elif oPaddleY < targetY: #other paddle below
     #   targetY += half_v_paddleSize + ball_frect.size[1]//2 - 2# put bottom of my paddle @ ball

    # hit ball @ corner of paddle
    if dy != "undef":
        if dy > 0: #going down
            targetY += half_v_paddleSize + ball_frect.size[1]//2 - 2# put top of my paddle @ ball
        elif dy < 0: #going up
            targetY -= half_v_paddleSize + ball_frect.size[1]//2 - 2# put bottom of my paddle @ ball

    if paddleY < targetY:
     return "down"
    else:
     return "up"
    
def store_pos(ballX, ballY):
    global ball_Xs
    global ball_Ys
    ball_Xs.append(ballX)
    ball_Ys.append(ballY)

def find_dx(ballXs):
    if len(ballXs) >= 2:
        return ballXs[-1] - ballXs[-2]
    else: 
        return "undef"

def find_dy(ballYs):
    if len(ballYs) >= 2:
        return ballYs[-1] - ballYs[-2]
    else: 
        return "undef"

def get_next_bounce(x, y, dx, dy, bounds):
    leftB, rightB, topB, bottomB = bounds
    d_left = x - leftB
    d_right = rightB - x
    d_top = y - topB
    d_bottom = bottomB - y

    next_bounce = False

    if dx > 0 and dy > 0: #down and right
        vert = (d_right/dx) * dy

        if vert < d_bottom:
            return False
        
        brown = (d_bottom/dy) * dx

        next_bounce = (x + brown, bottomB)

    if dx > 0 and dy < 0: #up and right
        vert = abs((d_right/dx) * dy)

        if vert < d_top:
            return False
        
        brown = (d_top/dy) * dx # pos div neg times pos = neg

        next_bounce = (x - brown, topB)

    if dx < 0 and dy > 0: #down and left
        vert = abs((d_left/dx) * dy) 

        if vert < d_bottom:
            return False
        
        brown = (d_bottom/dy) * dx # pos div pos times neg = neg

        next_bounce = (x + brown, bottomB)

    if dx < 0 and dy < 0: #up and left
        vert = abs((d_left/dx) * dy)

        if vert < d_top:
            return False
        
        brown = (d_top/dy) * dx # pos div neg times neg = pos

        next_bounce = (x - brown, topB)

    return next_bounce

def get_bounces(x, y, dx, dy, bounds):
    next_bounce = get_next_bounce(x, y, dx, dy, bounds)
    bounces = []
    counter = 0
    while next_bounce != False:
        bounces.append(next_bounce)
        nx, ny = next_bounce
        next_bounce = get_next_bounce(nx, ny, dx, -dy, bounds)
        counter += 1
        if counter >= 50: break
    
    return bounces