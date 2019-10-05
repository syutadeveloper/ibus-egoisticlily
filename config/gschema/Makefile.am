schemas_DATA = org.freedesktop.ibus.engine.egoisticlily.gschema.xml
schemasdir = $(datadir)/glib-2.0/schemas

$(schemas_DATA):

install-data-hook:
	if test -z "$(DESTDIR)"; then \
		glib-compile-schemas $(schemasdir); \
	fi

uninstall-hook:
	SCHEMAS_FILES=`ls $(schemasdir)/*.gschema.xml` || true;         \
	if test -z "$$SCHEMAS_FILES" &&                                 \
		test -f $(schemasdir)/gschemas.compiled; then                \
		rm $(schemasdir)/gschemas.compiled;                         \
	fi
