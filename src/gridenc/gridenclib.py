import string as __string
import random as __random
CHARACTERS = __string.ascii_letters + __string.punctuation + __string.digits + __string.whitespace
char_array = list(CHARACTERS)

def init_grid(width:int , seed:int):
    if len(char_array) % width != 0:
        raise Exception("Num of characters not divisible by width. Try something else")
        
    grid = []
    row_count = 0
    __random.seed(seed)
    for i in range(len(CHARACTERS)):
        choice = __random.choice(char_array)
        if i % width == 0:
            if i > (width-1):
                row_count += 1
            
            grid.append([])
            grid[row_count].append(choice)
            
        else:
            grid[row_count].append(choice)                  
        char_array.remove(choice)
    #WE GOT THE GRID!! (21/02/2025)
    return grid
 
def get_index(grid, value):
    for row_index, row in enumerate(grid):
        if value in row:
            col_index = row.index(value)
            return [row_index, col_index]
    return None

def grid_enc(encstr:str , grid , combine_prompt = None): #prompt format : [char_num] prompt1 [char_num] prompt_2 .... 
    save_grid = grid
    encoded_str_raw = []
    if combine_prompt is not None:
        prompt_arr = combine_prompt.split(" ")
        prompt_dict = {}
        
        for index in range(0 , len(prompt_arr) , 2):
            prompt_dict[prompt_arr[index]] = prompt_arr[index+1]
    
    for ind,j in enumerate(encstr):
        if combine_prompt is not None:    
            if str(ind) in prompt_dict.keys():
                 save_grid = grid_shift(save_grid , prompt_dict[str(ind)])
        val_index = get_index(save_grid , j)
        if val_index == None:
            return "Something went wrong"
        encoded_str_raw.append(str(val_index[0]))
        encoded_str_raw.append(str(val_index[1]))
        
         
    return " ".join(encoded_str_raw)
def grid_dec(decstr_raw:str , grid ,combine_prompt = None): 
    save_grid = grid
    decstr = decstr_raw.split(" ")
    decoded_str = ""
    if combine_prompt is not None:
        prompt_arr = combine_prompt.split(" ")
        prompt_dict = {}
        
        for index in range(0 , len(prompt_arr) , 2):
            prompt_dict[prompt_arr[index]] = prompt_arr[index+1]
    
    
    for l,i in zip(range(0 , len(decstr) , 2) , range(int(len(decstr)/2))):
        
        if combine_prompt is not None:
            if str(i) in prompt_dict.keys():
                    save_grid = grid_shift(save_grid , prompt_dict[str(i)])
            
        decoded_str = decoded_str +  save_grid[int(decstr[l])][int(decstr[l+1])]
    return decoded_str



    
#prototype complete 22/02/2025
def grid_shift(grid , prompt:str): #prompt format : nl \ nr \ nu \ nd
    num_raw , prompt_real = list(prompt)
    save_grid = grid
    num = int(num_raw)
    
    match prompt_real:
        case "u":
            for _ in range(num):
                new_grid = []
                for item in save_grid[1:]:
                    new_grid.append(item)
                new_grid.append(save_grid[0])    
                save_grid = new_grid
                
        case "d":
            for _ in range(num):
                new_grid = []
                new_grid.append(save_grid[len(save_grid)-1])
                for item in save_grid[ : len(save_grid)-1]:
                    new_grid.append(item)
                    
                save_grid = new_grid
        case "l":
            for _ in range(num):
                new_grid = []
                for i,item in enumerate(save_grid):
                    new_grid.append([])
                    for char in item[1:]:
                        new_grid[i].append(char)
                    if i+1 < len(save_grid):
                            
                        new_grid[i].append(save_grid[i+1][0])
                    else:
                        new_grid[i].append(save_grid[0][0])  
                save_grid = new_grid
        case "r":
            for _ in range(num):
                new_grid = []
                for i,item in enumerate(save_grid):
                    new_grid.append([])
                    if i-1 >= 0:
                            
                        new_grid[i].append(save_grid[i-1][len(save_grid[i-1]) - 1])
                    else:
                        new_grid[i].append(save_grid[len(save_grid) - 1][len(save_grid[len(save_grid) - 1]) -1])
                    for char in item[: len(item) - 1]:
                        new_grid[i].append(char)
                      
                save_grid = new_grid
                                  
                        
    return new_grid                        

    
     