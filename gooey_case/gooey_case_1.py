# -*- coding: utf-8 -*-
from gooey import Gooey, GooeyParser


@Gooey(target="ffmpeg", program_name='Frame Extraction v1.0', suppress_gooey_flag=True, language='chinese')
def main():
    parser = GooeyParser(description="Extracting frames from a movie using FFMPEG")
    ffmpeg = parser.add_argument_group('Frame Extraction Util')
    ffmpeg.add_argument('-i',
                        metavar='Input Movie',
                        help='The movie for which you want to extract frames',
                        widget='FileChooser')
    ffmpeg.add_argument('output',
                        metavar='Output Image',
                        help='Where to save the extracted frame',
                        widget='FileSaver',
                        )
    ffmpeg.add_argument('-ss',
                        metavar='Timestamp',
                        help='Timestamp of snapshot (in seconds)')
    ffmpeg.add_argument('-frames:v',
                        metavar='Timestamp',
                        default=1,
                        gooey_options={'visible': False})

    parser.parse_args()


if __name__ == '__main__':
    main()
