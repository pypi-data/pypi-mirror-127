### Title

tribunnews Scraper

### Descrption

* With tribunnews Scraper you can scrape search results and extract the contents produced by the search result.
* In tribunnews scraper it will scrape the data present of the website and give json data which contains the details of the contents on the website.

### JSON sample data
```sh
{
    "Scraper_detail_data": {
        "Tribunnews_com": "11 Oknum Polisi di Tanjungbalai Jual Belasan Kg Sabu Tangkapan ke Gembong Narkoba - Tribunnews.com",
        "black_crimson": "11 Oknum Polisi di Tanjungbalai Jual Belasan Kg Sabu Tangkapan ke Gembong Narkoba",
        "column_12": "Kota Lain",
        "column_3": "Nyambi Jualan Sabu, Pedagang Sayur di Pasar Keputran Ditangkap Polisi, 20 Paket Sabu Disita",
        "column_5": "14 tersangka yang diantaranya 11 bintara sampai perwira Polres Tanjungbalai dilimpahkan ke jaksa Kejari Tanjungbalai Asahan.",
        "feed": "Iklan Untuk AndaUlang tahun ke -110 mendirikan ROLEX - Diskon 90%PRCara menghilangkan lemak perut. -23 kg dalam 2 minggu. ResepPRBosan Botak? Rambut Tumbuh dalam 8 Menit! Baca Segera!PRDiabetes hilang selamanya & pankreas kembali sehat! 100% alamiPRWanita Tua Terkaya Ini Membocorkan Rahasia Kekayaannya! BacaPRNyeri sendi hilang setelah 3 hari: perhatikanPRRecommended by",
        "hide": "Sebanyak 11 oknum polisi di Polres Tanjungbalai, Asahan, Sumatera Utara terlibat kasus narkoba",
        "popIn_recommend_art_title": "Iklan untuk Anda: Diabetes Tipe 2? Lakukan Ini Segera (Tonton)",
        "selected": "Regional",
        "time": "Jumat, 1 Oktober 2021 19:48 WIB",
        "white": "istimewa"
    }
```

[Click Here for more](https://datakund-scraper.s3.amazonaws.com/datakund_87KS297BWOV3PJX_json.json)

### Run Scraper
```sh
from tribunnews_scraper import *
link="https://www.tribunnews.com/lifestyle/2021/10/01/surat-al-mulk-ayat-1-30-dalam-arab-dan-latin-lengkap-beserta-terjemahannya"
data=run_tribunnews_scraper(link)
```

### How it works?
* It takes URL of tribunnews page with a search keyword to scrape the data.
* It generates the json data which contains the information of the tribunnews search result.
* It gives the every detail present inside website in the form of json data.


### Examples
Below are some of the examples of URLs using which you can scrape:

* [Example 1](https://www.tribunnews.com/regional/2021/10/01/11-oknum-polisi-di-tanjungbalai-jual-belasan-kg-sabu-tangkapan-ke-gembong-narkoba)

* [Example2](https://www.tribunnews.com/lifestyle/2021/10/01/surat-al-mulk-ayat-1-30-dalam-arab-dan-latin-lengkap-beserta-terjemahannya)


### Queries/ Feedback
If you have some queries or feedback please contact us at following    
[Telegram](https://t.me/datakund)  
[Email](abhishek@datakund.com)









