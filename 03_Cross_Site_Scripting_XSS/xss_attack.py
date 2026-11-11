import html

print("XSS Attack Demonstration")

user_input = input("Enter your input: ")

print("\nVulnerable Output:")
print(user_input)

print("\nSecure Output:")
print(html.escape(user_input))

print("\nTesting Completed")

