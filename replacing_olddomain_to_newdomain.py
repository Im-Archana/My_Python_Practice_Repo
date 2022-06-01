def replacing_old_domain(email,old_domain,new_domain):
    if "@"+old_domain in email:
        index=email.index("@"+old_domain)
        new_email=email[:index]+"@"+new_domain
        return new_email
    return email
email=input("What's your old mail id?")
old_domain="gmail.com"
new_domain="google.com"

print("Your new email id is:" +str(replacing_old_domain(email,old_domain,new_domain)))
