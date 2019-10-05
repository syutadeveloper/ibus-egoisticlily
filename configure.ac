#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([ibus-egoisticliliy], [0.0.1], [syuta.hashimoto@gmail.com])
AM_INIT_AUTOMAKE

PACKAGE_DIR=`pwd`
AC_SUBST(PACKAGE_DIR)

AC_ARG_WITH(egoisticlily-model,
	[AC_HELP_STRING([--with-egoisticlily-model=PATH],
			[file path of egoisticlily model])],
	[EGOISTICLILY_MODEL_DIR="$withval"],
	[EGOISTICLILY_MODEL_DIR="`pwd`/model"])
AC_SUBST(EGOISTICLILY_MODEL_DIR)	


AC_CONFIG_FILES([
Makefile
src/Makefile
src/main.py
src/engine.py
src/factory.py
config/Makefile
config/egoisticlily/Makefile
config/gschema/Makefile
config/ibusengines/Makefile
config/ibusengines/egoisticlily.xml
])

AC_CONFIG_FILES(
[src/ibus-engine-egoisticlily],
[chmod +x src/ibus-engine-egoisticlily])

AC_OUTPUT
