print("please enter your current altitude")
cur_altitude=input()

if int(cur_altitude)>=10000:
    print('please go around ')
elif int(cur_altitude)<5000:
    print('land the plain by bringing it to 1000ft')
else:
    print('get Down')