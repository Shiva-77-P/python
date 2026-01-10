# No empty variable needed!
while True:
    command = input("Enter command: ")
    
    # Check inside the club
    if command == "exit":
        break  # <--- Smash the emergency glass and leave the loop
    
    print("Running:", command)

print("Shutting down")
