# Declare 4 container to store information
age = 50
name = "John Doe"
height = 6.3
isMale = True

# Store message in variable
message = (
    f"Persons Information\n"
    f"-------------------\n"
    f"Name: {name}\n"
    f"Age: {age} years\n"
    f"Height: {height}ft\n"
    f"Is Male: {isMale}"
)

message_alternative_formatting = (
    "Persons Information\n"
    "-------------------\n"
    "Name: " + name + "\n"
    "Age: " + age + "\n"
    "Height: " + height + "\n"
    "Is Male: " + isMale + "\n"
)

single_line_message = f"Persons Information\n-------------------\nName: {name}\nAge: {age} years\nHeight: {height}ft\nIs Male: {isMale}"

# Print information
print(message)