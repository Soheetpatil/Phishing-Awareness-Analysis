import re

phishing_keywords = [
    "urgent",
    "verify your account",
    "click here",
    "login now",
    "password",
    "bank account",
    "suspended",
    "limited time",
    "confirm identity",
    "otp"
]

def analyze_message(message):
    message = message.lower()

    # Remove extra spaces/newlines
    message = re.sub(r'\s+', ' ', message)

    red_flags = []

    for keyword in phishing_keywords:
        if keyword in message:
            red_flags.append(keyword)

    print("\n----- Analysis Report -----")

    if red_flags:
        print("⚠ Potential Phishing Detected!")

        print("\nRed Flags Found:")
        for flag in red_flags:
            print(f"• {flag}")

        print(f"\nTotal Red Flags: {len(red_flags)}")
        print("Risk Level: HIGH")
        print("Recommendation: Do NOT click links or share personal information.")

    else:
        print("✅ No obvious phishing indicators found.")
        print("Risk Level: LOW")

message = input("Enter email/message for analysis:\n")
analyze_message(message)