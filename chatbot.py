def chat():
    users=['hi','hello','world']
    bot=['hey buddy','vanakam','globe']
    userinput=input("you: ")
    i=0
    for user in users:
        if userinput==user:
            print('bot:'+bot[i])
            return chat()
        i=i+1


chat()
