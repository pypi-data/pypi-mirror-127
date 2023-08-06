#
# This file is part of pysmi software.
#
# Copyright (c) 2015-2020, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/pysmi/license.html
#
import sys

try:
    # noinspection PyUnresolvedReferences
    from urllib import url2pathname

    import urlparse

except ImportError:
    # noinspection PyUnresolvedReferences
    from urllib import parse as urlparse
    from urllib.request import url2pathname

from pysmi import error
from pysmi.reader.ftpclient import FtpReader
from pysmi.reader.httpclient import HttpReader
from pysmi.reader.localfile import FileReader
from pysmi.reader.zipreader import ZipReader


def getReadersFromUrls(*sourceUrls, **options):
    readers = []
    for sourceUrl in sourceUrls:
        mibSource = urlparse.urlparse(sourceUrl)

        if mibSource.scheme in ("", "file", "zip"):
            scheme = mibSource.scheme
            filePath = url2pathname(mibSource.path)
            if scheme != "file" and (
                filePath.endswith(".zip") or filePath.endswith(".ZIP")
            ):
                scheme = "zip"

            else:
                scheme = "file"

            if scheme == "file":
                readers.append(FileReader(filePath).setOptions(**options))
            else:
                readers.append(ZipReader(filePath).setOptions(**options))

        elif mibSource.scheme in ("http", "https"):
            readers.append(
                HttpReader(
                    mibSource.hostname or mibSource.netloc,
                    mibSource.port or 80,
                    mibSource.path,
                    ssl=mibSource.scheme == "https",
                ).setOptions(**options)
            )

        elif mibSource.scheme in ("ftp", "sftp"):
            readers.append(
                FtpReader(
                    mibSource.hostname or mibSource.netloc,
                    mibSource.path,
                    ssl=mibSource.scheme == "sftp",
                    port=mibSource.port or 21,
                    user=mibSource.username or "anonymous",
                    password=mibSource.password or "anonymous@",
                ).setOptions(**options)
            )

        else:
            raise error.PySmiError("Unsupported URL scheme %s" % sourceUrl)

    return readers
