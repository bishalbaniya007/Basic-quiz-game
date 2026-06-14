import json, random, os

# this function loads the json file
def load_file():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  file_path = os.path.join(script_dir, "questions.json")

  with open(file_path, "r") as f:
    questions = json.load(f)      # questions is a list of dictionaries
    return questions
  

def filter_questions(questions, difficulty):
  filtered_questions = []
  for item in questions:
    if item["difficulty"] == difficulty:
      filtered_questions.append(item)

  quiz_engine(filtered_questions, difficulty)


def quiz_engine(questions, difficulty):
  # shuffle the questions (questions -> list of dictionaries)
  random.shuffle(questions)
  
  # Pointing system
  if difficulty == 'easy':
    point = 1
  
  elif difficulty == 'medium':
    point = 2
  
  elif difficulty == 'hard':
    point = 3

  correct_answer = 0

  print("\n--- Welcome to Quiz Game ---\n")
  print(f"\n--- Level: {difficulty.capitalize()} ---\n")

  for i in range(10):
    question_data = questions[i]   # this stores a dict of question data

    print(f"{i+1}) {question_data['question']} \n")
    ans = input("Enter your answer: ").strip().lower()

    if ans == question_data['answer'].lower():
      print(f"Correct ✅. You earned {point} points. \n")
      correct_answer += 1

    else:
      print(f"Incorrect❌. The correct answer is {question_data['answer']}. \n")

  print(f"\n--- Correct answers: {correct_answer} / 10 ---")
  print(f"--- Your final score: {correct_answer * point} ---\n")
  

def play_again():
  while True:
    choice = input("\nWould you like to play again (y/n)? ").strip().lower()
    if choice == 'y':
      return True

    elif choice == 'n':
      return False

    else:
      print("Please enter a valid choice: ")
      

def main():
  questions = load_file()   
  while True:
    print("\n--- Menu ---\n")
    print("1. Easy")
    print("2. Medium")
    print("3. Difficult")
    print("4. Exit\n")

    try:
      choice = int(input("Enter your choice: "))

      if choice == 1:
        filter_questions(questions, 'easy')

      elif choice == 2:
        filter_questions(questions, 'medium')

      elif choice == 3:
        filter_questions(questions, 'hard')

      elif choice == 4:
        print("Exit")
        break

      else:
        print("\nInvalid choice! Please choose a valid option.\n")
        continue
    
    except ValueError:
      print("\nInvalid input! \n")
      continue

    
    if not play_again():
      print("--- Thank you for playing! ---\n")
      break

if __name__ == "__main__":
  main()
