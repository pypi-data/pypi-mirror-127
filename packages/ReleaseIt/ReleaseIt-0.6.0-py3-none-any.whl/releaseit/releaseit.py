"""ReleaseIt manages release notes for Python projects.

ReleaseIt keeps release notes for Python projects in a dict structure.
It aims to standardise, facilitate and automate the management of
release notes when publishing a project to GitHub, PyPI and
ReadTheDocs.  It is developed as part of the PackageIt project, but can
be used independently as well.

See also https://pypi.org/project/PackageIt/
"""

import logging
from pathlib import Path
import tempfile
import toml
from beetools.beearchiver import Archiver

_PROJ_DESC = __doc__.split("\n")[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = "0.0.3"

_TOML_CONTENTS_DEF = """
[0.0.0]
Version = '0.0.0'
Title = 'Creation of the project'
Description = ['List all the changes to the project here.',
               'Changes listed here will be in the release notes under the above heading.']
FileChanges = [['filename01.py','Insert change description here.'],
               ['filename02.txt','Insert change description here.']]
"""


class ReleaseIt:
    """ReleaseIt manages release notes for Python projects."""

    def __init__(self, p_src, p_parent_log_name="", p_verbose=True):
        """Initialize the class

        Parameters
        ----------
        p_src : Path
            Directory path where the release notes are or will be created in.
        p_parent_log_name : str, default = ''
            Name of the parent.  In combination witt he class name it will
            form the logger name.
        p_verbose: bool, default = True
            Write messages to the console.

        Examples
        --------
        >>> import tempfile
        >>> from pathlib import Path
        >>> t_releaseit = ReleaseIt(Path(tempfile.mkdtemp(prefix=_PROJ_NAME)))
        >>> t_releaseit.seq
        [['0', '0', '0']]
        """
        self.success = True
        if p_parent_log_name:
            self._log_name = "{}.{}".format(p_parent_log_name, _PROJ_NAME)
            self.logger = logging.getLogger(self._log_name)
        self.verbose = p_verbose

        self.src_pth = Path(p_src, "release.toml")
        if not self.src_pth.exists():
            self._create_def_config()
        self.release_notes = {}
        release_notes = toml.load(self.src_pth)
        self.seq = []
        self.curr_pos = -1
        self.element_cntr = 0
        if self._validate_release_notes(release_notes):
            self.release_notes = release_notes
            self._get_config_list()
            self._sort()
            self.curr_pos = 0
            self.element_cntr = len(self.seq)
        pass

    def __iter__(self):
        self.curr_pos = 0
        return self

    def __next__(self):
        if self.curr_pos < self.element_cntr:
            element = self.release_notes[self.seq[self.curr_pos][0]][
                self.seq[self.curr_pos][1]
            ][self.seq[self.curr_pos][2]]
            self.curr_pos += 1
            return element
        else:
            raise StopIteration

    def add_release_note(self, p_release_note):
        if self._check_release_note(p_release_note):
            release_parts = p_release_note["Version"].split(".")
            if release_parts[0] in self.release_notes.keys():
                if release_parts[1] in self.release_notes[release_parts[0]].keys():
                    self.release_notes[release_parts[0]][release_parts[1]][
                        release_parts[2]
                    ] = p_release_note
                else:
                    self.release_notes[release_parts[0]][release_parts[1]] = {
                        release_parts[2]: p_release_note
                    }
            else:
                self.release_notes[release_parts[0]] = {
                    release_parts[1]: {release_parts[2]: p_release_note}
                }
            self.seq.append(release_parts)
            self._sort()
            self.element_cntr = len(self.seq)
        pass

    def _create_def_config(self):
        """Create the "release.toml" configuration file.

        Create the "release.toml" configuration file with the default
        contents as if it is the first release (0.0.1).  If the file
        already exists, it will be overwritten.
        This method is called during instantiation of the class.

        Parameters
        ----------

        Returns
        -------
        release_pth : Path
            Path to the "release.toml" file.
        """
        self.src_pth.write_text(_TOML_CONTENTS_DEF)
        return self.src_pth

    def _get_config_list(self):
        for major in self.release_notes:
            for minor in self.release_notes[major]:
                for patch in self.release_notes[major][minor]:
                    self.seq.append([major, minor, patch])
        return self.seq

    def get_release_note(self, p_title):
        for rel in self.seq:
            if self.release_notes[rel[0]][rel[1]][rel[2]]["Title"] == p_title:
                return self.release_notes[rel[0]][rel[1]][rel[2]]
        return None

    def get_release_titles(self):
        titles = []
        for release in self.seq:
            titles.append(
                self.release_notes[release[0]][release[1]][release[2]]["Title"]
            )
        return titles

    def has_title(self, p_title):
        for seq in self.seq:
            if self.release_notes[seq[0]][seq[1]][seq[2]]["Title"] == p_title:
                return True
        return False

    def _sort(self):
        self.seq = sorted(self.seq, key=lambda release_notes: release_notes[2])
        self.seq = sorted(self.seq, key=lambda release_notes: release_notes[1])
        self.seq = sorted(self.seq, key=lambda release_notes: release_notes[0])
        return self.seq

    def _check_release_note(self, p_release_note):
        if "Description" not in p_release_note.keys():
            return False
        if not isinstance(p_release_note["Description"], list):
            return False
        if len(p_release_note["Description"]) <= 0:
            return False
        for desc in p_release_note["Description"]:
            if not isinstance(desc, str):
                return False

        if "FileChanges" not in p_release_note.keys():
            return False
        if not isinstance(p_release_note["FileChanges"], list):
            return False
        for i, item in enumerate(p_release_note["FileChanges"]):
            if not isinstance(item[0], str):
                return False
            if not isinstance(item[1], str):
                return False

        if "Title" not in p_release_note.keys():
            return False
        if self.has_title(p_release_note["Title"]):
            return False

        if "Version" not in p_release_note.keys():
            return False
        release_parts = p_release_note["Version"].split(".")
        if not release_parts[0].isnumeric():
            return False
        if not release_parts[1].isnumeric():
            return False
        if not release_parts[2].isnumeric():
            return False
        if release_parts in self.seq:
            return False

        return True

    def _validate_release_notes(self, p_release_notes):
        for major in p_release_notes:
            if not isinstance(major, str):
                return False
            if not major.isnumeric():
                return False
            for minor in p_release_notes[major]:
                if not isinstance(minor, str):
                    return False
                if not minor.isnumeric():
                    return False
                for patch in p_release_notes[major][minor]:
                    if not isinstance(patch, str):
                        return False
                    if not patch.isnumeric():
                        return False
                    release = p_release_notes[major][minor][patch]
                    if not "{}.{}.{}".format(major, minor, patch) == release["Version"]:
                        return False
                    if not self._check_release_note(release):
                        return False
        return True


def do_examples(p_cls=True):
    """A collection of implementation examples for ReleaseIt.

    A collection of implementation examples for ReleaseIt. The examples
    illustrate in a practical manner how to use the methods.  Each example
    show a different concept or implementation.

    Parameters
    ----------
    p_cls : bool, default = True
        Clear the screen or not at startup of Archiver

    Returns
    -------
    success : boolean
        Execution status of the method

    """
    success = do_example1(p_cls)
    return success


def do_example1(p_cls=True):
    """A working example of the implementation of ReleaseIt.

    Example1 illustrate the following concepts:
    1. Creates to object
    2. Create a default 'release.toml' file in teh designated (temp) directory

    Parameters
    ----------
    p_cls : bool, default = True
        Clear the screen or not at startup of Archiver

    Returns
    -------
    success : boolean
        Execution status of the method

    """
    success = True
    archiver = Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)
    archiver.print_header(p_cls=p_cls)
    releaseit = ReleaseIt(Path(tempfile.mkdtemp(prefix=_PROJ_NAME)))
    print(releaseit.src_pth)
    print(releaseit.release_notes)
    archiver.print_footer()
    return success


if __name__ == "__main__":
    do_examples()
