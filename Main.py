import os
import time

def ascii_art(tail_char, eye_char):
    art_height = 31
    art_width = 150
    

    for row in range(art_height):
        line = ""
        for col in range(art_width):  
            if row == 0:
                if 32 <= col <= 70 or col == 73 or col == 85:
                    line += "@"
                elif 74 <= col <= 84:
                    line += "+"
                elif col == 86:
                    line += "."
                elif 135 <= col <= 142:
                    line += "_"
                else:
                    line += " "
                    
            elif row == 1:
                if col == 32 or col == 70 or col == 73 or col == 85:
                    line += "@"
                elif col == 33 or col == 69:
                    line += "*"
                elif 74 <= col <= 84:
                    line += "+"
                elif col == 86:
                    line += "."
                elif col == 133 or col == 134:
                    line += "/"
                elif col == 136:
                    line += "\\"
                elif col == 138:
                    line += "1"
                elif col == 139:
                    line += "2"
                elif col == 143 or col == 144:
                    line += "\\"
                else:
                    line += " "
                    
            elif row == 2:
                if col == 32 or col == 70 or col == 73 or col == 85:
                    line += "@"
                elif col == 33 or col ==69 :
                    line += "*"
                elif col == 86:
                    line += "."
                elif col == 133 or col == 134 or col == 143 or col == 144:
                    line += "|"
                elif col == 137:
                    line += "\\"
                elif col == 139:
                    line += "|"
                else:
                    line += " "

            elif row == 3:
                if col == 32 or col == 70 or col == 73 or col == 85:
                    line += "@"
                elif col == 33 or col ==69 :
                    line += "*"
                elif 74 <= col <= 84:
                    line += "-"
                elif col == 86:
                    line += "."
                elif col == 133 or col == 134 or col == 143 or col == 144:
                    line += "|"
                elif col == 135:
                    line += "0"
                elif col == 136:
                    line += "9"
                elif col == 138:
                    line += "\\"
                elif col == 139:
                    line += "|"
                elif col == 141:
                    line += "0"
                elif col == 142:
                    line += "3"
                else:
                    line += " "

            elif row == 4:
                if col == 32 or col == 70 or col == 73 or col == 85:
                    line += "@"
                elif col == 33 or col ==69 :
                    line += "*"
                elif 39 <= col <= 41 or 60 <= col <= 64:
                    line += "_"
                elif col == 86 or col == 99 or col == 116:
                    line += "."
                elif 100 <= col <= 115:
                    line += ":"
                elif col == 133 or col == 134 or col == 143 or col == 144:
                    line += "|"
                else: 
                    line += " "

            elif row == 5:
                if col == 32 or col == 70 or col == 73 or col == 85:
                    line += "@"
                elif col == 33 or col == 69 :
                    line += "*"
                elif col == 38 or col == 59:
                    line += "("
                elif col == 41:
                    line += "_"
                elif col == 42:
                    line += "`"
                elif col == 43:
                    line += "\\"
                elif col == 65:
                    line += ")"
                elif 74 <= col <= 84:
                    line += ":"
                elif col == 86:
                    line += "."
                elif col == 99 or col == 116:
                    line += "+"
                elif col == 133 or col == 134:
                    line += "\\"
                elif col == 138:
                    line += "0"
                elif col == 139:
                    line += "6"
                elif col == 143 or col == 144:
                    line += "/"
                elif 135 <= col <= 142:
                    line += "_"
                else:
                    line += " "
                    
            elif row == 6:
                if col == 32 or col == 70 or col == 73 or col == 85:
                    line += "@"
                elif col == 33 or col ==69 :
                    line += "*"
                elif col == 38 or col == 59 or col == 65:
                    line += "|"
                elif col == 40 or col == 61:
                    line += "("
                elif col == 41 or 48 <= col <= 49 or 54 <= col <= 56:
                    line += "_"
                elif col == 42 or col == 44 or col ==63:
                    line += ")"
                elif 74 <= col <= 84:
                    line += ":"
                elif col == 86:
                    line += "."
                elif col == 99 or col == 116:
                    line += "+"
                else:
                    line += " "
                    
            elif row == 7:
                if col == 32 or col == 70 or 73 <= col <= 85:
                    line += "@"
                elif col == 33 or col ==69 :
                    line += "*"
                elif col == 38 or col == 59 or col == 61 or col == 63 or col == 65:
                    line += "|"
                elif col == 43:
                    line += "<"
                elif col == 44 or col == 47 or col == 53:
                    line += "'"
                elif col == 46 or col == 52: 
                    line += "/"
                elif 48 <= col <= 49:
                    line += "_"
                elif col == 50 or col == 57:
                    line += "`"
                elif col == 51:
                    line += "\\"
                elif col == 55:
                    line += "_"
                elif col == 58:
                    line += "\\"
                elif col == 86:
                    line += "."
                elif col == 99 or col == 116:
                    line += "+"
                else:
                    line += " "

            elif row == 8:
                if col == 32 or col == 70 or col == 73 or col == 85:
                    line += "@"
                elif col == 33 or col ==69 :
                    line += "*"
                elif col == 38 or col == 52 or col == 58 or col == 59 or col == 65 :
                    line += "|"
                elif col == 40 or col == 45 or col == 54 or col == 61 or col == 62:
                    line += "("
                elif col == 41:
                    line += "_"
                elif col == 42 or col == 44 or col == 56:
                    line += ")"
                elif 48 <= col <= 50:
                    line += "_"
                elif col == 51:
                    line += "/"
                elif col == 63:
                    line += "'"
                elif col == 64:
                    line += "\\"
                elif col == 86 or 92 <= col <= 98 or 117 <= col <= 123:
                    line += "."   
                elif col == 99 or col == 116:
                    line += "+"
                elif 100 <= col <= 115:
                    line += ":"
                else:
                    line += " "

            elif row == 9:
                if col == 32 or col == 70 or col == 73 or col == 85:
                    line += "@"
                elif col == 33 or col ==69 :
                    line += "*"
                elif col == 38 or col == 52 or col == 56 or col == 59:
                    line += "("
                elif 39 <= col <= 42 or col ==53 or 47 <= col <= 50 or col == 57 or col == 64 or 60 <= col <= 62:
                    line += "_"
                elif col == 43:
                    line += "/"
                elif col == 44:
                    line += "'"
                elif col == 45:
                    line += "`"
                elif col == 46 or col == 63:
                    line += "\\"
                elif col == 51 or col == 54 or col == 58 or col == 65:
                    line += ")"
                elif col == 86:
                    line += "."  
                elif 91 <= col <= 124:
                    line += "+"  
                else:
                    line += " "

            elif row == 10:
                if 7 <= col <= 9:
                    line += "_"
                elif 25 <= col <= 30  or 87 <= col <= 88:
                    line+= "_"
                elif col == 32 or col == 70 or 73 <= col <= 77 or 81 <= col <= 85:
                    line += "@"
                elif col == 33 or col ==69 or 90 <= col <= 125 :
                    line += "*"
                elif col == 86:
                    line += "."
                else:
                    line += " "

            elif row == 11:
                if col == 5 or col == 11:
                    line += "o"
                elif col == 6 or col == 10:
                    line += "|"
                elif col == 7 or col == 9:
                    line += "*"
                elif col == 24:
                    line += "/"
                
                elif col == 32 or col == 70 or 73 <= col <= 76 or col ==79 or 82 <= col <= 85:
                    line += "@"
                elif col == 33 or col ==69 or 90 <= col <= 125 :
                    line += "*"
                elif col == 86:
                    line += "."
                else:
                    line += " "
                    
            elif row == 12:
                if col == 5 or col == 11:
                    line += "o"
                elif col == 6 or col == 10:
                    line += "|"
                elif col == 7 or col == 9:
                    line += "*"
                elif col == 23:
                    line += "/"
                elif col == 32 or col == 70 or 73 <= col <= 77 or 81 <= col <= 85:
                    line += "@"
                elif col == 33 or col ==69 or 90 <= col <= 99 or 116 <= col <= 125:
                    line += "*"
                elif col == 86:
                    line += "."
                elif 100 <= col <= 115:
                    line += "="
                else:
                    line += " "

            elif row == 13:
                if col == 5 or col == 11:
                    line += "o"
                elif col == 6 or col == 10:
                    line += "|"
                elif col == 7 or col == 9:
                    line += "*"
                elif col == 24 or col ==26:
                    line += "("
                elif col == 25 or col ==27:
                    line += "\\"
                elif col == 22:
                    line += "/" 
                elif 32 <= col <= 70 or col == 73 or col == 85:
                    line += "@"
                elif 90 <= col <= 99 or 116 <= col <= 125:
                    line += "*"
                elif col == 86:
                    line += "."
                elif 74 <= col <= 84:
                    line += "+"
                elif col == 126:
                    line += "\\"
                else:
                    line += " "

            elif row == 14:
                if col == 10:
                    line += "/"
                elif col == 6 :
                    line += "\\"
                elif 7 <= col <= 9:
                    line += "="
                elif col == 21:
                    line += "/"
                elif col == 24:
                    line += "("
                elif col == 25 or col ==27 :
                    line += eye_char
                elif col == 26 or col == 86:
                    line += "."
                elif col == 28:
                    line += ")"
                elif 50 <= col <= 52 or col == 73 or col == 85:
                    line += "@"
                elif 74 <= col <= 84 or 101 <= col <= 114:
                    line += ":"
                elif 90 <= col <= 99 or 116 <= col <= 125:
                    line += "+"      
                elif col == 127:
                    line += "\\"
                else:
                    line += " "
                    

            elif row == 15:
                if 7 <= col <= 9:
                    line += "|"
                elif col == 20:
                    line += "/"
                elif col == 24:
                    line += "o"
                elif col == 25:
                    line += "_"
                elif col == 26 or col == 29:
                    line += "("
                elif col == 27 or col == 30:
                    line += "'"
                elif col == 28 or col == 31:
                    line += ")"
                    
                elif 48 <= col <= 54 or col == 73 or col == 85:
                    line += "@"
                elif 74 <= col <= 84 or 101 <= col <= 114:
                    line += ":"
                elif col == 86 or col == 100 or col == 115:
                    line += "."     
                elif col == 128:
                    line += "\\"
                else:
                    line += " " 
                
                
            elif row == 16:
                if 7 <= col <= 9:
                    line += "|"
                elif col == 19:
                    line += "/"
                elif col == 129:
                    line += "\\"
                else:
                    line += " "
                

            elif row == 17:
                if 7 <= col <= 9:
                    line += "|"
                elif 18 <= col <= 130:
                    line += "=" 
                elif col == 143 or col == 144:
                    line += "_"
                elif col == 145:
                    line += "/"
                elif col == 146:
                    line += ")"
                else:
                    line += " "

            if row == 18:
                if 7 <= col <= 9:
                    line += "|"
                elif col == 19 or col == 22 or col == 25 or col == 28 or col == 120 or col == 123 or col == 126 or col == 129:
                    line += "|"
                elif col == 140:
                    line += "."
                elif col == 141:
                    line += "-"
                elif col == 142 or col == 145:
                    line += "("
                elif col == 143 or col == 144:
                    line += "_"
                elif col == 146:
                    line += "="
                elif col == 147:
                    line += ":"
                else:
                    line += " "
                    
            if row == 19:
                if 7 <= col <= 9:
                    line += "|"
                elif col == 19 or col == 22 or col == 25 or col == 28 or col == 120 or col == 123 or col == 126 or col == 129:
                    line += "|"
                elif 4 <= col <= 6 or 10 <= col <= 12:
                    line += "_"
                elif col == 140:
                    line += "|"
                elif col == 145:
                    line += "\\"
                elif col == 146:
                    line += ")"
                else:
                    line += " "
  
            if row == 20:
                if 7 <= col <= 9:
                    line += "|"
                elif col == 19 or col == 22 or col == 25 or col == 28 or col == 120 or col == 123 or col == 126 or col == 129:
                    line += "|"
                elif col == 3:
                    line += "/"
                elif col == 13:
                    line += "\\"
                elif col == 134:
                    line += "("
                elif col == 135:
                    line += "\\"
                elif col == 136 or col == 137:
                    line += "_"
                elif col == 140:
                    line += "|"
                else:
                    line += " "
            
            if row == 21:
                if 7 <= col <= 9:
                    line += "|"
                elif col == 19 or col == 22 or col == 25 or col == 28 or col == 120 or col == 123 or col == 126 or col == 129:
                    line += "|"
                elif col == 2:
                    line += "/"
                elif col == 14:
                    line += "\\"
                elif col == 133:
                    line += ":"
                elif col == 134:
                    line += "="
                elif col == 135 or col == 138:
                    line += ")"
                elif col == 136 or col == 137:
                    line += "_"
                elif col == 139:
                    line += "-"
                elif col == 140:
                    line += "|"
                elif col == 143 or col == 144:
                    line += "_"
                elif col == 145:
                    line += "/"
                elif col == 146:
                    line += "("
                else:
                    line += " "

            if row == 22:
                if 7 <= col <= 9 or col == 1 or col == 15:
                    line += "|"
                elif col == 19 or col == 22 or col == 25 or col == 28 or col == 120 or col == 123 or col == 126 or col == 129:
                    line += "|"
                elif col == 134:
                    line += "("
                elif col == 135:
                    line += "/"
                elif col == 140:
                    line += "|"
                elif col == 141:
                    line += "-"
                elif col == 142 or col == 145:
                    line += "("
                elif col == 143 or col == 144:
                    line += "_"
                elif col == 146:
                    line += "="
                elif col == 147:
                    line += ":"
                elif col == 103:
                    line += "/"
                elif col == 104 or col == 110:
                    line += "^"
                elif 105 <= col <= 109:
                    line += "-"
                elif col == 111:
                    line += "\\"
                else:
                    line += " "
                    
            if row == 23:
                if 7 <= col <= 9:
                    line += "|"
                elif col == 19 or col == 22 or col == 25 or col == 28 or col == 120  or col == 123 or col == 126 or col == 129:
                    line += "|"
                elif col == 6:
                    line += "("
                elif col == 10:
                    line += ")"
                elif col == 2:
                    line += "\\"
                elif col == 14:
                    line += "/"
                elif 132 <= col <= 137:
                    line += "_"
                elif col == 140:
                    line += "|"
                elif col == 143:
                    line += "_"
                elif col == 145:
                    line += "\\"
                elif col == 146:
                    line += ")"
                elif col == 103 or col == 111:
                    line += "V"
                elif col == 104 or col == 105 or col == 107 or col == 109 or col == 110:
                    line += " "
                elif col == 106 or col == 108:
                    line += eye_char
                else:
                    line += " "
                    
                    
            if row == 24:
                if 7 <= col <= 9 or col == 3 or col == 13:
                    line += "|"
                elif col == 19 or col == 22 or col == 25 or col == 28 or col == 120 or col == 123 or col == 126 or col == 129:
                    line += "|"
                elif col == 131 or col == 142:
                    line += "/"
                elif col == 138 or col == 144:
                    line += "\\"
                elif col == 140:
                    line += "|"
                elif col == 103 or col == 111:
                    line += " "
                elif col == 104 or col == 110:
                    line += "|"
                elif col == 105 or col == 106 or col == 108 or col == 109:
                    line += " "
                elif col == 107:
                    line += "Y"
                else:
                    line += " "
                    
            if row == 25:
                
                if 7 <= col <= 9:
                    line += "|"
                elif col == 19 or col == 22 or col == 25 or col == 28 or col == 120 or col == 123 or col == 126 or col == 129:
                    line += "|"
                elif col == 2:
                    line += "/"
                elif col == 14:
                    line += "\\"
                elif col == 141:
                    line += "/"
                elif col == 139 or col == 145:
                    line += "\\"
                elif 136 <= col <= 138 or 143 <= col <= 144:
                    line += "_"
                elif col == 140:
                    line += "|"
                elif col == 103 or col == 104 or col == 110 or col == 111:
                    line += " "
                elif col == 105:
                    line += "\\"
                elif col == 106 or col == 108:
                    line += " "
                elif col == 107:
                    line += "Q"
                elif col == 109:
                    line += "/"
                else:
                    line += " "

            if row == 26:
                if 7 <= col <= 9:
                    line += "|"
                elif col == 19 or col == 22 or col == 25 or col == 28 or col == 120 or col == 123 or col == 126 or col == 129:
                    line += "|"
                elif 26 <= col <= 27 or 121 <= col <= 122:
                    line += "_"
                elif col == 1 :
                    line += "/"
                elif col == 15:
                    line += "\\"
                elif col == 135:
                    line += "["
                elif col == 145:
                    line += "]"
                elif col == 146:
                    line += "\\"
                elif col == 103 or col == 104 or col == 110 or col == 111:
                    line += " "
                elif col == 105:
                    line += "/"
                elif col == 106 or col == 108:
                    line += " "
                elif col == 107:
                    line += "-"
                elif col == 109:
                    line += "\\"
                else:
                    line += " "
                    
            if row == 27:
                if col == 0 or col == 16:
                    line += "|"
                elif col == 19 or col == 22  or col == 126 or col == 129:
                    line += "|"
                elif col == 6:
                    line += "["
                elif 7 <= col <= 9:
                    line += "="
                elif col == 10:
                    line += "]"
                elif col == 136 or col == 147:
                    line += "\\"
                elif col == 144:
                    line += "/"
                elif col == 103 or col == 104 or col == 106 or col == 107 or col == 108 or col == 109:
                    line += " "
                elif col == 105:
                    line += "|"
                elif col == 110:
                    line += "\\"
                else:
                    line += " "
                    
            if row == 28:
                if col == 1:
                    line += "\\"
                elif col == 19 or col == 22 or col == 126 or col == 129:
                    line += "|"
                elif col == 15:
                    line += "/"
                elif col == 137:
                    line += "\\"
                elif col == 143:
                    line += "/"
                elif col == 103 or col == 104 or col == 106 or col == 107 or col == 108 or col == 109 or col == 111 or col == 112 or col == 113 or col == 114 or col == 115 or col == 116 or col == 117:
                    line += " "
                elif col == 105:
                    line += "|"
                elif col == 110:
                    line += "\\"
                elif col == 118:
                    line += tail_char
                else:
                    line += " "

            if row == 29:
                if col == 2 or col == 14:
                    line += "'"
                elif col == 19 or col == 22 or col == 126 or col == 129:
                    line += "|"
                elif 20 <= col <= 21 or 127 <= col <= 128 :
                    line += "_"
                elif col == 3 or col == 13:
                    line += "."
                elif  5 <= col <= 11:
                    line += "_"
                elif col == 138:
                    line += "\\"
                elif 139 <= col <= 141:
                    line += "_"
                elif col == 142:
                    line += "/"
                elif col == 103 or col == 104 or col == 107 or col == 118:
                    line += " "
                elif col == 105 or col == 106:
                    line += "|"
                elif col == 108:
                    line += "("
                elif col == 109 or col == 110 or col == 111:
                    line += "_"
                elif col == 112:
                    line += "\\"
                elif col == 113 or col == 114 or col == 115 or col == 116 or col == 117:
                    line += "="
                
                else:
                    line += " "
            
                   
        print(line)

#ascii_art()


# Animation loop
tail_chars = [")", "("]
eye_chars = ["o", "-"]
while True:
    for tail_char, eye_char in zip(tail_chars, eye_chars):
        os.system('cls' if os.name == 'nt' else 'clear')
        ascii_art(tail_char, eye_char)
        time.sleep(0.5)
