import requests
def status():
    respond_fb = requests.get("https://www.facebook.com/")
    if respond_fb.status_code == 200:
        print("The page has been loaded successfully")
    elif respond_fb.status_code == 400:
        print("Something has gone wrong, please try again later")
    elif respond_fb.status_code == 404:
        print("Error 404 - Oops something went wrong")
    else:
        pass

#second iteration
# if post_codes_req.status_code:
#     print(" success")
# elif post_codes_req.status_code:
#