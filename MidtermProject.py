import requests
import urllib.request
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
    tab = {'title': title, 'url': url}      #i use dictionary
    tabs.append(tab)
    main()


def switchTab(url):
    if tabs:
        print("Tabs you have opened:", tabs)
        index_display = input("Enter the Index of the tab to display its content (press Enter for the last tab): ")
        if not index_display.strip():
            #https://urllib3.readthedocs.io/en/stable/reference/urllib3.poolmanager.html
             http = urllib3.PoolManager()
             url = tabs[-1]['url']
             response = requests.get(url)
             if response.status_code == 200:
                 data = http.request('GET', url)
             else:
                 print("invalid url")
        else:
            http = urllib3.PoolManager()
            index_display=int(index_display)
            url = tabs[index_display]['url']
            response = requests.get(url)
            if response.status_code == 200:
                data = http.request('GET', url)




        #https://stackoverflow.com/questions/20906416/beautifulsoup-soup-prettify-gives-strange-output
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract and print the HTML content
        html_content = soup.prettify()
        print(html_content)
    else:
        print("Failed to connect the web")



def CloseTab():
    # check if list isempty
    #     pass

    print("Tabs you have opened:", tabs)

    if tabs:
        while True:
            index = input("Enter the Index of the tab you wish to close: ")
            # fixee the index if user click enter without adding any index

            if  not index.strip():    #So if strip() means "if the result of strip() is not an empty string
                tabs.pop(-1)
                print("Last tab closed successfully.",tabs)
                main()
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
        switchTab(tabs)






main()
















