import random

name = ""
question = ""
answer = ""
random_number = random.randint(1, 12)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Maybe, maybe"
elif random_number == 11:
  answer = "Something tells me the answer may still not be revealed"
elif random_number == 12:
  answer = "Obviously no!"
else:
  answer = "Error"

if question == "" or question == " ":
  print("Magic 8-Ball's answer: You have nothing to question, I have nothing to answer.")
else:
  if name != "" and name != " ":
    print(name, "asks:", question)
  else:
    print("Question:", question)

  print("Magic 8-Ball's answer:", answer)