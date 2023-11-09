def displayMenu():
    print("1.Open Tab\n",
          "2.Close Tab\n",
          "3.Switch Tab\n",
          "4.Display all Tab\n",
          "5.Open Nested Tab\n",
          "6.Clear All Tabs\n",
          "7.Save Tabs\n",
          "8.Import Tabs\n",
          "9.Exit\n",)
def main():
 displayMenu()
choice = input("Enter Your Choice:")
if choice == "1":
    title = input("Enter The Title:")
    url = input("enter the URL:")


