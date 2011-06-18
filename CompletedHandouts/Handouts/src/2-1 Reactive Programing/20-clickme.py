from Panda import *

# Make a simple game that scores a point every time you click something that jumps around
score = var(0)     # Score
nextScore = var(1) # How much to score
text(score)     # Show the score

def move(m, v):
    m.position = # Move the model to a random place
    nextScore.set(1) # Set the score
    m.react1(localTimeIs(1), move)  # Wait 1 second to move

def scoreMe(m, v):
    score.add(nextScore.now())  # Score whatever the current score is
    nextScore.set(0)            # Prevent scoring twice at the same position
    
p = panda()
p.react(leftClick(p), scoreMe)
move(p, 0)  # Start the panda moving
start()

# Make the game more interesting:
#   Make the game slowly speed up
#   Sometimes paint the model a different color and make the score go down if you click it