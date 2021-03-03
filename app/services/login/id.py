class LoginId:
    """Order is fixed for each class variable. It is define in below format
        ({Html Element Identifier Value},{Method to access html identifier})
    """
    EMAIL = (r'/html/body/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/input',)
    PASSWORD = (r'/html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/input',)
    AGREEBUTTON= (r'/html/body/div[2]/div[2]/div/div[2]/div[2]/div[4]/input',)
    LOGINSUBMIT = (r'/html/body/div[2]/div[2]/div/div[2]/div[2]/button', )