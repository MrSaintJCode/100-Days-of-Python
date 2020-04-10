from bs4 import BeautifulSoup
import tkinter as tk
import requests
import sqlite3
import time, datetime, os

# -----------------------------------------------------
#           Coronavirus GUI Application
# - https://www.worldometers.info/coronavirus/ -
#           04/02/2020 - Justin St-Laurent
# -----------------------------------------------------
url = "https://www.worldometers.info/coronavirus/"
page = requests.get(url)

def error_handler(error_message):
    global error_handler_gui
    error_handler_gui = tk.Tk(className=" An Unexpected Error Occured")
    error_handler_gui.resizable(False, False)

    # Contents - Error Handler
    error_handler_message_label = tk.Label(error_handler_gui, text=error_message)
    error_handler_ok_button = tk.Button(error_handler_gui,text="Ok",command=error_handler_gui.destroy)

    # Display - Error Handler
    error_handler_message_label.pack()
    error_handler_ok_button.pack()

    print("")
    print("-- ERROR --")
    print(f"[X] {error_message}")

    error_handler_gui.mainloop()

def main(page):
    if page.status_code == 200:
        print("")
        print("[*] Page Successfully Retrieved")
    elif page.status_code == 404:
        error_handler("Page Not Found")

    def refresh(url, main_total_cases_label, main_total_deaths_label, main_total_recovered_label):
        selected_country = var.get()
        print(selected_country)
        if selected_country == 'Worldwide':
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
        else:
            page = requests.get(url + selected_country)
            soup = BeautifulSoup(page.content, 'html.parser')


        # Gathering Information
        total_cases = soup.find_all('span')[4].get_text()
        total_deaths = soup.find_all('span')[5].get_text()
        total_recovered = soup.find_all('span')[6].get_text()

        main_total_cases_label.config(text=total_cases)
        main_total_deaths_label.config(text=total_deaths)
        main_total_recovered_label.config(text=total_recovered)
        print("")
        print("--- Information Updated ---")
        print(f"Total Cases - {total_cases}")
        print(f"Total Deaths - {total_deaths}")
        print(f"Total Recovered - {total_recovered}")



        
    
    global main_gui
    main_gui = tk.Tk(className=" Worldometer")
    main_gui.geometry("250x320")
    main_gui.resizable(False, False)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Gathering Information
    total_cases = soup.find_all('span')[4].get_text()
    total_deaths = soup.find_all('span')[5].get_text()
    total_recovered = soup.find_all('span')[6].get_text()

    # Style - Main
    label_title_style = 'Helvetica 24 bold'
    label_title_fg = '#ededed'
    label_info_style = 'Helvetica 22'

    # Contents - Main
    spacing1 = tk.Label(main_gui,text= " ")
    spacing2 = tk.Label(main_gui,text= " ")
    spacing3 = tk.Label(main_gui,text= " ")

    main_total_cases_title_label = tk.Label(main_gui,text="Total Cases", font=label_title_style, fg=label_title_fg)
    main_total_cases_label = tk.Label(main_gui,text=total_cases, font=label_info_style,fg="#a8a8a8")

    main_total_deaths_title_label = tk.Label(main_gui,text="Total Deaths", font=label_title_style, fg=label_title_fg)
    main_total_deaths_label = tk.Label(main_gui,text=total_deaths,font=label_info_style,fg="#ed4e4e")

    main_total_recovered_title_label = tk.Label(main_gui,text="Total Recovered", font=label_title_style, fg=label_title_fg)
    main_total_recovered_label = tk.Label(main_gui, text=total_recovered,font=label_info_style,fg="#51cc3b")

    # Drop Down Menu - Main
    # Default Time - 1 Minute
    default_option = 'Worldwide'
    var = tk.StringVar(main_gui)
    var.set(default_option)
    countries = [default_option]
    for country in soup.find_all('a',{'class': ['mt_a'], 'href': True}):
        countries.append(country['href'])

    option_dropdown = tk.OptionMenu(main_gui, var, *countries)
    # Display - Main
    refresh_button = tk.Button(main_gui, text="Update", command=lambda:refresh(url,main_total_cases_label, main_total_deaths_label, main_total_recovered_label),width="20")

    # -- Total Cases --
    main_total_cases_title_label.pack()
    main_total_cases_label.pack()

    spacing1.pack()

    # -- Total Deaths --
    main_total_deaths_title_label.pack()
    main_total_deaths_label.pack()

    spacing2.pack()

    # -- Total Recovered -- 
    main_total_recovered_title_label.pack()
    main_total_recovered_label.pack()

    spacing3.pack()

    # -- Settings --
    refresh_button.pack()
    option_dropdown.pack()

    background_color = '#212121'

    main_total_cases_title_label.configure(bg=background_color)
    main_total_cases_label.configure(bg=background_color)

    main_total_deaths_title_label.configure(bg=background_color)
    main_total_deaths_label.configure(bg=background_color)

    main_total_recovered_title_label.configure(bg=background_color)
    main_total_recovered_label.configure(bg=background_color)

    refresh_button.configure(highlightbackground=background_color)
    option_dropdown.configure(bg=background_color)

    spacing1.configure(bg=background_color)
    spacing2.configure(bg=background_color)
    spacing3.configure(bg=background_color)

    main_gui.configure(bg=background_color)


    main_gui.mainloop()


if __name__ == '__main__':
    try:
        print("")
        print("-- BACKEND --")
        main(page)

    except (KeyboardInterrupt) as reason:
        error_handler(reason)
