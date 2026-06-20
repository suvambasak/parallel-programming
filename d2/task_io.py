import requests


def fetch_from_url(url: str) -> str:
    response = requests.get(url)
    assert response.ok
    return response.text


def save_content(id: int, url: str) -> None:
    print(f"Requesting URL: {id}")

    content = fetch_from_url(url)

    print(f"Saving content: {id}")
    with open(f"{id + 1}.txt", "w") as f:
        f.write(content)


if __name__ == "__main__":
    urls = [
        # Year 2020
        "https://wdc.kugi.kyoto-u.ac.jp/dst_final/202001/dst2001.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_final/202002/dst2002.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_final/202003/dst2003.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_final/202004/dst2004.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_final/202005/dst2005.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_final/202006/dst2006.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_final/202007/dst2007.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_final/202008/dst2008.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_final/202009/dst2009.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_final/202010/dst2010.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_final/202011/dst2011.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_final/202012/dst2012.for.request",
        # Year 2021
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202101/dst2101.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202102/dst2102.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202103/dst2103.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202104/dst2104.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202105/dst2105.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202106/dst2106.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202107/dst2107.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202108/dst2108.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202109/dst2109.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202110/dst2110.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202111/dst2111.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202112/dst2112.for.request",
        # Year 2022
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202201/dst2201.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202202/dst2202.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202203/dst2203.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202204/dst2204.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202205/dst2205.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202206/dst2206.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202207/dst2207.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202208/dst2208.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202209/dst2209.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202210/dst2210.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202211/dst2211.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202212/dst2212.for.request",
        # Year 2023
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202301/dst2301.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202302/dst2302.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202303/dst2303.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202304/dst2304.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202305/dst2305.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202306/dst2306.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202307/dst2307.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202308/dst2308.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202309/dst2309.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202310/dst2310.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202311/dst2311.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202312/dst2312.for.request",
        # Year 2024
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202401/dst2401.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202402/dst2402.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202403/dst2403.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202404/dst2404.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202405/dst2405.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202406/dst2406.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202407/dst2407.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202408/dst2408.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202409/dst2409.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202410/dst2410.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202411/dst2411.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202412/dst2412.for.request",
        # Year 2025
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202501/dst2501.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202502/dst2502.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202503/dst2503.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202504/dst2504.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202505/dst2505.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202506/dst2506.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202507/dst2507.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202508/dst2508.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202509/dst2509.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202510/dst2510.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202511/dst2511.for.request",
        "https://wdc.kugi.kyoto-u.ac.jp/dst_provisional/202512/dst2512.for.request",
    ]

    for idx, url in enumerate(urls):
        save_content(idx, url)
