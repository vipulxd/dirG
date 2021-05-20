import sys
import requests


print("     ")

print("""*****************************************************************""")
print("""******************Scripted By @marcrove**************************""")
print("""*****************************************************************""")
print("""*******dirG helps make pentester's list simple asf***************""")


def check_for_dir(dir_name, site_url):

    try:

        response = requests.request("GET", site_url + "/" + dir_name, verify=True)

        if response.status_code == 200:
            result_print(dir_name)
        else:
            pass

    except:
        print(" Specify protocol http or https")
        exit()


def result_print(dir_name):

    display_message = "/{0} Status Code: {1}"
    print(display_message.format(dir_name, 200))


if len(sys.argv) > 2:

    local_file = sys.argv[1]
    site_url = str(sys.argv[2])
    file = open(local_file, "r")

    # this is to grab the  first word form  the wordlist
    for line in file:
        dir = list((line.split()))
        for i in range(len(dir)):

            check_for_dir(dir[i], site_url)


else:
    print("Usage: python3 dirG.py _location_to_wordlist http://www.site.com")
exit()
