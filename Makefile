PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
PAGESDIR=$(INPUTDIR)/pages
POSTSDIR=$(INPUTDIR)/blog

GITHUB_PAGES_BRANCH=gh-pages

DATE := $(shell date +'%Y-%m-%d %H:%M:%S')
SLUG := $(shell echo '${NAME}' | sed -e 's/[^[:alnum:]]/-/g' | tr -s '-' | tr A-Z a-z)
EXT ?= md
EDITOR ?= vim

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=7000]              serve site at http://localhost:7000'
	@echo '   make stopserver                     stop local server                  '
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '   make newpost NAME="POST NAME"       create new post with input name    '
	@echo '   make newpage NAME="PAGE NAME"       create new page with input name    '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server 7000
endif

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

github: publish
	ghp-import -m "Generate EsseProduto site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)

newpost:
ifdef NAME
	echo "Title: $(NAME)" >  $(POSTSDIR)/$(SLUG).$(EXT)
	echo "Subtitle: " >> $(POSTSDIR)/$(SLUG).$(EXT)
	echo "Slug: $(SLUG)" >> $(POSTSDIR)/$(SLUG).$(EXT)
	echo "Date: $(DATE)" >> $(POSTSDIR)/$(SLUG).$(EXT)
	echo "meta_description: " >> $(POSTSDIR)/$(SLUG).$(EXT)
	echo ""              >> $(POSTSDIR)/$(SLUG).$(EXT)
	echo ""              >> $(POSTSDIR)/$(SLUG).$(EXT)
	${EDITOR} ${POSTSDIR}/${SLUG}.${EXT}
else
	@echo 'Variable NAME is not defined.'
	@echo 'Do make newpost NAME='"'"'Post Name'"'"
endif

newpage:
ifdef NAME
	echo "Title: $(NAME)" >  $(PAGESDIR)/$(SLUG).$(EXT)
	echo "Description: " >  $(PAGESDIR)/$(SLUG).$(EXT)
	echo "Slug: $(SLUG)" >> $(PAGESDIR)/$(SLUG).$(EXT)
	echo ""              >> $(PAGESDIR)/$(SLUG).$(EXT)
	echo ""              >> $(PAGESDIR)/$(SLUG).$(EXT)
	${EDITOR} ${PAGESDIR}/${SLUG}.$(EXT)
else
	@echo 'Variable NAME is not defined.'
	@echo 'Do make newpage NAME='"'"'Page Name'"'"
endif

.PHONY: html help clean regenerate serve publish github newpost newpage
