"""CLI interface for Google Drive API access."""

import argparse
import json

from auth import get_credentials
import client


def cmd_list(args):
    creds = get_credentials()
    files = client.list_files(creds, page_size=args.limit)
    print(json.dumps(files, indent=2))


def cmd_folder(args):
    creds = get_credentials()
    files = client.list_files_in_folder(creds, args.folder, page_size=args.limit)
    print(json.dumps(files, indent=2))


def cmd_search(args):
    creds = get_credentials()
    files = client.search_files(creds, args.search, page_size=args.limit)
    print(json.dumps(files, indent=2))


def cmd_download(args):
    creds = get_credentials()
    client.download_file(creds, args.file_id, args.output)
    print(f"Downloaded to {args.output}")


def cmd_info(args):
    creds = get_credentials()
    meta = client.get_file_metadata(creds, args.file_id)
    print(json.dumps(meta, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Google Drive API CLI")
    parser.add_argument("--limit", type=int, default=10, help="Max results to return")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true", dest="list_files", help="List top-level files")
    group.add_argument("--folder", type=str, help="List files in a folder by ID")
    group.add_argument("--search", type=str, help="Search files by name")
    group.add_argument("--info", type=str, metavar="FILE_ID", help="Get file metadata")
    group.add_argument("--download", type=str, metavar="FILE_ID", help="Download a file by ID")

    parser.add_argument("--output", type=str, metavar="PATH", help="Output path for --download")

    args = parser.parse_args()

    if args.list_files:
        cmd_list(args)
    elif args.folder:
        cmd_folder(args)
    elif args.search:
        cmd_search(args)
    elif args.info:
        args.file_id = args.info
        cmd_info(args)
    elif args.download:
        if not args.output:
            parser.error("--download requires --output PATH")
        args.file_id = args.download
        cmd_download(args)


if __name__ == "__main__":
    main()
