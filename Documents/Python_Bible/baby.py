from random import choice

questions = ["why is the sky blue?", "Why that?", "where are all the dinosaurs?"]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()
print("Oh... Okay")
