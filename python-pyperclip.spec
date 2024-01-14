#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A cross-platform clipboard module for Python
Summary(pl.UTF-8):	Wieloplatformowy moduł schowka dla Pythona
Name:		python-pyperclip
Version:	1.8.2
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pyperclip/pyperclip-%{version}.tar.gz
# Source0-md5:	853603b2e8fa1b13622fdbe72d1fb201
URL:		https://pypi.org/project/pyperclip/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.1
BuildRequires:	python3-modules >= 1:3.1
BuildRequires:	python3-setuptools
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cross-platform clipboard module for Python. (only handles plain text
for now)

%description -l pl.UTF-8
Wieloplatformowy moduł schowka dla Pythona (obecnie obsługuje tylko
czysty tekst).

%package -n python3-pyperclip
Summary:	A cross-platform clipboard module for Python
Summary(pl.UTF-8):	Wieloplatformowy moduł schowka dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.1

%description -n python3-pyperclip
A cross-platform clipboard module for Python. (only handles plain text
for now)

%description -n python3-pyperclip -l pl.UTF-8
Wieloplatformowy moduł schowka dla Pythona (obecnie obsługuje tylko
czysty tekst).

%package apidocs
Summary:	API documentation for Python pyperclip module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pyperclip
Group:		Documentation

%description apidocs
API documentation for Pythona pyperclip module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pyperclip.

%prep
%setup -q -n pyperclip-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python} tests/test_pyperclip.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} tests/test_pyperclip.py
%endif
%endif

%if %{with doc}
%{__make} -C docs -j1 html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGES.txt LICENSE.txt README.md
%{py_sitescriptdir}/pyperclip
%{py_sitescriptdir}/pyperclip-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pyperclip
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGES.txt LICENSE.txt README.md
%{py3_sitescriptdir}/pyperclip
%{py3_sitescriptdir}/pyperclip-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
