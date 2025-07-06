questions={
    1:
        {
        "q":"Who developed Python Programming Language?",
        "a":"Wick van Rossum",
        "b":"Rasmus Lerdorf",
        "c":"Guido van Rossum",
        "d":"Niene Stom"
        },  
    2:  {
        "q":"Is Python case sensitive when dealing with identifiers?",
        "a":"no",
        "b":"yes",
        "c":"machine dependent",
        "d":"none of the mentioned"
        },
    3:
        {
        "q":"Which of the following is the correct extension of the Python file?",
        "a":".python",
        "b":".pl",
        "c":".py",
        "d":".p"
        },
    4:  {
        "q":"All keywords in Python are in _________",
        "a":"Capitalized",
        "b":"lower case",
        "c":" UPPER CASE",
        "d":"None of the mentioned"
        },
    5:  {
        "q":"Which keyword is used for function in Python language?",
        "a":"Function",
        "b":"def",
        "c":"Fun",
        "d":"Define"
        }
    }  
#list storing correct choices of answers
list=["c","b","c","d","b"]
#for storing user's choices
user_list=[]
#for storing mark
mark=0
for i in questions:     
    
    print(i,". ",questions[i]["q"])
    print("\ta. ",questions[i]["a"])
    print("\tb. ",questions[i]["b"])
    print("\tc. ",questions[i]["c"])
    print("\td. ",questions[i]["d"])
    answer=input("enter the answer\t")
    user_list.append(answer)
    if answer==list[i-1]:
        mark+=1
    
print("your mark is",mark)        

    
