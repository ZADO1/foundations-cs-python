import urllib.request
import requests
from bs4 import BeautifulSoup
import urllib3
def displayMenu():
    print("1.Open Tab\n"+
          "2.Close Tab\n"+
          "3.Switch Tab\n"+
          "4.Display all Tab\n"+
          "5.Open Nested Tab\n"+
          "6.Clear All Tabs\n"+
          "7.Save Tabs\n"+
          "8.Import Tabs\n"+
          "9.Exit")


tabs = []
def openTab():
    title = input("Enter The Title of the Website:")
    url = input("Enter the URl:")
    tab = {'title': title, 'url': url}      # use dictionary
    tabs.append(tab)
    main()


def switchTab(url):
    if tabs:
        print("Tabs you have opened:", tabs)
        index_display = input("Enter the Index of the tab to display its content (press Enter for the last tab): ")

        if not index_display.strip():
            http = urllib3.PoolManager()
            url = tabs[-1]['url']
            response = requests.get(url)
            if response.status_code == 200:          #https://stackoverflow.com/questions/1892161/what-does-result-status-code-200-in-python-mean
                data = http.request('GET', url)
            else:
                print("Invalid URL")
        else:
            try:
                http = urllib3.PoolManager()
                index_display = int(index_display)
                url = tabs[index_display]['url']
                response = requests.get(url)

                if response.status_code == 200:
                    data = http.request('GET', url)
                else:
                    print("Invalid URL")
            except (ValueError, IndexError):
                print("Invalid index.")
                return

        soup = BeautifulSoup(response.text, 'html.parser')
        html_content = soup.prettify()
        print(html_content)
    else:
        print(" no tabs opened.")



def CloseTab():
    print("Tabs you have opened:", tabs)

    if tabs:
        while True:
            index = input("Enter the Index of the tab you wish to close: ")

            if not index.strip():
                tabs.pop(-1)
                print("Last tab closed successfully.", tabs)
                main()
            elif 0 <= int(index) < len(tabs):  # Convert index to integer
                tabs.pop(int(index))
                print(f"Tab at index {index} closed successfully.")
                print("Tabs you have opened:", tabs)
                main()  # Go back to the main menu after closing the tab
            else:
                print("Invalid index. Please enter a valid index.")
                print("Tabs you have opened:", tabs)
    else:
        print("No tab to close.")


def displayTabs():
    if tabs:
        print("Tabs you have opened:")
        for index in range(len(tabs)):
            print(f"{tabs[index]['title']}")
    else:
        print("No tabs to display:(")

def clearAllTabs():
    tabs.clear()
    print("All tabs closed successfully.")


def main():
    displayMenu()
    choice = input("Enter Your Choice:")
    if choice == "1":
        openTab()

    elif choice =="2":
        CloseTab()
    elif choice == "3":
        switchTab(tabs)
    elif choice == "4":
        displayTabs()
    elif choice == "6":
        clearAllTabs()
        main()






main()