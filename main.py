import datetime, random

def getBirthdays(numberOfBirthdays):
  """Returns a list of random date objects for birthdays."""
  birthdays = []
  for i in range(numberOfBirthdays):
    # The year is unimportant for our purposes, as long as it is a leap year.
    startOfYear = datetime.date(2001, 1, 1)
    randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
    birthday = startOfYear + randomNumberOfDays
    birthdays.append(birthday)
  return birthdays

def getMatch(birthdays):
  """Returns the date which the same birthday occurs among people."""
  # Check for match of birthdays
  matches = {}
  for a, birthdayA in enumerate(birthdays):
    for b, birthdayB in enumerate(birthdays):
      if birthdayA == birthdayB and a != b:
        matches[birthdayA] = matches.get(birthdayA, 0) + 1
  return matches

# Display the intro:
print('''Birthday Paradox''')

# Set up a tuple of months:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
  # Ask the user how many birthdays to generate:
  print('How many birthdays shall I generate? (Max 100)')
  response = input()
  if response.isdecimal() and (0 < int(response) <= 100):
    numBDays = int(response)
    break
  else:
    print('Please enter a number between 1 and 100.')
    
# Generate and display the birthdays:
print('\nHere are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
  if i: print(', ', end='')
  print(MONTHS[birthday.month - 1], birthday.day, end='')
print()
print()

# Determine if there are two birthdays that match:
matches = getMatch(birthdays)
if matches:
  print('In this group of', numBDays, 'people, there is a birthday match.')
  print('Here are their birthdays:')
  for match in matches:
    print(' ', MONTHS[match.month - 1], match.day)
else:
  print('In this group of', numBDays, 'people, there are no matching birthdays.')
print()

# Run through 100,000 groups of 23 people:
print('Generating', 100000, 'groups of', numBDays, 'people...')
input('Press Enter to begin...')

print('Let\'s run 100,000 tests...')
simMatch = 0
for i in range(100000):
  birthdays = getBirthdays(numBDays)
  matches = getMatch(birthdays)
  if matches:
    simMatch = simMatch + 1
print('Out of 100,000 groups of', numBDays, 'people, there was a matching birthday in that group', simMatch, 'times.')

# Display outro:
probability = round(simMatch / 100000 * 100, 2)
print('That means that', numBDays, 'people have a', probability, '% chance of having a matching birthday in their group.')
print('matching birthday in their group', simMatch, 'people, there was a')
print('that', numBDays, 'people have a', probability, '% chance of having a')
print('matching birthday in their group.')
print('That\'s probably more than you would think!')
print('\n\n\nThanks for playing!')
