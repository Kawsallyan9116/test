import smtplib, ssl

port = 465  # For SSL
password = "TismNGap16"
message = "Hai Kawbar"
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("kawsallyan16gmail.com", password)
    server.sendmail("kawsallyan16gmail.com","kawsallyan16gmail.com", message)