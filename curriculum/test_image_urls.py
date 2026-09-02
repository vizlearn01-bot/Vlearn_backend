import requests
import time

urls = [
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/City_Market_in_Nairobi.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/4/4f/Nairobi%27s_Central_Business_District_Landmark_Skyscrapers..jpg",
    "https://upload.wikimedia.org/wikipedia/commons/7/77/CBK_Nairobi_1973.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/e/eb/Kenyan_Samburu_children_in_a_classroom.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/9/96/Nairobi_City_Market%2C_2025_%2801%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/4/48/Nairobi_City_Market%2C_2025_%2803%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/8/82/Nairobi_Skyline_Savannah_Kenya_May19_R1600687.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/b/b3/Kenya_Office_Work.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/b/be/Jua_Kali_cooking_pots.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/7/7a/Maasai_Market-Nairobi.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/f/fa/Tea_farming_in_Kericho_09.JPG",
    "https://upload.wikimedia.org/wikipedia/commons/d/d1/Bank_House_%28Nairobi%29%2C_2025_%2801%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/1/14/Central_Bank_of_Kenya.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/4/40/M-PESA_mobile_money_and_Equity_agent%2C_Nairobi%2C_Kenya.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/0/06/Students_at_Shimo_la_Tewa_Secondary_School.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/0/02/Women_smallholder_farmers_in_Kenya.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/0/06/Fruits_Vendor_Kenya.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/4/48/Market_Kenya.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/e/e7/Credit_Tojo_Andrianarivo_Safari_Doctors.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/0/06/Korea_Kenya_Business_Partnership_03_%2827531512245%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/e/e2/Kenya_Medical_Training_College_Karen_Campus_entrance.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/2/2d/Korea_Kenya_Business_Partnership_02_%2826923130753%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/6/60/Aerial_view_of_the_Nairobi_skyline_from_the_KICC_roof.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/6/61/Express_passenger_train_on_the_Mombasa_-_Nairobi_Standard_Gauge_Railway.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg",
]

headers = {
    'User-Agent': 'VLearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa) python-requests/2.31'
}

for u in urls:
    try:
        r = requests.head(u, headers=headers, timeout=5, allow_redirects=True)
        if r.status_code == 200:
            print(f"[OK 200] {u.split('/')[-1]}")
        else:
            r2 = requests.get(u, headers=headers, timeout=5, stream=True)
            print(f"[{r2.status_code}] {u.split('/')[-1]}")
    except Exception as e:
        print(f"[ERR] {u.split('/')[-1]}: {e}")
    time.sleep(0.1)
