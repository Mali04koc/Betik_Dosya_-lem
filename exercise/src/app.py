from src.dosya_islemleri import read_csv, write_json, write_text
from src.processing import stats, build_report, clean_records
from pathlib import Path
def main():
    base = Path(__file__).resolve().parent.parent / "data"
    read_doc = str(base / "people.csv")
    cleaned_json = str(base / "cleaned_records.json")
    write_doc = str(base / "stats.json")
    write_txt = str(base / "report.txt")

    #Oku
    rows = read_csv(read_doc)
    # Temizle
    cleaned = clean_records(rows)
    # İstatistik
    st = stats(cleaned)

    # Çıktılar
    write_json(cleaned_json, cleaned)
    write_json(write_doc, st)
    write_text(write_txt, build_report(st))
    print("bitti")

if __name__=="__main__":
    main()