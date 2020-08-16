#PROBLEMS 
#sort log 
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

def unitTest():
    assert reorderLogFiles(logs) == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"] , "Failed test"

def reorderLogFiles(logs):
    def custom_sort(log):
        _id, contetn = log.split(" ",1)
        return (0, contetn, _id) if contetn[0].isalpha() else (1,)
    
    return sorted(logs,key=custom_sort)
