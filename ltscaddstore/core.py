# Insert your code here.
import pyperclip
import requests
from lxml import etree
import os
import time

def download():
     print("""--------------------------------------
Script Name: LTSC Microsoft Store Latest Version Download Script
Github project address: https://github.com/Goojoe/LTSC-ADD-Microsoft-Store
Author: Cuckoo Joe
Translated By: Guinness Shepherd
-----------------------------------------""")

     def check_name(file_name,keyword1):
         keyword2="_neutral_"
         if (keyword1 in file_name) or (keyword2 in file_name):
             return 1
         else:
             return 0

     name =input("""Please select an architecture (enter a number):
1 arm
2 arm64
3x64
4x86
:""")

     name = int(name)
     name-=1

     # Schema list
     keyword_list=["_arm_","_arm64_","_x64_","_x86_"]

     save_path_root = input("Enter save path:\n:")

     # Create the file if it doesn't exist
     if not os.path.exists(save_path_root):
         os.mkdir(save_path_root)

     api_url = "https://store.rg-adguard.net/api/GetFiles"
     store_url = "https://www.microsoft.com/store/productId/9WZDNCRFJBMP"
     success_text = "<p>The links were successfully received from the Microsoft Store server.</p>"

     # acting
     is_proxy = input("Do you need to configure HTTP proxy (y/n):\n:")
     if is_proxy == "y":
         http = input("Please enter HTTP proxy example: (127.0.0.1:1080):\n")
         proxies = {
         "http": http,
         "https": http
     }
     elif is_proxy == "n":
         proxies = {}
         print("No proxy required")
     else:
         print("Input error, exit")
         exit()

     print("request, please wait, if you fail, you can try to configure the proxy")

     # reptiles
     headers = {
         "Content-Type": "application/x-www-form-urlencoded"
     }
     data = {
         "type": "url",
         "url":store_url
     }

     # API requests
     response = requests. post(url=api_url,data=data,headers=headers,proxies=proxies)

     response.encoding = "utf-8"

     if response.status_code == 200:
         print("The request is successful, please wait patiently for 1-10 minutes to download the file")
     else:
         print("Network request failed")
         exit()


     html = etree.HTML(response.content.decode()) # pass string
     link = html.xpath("//a/@href")
     link_text = html.xpath("//a/text()")
     li=["BlockMap","eappxbundle","emsixbundle"]

     # download code
     if len(link) == len(link_text):
         for i in range(len(link)):
             li2=[0 for p in li if (p in link_text[i])]
             if len(li2)==0:
                 if check_name(link_text[i],keyword_list[name]):
                     try:
                         f = requests. get(link[i])
                         with open(f"{save_path_root}/{link_text[i]}","wb") as code:
                             code. write(f. content)
                         print("{} downloaded successfully".format(link_text[i]))
                     except:
                         print("{} failed to download".format(link_text[i]))

     # install script
     install_file_content = """Add-AppxPackage *.Appx
Add-AppxPackage *.AppxBundle
Add-AppxPackage *.Msixbundle
Write-Output "==========================================="
Write-Output "The Microsoft Store was installed"
Write-Output "==========================================="
pause
"""
     if not os.path.exists(f"{save_path_root}/install_ms-store.ps1"):
         print("Create installation script")
         with open(f"{save_path_root}/install_ms-store.ps1", "w") as install_file:
             install_file.write(install_file_content)
             install_file. close()
     else:
         print("The installation script already exists, stop creating it")

     pyperclip.copy("Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine -Force")
     print("""
Right-click and use Powershell to execute install_ms-store.ps1, if it appears:
--------------------
Disable script execution on this system
--------------------
Please open Powershell with <Administrator> privileges and execute:
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine -Force

command copied to clipboard
You can paste with Ctrl + V or right mouse button in the PowerShell window
""")
     print("The download is complete, the folder will be opened automatically after 10 seconds")

     time. sleep(10)
     os.startfile(save_path_root)

if __name__ == "__main__":
     download()
