import bankdemo as banking

def main():
    while True:
        print("\n1. Add new Client")
        print("2. Update existing client")
        print("3. Delete Client")
        print("4. Display Client")
        print("5. Display Total")
        print("6. Money Transfer")
        print("7. Make VIP")
        print("8. Exit")
        
        option = int(input("\nSelect an option: "))

        if option == 1:
            name = input("Enter the new Client name: ")
            dob = input("Enter the new Client Date of Birth(YYYY-MM-DD): ")
            balance = float(input("Enter the Client Balance : "))
            banking.add_client(banking.load_clients(),name, dob, balance)
            print("Client added successfully. ")

        elif option == 2:
            client_id = int(input("Enter Client ID"))
            name = input("Enter new Client name(leave empty to keep current.)")
            dob = input("Enter new Client DOB(YYYY-MM-DD)(leave empty to keep current.)")
            balance = input("Enter new Client balance(leave empty to keep current.)")
            banking.update_client(banking.load_clients(),client_id, name, dob, balance)
            print("Client updated successfully. ")

        elif option == 3:
            client_id = int(input("Enter client ID: "))
            banking.delete_client(banking.load_clients(),client_id)
            print("Client deleted successfully. ")

        elif option == 4:
            client_id = int(input("Enter Client ID: "))
            banking.display_client(banking.load_clients(),client_id)
            
        elif option == 5:
            banking.display_total(banking.load_clients())

        elif option == 6:
            client_id1 = int(input("Enter client ID to make transfer from : "))
            client_id2 = int(input("Enter client ID to make transfer to : "))
            amount = float(input("Enter the amount to be transfer :  "))
            banking.make_trasfer(banking.load_clients(), client_id1, client_id2, amount)    

        elif option == 7:
            banking.make_vip(banking.load_clients())    
            pass

        elif option == 8:
            print("Exiting the program. Have a nice day!")
            break

        else:
            print("Invalid option. Please try again. ")    


main()            