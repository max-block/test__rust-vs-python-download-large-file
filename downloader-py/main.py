from tqdm import tqdm
import requests


def main():
    url = "https://releases.ubuntu.com/20.04/ubuntu-20.04.4-desktop-amd64.iso"
    path = "../tmp/python__ubuntu.iso"
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with open(path, 'wb') as file, tqdm(
        desc=path,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


if __name__ == "__main__":
    main()
