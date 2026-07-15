import requests
import xml.etree.ElementTree as ET

# EPG havolalari ro'yxati
urls = [
    "https://stream-tv-new-kino.hf.space/epg.xml",
    "https://itvuz-kulgu.hf.space/epg.xml",
    "https://kinostream3-premiera-1.hf.space/epg.xml",
    "https://kinostream3-premiera-2.hf.space/epg.xml",
    "https://stream-tv-hind-movie.hf.space/epg.xml",
    "https://stream-tv-digital.hf.space/epg.xml",
    "https://kinostream4-asil-tv.hf.space/epg.xml",
    "https://kinostream4-asil-tv2.hf.space/epg.xml",
    "https://scottadkins-stream.hf.space/epg.xml",
    "https://scottadkins-uill-smit.hf.space/epg.xml",
    "https://kinostream-jackie-chan.hf.space",
    "https://kinostream-denzel.hf.space/epg.xml",
    "https://kinostream2-tony-jaa.hf.space/epg.xml",
    "https://kinostream2-jason-statham.hf.space/epg.xml"
    

    
]

def merge_epg():
    # Asosiy XML strukturasi
    root = ET.Element("tv", generator_info_name="MergedEPG")
    
    for url in urls:
        print(f"Yuklanmoqda: {url}")
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                # Faylni xotiraga yuklash
                tree = ET.fromstring(response.content)
                # Barcha channel va programme teglari
                for child in tree:
                    root.append(child)
        except Exception as e:
            print(f"Xatolik yuz berdi {url}: {e}")

    # Birlashtirilgan faylni yozish
    tree = ET.ElementTree(root)
    tree.write("merged_epg.xml", encoding="utf-8", xml_declaration=True)
    print("Tayyor: merged_epg.xml fayli yaratildi.")

if __name__ == "__main__":
    merge_epg()
