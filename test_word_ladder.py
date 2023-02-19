import pytest
from word_ladder import *

filename = "english.txt"


@pytest.mark.parametrize("start,end,expected", [
    # ("at", "it", [["at", "it"]]),
    # ("cat", "cog", [["cat", "cot", "cog"]]),
    # ("work", "play", [["work", "fork", "form", "foam", "flam", "flay", "play"]]),
    ("awake", "sleep", [["awake", "aware", "sware", "share", "sharn", "shawn", "shewn", "sheen", "sheep", "sleep"],
                        ["awake", "aware", "sware", "share", "shire", "shirr", "shier", "sheer", "sheep", "sleep"]]),
])
def test_generate(start, end, expected):
    lexicon = read_lexicon(filename)
    assert generate(start, end, lexicon) == expected
