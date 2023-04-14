#%%
#get user email address

email=input("What is your email address?: ")

#slice out user name

user=email[:email.index("@")]

#slicer domain name

domain=email[email.index("@")+1 :]

#format message
output="your username is {} and your domain name is {}".format(user,domain)

#display output message
print(output)

# %%
