import re
Email = input("Enter Your Email : ")
# with using regex
# The local part can contain from 2 to 64 characters.
# Cannot contain any whitespace characters or two consecutive dots.
req_pattern = r"^[a-zA-Z0-9!#$%&*+-/=?^_{|}~].{1,63}@[a-zA-Z0-9.]+$"
white_space = r"\s" # to check whether white space is present or not.
twodots = r"\.{2}" # to check for two consecutive dots.
if re.match(req_pattern, Email) and not re.findall(white_space,Email) and not re.findall(twodots,Email) :
    print("Valid Email")
else:
    print("Invalid Email")

# without using regex
email = Email.split("@")
if len(email)>2:
    print("Invalid Email")
else:
    if ".." in email[0] or " " in email[0] or len(email[0])<2 or len(email[0]) > 64:
        print("Invalid Email")
    else:
        print("Valid Email")