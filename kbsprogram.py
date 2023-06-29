import random

def indexnumber(num):
  dictionary = {'A': '0', 'B': '1', 'C': '2', 'D': '3'}
  return dictionary[num]

def number(L):
  n = random.choice(L)
  L.remove(n)
  return L, n

def Lifeline1(n):
  print("Q" + str(i + 1) + ": " + Questions[n][0])
  correctOptionNumber = int(indexnumber(Questions[n][2]))
  indexlist = ['0', '1', '2', '3']
  indexlist.pop(correctOptionNumber)
  AnotherOption = int(random.choice(indexlist))

  if int(correctOptionNumber) < int(AnotherOption):
    print(Questions[n][1][correctOptionNumber] + '\n' +
          Questions[n][1][AnotherOption])
  else:
    print(Questions[n][1][AnotherOption] + '\n' +
          Questions[n][1][correctOptionNumber])


def Lifeline2(n):
  if Questions[n][2] == 'A':
    List = [
      "|\n|\n|\n|\t|||\n|\t|||\n|\t|||\n|\t|||\n|\t|||\n|\t|||\n|\t|||\t|||\n|_______|||_____|||_____|||__________\n         A       B       C       D\n",
      "|\n|\n|\n|\n|\t|||\n|\t|||\n|\t|||\n|\t|||\n|\t|||\t   \t   \t|||\n|\t|||\t   \t   \t|||\n|_______|||_____________|||_____|||__\n         A       B       C       D\n"
    ]
    print(random.choice(List))

  if Questions[n][2] == 'B':
    List = [
      "|\n|\n|\n|\t   \t|||\n|\t   \t|||\n|\t   \t|||\n|\t   \t|||\n|\t   \t|||\n|\t   \t|||\t   \t|||\n|_______|||_____|||_____________|||____\n         A       B       C       D\n",
      "|\n|\n|\n|\n|\n|\t   \t|||\n|\t   \t|||\n|\t|||\t|||\n|\t|||\t|||\t   \t|||\n|_______|||_____|||_____________|||____\n         A       B       C       D\n"
    ]
    print(random.choice(List))

  if Questions[n][2] == 'C':
    List = [
      "|\n|\n|\n|\t   \t   \t|||\n|\t   \t   \t|||\n|\t   \t   \t|||\n|\t   \t   \t|||\n|\t   \t   \t|||\n|\t   \t   \t|||\t|||\n|_______________|||_____|||_____|||____\n         A       B       C       D\n",
      "|\n|\n|\n|\n|\n|\t   \t   \t|||\n|\t   \t   \t|||\n|\t|||\t   \t|||\n|\t|||\t   \t|||\t|||\n|_______|||_____|||_____|||_____|||____\n         A       B       C       D\n"
    ]
    print(random.choice(List))

  if Questions[n][2] == 'D':
    List = [
      "|\n|\n|\t   \t   \t   \t|||\n|\t   \t   \t   \t|||\n|\t   \t   \t   \t|||\n|\t   \t   \t   \t|||\n|\t   \t   \t   \t|||\n|\t   \t   \t   \t|||\n|\t   \t   \t   \t|||\n|_______|||_____________|||_____|||____\n         A       B       C       D\n",
      "|\n|\n|\n|\n|\n|\t   \t   \t   \t|||\n|\t   \t   \t   \t|||\n|\t|||\t   \t   \t|||\n|\t|||\t   \t   \t|||\n|_______|||_____|||_____|||_____|||____\n         A       B       C       D\n"
    ]
    print(random.choice(List))


def Lifeline3(L, n):
  L, n = number(L)
  print('Q' + str(i + 1) + ': ' + Questions[n][0])
  for x in range(4):
    print('   ' + Questions[n][1][x])
  return L, n


def LifeLines(L, n, Lifeline):
  if Lifeline == []:
    print("You have used all your lifelines\n")
    return L, n, Lifeline
  else:
    print("\nWhich Lifeline do your want to use: ")
    print(
      "Lifeline 1: 50-50\tLifeline 2: Audience Poll\tLifeline 3: Flip the Question\n"
    )
    while True:
      lifeline_number = input("Enter the lifeline number: ")
      if lifeline_number not in ['1', '2', '3']:
        print("This is not a valid Lifeline Number.")
        return L, n, Lifeline
      else:
        if lifeline_number not in Lifeline:
          print("You have used this lifeline.\nTry another one\n")
          return L, n, Lifeline
        else:
          if lifeline_number == '1':
            Lifeline.remove('1')
            Lifeline1(n)
            return L, n, Lifeline
          elif lifeline_number == '2':
            Lifeline.remove('2')
            Lifeline2(n)
            return L, n, Lifeline
          elif lifeline_number == '3':
            Lifeline.remove('3')
            L, n = Lifeline3(L, n)
            return L, n, Lifeline
        break


def money(numberofQuestions):
  L = [
    '0', '1,000', '2,000', '3,000', '5,000', '10,000', '20,000', '40,000',
    '80,000', '1,60,000', '3,20,000', '6,40,000', '12,50,000', '25,00,000',
    '50,00,000', '1,00,00,000', '7,00,00,000'
  ]
  return L[numberofQuestions]


Questions = [
  [
    "According to the 2011 tiger census report of the national Tiger conservation Authority, what is the estimated population of tigers in India?",
    ["A: 1411", "B: 1127", "C: 2822", "D: 1706"], "D"
  ],
  [
    "Which of these symbols is normally used to indicate the direction of a place?",
    ["A: Bow", "B: Arrow", "C: Mace", "D: Sword"], "B"
  ],
  [
    "Complete this line from a Bhajan bythe bhakti poet Narsinh Mehta “Vaishnav Jan To tene Kahiye Je ___”?",
    [
      "A: Nahin Aiso Janam Barambar", "B: Sabka Data Ram",
      "C: Peerh Paraye Janeyray", "D: Lagan Lagi Ram Ki"
    ], "C"
  ],
  [
    "Which of these is the name of the anti-corruption initiative started by the Central Vigilance Commission of India?",
    [
      "A: Break your silence", "B: Blow your whistle", "C: Mind your business",
      "D: Clean your system"
    ], "B"
  ],
  [
    "Complete this hindi proverb: “___ ke gale me ghanti baandhna” that means to do a tough job?",
    ["A: Kuee", "B: Billi", "C: Sher", "D: Chuha"], "C"
  ],
  [
    "What does a twelfth of a foot equal to?",
    ["A: An inch", "B: A centimetre", "C: A metre", "D: A Yard"], "A"
  ],
  [
    "Which of these fruits of vegetables grows underwater?",
    ["A: Kachnaar", "B: Shakarkand", "C: Shareefa", "D: Singhara"], "D"
  ],
  [
    "After which of these freedom fighters is a district in Uttarakhand named?",
    [
      "A: Bhagat Singh", "B: Chandrashekhar Azad", "C: Sukhdev",
      "D: Udham Singh"
    ], "D"
  ],
  [
    "Who became the first National Security Advisor of India in 1998?",
    ["A: Brajesh Mishra", "B: M K Narayan", "C: J N Dixit", "D: K C Pant"], "A"
  ],
  [
    "In the Mahabharata, which of these characters died after the battle of kurukshetra was over?",
    ["A: Shakuni", "B: Shalya", "C: Kansa", "D: Bhishma"], "D"
  ],
  [
    "Which of these numbers is popularly known as the Hardy-Ramanujan number?",
    ["A: 1927", "B: 1729", "C: 1239", "D: 1947"], "B"
  ],
  [
    "Which of these is a Hindi phrase for “a stupid person”?",
    [
      "A: Akal ka Dushman", "B: Kaan Ka Kachcha", "C: Akal Dhadh",
      "D: Akela Dukela"
    ], "A"
  ],
  [
    "Which of these figures is also called a Mahatma?",
    [
      "A: B R Ambedkar", "B: Jyotibha Phule", "C: Vinobha Bhave",
      "D: Dhondo Keshav Karve"
    ], "B"
  ],
  [
    "Which is the heaviest internal organ in the human body?",
    ["A: Pancreas", "B: Heart", "C: Liver", "D: Lungs"], "C"
  ],
  [
    "Which of the following states does not border Andhra Pradesh?",
    ["A: Madhya Pradesh", "B: Odisha", "C: Maharashtra", "D: Tamil Nadu"], "A"
  ],
  [
    "Which of these badminton superseries tournaments did Saina Nehwal win in October 2012?",
    [
      "A: Malaysia Open", "B: Singapore Open", "C: Denmark Open",
      "D: Indonesia Open"
    ], "C"
  ],
  [
    "What motto is inscribed in Devanagari script on State Emblem of India?",
    [
      "A: Mera Bharat Mahan", "B: Vanede Mataram", "C: Satyamev Jayate",
      "D: Sare Jahan Se Sccha"
    ], "C"
  ]
]

# Rules of this Game
print("Welcome to my game : KBC (Kaun Banega Crorepati)")
print(
  "In this game, you have three lifelines : 50-50, Audience Poll & Change Question"
)
print("You can use lifeline only once...")
print("\nAll the very best....\n\n")

L, i, Lifeline = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                  16], 0, ['1', '2', '3']
while i <= 15:
  L, n = number(L)
  print('Q' + str(i + 1) + ': ' + Questions[n][0])
  for x in range(4):
    print('   ' + Questions[n][1][x])

  while True:
    Answer = input(
      "\nEnter the correct option or Type 'Lifeline' to use Lifelines: "
    ).capitalize()
    if Answer == Questions[n][2]:
      print("Correct !!\t\t\tYou earned ₹" + money(i + 1))
      print("The correct answer is\t\"",
            Questions[n][1][int(indexnumber(Questions[n][2]))], "\"\n")
      break
    elif Answer.upper() in ['LIFELINE', 'LIFELINES']:
      L, n, Lifeline = LifeLines(L, n, Lifeline)
    else:
      print("Wrong !!\t\t\tYou earned ₹" + money(i))
      print("The correct answer is\t\"",
            Questions[n][1][int(indexnumber(Questions[n][2]))], "\"")
      print("Thanks for playing !!")
      i = 20
      break

  i += 1

  if i == 16:
    print("Congratulations..... You win ₹7,00,00,000")
    print("Thanks for playing !!")