# Copyright (C) 2012 Alex Nisnevich
# Licensed under the MIT license

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import re
import os

from MarkdownPP.Module import Module
from MarkdownPP.Transform import Transform

youtube_url_re = re.compile(r'^!VIDEO\s+"https?://www\.youtube\.com'
                            r'/embed/([a-zA-Z0-9_\-]*)"')
glowfoto_server_re = re.compile(r"<uploadform>(.*)</uploadform>")
glowfoto_image_re = re.compile(r"<thumburl>(.*)</thumburl>")
codere = re.compile(r"^(    |\t)")
fencedcodere = re.compile(r"^```\w*$")

play_button_url = 'http://i.imgur.com/1IHylPh.png'


class YoutubeEmbed(Module):
    """
    Converts Youtube embed objects into links with screenshots,
    taken from Youtube.
    """

    def transform(self, data):
        transforms = []
        in_fenced_code_block = False
        linenum = 0

        for line in data:
            # Handling fenced code blocks (for Github-flavored markdown)
            if fencedcodere.search(line):
                if in_fenced_code_block:
                    in_fenced_code_block = False
                else:
                    in_fenced_code_block = True

            # Are we in a code block?
            if not in_fenced_code_block and not codere.search(line):
                match = youtube_url_re.search(line)
                if match:
                    # find URL of youtube video and screenshot
                    url = match.group(1)
                    image_url = 'http://img.youtube.com/vi/%s/0.jpg' % url
                    video_url = 'http://www.youtube.com/watch?v=%s' % url
                    processed_image_dir = os.path.join('images', 'youtube')
                    processed_image_path = os.path.join(processed_image_dir,
                                                        '%s.png' % url)

                    # do we already have a screenshot?
                    if not os.path.isfile(processed_image_path):
                        # create directories if needed
                        if not os.path.exists(processed_image_dir):
                            os.makedirs(processed_image_dir)

                        self._add_play_button(image_url, processed_image_path)

                    image_link = ('[![Link to Youtube video](%s)](%s)\n' %
                                  (processed_image_path, video_url))
                    transforms.append(Transform(linenum, "swap", image_link))

            linenum += 1

        return transforms

    def _add_play_button(self, image_url, image_path):
        """Try to add a play button to the screenshot."""
        try:
            from PIL import Image
            from tempfile import NamedTemporaryFile
            import urllib
            try:
                urlretrieve = urllib.request.urlretrieve
            except ImportError:
                urlretrieve = urllib.urlretrieve

            # create temporary files for image operations
            with NamedTemporaryFile(suffix=".jpg") as screenshot_img:
                with NamedTemporaryFile(suffix=".jpg") as button_img:
                    # grab screenshot and button image
                    urlretrieve(image_url, screenshot_img.name)
                    urlretrieve(play_button_url, button_img.name)

                    # layer the images using PIL and save
                    with Image.open(screenshot_img.name) as background:
                        with Image.open(button_img.name) as foreground:
                            background.paste(foreground, (90, 65), foreground)
                            background.save(image_path)

        except ImportError as e:
            print(e)

        except Exception as e:
            print('Unable to add play button to YouTube '
                  'screenshot (%s). Using the screenshot '
                  'on its own instead.' % e)
