import re

#pass your puzzle input in below path
#change the file name based upon you input file
file1="input1.txt" #puzzle 1
file2="input2.txt" #puzzle 1

red_cube = 12 
green_cube = 13 
blue_cube = 14

#core logic to check the game feasibility and return false or true
def check_ball(ball_number,ball_colour):
    match ball_colour:
        case 'red':
            if int(ball_number) <= red_cube:
                return True
            else:
                return False
        case 'green':
            if int(ball_number) <= green_cube:
                return True
            else:
                return False;
        case 'blue':
            if int(ball_number) <= blue_cube:
                return True
            else:
                return False
            
def solution1(line, total_game):
    isGamePossible = True
    gameid = re.findall('[0-9]+',line.split(":")[0])
    line = line.replace("\n"," ").strip()
    ball_details= (line.split(":")[1]).split(";")
    for ball_detail in ball_details:
        for ball in ball_detail.split(","):
            isGamePossible = check_ball(ball.split()[0],ball.split()[1])
            #print(isGamePossible)
            if isGamePossible == False:
                return 0        
    if isGamePossible:
        return int(gameid[0])
    else:
        return 0
        
def solution2(ball_number,ball_colour):
    #initilize the count
    min_ball_red = 0
    min_ball_green = 0
    min_ball_blue = 0
    
    ball_details= (line.split(":")[1]).split(";")
    #print("ball details :", ball_details)
    for ball_detail in ball_details:
        for ball in ball_detail.split(","):
            #check ball count and set min count required to play the game
            match ball.split()[1]:
                case 'red':
                    if int(ball.split()[0]) >= min_ball_red:
                        min_ball_red = int(ball.split()[0])
                    continue;
                case 'green':
                    if int(ball.split()[0]) >= min_ball_green:
                        min_ball_green = int(ball.split()[0])
                    continue
                case 'blue':
                    if int(ball.split()[0]) >= min_ball_blue:
                        min_ball_blue = int(ball.split()[0])
                    continue;
    return min_ball_red*min_ball_green*min_ball_blue

#main function
if __name__ == "__main__":
    solution_1 = 0
    solution_2 = 0
    #Reading Input file and parse it line by line
    #You may put the file parsing logic in solution1 and solution 2 functions
    with open(file1) as filehandler:
        for line in filehandler.readlines():
            #I used common input file. Therefore, kept solution 
            solution_1 += solution1(line,solution_1)
        print("Solution 1 Result --> ",solution_1)
           
            
    with open(file2) as filehandler:
        for line in filehandler.readlines():
            #I used common input file. Therefore, kept solution 
            solution_2 += solution2(line, solution_2)
        print("Solution 2 Result --> ",solution_2)
            
