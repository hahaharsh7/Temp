class LoginId:
    """Order is fixed for each class variable. It is define in below format
        ({Html Element Identifier Value},{Method to access html identifier})
    """
    EMAIL = (r'Email','id')
    PASSWORD = (r'//*[@id="Password"]',)
    AGREEBUTTON= (r'//*[@id="home"]/section/div/div/div[1]/form/div[3]/label/input',)
    LOGINSUBMIT = (r'//*[@id="home"]/section/div/div/div[1]/form/div[4]/div/input', )