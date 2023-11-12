import webbrowser
import requests
from bs4 import BeautifulSoup
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


def switchTab(url):
    print("Tabs you have opened:", tabs)
    if tabs:
        index_display = int(input("Enter the Index of the tab to display its content (press Enter for the last tab): "))





def CloseTab():
    # check if list isempty

    print("Tabs you have opened:", tabs)

    if tabs:
        while True:
            index = int(input("Enter the Index of the tab you wish to close: "))
            # fixee the index if user click enter without adding any index
            if index =="":
                tabs.pop(-1)
                print("Last tab closed successfully.")
            elif 0 <= index < len(tabs):
               tabs.pop(index)
               print(f"Tab at index {index} closed successfully.")
               print("Tabs you have opened:", tabs)
            else:
              print("Invalid index. Please enter a valid index.")
              print("Tabs you have opened:", tabs)
    else:
        print("No tab to close.")









def main():
    displayMenu()
    choice = input("Enter Your Choice:")
    if choice == "1":
        openTab()

    elif choice =="2":
        CloseTab()
    elif choice == "3":
        switchTab()






main()
















