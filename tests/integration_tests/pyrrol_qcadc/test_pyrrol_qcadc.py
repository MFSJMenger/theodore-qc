from .. import file_diff, call_tden, get_folder_name
from .. import remove_file
import os

PWD = get_folder_name(__file__)
LIBWFA = os.path.join(PWD, 'libwfa')



def test_pyrrol_libwfa():
    call_tden("tden.in.libwfa", folder=LIBWFA)
    assert file_diff("tden_summ.txt.libwfa", "tden_summ.txt.libwfa.ref" ,folder=LIBWFA)
    remove_file("tden_summ.txt.libwfa", folder=LIBWFA)
