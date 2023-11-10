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

    print("Tabs you have opened:", tabs)

    if tabs:
        while True:
            index = int(input("Enter the Index of the tab you wish to close: "))
            if 0 <= index < len(tabs):
               tabs.pop(index)
               print(f"Tab at index {index} closed successfully.")
               print("Tabs you have opened:", tabs)
            else:
              print("Invalid index. Please enter a valid index.")
              print("Tabs you have opened:", tabs)
    else:
        print("No tab to close.")















            # def CloseTab():
#     print("tab  you have opened ",tabs)
#     if tabs:
#         index =int( input("Enter the Index of the tab you wish to close: "))
#         if 0 >= index <= len(tabs):
#             return
#
#             tabs.pop(index)
#         # elif index == '':
#         #     index = int(index)
#         #     index = -1
#         else:
#              print("Invalid index.")
#     else:
#         print("no tab to close")









    #     print("No tabs to close")
    # else:
    #    index = input("Enter the Index of the tab you wish to close: ")
    #         index = int(index)
    #
    #    if index =='':
    #
    #      index = -1
    #
    #    else:
    #     index = int(index)
    #     if 0>= index >= len(tabs):
    #
    #     else:
    #         print("Invalid index.")
    #
    #         return
    #     tabs.pop(index)

    # main()



def main():
    displayMenu()
    choice = input("Enter Your Choice:")
    if choice == "1":
        openTab()

    elif choice =="2":
        CloseTab()






main()
















