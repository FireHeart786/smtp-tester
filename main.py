import smtplib

smtp_file = input("Enter file containing SMTP usernames and passwords: ")
smtp_port = input("Enter SMTP port (default is 587): ")

live_smtp_file = "live_smtp.txt"
dead_smtp_file = "dead_smtp.txt"

with open(smtp_file, "r") as f:
    lines = f.readlines()

for line in lines:
    try:
        username, password = line.strip().split("::")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        with open(live_smtp_file, "a") as f:
            f.write(line)
        print("SMTP login successful for " + username + "!")
    except Exception as e:
        with open(dead_smtp_file, "a") as f:
            f.write(line)
        print("SMTP login failed for " + username + ". Error: " + str(e))
    finally:
        server.quit()
