import re

email = input("What's your email? ").strip()

# if re.search(r".+@.+\.edu", email):
# if re.search(".*@.*", email):
# if re.search("..*@..*", email):
# if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
# if re.search(r"^\w+@\w+\.edu$", email):
# if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email):

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
