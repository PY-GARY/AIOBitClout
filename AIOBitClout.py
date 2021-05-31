import requests
import os
import base64

logo = "\n\
                            ██████╗ ██╗████████╗ ██████╗██╗      ██████╗ ██╗   ██╗████████╗\n\
                            ██╔══██╗██║╚══██╔══╝██╔════╝██║     ██╔═══██╗██║   ██║╚══██╔══╝\n\
                            ██████╔╝██║   ██║   ██║     ██║     ██║   ██║██║   ██║   ██║   \n\
                            ██╔══██╗██║   ██║   ██║     ██║     ██║   ██║██║   ██║   ██║   \n\
                            ██████╔╝██║   ██║   ╚██████╗███████╗╚██████╔╝╚██████╔╝   ██║   \n\
                            ╚═════╝ ╚═╝   ╚═╝    ╚═════╝╚══════╝ ╚═════╝  ╚═════╝    ╚═╝"

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def get_info():
    try:
        clear()

        print(f"""{logo}\n\n
            Type the username of the user.
        """)

        rep_username = input("\n\t=> ")

        response = requests.post("https://bitclout.com/api/v0/get-single-profile", json={"Username": rep_username})

        username = response.json()["Profile"]["Username"]
        verified = response.json()["Profile"]["IsVerified"]
        description = response.json()["Profile"]["Description"]
        holders = response.json()["Profile"]["CoinEntry"]["NumberOfHolders"]
        publickey = response.json()["Profile"]["PublicKeyBase58Check"]

        response2 = requests.post("https://bitclout.com/api/v0/get-follows-stateless", headers={"Content-Type": "application/json"}, data='{"Username":"'+rep_username+'","PublicKeyBase58Check":"","GetEntriesFollowingUsername":true,"LastPublicKeyBase58Check":""}')

        followers = response2.json()["NumFollowers"]

        response3 = requests.post("https://bitclout.com/api/v0/get-follows-stateless", headers={"Content-Type": "application/json"}, data='{"Username":"'+rep_username+'","PublicKeyBase58Check":"","GetEntriesFollowingUsername":false,"LastPublicKeyBase58Check":""}')

        followings = response3.json()["NumFollowers"]

        clear()

        print(f"""{logo}\n\n
                \t\t\t\t 
                \t\t\t\t Username:      [ {username} ] 
                \t\t\t\t Followers:     [ {followers} ] 
                \t\t\t\t Followings:    [ {followings} ] 
                \t\t\t\t Description:   [ {description} ] 
                \t\t\t\t Verified:      [ {verified} ]
                \t\t\t\t Public Key:    [ {publickey} ] 
                
                \t\t\t\t Coin Holders:  [ {holders} ] 
        """)

        input("\t\tPress Enter...")
        main()

    except:
        input("\n\n\tError press enter...")
        main()

def launch_miner():
    try:
        clear()

        print(f"""{logo}\n\n
            Enter you're Public Key.
        """)

        key = input("\n\t=> ")
        print("\n\n")

        os.system(f"cloutreactor-windows-amd64.exe --public-key {key}")
    
    except:
        input("\n\n\tError press enter...")
        main()

def pp_downloader():
    try:
        clear()

        print(f"""{logo}\n\n
            Enter the username.
        """)
        username = input("\n\t=> ")

        response2 = requests.post("https://bitclout.com/api/v0/get-single-profile", json={"PublicKeyBase58Check":"","Username":username})
        img = response2.json()["Profile"]["ProfilePic"]
        data = img.split(",")[1]

        imgdata = base64.b64decode(data)

        filename = f'profile_picture\\{username}.jpg'

        with open(filename, 'wb') as f:
            f.write(imgdata)

        os.system(f"profile_picture\\{username}.jpg")

        print("\n\tProfile picture downloaded !")
        
        input("\t\tPress Enter...")
        main()

    except:
        input("\n\n\tError press enter...")
        main()

def main():
    try:
        clear()
        print(f"""{logo}\n\n
            [1] - Get Profile Info\t[2] - Profile Picture Download

            [A] - Miner
        """)

        choice = input("\n\t=> ")

        if choice == "1":
            get_info()
        elif choice == "2":
            pp_downloader()
        elif choice == "A":
            launch_miner()
        else:
            main()
    except:
        input("\n\n\tError press enter...")
        main()




if __name__ == "__main__":
    main()