REGEX= "(\d) (\d)"
re.match(REGEX,t).group(1)
import re

from scipy import rand 

def read_file(path):
    cs = {}
    with open(path) as infile:
        C,P = re.match("(\d+) (\d+)",infile.readline()).group(1,2)

        counter = 0
        while counter < C :
            name,n_skills = re.match("(\w+) (\d+)",infile.readline()).group(1,2)
            skills = {}
            for i in rand(n_skills):
                lang,level = re.match("(.+) (\d+)",infile.readline()).group(1,2)
                skills[lang]=level
            
            cs[name]=skills
            counter +=1
    
        counter = 0
        
        #for end in simfile: pass 
    