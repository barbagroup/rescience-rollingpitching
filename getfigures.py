#! /usr/bin/env python3
"""Download figures from GitHub repository `petibm-rollingpitching`."""

import argparse
import pathlib
import urllib.request


def parse_command_line():
    """Parse the command-line options."""
    formatter_class = argparse.ArgumentDefaultsHelpFormatter
    descr = 'Download figures from GitHub repository based on LaTeX content.'
    parser = argparse.ArgumentParser(description=descr,
                                     formatter_class=formatter_class)
    repo_url = 'https://github.com/barbagroup/petibm-rollingpitching'
    parser.add_argument('--git', dest='repo_url',
                        type=str,
                        default=repo_url,
                        help='URL of the GitHub repository')
    parser.add_argument('--branch', dest='branch',
                        type=str,
                        default='master',
                        help='Git branch to watch')
    parser.add_argument('--outdir', dest='outdir',
                        type=str,
                        default='figures',
                        help='Path of the output directory')
    return parser.parse_args()


def main(args):
    """Download figures from GitHub repository based on LaTeX content."""
    maindir = pathlib.Path(__file__).absolute().parent

    # Get relative path of figures included in LaTeX file.
    figures = []
    texfile = maindir / 'content.tex'
    with open(texfile, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            if line.lstrip().startswith(r'\includegraphics'):
                figures.append(line[line.find('{') + 1:line.find('}')])

    for figure in figures:
        print(f'Downloading {figure} ...')
        figdir = pathlib.Path(args.outdir) / pathlib.Path(figure).parent
        figdir.mkdir(parents=True, exist_ok=True)
        parts = figure.split('/')
        urlpath = '/'.join([args.repo_url, 'raw', args.branch,
                            'runs', *parts[:-1], 'figures', parts[-1]])
        dest = pathlib.Path(args.outdir) / figure
        urllib.request.urlretrieve(urlpath, dest)


if __name__ == '__main__':
    args = parse_command_line()
    main(args)
