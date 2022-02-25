import re


def read_file(path):
    cs = {}
    projects = {}
    with open(path) as infile:
        C,P = re.match("(\d+) (\d+)",infile.readline()).group(1,2)
     
        counter = 0
        while counter < int(C) :
            name,n_skills = re.match("(\w+) (\d+)",infile.readline()).group(1,2)
            skills = {}
            for i in range(int(n_skills)):
                lang,level = re.match("(.+) (\d+)",infile.readline()).group(1,2)
                skills[lang]=int(level)
            
            cs[name]=skills
            counter +=1

        counter = 0
        while counter < int(P) :
            regex = "([\w|\d]+) (\d+) (\d+) (\d+) (\d+)"
            name,D,S,B,R = re.match(regex,infile.readline()).group(1,2,3,4,5)
            roles={}
            for i in range(int(R)):
                lang,level = re.match("(.+) (\d+)",infile.readline()).group(1,2)
                roles[lang]=int(level)
            projects[name]={
                "D" : int(D),
                "B" : int(B),
                "S" : int(S),
                "R" : int(R),
                "roles" : roles
            }
            counter +=1

    return cs,projects
  

read_file("a_an_example.in.txt")
