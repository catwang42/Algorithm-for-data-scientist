#flattern nested list 
nested = [1,2,[3,4],5,6,[8,9],10]
output = []
def flattern(nested):
    for i in nested:
        if isinstance(i, list):
            flattern(i)
        else:
            output.append(i)

nested2=[[1,2],[3,4,5],[6]]            
flattern = [i for sublist in nested2 for i in sublist]

#flattern a nested json 
unflat_json = {'user' : 
               {'Rachel': 
                {'UserID':1717171717, 
                'Email': 'rachel1999@gmail.com',  
                'friends': ['John', 'Jeremy', 'Emily'] 
                } 
               } 
              } 
              
def flatternJson(nested_json):
    output={}
    def flattern(nested,name):
        if isinstance(nested,dict):
            for item in nested:
                flattern(nested[item],name+item+'_')
        elif isinstance(nested, list):
            i = 0 
            for item in nested:
                flattern(item,name+i+'_')
        else:
            output[name[:-1]] = x 
    flattern[nested_json]
    return output 
