import os
import sys
from ever2simple.converter import EverConverter
import argparse


def main():
    parser = argparse.ArgumentParser(prog=None,
            description="Convert Evernote.enex files to Markdown",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('enex_file', help="the path to the Evernote.enex file")
    parser.add_argument('-o', '--output',
            help="the path to the output file or directory, omit to output to the terminal (stdout)")
    parser.add_argument('-f', '--format',
            help="the output format, json, csv or a directory",
            choices=['json', 'csv', 'dir'], default='json')
    parser.add_argument('-m', '--metadata',
            help="For directory output only. Specify the metadata you\
            would like to add on top of the markdown file. Valid options are\
            'all', 'title', 'created', and 'keywords'. Default is 'all'. You can\
            specify this argument multiple times, by which you can also control\
            the order in which metadata lines are printed.\
            Metadata is printed in MultiMarkdown format.",
            choices=['all', 'title', 'date', 'keywords'],
            action='append')
    
    args = parser.parse_args()
    filepath = os.path.expanduser(args.enex_file)
    if not os.path.exists(filepath):
        print('File does not exist: {}'.format(filepath))
        sys.exit(1)
    converter = EverConverter(filepath, args.output, args.format, args.metadata)
    converter.convert()
    sys.exit()


if __name__ == '__main__':
    main()
