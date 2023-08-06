#!/bin/python

#
#   fsub is a script for cleaning, editing and fixing a SubRip (.srt) file
#   Copyright (C) 2021  Augusto Lenz Gunsch
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
#   Contact information available in my website: https://augustogunsch.xyz
#

import sys
import argparse
import re
import chardet
import os


class Time:
    def __init__(self, time_str, file_name, line_number):
        parsed_time = time_str.split(':')
        try:
            h = int(parsed_time[0])
            m = int(parsed_time[1])
            ms = int(parsed_time[2].replace(',', ''))
            # self.time: time in milliseconds
            self.time = h * 3600000 + m * 60000 + ms
        except Exception:
            print('Invalid time format detected ({}:{})'
                  .format(file_name, line_number),
                  file=sys.stderr)
            sys.exit(1)

    def add(self, ms):
        self.time += ms

    def __repr__(self):
        ms = self.time % 1000
        s = (self.time % 60000) / 1000
        m = (self.time / 60000) % 60
        h = self.time / 3600000
        return '%02d:%02d:%02d,%03d' % (h, m, s, ms)


class Subtitle:
    def __init__(self, lines, file_name, line_number):
        try:
            # This is mostly ignored, as the subtitles are renumbered later
            self.number = int(lines.pop(0))
        except Exception:
            print('Invalid line number detected ({}:{})'
                  .format(file_name, line_number),
                  file=sys.stderr)
            sys.exit(1)

        line_number += 1

        try:
            time_span = lines.pop(0).split(' --> ')

            self.time_start = Time(time_span[0], file_name, line_number)
            self.time_end = Time(time_span[1], file_name, line_number)
        except Exception:
            print('Invalid time span format detected ({}:{})'
                  .format(file_name, line_number),
                  file=sys.stderr)
            sys.exit(1)

        self.content = lines

    def shift(self, ms):
        self.time_start.add(ms)
        self.time_end.add(ms)

    def matches(self, regexp):
        for line in self.content:
            if regexp.findall(line):
                return True
        return False

    def __repr__(self):
        return '{}\n{} --> {}\n{}'.format(
                self.number,
                self.time_start, self.time_end,
                os.linesep.join(self.content)
        )


def clean(subs, cfg):
    # Read expressions in ~/.config/fsubrc
    if not cfg:
        cfg = open(os.getenv('HOME') + '/.config/fsubrc', 'r')
    lines = re.split(r'\r?\n', cfg.read().strip())
    expressions = list(map(re.compile, lines))
    cfg.close()

    # Cancel if no expression
    if len(expressions) == 0:
        return

    # Remove lines matching any expression
    for regexp in expressions:
        subs = filter(lambda sub: not sub.matches(regexp), subs)

    return list(subs)


def shift(subs, ms):
    for sub in subs:
        sub.shift(ms)
    return list(filter(lambda sub: sub.time_start.time >= 0, subs))


def strip_html(subs):
    for sub in subs:
        for i in range(0, len(sub.content)):
            sub.content[i] = re.sub('<.+>', '', sub.content[i])


def process_file(args, file):
    # Read the input file
    contents = file.read()
    file.close()

    # Decode the file contents
    encoding = chardet.detect(contents)['encoding']
    if encoding is None:
        print('Corrupt or empty file ({})'.format(file.name),
              file=sys.stderr)
        sys.exit(1)
    contents = contents.decode(encoding)

    # Count empty lines at the beginning
    r = re.compile(r'\r?\n')
    line_number = 1
    for line in r.split(contents):
        if len(line) == 0 or line.isspace():
            line_number += 1
        else:
            break

    # Split subtitles on empty lines
    subs = re.split(r'(?:\r?\n){2}', contents.strip())

    # Create Subtitle objects
    subs_objs = []
    for sub in subs:
        lines = list(r.split(sub))
        subs_objs.append(Subtitle(lines, file.name, line_number))
        line_number += len(lines) + 3

    # Clean if --clean is passed
    if args.clean:
        subs_objs = clean(subs_objs, args.config_file)

    # Shift if --shift is passed
    if args.shift:
        subs_objs = shift(subs_objs, args.shift)

    # Strip HTML if --no-html is passed
    if args.no_html:
        strip_html(subs_objs)

    # Fix numbering
    i = 1
    for sub in subs_objs:
        sub.number = i
        i += 1

    # Join Subtitle objects back to a string
    contents = (os.linesep + os.linesep).join(map(repr, subs_objs))

    # Write output
    output = open(file.name, 'w', encoding='utf-8')
    output.write(contents)
    output.write(os.linesep)


def main():
    parser = argparse.ArgumentParser(
        description='Fix, edit and clean SubRip (.srt) files.',
        add_help=True
    )

    parser.add_argument(
        '-c', '--clean',
        help='removes subtitles matching regular expressions ' +
             'listed in ~/.config/fsubrc (this is the default ' +
             'behavior if no other flag is passed)',
        action='store_true'
    )

    parser.add_argument(
        '-s', '--shift',
        help='shifts all subtitles by MS milliseconds, which ' +
             'may be positive or negative',
        metavar='MS',
        action='store',
        type=int
    )

    parser.add_argument(
        '-n', '--no-html',
        help='strips HTML tags from subtitles content',
        action='store_true'
    )

    parser.add_argument(
        '-f', '--config-file',
        help='overwrites the default config file (~/.config/fsubrc)',
        metavar='FILE',
        action='store',
        type=argparse.FileType('r')
    )

    parser.add_argument(
        'files',
        help='list of input files (they all must be SubRip files)',
        metavar='file',
        type=argparse.FileType('rb+'),
        nargs='+'
    )

    args = parser.parse_args()

    # Make sure --clean is the default
    if not args.shift and not args.no_html:
        args.clean = True

    # Validate options
    if not args.clean and args.config_file:
        print('-f requires -c', file=sys.stderr)
        exit(1)

    # Check if all files are .srt
    for file in args.files:
        if file.name[-4:] != '.srt':
            print('File {} is not a SubRip file'.format(file.name),
                  file=sys.stderr)
            sys.exit(1)

    for file in args.files:
        process_file(args, file)


if __name__ == '__main__':
    main()
