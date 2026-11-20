#!/usr/bin/env python3
"""闰年判断工具：不带参数时检查当前年份，也可以指定一个或多个年份。"""
from __future__ import annotations

import argparse
import datetime


def is_leap(year: int) -> bool:
    """公历闰年规则：能被 4 整除，但不能被 100 整除；能被 400 整除的除外。"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def parse_year(text: str) -> int:
    try:
        year = int(text)
    except ValueError:
        raise argparse.ArgumentTypeError(f"不是有效年份: {text!r}")
    if not 1 <= year <= 9999:
        raise argparse.ArgumentTypeError(f"年份需在 1-9999 之间: {year}")
    return year


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("years", nargs="*", type=parse_year, help="要检查的年份，缺省为当前年份")
    parser.add_argument("-q", "--quiet", action="store_true", help="只输出 yes / no")
    args = parser.parse_args(argv)

    years = args.years or [datetime.date.today().year]
    for year in years:
        leap = is_leap(year)
        if args.quiet:
            print("yes" if leap else "no")
        else:
            print(f"{year} {'是' if leap else '不是'}闰年")

    # 全部为闰年时退出码为 0，否则为 1，方便在脚本里直接判断
    return 0 if all(is_leap(y) for y in years) else 1


if __name__ == "__main__":
    raise SystemExit(main())