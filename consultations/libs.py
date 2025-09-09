from bs4 import BeautifulSoup

def remove_watermark(content):
    if content:
        soup = BeautifulSoup(content, "html.parser")
        
        # البحث عن الفقرة التي تحتوي على data-f-id="pbf"
        for p in soup.find_all("p", attrs={"data-f-id": "pbf"}):
            p.decompose()  # إزالة العنصر بالكامل
        
        # تحديث المحتوى بعد التنظيف
        content = str(soup)
        return content
