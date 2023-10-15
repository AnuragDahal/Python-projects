import webbrowser as web  # built in module


def automate():
    # a = "www."
# frequently used websites
    urls = ("google.com", "youtube.com", "github.com",
            "stackoverflow.com", "gmail.com")
    # while True:
    #     url = input("Enter website name you want to open: ")

# open all urls in new tab
    for url in urls:
        web.open_new_tab(url)


automate()
