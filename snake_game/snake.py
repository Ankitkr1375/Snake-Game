from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        # Starting positions for the snake segments
        self.start_pos = STARTING_POSITIONS
        self.segments = []  # List to hold all segments of the snake
        self.create_snake()  # Method to initialize the snake
        self.head = self.segments[0]
    def create_snake(self):
        """Creates the initial snake with segments."""
        for position in self.start_pos:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)  # Set segment at specified position
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
   
    def move(self):
        """Moves the snake forward by updating segment positions."""
        # Start from the last segment and move backwards
        for seg_no in range(len(self.segments) - 1, 0, -1):
            # Get the x and y position of the segment in front
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            # Move the current segment to the position of the one in front
            self.segments[seg_no].goto(new_x, new_y)
        # Move the head (first segment) forward
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)