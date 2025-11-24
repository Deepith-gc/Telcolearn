import os

while True:
    print("\n===== MENU =====")
    print("1. Test if an IP is reachable")
    print("2. Calculate latency summary")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # --- OPTION 1: Ping Test ---
    if choice == "1":
        ip = input("Enter an IP address: ")
        print(f"Pinging {ip} ...")

        # Windows uses -n, Linux/Mac uses -c
        if os.name == "nt":
            command = f"ping -n 1 {ip}"
        else:
            command = f"ping -c 1 {ip}"

        result = os.system(command)

        if result == 0:
            print(f"{ip} is reachable!")
        else:
            print(f"{ip} is NOT reachable.")

    # --- OPTION 2: Latency Summary ---
    elif choice == "2":
        values = input("Enter comma-separated latency values: ")

        try:
            numbers = list(map(float, values.split(",")))

            minimum = min(numbers)
            maximum = max(numbers)
            average = sum(numbers) / len(numbers)

            print("\nLatency Summary")
            print("Min:", minimum)
            print("Max:", maximum)
            print("Average:", average)

        except:
            print("Invalid input! Please enter numbers only.")

    # --- OPTION 3: Exit ---
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
