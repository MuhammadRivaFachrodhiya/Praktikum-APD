from menu import *
from login import *
from regis import *
clear()
os.system('pip install pandas')
os.system('pip install tabulate')
os.system('pip install prettytable')
def main():      
        while True:
                clear()
                tampilkanMenutama()
                try:
                        choice = inputTengah("Pilihan anda -> ")
                        clear()
                        if not choice:
                                raise ValueError("\t\t\t\t\t\t\t\t\t\t\t\tPilihan menu tidak boleh kosong.")
                        if not re.match("^[A-Za-z0-9]*$", choice):
                                raise ValueError("\t\t\t\t\t\t\t\t\t\t\tPilihan menu tidak boleh menggunakan karakter spesial.")
                        if choice not in ['0','1','2']:
                                raise ValueError("\t\t\t\t\t\t\t\t\t\t\t     Pilihan menu harus berupa angka (0,1,2).")
                               
                        if choice == "1":
                                statusLogin = login()
                                if statusLogin:
                                        for user in datauser["akun"]:
                                           if user["username"] == statusLogin["username"]:
                                                if user["role"] == "Owner":
                                                        ownerMenu()
                                                elif user["role"] == "Pembeli":
                                                        username = statusLogin["username"]
                                                        pembeliMenu(username)
                        elif choice == "2":
                                register() 
                                clear()
                                print_tengah("Sedang membuat akun. . . .")
                                time.sleep(2)
                                loading()
                                lanjut()

                        elif choice == "0":
                               print_tengah("Terimakasih telah menggunakan program kami")
                               break
                except Exception as e:
                        clear()
                        print(e)
                        lanjut()

                        
main()             
           

        