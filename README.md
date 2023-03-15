# smtp-tester
This script reads the file containing SMTP usernames and passwords, and iterates over each line, extracting the username and password. It then attempts to establish a connection to the SMTP server using the provided credentials, and logs the result (success or failure) to the appropriate output file.

# user&pass list format

      username::password
      
Note that this script assumes that the input file is in the format username::password, with each username/password combination on a separate line.
