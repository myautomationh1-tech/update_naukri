class ProfileLocators:
    button_complete_profile_xpath = "//a[@href='/mnjuser/profile']"
    resume_headline_xpath = "//span[@class='widgetTitle typ-16Bold' and contains(text(),'Resume headline')]"
    edit_icon_resume_headline = "//span[text()='Resume headline']/following-sibling::span[contains(@class,'edit')]"
    input_field_xpath = "//textarea[@id='resumeHeadlineTxt']"
    save_button_xpath = "//button[@class='btn-dark-ot' and @type='submit']"