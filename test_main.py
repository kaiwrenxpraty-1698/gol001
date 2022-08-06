from main import *
from unittest.mock import patch

def test_main(capsys):
    with patch("sys.argv", ["main", "--option", 2]):
        main()
        captured = capsys.readuterr()
        assert captured.out == 1