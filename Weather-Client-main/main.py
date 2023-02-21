import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font
from PIL import ImageTk,Image
import json
import datetime
import requests
from configparser import ConfigParser
import webbrowser

from src.localization.languages import all_languages


settings = ConfigParser()
SettingsParser = settings.read('src/settings.ini')

api_key = settings.get('global', 'api_key')
lang = settings.get('global', 'lang')
global units
units = settings.get('global', 'units')
version = settings.get('global', 'version')
author = settings.get('global', 'author')
last_major_update = settings.get('global', 'last_major_update')

color_bg = settings.get('GUI', 'color_bg')
color_button = settings.get('GUI', 'color_button')
color_button_text = settings.get('GUI', 'color_button_text')
color_entry = settings.get('GUI', 'color_entry')
color_entry_text = settings.get('GUI', 'color_entry_text')
color_title = settings.get('GUI', 'color_title')
color_text = settings.get('GUI', 'color_text')
color_subtext = settings.get('GUI', 'color_subtext')

unknown_img = "src/img/unknown.png"

strings = all_languages[lang]



root = tk.Tk()
root.state("zoomed")
root.title(strings['app_title'])
root.resizable(False, False)
root.config(bg=color_bg)
root.iconbitmap("src/logo.ico")


# ---- FUNCTIONS ----
def show_error(error):
    tk.messagebox.showerror(title=error, message=error)

def CloseWindow():
    root.destroy()

def open_webpage(url):
    webbrowser.open_new(url)

def set_theme(theme):
    if theme == "light_theme":
        bg_color_code = "#FFFFFF"
        button_color_code = "#818181"
        button_text_color_code = "#FFFFFF"
        entry_color_code = "#818181"
        entry_text_color_code = "#FFFFFF"
        title_color_code = "#000000"
        text_color_code = "#818181"
        subtext_color_code = "#818181"
    elif theme == "dark_theme":
        bg_color_code = "#202020"
        button_color_code = "#B8B8B8"
        button_text_color_code = "#202020"
        entry_color_code = "#B8B8B8"
        entry_text_color_code = "#202020"
        title_color_code = "#6C6C6C"
        text_color_code = "#B8B8B8"
        subtext_color_code = "#B8B8B8"
    elif theme == "console_theme":
        bg_color_code = "#0C0C0C"
        button_color_code = "#16C60C"
        button_text_color_code = "#0C0C0C"
        entry_color_code = "#16C60C"
        entry_text_color_code = "#0C0C0C"
        title_color_code = "#16C60C"
        text_color_code = "#16C60C"
        subtext_color_code = "#16C60C"
    elif theme == "macos_theme":
        bg_color_code = "#FFFFFF"
        button_color_code = "#1F83FD"
        button_text_color_code = "#FFFFFF"
        entry_color_code = "#1F83FD"
        entry_text_color_code = "#FFFFFF"
        title_color_code = "#1D1B1E"
        text_color_code = "#1D1B1E"
        subtext_color_code = "#2c333d"
    elif theme == "blallo_theme":
        bg_color_code = "#0A3D58"
        button_color_code = "#BE7C0E"
        button_text_color_code = "#051D2A"
        entry_color_code = "#BE7C0E"
        entry_text_color_code = "#051D2A"
        title_color_code = "#F19E12"
        text_color_code = "#BE7C0E"
        subtext_color_code = "#BE7C0E"
    elif theme == "shock_theme":
        bg_color_code = "#202355"
        button_color_code = "#497585"
        button_text_color_code = "#AEFF00"
        entry_color_code = "#497585"
        entry_text_color_code = "#AEFF00"
        title_color_code = "#AEFF00"
        text_color_code = "#00FFD9"
        subtext_color_code = "#00FFD9"
    elif theme == "forest_theme":
        bg_color_code = "#586E54"
        button_color_code = "#1B666B"
        button_text_color_code = "#18292A"
        entry_color_code = "#1B666B"
        entry_text_color_code = "#18292A"
        title_color_code = "#4CA5AC"
        text_color_code = "#272D25"
        subtext_color_code = "#272D25"
    elif theme == "eruption_theme":
        bg_color_code = "#6D6362"
        button_color_code = "#2C333D"
        button_text_color_code = "#CCCBC7"
        entry_color_code = "#2C333D"
        entry_text_color_code = "#CCCBC7"
        title_color_code = "#9D1813"
        text_color_code = "#612220"
        subtext_color_code = "#2C333D"
    elif theme == "":
        return
    else:
        return
    root.configure(bg=bg_color_code)
    main_frame.configure(bg=bg_color_code)
    top_bar.configure(bg=bg_color_code)
    reload_button.configure(bg=button_color_code, fg=button_text_color_code)
    search_button.configure(bg=button_color_code, fg=button_text_color_code)
    city_entry.configure(bg=entry_color_code, fg=entry_text_color_code)
    main_infos.configure(bg=bg_color_code)
    city_state_result.configure(bg=bg_color_code)
    city_state_result_label.configure(bg=bg_color_code, fg=title_color_code)
    icon_temp_result.configure(bg=bg_color_code)
    icon_result.configure(bg=bg_color_code)
    temp_result.configure(bg=bg_color_code)
    temp_now_result_label.configure(bg=bg_color_code, fg=title_color_code)
    temp_cent_label.configure(bg=bg_color_code, fg=text_color_code)
    temp_maxmin_result.configure(bg=bg_color_code)
    temp_max_result_label.configure(bg=bg_color_code, fg=text_color_code)
    temp_min_result_label.configure(bg=bg_color_code, fg=text_color_code)
    desc_result.configure(bg=bg_color_code)
    desc_result_label.configure(bg=bg_color_code, fg=title_color_code)
    update_result_label.configure(bg=bg_color_code, fg=text_color_code)
    secondary_infos.configure(bg=bg_color_code)
    humidity_result.configure(bg=bg_color_code)
    humidity_result_label.configure(bg=bg_color_code, fg=text_color_code)
    clouds_result.configure(bg=bg_color_code)
    clouds_result_label.configure(bg=bg_color_code, fg=text_color_code)
    precipitations_result.configure(bg=bg_color_code)
    precipitations_result_label.configure(bg=bg_color_code, fg=text_color_code)
    wind_result.configure(bg=bg_color_code)
    wind_result_label.configure(bg=bg_color_code, fg=text_color_code)
    update_result.configure(bg=bg_color_code)
    update_result_label.configure(bg=bg_color_code, fg=subtext_color_code)

    settings.set('GUI', 'color_bg', bg_color_code)
    settings.set('GUI', 'color_button', button_color_code)
    settings.set('GUI', 'color_button_text', button_text_color_code)
    settings.set('GUI', 'color_entry', entry_color_code)
    settings.set('GUI', 'color_entry_text', entry_text_color_code)
    settings.set('GUI', 'color_title', title_color_code)
    settings.set('GUI', 'color_text', text_color_code)
    settings.set('GUI', 'color_subtext', subtext_color_code)
    with open('src/settings.ini', 'w') as f:
        settings.write(f)

def set_unitsystem(system):
    settings.set('global', 'units', system)

    with open('src/settings.ini', 'w') as f:
        settings.write(f)
    Update_Weather()

def set_language(language):
    settings.set('global', 'lang', language)
    if language == 'en':
        settings.set('global', 'units', 'imperial')
    elif language == 'it':
        settings.set('global', 'units', 'metric')
    else:
        pass
    with open('src/settings.ini', 'w') as f:
        settings.write(f)
    lang = language
    Update_Weather()

def deg_to_compass(num):
    val = int((num / 22.5) + .5)
    arr = ["N", "N-NE", "NE", "E-NE", "E", "E-SE", "SE", "S-SE", "S", "S-SW", "SW", "W-SW", "W", "W-NW", "NW", "N-NW"]
    return arr[(val % 16)]

def time_conversion(unix):
    time_to_convert = int(unix)
    return datetime.datetime.fromtimestamp(time_to_convert).strftime("%d/%m/%Y %H:%M:%S")

def icon_finder(icon_id):
    icons = {
        "01d" : "clear-day",
        "01n" : "clear-night",
        "02d" : "partly-cloudy-day",
        "02n" : "partly-cloudy-night",
        "03d" : "cloudy-day",
        "03n" : "cloudy-night",
        "04d" : "cloudy",
        "04n" : "cloudy",
        "09d" : "rain-day",
        "09n" : "rain-night",
        "10d" : "rain",
        "10n" : "rain",
        "11d" : "storm-day",
        "11n" : "storm-night",
        "13d" : "snow-day",
        "13n" : "snow-night",
        "50d" : "fog-day",
        "50n" : "fog-night",
    }

    global icon
    image_path = "src/img/" + icons[icon_id] + ".png"
    img_src = Image.open(image_path)
    img_src.save("src/logo.ico")
    root.iconbitmap("src/logo.ico")
    img_resized = img_src.resize((150, 150))
    icon = ImageTk.PhotoImage(img_resized)
    return icon

def image_resize(img):
    img_src = Image.open(img)
    img_resized = img_src.resize((150, 150))
    img_output = ImageTk.PhotoImage(img_resized)
    return img_output

def get_backup_data():

    with open("src/backup/backup.json", "r") as backup_file:
        backup_api = json.loads(backup_file.read())

    global city
    city = backup_api['name']

    units = settings.get('global', 'units')

    weather = backup_api['weather'][0]
    icon_id = weather['icon']
    weather_main = weather['main']
    weather_description = weather['description']

    weather_city = backup_api['name']

    sys = backup_api['sys']
    weather_country = sys['country']

    weather_timezone = backup_api['timezone']

    main = backup_api['main']
    main_temperature = main['temp']
    max_temperature = main['temp_max']
    min_temperature = main['temp_min']
    main_humidity = main['humidity']

    wind = backup_api['wind']
    wind_speed = wind['speed']
    wind_speed_kmh = wind_speed * 3.6
    wind_degrees = wind['deg']
    wind_direction = deg_to_compass(wind_degrees)

    clouds = backup_api['clouds']
    clouds_percent = clouds['all']

    try:
        if backup_api['rain']:
            rain = backup_api['rain']
            rain_lasth = rain['1h']
            rain_presence = 1
    except KeyError:
        rain_presence = 0
        pass

    try:
        if backup_api['snow']:
            snow = backup_api['snow']
            snow_lasth = snow['1h']
            snow_presence = 1
    except KeyError:
        snow_presence = 0
        pass

    unix_datetime = backup_api['dt']
    measure_datetime = time_conversion(unix_datetime)

    img = icon_finder(icon_id)

    icon_result.itemconfig(icon_result_container, image=img)

    city_state_result_label.config(text=f"{weather_city}, {weather_country}")

    main_temperature_rounded = round(main_temperature, 1)
    temp_now_result_label.config(text=f"{main_temperature_rounded}")
    temp_cent_label.config(text=strings[f'{units}_temp_symbol'])

    max_temperature_rounded = round(max_temperature)
    temp_max_result_label.config(text=f"{strings['max_temp']}: {max_temperature_rounded}°C")
    min_temperature_rounded = round(min_temperature)
    temp_min_result_label.config(text=f"{strings['min_temp']}: {min_temperature_rounded}°C")

    desc_result_label.config(text=f"{weather_description.title()}")
    update_result_label.config(text=f"{strings['last_updated']}: {measure_datetime}")

    humidity_result_label.config(text=f"{strings['humidity']}: {main_humidity}%")
    clouds_result_label.config(text=f"{strings['clouds']}: {clouds_percent}%")

    if rain_presence == 1:
        rain_lasth_rounded = round(rain_lasth, 1)
        precipitations_result_label.config(text=f"{strings['precipitations']}: {strings['rain']} ({rain_lasth_rounded} mm)")
    elif snow_presence == 1:
        snow_lasth_rounded = round(snow_lasth, 1)
        precipitations_result_label.config(text=f"{strings['precipitations']}: {strings['snow']} ({snow_lasth_rounded} mm)")
    else:
        precipitations_result_label.config(text=f"{strings['precipitations']}: {strings['no_precipitations']}")
        pass

    wind_speed_rounded = round(wind_speed_kmh)
    if units == "metric":
        wind_result_label.config(text=f"{strings['wind']}: {wind_direction}  {wind_speed_rounded} {strings['wind_speed_metric']}")
    elif units == "imperial":
        wind_result_label.config(text=f"{strings['wind']}: {wind_direction}  {wind_speed_rounded} {strings['wind_speed_imperial']}")

def Search_Weather(event=None):

    global city
    city = city_entry.get()

    units = settings.get('global', 'units')
    lang = settings.get('global', 'lang')

    strings = all_languages[lang]

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}&lang={lang}"

    api_request = requests.get(url)

    api_request_status = api_request.status_code

    if api_request_status == 200:
        with open("src/backup/backup.json", "w") as backup_file:
            json.dump(api_request.json(), backup_file, indent=4)
            backup_file.close()
    elif api_request_status == 400:
        show_error("Nothing to geocode")
        return
    elif api_request_status == 401:
        show_error("Invalid API key")
        return
    elif api_request_status == 404:
        show_error("city not found")
        return
    elif api_request_status == 429:
        show_error("Too many requests")
        return
    else:
        return

    api = json.loads(api_request.content)

    weather = api['weather'][0]
    icon_id = weather['icon']
    weather_main = weather['main']
    weather_description = weather['description']

    weather_city = api['name']

    sys = api['sys']
    weather_country = sys['country']

    weather_timezone = api['timezone']

    main = api['main']
    main_temperature = main['temp']
    max_temperature = main['temp_max']
    min_temperature = main['temp_min']
    main_humidity = main['humidity']

    wind = api['wind']
    wind_speed = wind['speed']
    wind_speed_kmh = wind_speed * 3.6
    wind_degrees = wind['deg']
    wind_direction = deg_to_compass(wind_degrees)

    clouds = api['clouds']
    clouds_percent = clouds['all']

    try:
        if api['rain']:
            rain = api['rain']
            rain_lasth = rain['1h']
            rain_presence = 1
    except KeyError:
        rain_presence = 0
        pass

    try:
        if api['snow']:
            snow = api['snow']
            snow_lasth = snow['1h']
            snow_presence = 1
    except KeyError:
        snow_presence = 0
        pass

    unix_datetime = api['dt']
    measure_datetime = time_conversion(unix_datetime)

    img = icon_finder(icon_id)
    icon_result.itemconfig(icon_result_container, image=img)

    city_state_result_label.config(text=f"{weather_city}, {weather_country}")

    main_temperature_rounded = round(main_temperature, 1)
    temp_now_result_label.config(text=f"{main_temperature_rounded}")
    temp_cent_label.config(text=strings[f'{units}_temp_symbol'])

    max_temperature_rounded = round(max_temperature)
    temp_max_result_label.config(text=f"{strings['max_temp']}: {max_temperature_rounded}{strings[f'{units}_temp_symbol']}")
    min_temperature_rounded = round(min_temperature)
    temp_min_result_label.config(text=f"{strings['min_temp']}: {min_temperature_rounded}{strings[f'{units}_temp_symbol']}")

    desc_result_label.config(text=f"{weather_description.title()}")
    update_result_label.config(text=f"{strings['last_updated']}: {measure_datetime}")

    humidity_result_label.config(text=f"{strings['humidity']}: {main_humidity}%")
    clouds_result_label.config(text=f"{strings['clouds']}: {clouds_percent}%")
    if rain_presence == 1:
        rain_lasth_rounded = round(rain_lasth, 1)
        precipitations_result_label.config(text=f"{strings['precipitations']}: {strings['rain']} ({rain_lasth} mm)")
    elif snow_presence == 1:
        snow_lasth_rounded = round(snow_lasth, 1)
        precipitations_result_label.config(text=f"{strings['precipitations']}: {strings['snow']} ({snow_lasth_rounded} mm)")
    else:
        precipitations_result_label.config(text=f"{strings['precipitations']}: {strings['no_precipitations']}")
        pass
    wind_speed_rounded = round(wind_speed_kmh)
    if units == "metric":
        wind_result_label.config(
            text=f"{strings['wind']}: {wind_direction}  {wind_speed_rounded} {strings['wind_speed_metric']}")
    elif units == "imperial":
        wind_result_label.config(
            text=f"{strings['wind']}: {wind_direction}  {wind_speed_rounded} {strings['wind_speed_imperial']}")

    city_entry.delete("0", tk.END)

def Update_Weather():

    units = settings.get('global', 'units')
    lang = settings.get('global', 'lang')

    strings = all_languages[lang]

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}&lang={lang}"

    api_request = requests.get(url)

    api_request_status = api_request.status_code

    if api_request_status == 200:
        with open("src/backup/backup.json", "w") as backup_file:
            json.dump(api_request.json(), backup_file, indent=4)
            backup_file.close()
    elif api_request_status == 400:
        show_error("Nothing to geocode")
        return
    elif api_request_status == 401:
        show_error("Invalid API key")
        return
    elif api_request_status == 404:
        show_error("city not found")
        return
    elif api_request_status == 429:
        show_error("Too many requests")
        return
    else:
        return

    api = json.loads(api_request.content)

    weather = api['weather'][0]
    icon_id = weather['icon']
    weather_main = weather['main']
    weather_description = weather['description']

    weather_city = api['name']

    sys = api['sys']
    weather_country = sys['country']

    weather_timezone = api['timezone']

    main = api['main']
    main_temperature = main['temp']
    max_temperature = main['temp_max']
    min_temperature = main['temp_min']
    main_humidity = main['humidity']

    wind = api['wind']
    wind_speed = wind['speed']
    wind_speed_kmh = wind_speed * 3.6
    wind_degrees = wind['deg']
    wind_direction = deg_to_compass(wind_degrees)

    clouds = api['clouds']
    clouds_percent = clouds['all']

    try:
        if api['rain']:
            rain = api['rain']
            rain_lasth = rain['1h']
            rain_presence = 1
    except KeyError:
        rain_presence = 0
        pass

    try:
        if api['snow']:
            snow = api['snow']
            snow_lasth = snow['1h']
            snow_presence = 1
    except KeyError:
        snow_presence = 0
        pass

    unix_datetime = api['dt']
    measure_datetime = time_conversion(unix_datetime)

    img = icon_finder(icon_id)
    icon_result.itemconfig(icon_result_container, image=img)

    city_state_result_label.config(text=f"{weather_city}, {weather_country}")

    main_temperature_rounded = round(main_temperature, 1)
    temp_now_result_label.config(text=f"{main_temperature_rounded}")
    temp_cent_label.config(text=strings[f'{units}_temp_symbol'])

    max_temperature_rounded = round(max_temperature)
    temp_max_result_label.config(text=f"{strings['max_temp']}: {max_temperature_rounded}{strings[f'{units}_temp_symbol']}")
    min_temperature_rounded = round(min_temperature)
    temp_min_result_label.config(text=f"{strings['min_temp']}: {min_temperature_rounded}{strings[f'{units}_temp_symbol']}")

    desc_result_label.config(text=f"{weather_description.title()}")
    update_result_label.config(text=f"{strings['last_updated']}: {measure_datetime}")

    humidity_result_label.config(text=f"{strings['humidity']}: {main_humidity}%")
    clouds_result_label.config(text=f"{strings['clouds']}: {clouds_percent}%")
    if rain_presence == 1:
        rain_lasth_rounded = round(rain_lasth, 1)
        precipitations_result_label.config(text=f"{strings['precipitations']}: {strings['rain']} ({rain_lasth_rounded} mm)")
    elif snow_presence == 1:
        snow_lasth_rounded = round(snow_lasth, 1)
        precipitations_result_label.config(text=f"{strings['precipitations']}: {strings['snow']} ({snow_lasth_rounded} mm)")
    else:
        precipitations_result_label.config(text=f"{strings['precipitations']}: {strings['no_precipitations']}")
        pass
    wind_speed_rounded = round(wind_speed_kmh)
    if units == "metric":
        wind_result_label.config(
            text=f"{strings['wind']}: {wind_direction}  {wind_speed_rounded} {strings['wind_speed_metric']}")
    elif units == "imperial":
        wind_result_label.config(
            text=f"{strings['wind']}: {wind_direction}  {wind_speed_rounded} {strings['wind_speed_imperial']}")

def OpenInfo():
    Settings = tk.Toplevel(root)
    Settings.title(strings['info_title'])
    Settings.geometry("300x250")
    Settings.resizable(False, False)

    # ---- FUNCTIONS ----
    def close_windows():
        Settings.destroy()
        Settings.update()

    def open_webpage(url):
        webbrowser.open_new(url)

    # -- SettingsFrame --
    SettingsFrame = tk.Frame(Settings)
    SettingsFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    # -- SettingsTabFrame --
    SettingsTabFrame = tk.Frame(SettingsFrame)
    SettingsTabFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    # -- SettingsTabs --
    SettingsTab = ttk.Notebook(SettingsTabFrame)

    # -- PreferencesTab --
    PreferencesTab = ttk.Frame(SettingsTab)

    # -- InfoTab --
    InfoTab = ttk.Frame(SettingsTab)

    # -- InfoLabelFrame --
    InfoLabelFrame = tk.Frame(InfoTab)
    InfoLabelFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    # LogoTitleFrame
    LogoTitleFrame = tk.Frame(InfoLabelFrame)
    LogoTitleFrame.pack(fill=tk.X, side=tk.TOP, anchor=tk.N, padx=5)

    # Logo
    load = Image.open("src/img/cloudy-day.png")
    image = load.resize((50, 50), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(image)
    img_about = tk.Label(LogoTitleFrame, image=render)
    img_about.image = render
    img_about.pack(side=tk.LEFT)

    # TitleLabel
    TitleLabel = tk.Label(LogoTitleFrame, text=strings['info_name'], font=("Arial", 25))
    TitleLabel.pack(side=tk.LEFT, anchor=tk.NW, padx=5, pady=1)

    # SubtitleLabel
    SubtitleLabel = tk.Label(InfoLabelFrame, text=strings['info_name'])
    SubtitleLabel.pack(side=tk.TOP, anchor=tk.NW, padx=10)

    # VersionLabel
    VersionLabel = tk.Label(InfoLabelFrame, text=f"v{version}")
    VersionLabel.pack(side=tk.TOP, anchor=tk.NW, padx=10)

    # P1LabelFrame
    P1LabelFrame = tk.Frame(InfoLabelFrame)
    P1LabelFrame.pack(fill=tk.X, side=tk.TOP, anchor=tk.NW, padx=10)

    # P1Label
    P1Label = tk.Label(P1LabelFrame, text=strings['info_api_usage'])
    P1Label.pack(side=tk.LEFT, anchor=tk.NW)

    # P1Link
    P1Link = tk.Label(P1LabelFrame, text="openweathermap.com", fg="blue", cursor="hand2")
    P1Link.pack(side=tk.LEFT)
    P1font = tk.font.Font(P1Link, P1Link.cget("font"))
    P1font.configure(underline=True)
    P1Link.configure(font=P1font)
    P1Link.bind("<Button-1>", lambda e: open_webpage("https://openweathermap.org/api"))

    # P2LabelFrame
    P2LabelFrame = tk.Frame(InfoLabelFrame)
    P2LabelFrame.pack(fill=tk.X, side=tk.TOP, anchor=tk.NW, padx=10)

    # P2Label
    P2Label = tk.Label(P2LabelFrame, text=strings['info_icons_by'])
    P2Label.pack(side=tk.LEFT, anchor=tk.NW)

    # P2Link
    P2Link = tk.Label(P2LabelFrame, text="Jelle Dekkers", fg="blue", cursor="hand2")
    P2Link.pack(side=tk.LEFT)
    P2font = tk.font.Font(P2Link, P2Link.cget("font"))
    P2font.configure(underline=True)
    P2Link.configure(font=P2font)
    P2Link.bind("<Button-1>", lambda e: open_webpage("https://www.deviantart.com/aj-dekkers/art/JDWI-Jelle-Dekkers-Weather-Icons-862700188"))

    # P3LabelFrame
    P3LabelFrame = tk.Frame(InfoLabelFrame)
    P3LabelFrame.pack(fill=tk.X, side=tk.TOP, anchor=tk.NW, padx=10)

    # P3Link1
    P3Link1 = tk.Label(P3LabelFrame, text="Source", fg="blue", cursor="hand2")
    P3Link1.pack(side=tk.LEFT)
    P3font1 = tk.font.Font(P3Link1, P3Link1.cget("font"))
    P3font1.configure(underline=True)
    P3Link1.configure(font=P2font)
    P3Link1.bind("<Button-1>", lambda e: open_webpage("https://github.com/66Bunz/Weather-Client"))

    # P3Link2
    P3Link2 = tk.Label(P3LabelFrame, text=strings['info_changenotes'], fg="blue", cursor="hand2")
    P3Link2.pack(side=tk.LEFT)
    P3font2 = tk.font.Font(P3Link2, P3Link2.cget("font"))
    P3font2.configure(underline=True)
    P3Link2.configure(font=P3font2)
    P3Link2.bind("<Button-1>", lambda e: open_webpage("https://github.com/66Bunz/Weather-Client/releases"))

    # CopyrightLabel
    CopyrightLabel = tk.Label(InfoLabelFrame, text=f"Copyright © {last_major_update} - {author}")
    CopyrightLabel.pack(side=tk.BOTTOM, anchor=tk.NE, padx=10)

    SettingsTab.add(InfoTab, text="Info")
    SettingsTab.pack(expand=1, fill="both")

    # -- SettingsButtonsFrame --
    SettingsButtonsFrame = tk.Frame(SettingsFrame, height=30)
    SettingsButtonsFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=False)

    CloseButton = tk.Button(SettingsButtonsFrame, text=strings['info_close_button'], command=close_windows)
    CloseButton.pack(side=tk.RIGHT, padx=5, pady=2)

global search_query
search_query = tk.StringVar()

# ---------------------------------------------------------------------

# -- MenuBar --
MenuBar = tk.Menu(root)

# FirstMenu
FirstMenu = tk.Menu(MenuBar, tearoff=False)
FirstMenu.add_command(label=strings['menubar-file-exit'], command=CloseWindow)
MenuBar.add_cascade(label=strings['menubar-file'], menu=FirstMenu)

# Settings
SettingsMenu = tk.Menu(MenuBar, tearoff=False)
AppearanceSubmenu = tk.Menu(SettingsMenu, tearoff=False)
AppearanceSubmenu.add_command(label=strings['menubar-settings-themes-light'], command=lambda: set_theme("light_theme"))
AppearanceSubmenu.add_command(label=strings['menubar-settings-themes-dark'], command=lambda: set_theme("dark_theme"))
AppearanceSubmenu.add_command(label=strings['menubar-settings-themes-console'], command=lambda: set_theme("console_theme"))
AppearanceSubmenu.add_command(label=strings['menubar-settings-themes-macos'], command=lambda: set_theme("macos_theme"))
AppearanceSubmenu.add_command(label=strings['menubar-settings-themes-blallo'], command=lambda: set_theme("blallo_theme"))
AppearanceSubmenu.add_command(label=strings['menubar-settings-themes-shock'], command=lambda: set_theme("shock_theme"))
AppearanceSubmenu.add_command(label=strings['menubar-settings-themes-forest'], command=lambda: set_theme("forest_theme"))
AppearanceSubmenu.add_command(label=strings['menubar-settings-themes-eruption'], command=lambda: set_theme("eruption_theme"))
SettingsMenu.add_cascade(label=strings['menubar-settings-themes'], menu=AppearanceSubmenu)
SystemSubmenu = tk.Menu(SettingsMenu, tearoff=False)
SystemSubmenu.add_command(label=strings['menubar-settings-units-metric'], command=lambda: set_unitsystem("metric"))
SystemSubmenu.add_command(label=strings['menubar-settings-units-imperial'], command=lambda: set_unitsystem("imperial"))
SettingsMenu.add_cascade(label=strings['menubar-settings-units'], menu=SystemSubmenu)
LanguageSubmenu = tk.Menu(SettingsMenu, tearoff=False)
LanguageSubmenu.add_command(label=strings['menubar-settings-language-english'], command=lambda: set_language("en"))
LanguageSubmenu.add_command(label=strings['menubar-settings-language-italian'], command=lambda: set_language("it"))
SettingsMenu.add_cascade(label=strings['menubar-settings-language'], menu=LanguageSubmenu)
MenuBar.add_cascade(label=strings['menubar-settings'], menu=SettingsMenu)

# HelpMenu
HelpMenu = tk.Menu(MenuBar, tearoff=False)
HelpMenu.add_command(label=strings['menubar-help-issue'], command=lambda: open_webpage("https://github.com/66Bunz/Weather-Client/issues"))
HelpMenu.add_command(label=strings['menubar-help-developer'], command=lambda: open_webpage(
    "https://github.com/66Bunz/Weather-Client/discussions"))
HelpMenu.add_command(label=strings['menubar-help-feedback'], command=lambda: open_webpage(
    "https://github.com/66Bunz/Weather-Client/discussions"))
HelpMenu.add_separator()
HelpMenu.add_command(label=strings['menubar-help_about'], command=OpenInfo)
MenuBar.add_cascade(label=strings['menubar-help'], menu=HelpMenu)

root.config(menu=MenuBar)

# -- BarFrame --
top_bar = tk.Frame(root, bg=color_bg, height=40)
top_bar.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)
top_bar.pack_propagate(0)

reload_button = tk.Button(top_bar, text=strings['reload_button'], font=("Arial", 10), bd=2, relief=tk.GROOVE, bg=color_button, fg=color_button_text, command=Update_Weather)
reload_button.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

search_button = tk.Button(top_bar, text=strings['search_button'], font=("Arial", 10), bd=2, relief=tk.GROOVE, bg=color_button, fg=color_button_text, command=Search_Weather)
search_button.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)

city_entry = tk.Entry(top_bar, textvariable=search_query, font=("Arial",13), bd=2, justify=tk.LEFT, relief=tk.GROOVE, width=18, bg=color_entry, fg=color_entry_text)
city_entry.bind("<Return>", Search_Weather)
# city_entry.insert(0, ")
city_entry.pack(side=tk.RIGHT, fill=tk.Y, padx=15, pady=5)

# -- MainFrame --
main_frame = tk.Frame(root, bg=color_bg, height=490)
main_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5)
main_frame.pack_propagate(0)

main_infos = tk.Frame(main_frame, bg=color_bg, height=300)
main_infos.pack(side=tk.TOP, fill=tk.X, padx=5)
main_infos.pack_propagate(0)

city_state_result = tk.Frame(main_infos, bg=color_bg, height=50)
city_state_result.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

city_state_result_label = tk.Label(city_state_result, bg=color_bg, fg=color_title, text="City, State", font=("Arial", 40))
city_state_result_label.pack(fill=tk.BOTH)

icon_temp_result = tk.Frame(main_infos, bg=color_bg, height=150, width=310)
icon_temp_result.pack(side=tk.TOP, padx=5, pady=5)

icon_result = tk.Canvas(icon_temp_result, height=150, width=150, bg=color_bg, bd=0, highlightthickness=0, relief="ridge")
icon_result.pack(side=tk.LEFT, padx=5)

img = image_resize(unknown_img)
icon_result_container = icon_result.create_image(75,75, anchor=tk.CENTER, image=img)

temp_result = tk.Frame(icon_temp_result, bg=color_bg, height=150, width=150)
temp_result.pack(side=tk.RIGHT, padx=5)

temp_now_result = tk.Frame(temp_result, bg=color_bg, height=100, width=100)
temp_now_result.pack(side=tk.TOP, anchor=tk.NW)

temp_now_result_label = tk.Label(temp_now_result, bg=color_bg, fg=color_title, text="##", font=("Arial", 60))
temp_now_result_label.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.BOTH)

temp_cent_label = tk.Label(temp_now_result, bg=color_bg, fg=color_text, text=strings[f'{units}_temp_symbol'], font=("Arial", 40))
temp_cent_label.pack(side=tk.LEFT, anchor=tk.N, fill=tk.BOTH)

temp_maxmin_result = tk.Frame(temp_result, bg=color_bg, height=50, width=150)
temp_maxmin_result.pack(side=tk.LEFT)

temp_max_result_label = tk.Label(temp_maxmin_result, bg=color_bg, fg=color_text, text="Max temperature: ##°C", font=("Arial", 12))
temp_max_result_label.pack(fill=tk.BOTH)

temp_min_result_label = tk.Label(temp_maxmin_result, bg=color_bg, fg=color_text, text="Min temperature: ##°C", font=("Arial", 12))
temp_min_result_label.pack(fill=tk.BOTH)

desc_result = tk.Frame(main_infos, bg=color_bg, height=50, width=400)
desc_result.pack(side=tk.TOP, fill=tk.Y, padx=5, pady=5)
desc_result.pack_propagate(0)

desc_result_label = tk.Label(desc_result, text="Weather conditions", font=("Arial", 30), bg=color_bg, fg=color_title)
desc_result_label.pack(fill=tk.Y)

secondary_infos = tk.Frame(main_frame, bg=color_bg, height=125)
secondary_infos.pack(side=tk.TOP, fill=tk.BOTH, padx=5)
secondary_infos.pack_propagate(0)

secondary_infos.columnconfigure(0, weight=1)
secondary_infos.columnconfigure(1, weight=1)
secondary_infos.columnconfigure(2, weight=1)
secondary_infos.columnconfigure(3, weight=1)

humidity_result = tk.Frame(secondary_infos, bg=color_bg, height=115, width=255)
humidity_result.grid(column=0, row=0, padx=5)

humidity_result_label = tk.Label(humidity_result, bg=color_bg, fg=color_text, text="Humidity: ##%", font=("Arial", 12))
humidity_result_label.pack(padx=5)

clouds_result = tk.Frame(secondary_infos, bg=color_bg, height=115, width=255)
clouds_result.grid(column=1, row=0, padx=5)

clouds_result_label = tk.Label(clouds_result, bg=color_bg, fg=color_text, text="Clouds: #%", font=("Arial", 12))
clouds_result_label.pack(padx=5)

precipitations_result = tk.Frame(secondary_infos, bg=color_bg, height=115, width=255)
precipitations_result.grid(column=2, row=0, padx=5)

precipitations_result_label = tk.Label(precipitations_result, bg=color_bg, fg=color_text, text="Precipitations: #", font=("Arial", 12))
precipitations_result_label.pack(padx=5)

wind_result = tk.Frame(secondary_infos, bg=color_bg, height=115, width=255)
wind_result.grid(column=3, row=0, padx=5)

wind_result_label = tk.Label(wind_result, bg=color_bg, fg=color_text, text="Wind: # #", font=("Arial", 12))
wind_result_label.pack(padx=5)

update_result = tk.Frame(main_frame, bg=color_bg, height=20, width=400)
update_result.pack(side=tk.BOTTOM, fill=tk.Y, padx=5)
update_result.pack_propagate(0)

update_result_label = tk.Label(update_result, text="Last updated: ##/##/## ##:##:##", font=("Arial", 10), bg=color_bg, fg=color_subtext)
update_result_label.pack(fill=tk.Y)

get_backup_data()
root.mainloop()




# TODO: fare checker online per aggiornamenti (guarda releases github)

