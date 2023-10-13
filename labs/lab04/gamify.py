'''We assume that the user is always either running, carrying textbooks, or resting. The user accumulates 
hedons and health points according to the following rules.
 The user starts out with 0 health points, and 0 hedons.
 The user is always either running, carrying textbooks, or resting.
 Running gives 3 health points per minute for up to 180 minutes, and 1 health point per minute for
every minute over 180 minutes that the user runs. (Note that if the user runs for 90 minutes, then
rests for 10 minutes, then runs for 110 minutes, the user will get 600 health points, since they rested
in between the times that they ran.)
 Carrying textbooks always gives 2 health points per minute.
 Resting gives 0 hedons per minute.
 Both running and carrying textbooks give -2 hedons per minute if the user is tired and isn't using
a star (definition: the user is tired if they finished running or carrying textbooks less than 2 hours
before the current activity started.) For example, for the purposes of this rule, the user will be tired
if they run for 2 minutes, and then start running again straight away.
'''
def get_cur_hedons():
    '''Returns the current number of hedons'''
    return cur_hedons

def get_cur_health():
    '''Returns the current number of health points'''
    return cur_health

def offer_star(activity):
    global cur_star_activity
    cur_star_activity = activity


#The function simulates the user’s performing activity activity for duration minutes. Assume duration
#is a positive int. If activity is not one of "running", "textbooks", or "resting", running the function
#should have no effect.
def perform_activity(activity, duration):
    global cur_hedons, cur_health, cur_time, last_activity, last_activity_duration, last_finished, bored_with_stars

    cur_time = 0

    if activity == "running":
        if duration > 180:
            cur_health += 3 * 180 + (duration - 180)
        else:
            cur_health += duration * 3

        if last_activity == 'running' or last_activity == 'textbooks' and cur_time - last_finished < 120:
            if cur_star_activity == 'running':
                if duration > 10:
                    cur_hedons += 10 + (-2) * (duration - 10)
                else:
                    cur_hedons += duration
            else:
                cur_hedons -= 2 * duration
        else:
            if cur_star_activity == 'running':
                if duration > 10:
                    cur_hedons += 5 * 10 + (-2) * (duration - 10)
                else:
                    cur_hedons += 5 * duration

            else:
                if duration > 10:
                    cur_hedons += 2 * 10 + (-2) * (duration - 10)
                else:
                    cur_hedons += 2 * duration
    
        last_finished = cur_time

    elif activity == "textbooks":
        cur_health += 2 * duration

        if last_activity == 'running' or last_activity == 'textbooks' and cur_time - last_finished < 120:
            cur_hedons -= 2 * duration
        else:
            if duration > 20:
                cur_hedons += 1 * 20 + (-1) * (duration - 20)
            else:
                cur_hedons += 1 * duration
    
        last_finished = cur_time

    elif activity == "resting":
        pass
    
    last_activity = activity
    last_activity_duration = duration
    cur_time += duration
    
    
def star_can_be_taken(activity):
    #The function returns True iff a star can be used to get more hedons for activity activity. A star can only
#be taken if no time passed between the star’s being offered and the activity, and the user is not bored with
#stars, and the star was offered for activity activity.
    global cur_time, bored_with_stars, last_activity, last_activity_duration
    return cur_time - last_finished == 0 and not bored_with_stars and last_activity == activity

def most_fun_activity_minute():
#The function returns the activity (one of "resting", "running", or "textbooks") which would give the
#most hedons if the person performed it for one minute at the current time.
    global cur_hedons, cur_health, cur_time, last_activity, last_activity_duration, last_finished, bored_with_stars

    running_hedons, textbooks_hedons, resting_hedons = 0, 0, 0

    if last_activity == 'running' or last_activity == 'textbooks' and cur_time - last_finished < 120:
        if cur_star_activity == 'running':
            running_hedons += 1
        else:
            running_hedons -= 2
    else:
        if cur_star_activity == 'running':
            running_hedons += 5
        else:
            running_hedons += 2
        
    if last_activity == 'running' or last_activity == 'textbooks' and cur_time - last_finished < 120:
        textbooks_hedons -= 2
    else:
        textbooks_hedons += 1

    if running_hedons > textbooks_hedons and running_hedons > resting_hedons:
        return "running"
    elif textbooks_hedons > running_hedons and textbooks_hedons > resting_hedons:
        return "textbooks"
    else:
        return "resting"

def initialize():
#The function initialize all the global variables in the program. 
    global cur_hedons, cur_health
    global cur_time
    global last_activity, last_activity_duration
    global last_finished
    global bored_with_stars 
    global cur_star_activity, cur_star
    cur_hedons = 0
    cur_health = 0 
    cur_star = None
    cur_star_activity = None  
    bored_with_stars = False
    last_activity = None
    last_activity_duration = 0
    cur_time = 0
    last_finished = -1000
    num_stars= []

if __name__ == '__main__':
    initialize()
    # perform_activity("running", 10)
    # print(get_cur_hedons())
    # print(get_cur_health())
    # offer_star("running")
    # print(most_fun_activity_minute())
    # perform_activity("running", 5)
    # print(get_cur_hedons())
    # print(get_cur_health())
    perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10