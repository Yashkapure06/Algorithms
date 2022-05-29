import datetime
print("Would You like to give me any name?") 
bot_name = input("Please give me the name you want: ")



def lower_ques(d):
  new_dict = dict((k.lower(), v.lower()) for k, v in d.items())
  return new_dict

question={
    'Hi':"Hello!",
    'Hello':"Hi There!",
    'What is your name':f"My name  is {bot_name}!",  
    '': "Please enter valid input",
    'What is current time': f"{datetime.datetime.now()}",
    'exit':""
}

lower_questions = lower_ques(question)


user_name = input("Please enter your name?")
print(f"Welcome {user_name}!, I {bot_name} welcome's you in the world of AI!" )
while True:
  query = input(f"{user_name}: ").lower()
  if(query in lower_questions.keys()):
    if (query == "exit"):
      print("Bye Have a nice day!")
      break;
    else:
      print(f"{bot_name}: {lower_questions[query]}")
  else:
    print("Opps! worng input!")
