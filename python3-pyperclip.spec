#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	A cross-platform clipboard module for Python
Summary(pl.UTF-8):	Wieloplatformowy moduł schowka dla Pythona
Name:		python3-pyperclip
Version:	1.9.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pyperclip/pyperclip-%{version}.tar.gz
# Source0-md5:	43f9e69bf948139055683d28080787f4
Patch0:		pyperclip-tests.patch
URL:		https://pypi.org/project/pyperclip/
# 3.6 is minimum for f-strings
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cross-platform clipboard module for Python. (only handles plain text
for now)

%description -l pl.UTF-8
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
%patch -P0 -p1

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} tests/test_pyperclip.py
%endif

%if %{with doc}
%{__make} -C docs -j1 html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGES.txt LICENSE.txt README.md
%{py3_sitescriptdir}/pyperclip
%{py3_sitescriptdir}/pyperclip-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
