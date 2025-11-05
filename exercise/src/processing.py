from .dekorator import required_columns


@required_columns({"name", "age", "city"})
def clean_records(rows: list[dict]) -> list[dict]:
    cleaned: list[dict] = []
    for r in rows:
        name = (r.get("name") or "").strip()
        age_raw = (r.get("age") or "").strip()
        city = (r.get("city") or "").strip()

        if not age_raw.isdigit():
            continue
        age = int(age_raw)
        cleaned.append({"name": name, "age": age, "city": city})
    return cleaned


@required_columns({"name", "age", "city"})
def stats(rows: list[dict]) -> dict:
    if not rows:
        return {"count": 0, "avg_age": 0, "by_city": {}}
    ages = [int(r["age"]) for r in rows if str(r["age"]).strip() != ""]
    by_city: dict[str, int] = {}
    for r in rows:
        c = r["city"]
        by_city[c] = by_city.get(c, 0) + 1
    avg = sum(ages) / len(ages) if ages else 0
    return {"count": len(rows), "avg_age": avg, "by_city": by_city}


def build_report(st: dict) -> str:
    lines: list[str] = []
    lines.append("Rapor")
    lines.append("")
    lines.append(f"Geçerli kayıt sayısı: {st.get('count', 0)}")
    lines.append(f"Ortalama yaş: {st.get('avg_age', 0)}")
    lines.append("Şehir dağılımı:")
    for c, n in st.get("by_city", {}).items():
        lines.append(f"- {c}: {n}")
    return "\n".join(lines) + "\n"
