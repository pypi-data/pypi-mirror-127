import argparse
import csv
import requests
import subprocess
import sys

from typing import List, Optional
from urllib.parse import urlparse


DOWNLOAD_ATTEMPTS = 3


def download_file(file_url, md5: bytes):
    file_name = file_url.split("/")[-1]
    sys.stdout.write(f"Downloading and verifying {file_name}... ")
    sys.stdout.flush()

    attempts = 1

    while True:
        subprocess.check_output(["wget", file_url], stderr=subprocess.PIPE)
        h = subprocess.check_output(["md5sum", file_name]).split(b" ")[0]

        if h == md5:
            break

        sys.stdout.write(f"\n\thash mismatch: downloaded file hash '{h}' != recorded hash '{md5}'\n")
        attempts += 1
        if attempts > DOWNLOAD_ATTEMPTS:
            sys.stdout.write("VERIFICATION FAILED (MULTIPLE HASH MISMATCH.)\n")
            return

        sys.stdout.write(f"\tretrying (attempt {attempts} of {DOWNLOAD_ATTEMPTS})\n")
        subprocess.check_output(["rm", "-f", file_name])

    sys.stdout.write("done.\n")
    sys.stdout.flush()


def main(args: Optional[List[str]] = None):
    parser = argparse.ArgumentParser(
        description="Utility Python package to download Genome-in-a-Bottle data from their index files.")

    parser.add_argument("index", help="Index file or URL to get data links and hashes from.")

    p_args = parser.parse_args(args or sys.argv[1:])

    index = p_args.index
    index_parts = urlparse(index)

    if index_parts.scheme in ("http", "https", "ftp"):
        if index_parts.netloc == "github.com":
            path_parts = index_parts.path.split("/")
            if path_parts[3] == "blob":  # Non-raw GH content
                index = index_parts.scheme + "://" + index_parts.netloc + \
                    "/".join(path_parts[:3]) + "/raw/" + "/".join(path_parts[4:])

        index_res = requests.get(index, allow_redirects=True)

        if index_res.status_code >= 300:
            print(f"Error: index request returned non-2XX status code: {index_res.status_code}")
            exit(1)

        index_contents = index_res.content.decode("utf-8").split("\n")

    else:
        with open(index, "r") as fh:
            index_contents = fh.read()

    index_reader = csv.DictReader(index_contents, delimiter="\t")

    for row in index_reader:
        if "FASTQ" in row:
            download_file(row["FASTQ"], bytes(row["FASTQ_MD5"], encoding="ascii"))

        if "PAIRED_FASTQ" in row:
            download_file(row["PAIRED_FASTQ"], bytes(row["PAIRED_FASTQ_MD5"], encoding="ascii"))


if __name__ == "__main__":
    main()
