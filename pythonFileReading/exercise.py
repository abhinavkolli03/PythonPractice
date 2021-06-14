quiz = open("questions.txt", "r")
quiz = [line.strip() for line in quiz]
n = 0
m = 0
for line in quiz:
    q, a = line.split("=")
    user_answer = input(f"{q}=")
    if a == user_answer:
        n += 1
    m += 1
result_file = open("results.txt", "w")
results = result_file.write(f"Your final score is {n}/{m}.")
result_file.close()