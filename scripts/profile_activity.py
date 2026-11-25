"""Refresh the profile cards from GitHub's public account and contribution calendar."""

import json
import re
from calendar import isleap
from datetime import date, datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET


USER = "Ayushcv-46"
ASSETS = Path(__file__).resolve().parents[1] / "assets" / "activity"
DAY = timedelta(days=1)
INK, PAPER, GOLD, TEAL = "#102c3c", "#fff4db", "#ffc363", "#71dfcb"


def fetch(url):
    request = Request(url, headers={"User-Agent": "Ayushcv-46-profile", "Accept-Language": "en"})
    with urlopen(request, timeout=30) as response:
        return response.read().decode()


class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dates = {}
        self.tips = {}
        self.active = None
        self.summary = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "td" and "data-date" in attrs:
            self.dates[attrs["id"]] = date.fromisoformat(attrs["data-date"])
        if tag == "tool-tip":
            self.active = attrs.get("for")
        if tag == "h2" and attrs.get("id") == "js-contribution-activity-description":
            self.active = "summary"

    def handle_data(self, data):
        if self.active == "summary":
            self.summary += data
        elif self.active:
            self.tips[self.active] = self.tips.get(self.active, "") + data

    def handle_endtag(self, tag):
        if tag in ("tool-tip", "h2"):
            self.active = None


def year_counts(year, today):
    url = f"https://github.com/users/{USER}/contributions?from={year}-01-01&to={year}-12-31"
    parser = CalendarParser()
    parser.feed(fetch(url))
    counts = {}
    for key, day in parser.dates.items():
        if day.year != year or day > today:
            continue
        value = re.match(r"(No|[\d,]+) contributions? on ", parser.tips[key].strip())
        if not value or day in counts:
            raise ValueError(f"Unexpected contribution data for {day}")
        number = value[1].replace(",", "")
        counts[day] = 0 if number == "No" else int(number)
    length = today.timetuple().tm_yday if year == today.year else 365 + isleap(year)
    summary = re.search(r"([\d,]+)\s+contributions?\s+in\s+" + str(year), parser.summary)
    if len(counts) != length or not summary or sum(counts.values()) != int(summary[1].replace(",", "")):
        raise ValueError(f"Incomplete calendar or mismatched yearly total for {year}")
    return counts


def streaks(counts, today):
    run = longest = 0
    for day in sorted(counts):
        run = run + 1 if counts[day] else 0
        longest = max(longest, run)
    end = today if counts[today] else today - DAY
    current = 0
    while counts.get(end, 0):
        current += 1
        end -= DAY
    return current, longest


def label(x, y, value, size, color=PAPER, family="Arial, sans-serif", extra=""):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" {extra}>{value}</text>'


def frame(title, description, background, contents):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="354" height="183" viewBox="0 0 354 183" role="img">
  <title>{title}</title><desc>{description}</desc>
  <rect width="354" height="183" fill="{background}"/>
  {contents}
</svg>
"""


def cards(account, counts, today):
    # Twelve Monday-starting weeks, including this week's partial interval.
    monday = today - timedelta(days=today.weekday() + 77)
    weeks = [sum(counts.get(monday + timedelta(days=i * 7 + n), 0) for n in range(7)) for i in range(12)]
    peak = max(max(weeks), 1)
    bars = []
    for i, value in enumerate(weeks):
        height = max(1, round(34 * value / peak))
        color = GOLD if i == 11 else TEAL
        bars.append(f'<rect x="{21 + i * 26}" y="{141 - height}" width="19" height="{height}" fill="{color}"><title>{monday + timedelta(weeks=i)}: {value} contributions</title></rect>')
    repo_count = account["public_repos"]
    active_days = sum(v > 0 for k, v in counts.items() if today - timedelta(days=365) < k <= today)
    stats = (
        label(20, 26, "GITHUB ACTIVITY", 13, TEAL, "monospace", 'letter-spacing="2"')
        + label(333, 26, today.isoformat(), 12, PAPER, "monospace", 'text-anchor="end"')
        + label(20, 71, repo_count, 38, PAPER, "Georgia, serif")
        + label(181, 71, active_days, 38, PAPER, "Georgia, serif")
        + label(20, 91, "Public repositories", 14)
        + label(181, 91, "Active days / 365", 14)
        + "".join(bars)
        + label(20, 165, "Contributions by week · last 12 weeks", 13)
    )
    current, longest = streaks(counts, today)
    total = sum(counts.values())
    streak = label(20, 26, "CONTRIBUTION STREAKS", 13, INK, "monospace", 'letter-spacing="2"')
    for y, name, number in [(69, "Total Contributions", f"{total:,}"), (111, "Current Streak", f"{current} days"), (153, "Longest Streak", f"{longest} days")]:
        streak += label(20, y, name, 17, INK)
        streak += label(333, y, number, 25, INK, "Georgia, serif", 'text-anchor="end"')
        streak += f'<path d="M20 {y+10}H333" stroke="#cdbd9d"/>'
    desc = f"{USER}, through {today} UTC."
    return {
        "github.svg": frame("GitHub activity", f"{desc} {repo_count} public repositories. {active_days} active days in the last year. Weekly totals: {', '.join(map(str, weeks))}.", INK, stats),
        "streak.svg": frame("Contribution streaks", f"{desc} {total} total contributions. Current streak {current} days. Longest streak {longest} days.", PAPER, streak),
    }


def main():
    account = json.loads(fetch(f"https://api.github.com/users/{USER}"))
    if account["login"] != USER:
        raise ValueError("Unexpected GitHub account")
    today = datetime.now(timezone.utc).date()
    counts = {}
    for year in range(date.fromisoformat(account["created_at"][:10]).year, today.year + 1):
        counts.update(year_counts(year, today))
    result = cards(account, counts, today)
    for svg in result.values():
        ET.fromstring(svg)
    ASSETS.mkdir(parents=True, exist_ok=True)
    for name, svg in result.items():
        (ASSETS / name).write_text(svg, encoding="utf-8")
    print(f"{USER} · {today} · {sum(counts.values())} contributions · current/longest {streaks(counts, today)}")


if __name__ == "__main__":
    main()
