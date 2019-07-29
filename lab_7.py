import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    stampID= snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(stampID)
    #Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for S in range(START_LENGTH):
    x_pos=snake.xcor() #Get x-position with snake.pos()[0]
    y_pos=snake.ycor()

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()
def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position

snake.direction = "Up"
def up():
    snake.direction="Up" #Change direction to up
    move_snake() #Update the snake drawing 
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!
snake.direction = "Down"
def down():
    snake.direction="Down" #Change direction to Down
    move_snake() #Update the snake drawing 
    print("You pressed the down key!")
snake.direction = "Left"
def left():
    snake.direction="Left" #Change direction to left
    move_snake() #Update the snake drawing 
    print("You pressed the left key!")
def right():
    snake.direction="Right" #Change direction to left
    move_snake() #Update the snake drawing 
    print("You pressed the right key!")
turtle.onkeypress(up, "Up") # Create listener for up key
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        UP_EDGE = 250
        DOWN_EDGE = -250
        RIGHT_EDGE = 400
        LEFT_EDGE = -400
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif snake.direction=="Left":
        snake.goto(x_pos- SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif snake.direction=="Right":
        snake.goto(x_pos+ SQUARE_SIZE, y_pos)
        print("You moved right!")
    

    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif new_x_pos <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()
    elif new_y_pos >= UP_EDGE:
         print("You hit the up edge! Game over!")
         quit()
    elif new_y_pos <= DOWN_EDGE:
         print("You hit the right edge! Game over!")
         quit()

     # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE

    


    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE

    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()

    ######## SPECIAL PLACE - Remember it for Part 5

    #remove the last piece of the snake (Hint Functions are FUN!)
    remove_tail()
    




turtle.mainloop() 

