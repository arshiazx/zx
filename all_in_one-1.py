print("!!!!این برنامه برای گیم و حساب و هرکاری که فکرش رو میکنید ساخته شده !!!!")
print("برای گیم:game     برای حساب عدد ها و...:hesab      برای بازی سن:sen  ")
y = str(input("کاری که میخواهید انجام دهید را وارد کنید:"))
x = int(input("لطفا عدد مورد نظر خود را وارد کنید:"))
print("راهنما: برای تعیین زوج یا فرد بودن عددی که وارد کردید:A_Z  برای تعیین ارزش مکانی عدد:A_K")
if y == "A_Z":
    a = (x % 10 == 0 or 2 or 4 or 6 or 8)
    if a == True:
        print("عدد شما زوج است ")
    else:
        print("عدد شما فرد است")
a = (x % 10 == 0 or 2 or 4 or 6 or 8)
yekan = x % 10
dahgan = (x// 10) %10
sadgan = (x // 100)% 10
hezrgan = (x // 1000)
if y == 'A_K':
    print("راهنما: یکان:1  دهگان:2  صد گان:3  هزارگان:4 ")
    s = int(input("لطفا با توجه به راهنما عدد مورد نظر را وارد کنید:"))
    if s == 1:
         print(yekan)
    if s == 2:
         print(dahgan)
    if s == 3:
         print(sadgan)
    if s == 4:
         print(hezrgan)
if y == "game":
    import random
    baze = int(input("لطفا یک بازه برای کامپیوتر تعریف کنید:"))
    javab = random.randint(1, baze)
    hads = int(input(["lotfan az 1 ta", baze, 'hads bezanid']))
    while hads != javab:
        if hads > javab:
            print("!!! حدس شما بزرگ تر از عدد انتخوابی کامپیوتر است !!!")
        if hads < javab:
            print("!!! حدس شما کوچک تر از حدس کامپیوتر است!!!")
        hads = int(input(['lotfan az 1 ta', baze, "yeck adady ro hads bezandi:"]))
        if hads == javab:
            print("!!! حدس شما درست است !!!")
if y == "sen":
    while 13 == 13:
        sen = int(input("سنت رو بگو دادا: "))
        if sen < 6 or sen == 6:
            print("شما بچه سال هستید")
        if sen > 6 and sen < 12 or sen == 12:
            print("شما در استانه بزرگ شدن دودول هستید...!!")
        if sen > 12 and sen < 18 or sen == 18:
            print(
                "شما در استانه در امدن از بچه سالی و 3 سانتی شدن ال تناسلی هستید اگر شما عرشیا هستید منظور من 3 سانت تو رفتگی است..!!!")
        if sen > 18 and sen < 26 or sen == 26:
            print(
                "شما باید به فکر پیدا کردن دوست دختر و سکس باشید البته اگر شما عرشیا هستید بهتره این فکر رو نکنی چون دودولی نداری!!!!!.")
        if sen > 26 and sen < 36 or sen == 36:
            print(
                "شما باید به فکر بچه دار شدن باشید البته اگر شرایط مالی رو داشته باشید (بازهم اشاره کنم اگر شما عرشیا هستید باز هم نمیتونید به این موضوع فکر کنی چون 9 سانتم نداری)")
        if sen > 36 and sen < 42 or sen == 42:
            print("شما قید بچه دار شدن رو بزنید. البته اگر عرشیا هستی تلاش کن شاید 9 سانت شده باشه")
        if sen > 42 and sen < 52 or sen == 52:
            print(
                "شما باید کار هایتان را انجام دهید چون احتمال داره بمیرید . ولی عرشیا جان شما تلاش کن مطما باش 9 سانت میشه")
        if sen > 52 and sen < 62 or sen == 62:
            print("خوش حالم که زنده اید.     عرشیا جان تولد بچت مبارک!!!!")
        if sen > 62 and sen < 72:
            print("بنازم هنوز زنده ای !!!!")
        if sen > 72 and sen < 82:
            print("داداش نمیخوای بمیری ؟؟؟!!! عرشیا جان تولد بچه 2 مبارک")
        if sen > 82 and sen < 102:
            print("الووو بزار یه زنگ بزنم ازراییل")
        if sen == 0:
            break
y = str(input("کاری که میخواهید انجام دهید را وارد کنید:"))
if y == "jam":
    print("جمع و تفرثق کیری و تخمی زیر را حل کنید: ")
    javab = input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:   98+91=")
    if javab == str:
        print("فقط عدد تایپ کن کونی!!!")
    javab2 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:       118+1856="))
    if javab2 == str:
        print("فقط عدد تایپ کن کونی!!!")
    javab3 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:          1376+1111="))
    if javab3 == str:
        print("فقط عدد تایپ کن کونی!!!")
    javab4 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:       1313+1656="))
    if javab4 == str:
        print("فقط عدد تایپ کن کونی!!!")
    javab5 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:            1178+8744="))
    if javab5 == str:
        print("فقط عدد تایپ کن کونی!!!!")
    javab6 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:             1543+6547="))
    if javab6 == str:
        print("فقط عدد تایپ کن کونی!!!")
    javab7 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:                   9806+1123="))
    if javab7 == str:
        print("فقط عدد تایپ کن کونی!!!")
    javab8 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:                      1314+3131="))
    if javab8 == str:
        print("فقط عدد تایپ کن کونی!!!")
    javab9 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:                           1235+4567="))
    if javab9 == str:
        print("فقط عدد تایپ کن کونی!!!")
    javab10 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:                           143433+135566="))
    if javab2 == 1974 and javab == 189 and javab3 == 2487 and javab4 == 2969 and javab5 == 9922 and javab6 == 8090 and javab7 == 10929 and javab8 == 4445 and javab9 == 5802 and javab10 == 278999:
        print('جواب های کیری و تخمی شما درست است ☻☻☻☻☻☻')
    else:
        print("کیرم تو مغزه کص شرت بره جمع هم بلد نیستی انجام بدی???!!!!")
    if javab or javab3 or javab2 or javab4 or javab5 or javab6 or javab7 or javab8 or javab9 or javab10 == 0:
        break
y = str(input("کاری که میخواهید انجام دهید را وارد کنید:"))
while 5 != 0:
    if y == 'A_K':
        print("راهنما: یکان:1  دهگان:2  صد گان:3  هزارگان:4 ")
        print("!!!برای خروج از (0) استفاده کنید!!!")
        s = int(input("لطفا با توجه به راهنما عدد مورد نظر را وارد کنید:"))
        if s == 1:
            print(yekan)
        if s == 2:
            print(dahgan)
        if s == 3:
            print(sadgan)
        if s == 4:
            print(hezrgan)
        if s == 0:
            break
while 10 == 10:
    if y == "A_Z":
        a = (x % 10 == 0 or 2 or 4 or 6 or 8)
        if a == True:
            print("عدد شما زوج است ")
        else:
            print("عدد شما فرد است")
y = str(input("کاری که میخواهید انجام دهید را وارد کنید:"))
while 3 == 3:
    if y == "game":
        import random
        baze = int(input("لطفا یک بازه برای کامپیوتر تعریف کنید:"))
        javab = random .randint(1,baze)
        hads = int(input(["lotfan az 1 ta",baze,'hads bezanid'] ))
        while hads != javab:
            if hads > javab:
                print("!!! حدس شما بزرگ تر از عدد انتخوابی کامپیوتر است !!!")
            if hads < javab:
                print("!!! حدس شما کوچک تر از حدس کامپیوتر است!!!")
            hads = int(input(['lotfan az 1 ta', baze, "yeck adady ro hads bezandi:"]))
            if hads == javab:
                print("!!! حدس شما درست است !!!")
            if hads == 0:
                break
y = str(input("کاری که میخواهید انجام دهید را وارد کنید:"))
while 7 == 7:
    if y == "sen":
        sen = int(input("سنت رو بگو دادا: "))
        if sen < 6 or sen == 6:
            print("شما بچه سال هستید")
        if sen > 6 and sen < 12 or sen == 12:
            print("شما در استانه بزرگ شدن دودول هستید...!!")
        if sen > 12 and sen < 18 or sen == 18:
            print(
                "شما در استانه در امدن از بچه سالی و 3 سانتی شدن ال تناسلی هستید اگر شما عرشیا هستید منظور من 3 سانت تو رفتگی است..!!!")
        if sen > 18 and sen < 26 or sen == 26:
            print(
                "شما باید به فکر پیدا کردن دوست دختر و سکس باشید البته اگر شما عرشیا هستید بهتره این فکر رو نکنی چون دودولی نداری!!!!!.")
        if sen > 26 and sen < 36 or sen == 36:
            print(
                "شما باید به فکر بچه دار شدن باشید البته اگر شرایط مالی رو داشته باشید (بازهم اشاره کنم اگر شما عرشیا هستید باز هم نمیتونید به این موضوع فکر کنی چون 9 سانتم نداری)")
        if sen > 36 and sen < 42 or sen == 42:
            print("شما قید بچه دار شدن رو بزنید. البته اگر عرشیا هستی تلاش کن شاید 9 سانت شده باشه")
        if sen > 42 and sen < 52 or sen == 52:
            print(
                "شما باید کار هایتان را انجام دهید چون احتمال داره بمیرید . ولی عرشیا جان شما تلاش کن مطما باش 9 سانت میشه")
        if sen > 52 and sen < 62 or sen == 62:
            print("خوش حالم که زنده اید.     عرشیا جان تولد بچت مبارک!!!!")
        if sen > 62 and sen < 72:
            print("بنازم هنوز زنده ای !!!!")
        if sen > 72 and sen < 82:
            print("داداش نمیخوای بمیری ؟؟؟!!! عرشیا جان تولد بچه 2 مبارک")
        if sen > 82 and sen < 102:
            print("الووو بزار یه زنگ بزنم ازراییل")
y = str(input("کاری که میخواهید انجام دهید را وارد کنید:"))
while 6 == 6:
    if y == "jam":
        print("جمع و تفرثق کیری و تخمی زیر را حل کنید: ")
        javab = input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:   98+91=")
        if javab == str:
            print("فقط عدد تایپ کن کونی!!!")
        javab2 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:       118+1856="))
        if javab2 == str:
            print("فقط عدد تایپ کن کونی!!!")
        javab3 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:          1376+1111="))
        if javab3 == str:
            print("فقط عدد تایپ کن کونی!!!")
        javab4 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:       1313+1656="))
        if javab4 == str:
            print("فقط عدد تایپ کن کونی!!!")
        javab5 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:            1178+8744="))
        if javab5 == str:
            print("فقط عدد تایپ کن کونی!!!!")
        javab6 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:             1543+6547="))
        if javab6 == str:
            print("فقط عدد تایپ کن کونی!!!")
        javab7 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:                   9806+1123="))
        if javab7 == str:
            print("فقط عدد تایپ کن کونی!!!")
        javab8 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:                      1314+3131="))
        if javab8 == str:
            print("فقط عدد تایپ کن کونی!!!")
        javab9 = int and str(input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:                           1235+4567="))
        if javab9 == str:
            print("فقط عدد تایپ کن کونی!!!")
        javab10 = int and str(
            input("لطفا جمع و تفریق تخمی رو به رو را حل کنید:                           143433+135566="))
        if javab2 == 1974 and javab == 189 and javab3 == 2487 and javab4 == 2969 and javab5 == 9922 and javab6 == 8090 and javab7 == 10929 and javab8 == 4445 and javab9 == 5802 and javab10 == 278999:
            print('جواب های کیری و تخمی شما درست است ☻☻☻☻☻☻')
        else:
            print("کیرم تو مغزه کص شرت بره جمع هم بلد نیستی انجام بدی???!!!!")