def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode \n2. Decode \n3. Quit")
        choice = int(input("Please enter an option:"))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
        #elif choice == 2:


def encode(password):
    pass_list = []
    encoded_password = ""
    for i in range(0, len(password)):
        pass_list.append(int(password[i]))
    for i in range(0, len(pass_list)):
        pass_list[i] =int(pass_list[i]) + 3
    for i in range(0, len(pass_list)):
        encoded_password  += str(pass_list[i])
    return  encoded_password




if __name__ == "__main__":
    main()