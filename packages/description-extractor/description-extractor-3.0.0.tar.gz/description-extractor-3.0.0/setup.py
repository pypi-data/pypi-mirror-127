from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import subprocess


RELEASE = True
VERSION_MAJOR = 3
VERSION_MINOR = 0
VERSION_PATCH = 0
VERSION = '.'.join(map(str, [VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH]))
if not RELEASE:
    VERSION += '-dev'


class git_clone_external(build_ext):
    def run(self):
        subprocess.check_call(['rm', '-rf', 'extractor-core'])
        subprocess.check_call(['git', 'clone', 'https://github.com/mutalyzer/extractor-core.git'])
        build_ext.run(self)

extractor = Extension('extractor',
                      sources = ['extractor-wrapper.cc',
                                 'extractor-core/src/extractor.cc'],
                      extra_compile_args = ['-Wextra',
                                            '-Wpedantic',
                                            '-std=c++17'])

setup(name = 'description-extractor',
      version = VERSION,
      cmdclass = {'build_ext': git_clone_external},
      description = 'HGVS variant description extractor',
      ext_modules = [extractor]
)
