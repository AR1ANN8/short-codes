user_name = 'arian.nb'
password_ = '1234'
user_name_ = input("نام کاربری خود را وارد کنید:")
password = input("رمز عبور خود را وارد کنید:")
if user_name_ != user_name or password_ != password:
    print("نام کاربری یا رمز عبور صحیح نمی باشد")
else:
    book_store = {
    'ساراماگو': 'کوری',
    'دیل کارنگی': 'آیین زندگی',
    'چارلز داروین': 'منشا انواع',
    'مارگارت میشل': 'بر باد رفته'
}
while True:
    print("1. موجودی")
    print("2. امانت")
    print("3. بازگشت")
    print("4. خروج")
    user_choice = input(":انتخاب")
    if user_choice == '1':
        print(book_store)
    elif user_choice == '2':
        print(book_store)
        requested_book = input("نام کتاب مورد نظر خود را وارد کنید:")
        if requested_book == 'ساراماگو':
            print(book_store['ساراماگو'])
            print(book_store['دیل کارنگی'], book_store['چارلز داروین'], book_store['مارگارت میشل'])
        elif requested_book == 'دیل کارنگی':
            print(book_store['دیل کارنگی'])
            print(book_store['ساراماگو'], book_store['چارلز داروین'], book_store['مارگارت میشل'])
        elif requested_book == 'چارلز داروین':
            print(book_store['چارلز داروین'])
            print(book_store['ساراماگو'], book_store['دیل کارنگی'], book_store['مارگارت میشل'])
        elif requested_book == 'مارگارت میشل':
            print(book_store['مارگارت میشل'])
            print(book_store['ساراماگو'], book_store['دیل کارنگی'], book_store['چارلز داروین'])
    elif user_choice == '3':
            return_book = input("نام کتاب مورد نظر خودرا جهت بازگرداندن کتاب وارد کنید:")
            if return_book == 'ساراماگو':
                print(book_store['ساراماگو'], book_store['دیل کارنگی'], book_store['چارلز داروین'], book_store['مارگارت میشل'])
            elif return_book == 'دیل کارنگی':
                print(book_store['ساراماگو'] ,book_store['دیل کارنگی'] ,book_store['چارلز داروین'], book_store['مارگارت میشل'])
            elif return_book == 'چارلز داروین':
                print(book_store['ساراماگو'], book_store['دیل کارنگی'], book_store['چارلز داروین'] ,book_store['مارگارت میشل'])
            elif return_book =='مارگارت میشل':
                print(book_store['ساراماگو'], book_store['دیل کارنگی'], book_store['چارلز داروین'], book_store['مارگارت میشل'])
    else:
        if user_choice == '4':
                    print("خدانگهدار")
                    break

from datetime import datetime
alarm_hour = int(input("enter hour:"))
alarm_minute = int(input("enter minute:"))
while True:
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    if hour == alarm_hour and minute == alarm_minute:
        print("wake up")
        break

for i in range(1 ,10):
    for j in range(1 ,10):
        print(f'{i} * {j}')

