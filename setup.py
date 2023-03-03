
from numpy.distutils.core import setup, Extension
from numpy.distutils.misc_util import Configuration


# define PROSAIL Fortran library
prosail_fortran_lib = Extension(
    name='_prosail_model',
    sources = [
        './pyprosail/MODULE_PRO4SAIL.f90',
        './pyprosail/dataSpec_P5B.f90',
        './pyprosail/LIDF.f90',
        './pyprosail/dladgen.f',
        './pyprosail/PRO4SAIL.f90',
        './pyprosail/prospect_5B.f90',
        './pyprosail/tav_abs.f90',
        './pyprosail/volscatt.f90',
        './pyprosail/PyPROSAIL.f90'
    ]
)

# define Python package setup
setup(
    name='pyprosail',
    packages=['pyprosail'],
    version='1.0.1',
    ext_modules=[prosail_fortran_lib]
)



# def configuration(parent_package='',top_path=None):
#
#     config = Configuration(
#         '',
#         parent_package,top_path,
#         name = "pyprosail",
#         version = "1.0.1",
#         description = """PyProSAIL is a Python interface to the ProSAIL combined leaf and canopy optical model. For more information see http://pyprosail.readthedocs.org.""",
#         packages = ['pyprosail'],
#         author = "Robin Wilson",
#         author_email = "robin@rtwilson.com",
#         url = "http://packages.python.org/PyPROSAIL",
#         classifiers           =[
#             "Development Status :: 5 - Production/Stable",
#             "Intended Audience :: Science/Research",
#             "Topic :: Scientific/Engineering :: Atmospheric Science",
#             "Topic :: Scientific/Engineering :: Physics",
#             "Topic :: Software Development :: Libraries :: Python Modules",
#             "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
#             "Programming Language :: Python"
#         ])
#
#     config.add_extension(
#         '_prosail_model',
#         sources = [
#             './pyprosail/MODULE_PRO4SAIL.f90',
#             './pyprosail/dataSpec_P5B.f90',
#             './pyprosail/LIDF.f90',
#             './pyprosail/dladgen.f',
#             './pyprosail/PRO4SAIL.f90',
#             './pyprosail/prospect_5B.f90',
#             './pyprosail/tav_abs.f90',
#             './pyprosail/volscatt.f90',
#             './pyprosail/PyPROSAIL.f90'
#         ]
#     )
#     return config
#
# if __name__ == "__main__":
#
#     from numpy.distutils.core import setup
#     setup(**configuration(top_path='').todict())
