import webbrowser

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
tabs = []
def openTab():
    title = input("Enter The Title of the Website:")
    url = input("Enter the URl:")
    tab = {'title': title, 'url': url}      #i use dictionary
    tabs.append(tab)
    main()

def CloseTab():
    print("tab  you have opened ",tabs)
    if not tabs:
        print("No tabs to close")
    index = input("Enter the Index of the tab you wish to close: ")
    tabs.pop(index)






    if index =='':
        index = -1

    else:
        index = int(index)
        if index < -1 or index >= len(tabs):
            print("Invalid index.")
    main()





    # main()




def main():
    displayMenu()
    choice = input("Enter Your Choice:")
    if choice == "1":
        openTab()

    elif choice =="2":
        CloseTab()






main()
















