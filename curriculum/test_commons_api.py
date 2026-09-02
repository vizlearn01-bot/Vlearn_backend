import requests
import time

def verify_commons_file(filename):
    api_url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": f"File:{filename}",
        "prop": "imageinfo",
        "iiprop": "url|mime|size|extmetadata",
        "format": "json"
    }
    headers = {
        "User-Agent": "VLearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa)"
    }
    try:
        r = requests.get(api_url, params=params, headers=headers, timeout=10)
        data = r.json()
        pages = data.get("query", {}).get("pages", {})
        for page_id, page in pages.items():
            if page_id == "-1":
                return None, f"File:{filename} not found on Wikimedia Commons"
            imageinfo = page.get("imageinfo", [{}])[0]
            direct_url = imageinfo.get("url")
            return direct_url, page.get("title")
    except Exception as e:
        return None, str(e)

test_files = [
    "City_Market_in_Nairobi.jpg",
    "Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
    "Nairobi's_Central_Business_District_Landmark_Skyscrapers..jpg",
    "CBK_Nairobi_1973.jpg",
    "Analyzing_Financial_Data_(5099605109).jpg",
    "Kenyan_Samburu_children_in_a_classroom.jpg",
    "Tea_farming_in_Kericho_09.JPG",
    "Bank_House_(Nairobi),_2025_(01).jpg",
    "Central_Bank_of_Kenya.jpg",
    "M-PESA_mobile_money_and_Equity_agent,_Nairobi,_Kenya.jpg",
    "Students_at_Shimo_la_Tewa_Secondary_School.jpg",
    "Jua_Kali_cooking_pots.jpg",
    "Maasai_Market-Nairobi.jpg",
    "Women_smallholder_farmers_in_Kenya.jpg",
    "Fruits_Vendor_Kenya.jpg",
    "Market_Kenya.jpg",
    "Credit_Tojo_Andrianarivo_Safari_Doctors.jpg",
    "Korea_Kenya_Business_Partnership_03_(27531512245).jpg",
    "Korea_Kenya_Business_Partnership_02_(26923130753).jpg",
    "Kenya_Medical_Training_College_Karen_Campus_entrance.jpg",
    "Jua_Kali_fabricator.jpg"
]

print("Verifying via Wikimedia API:")
for f in test_files:
    url, title = verify_commons_file(f)
    print(f"[{'FOUND' if url else 'MISSING'}] {f} -> {url}")
    time.sleep(0.1)
