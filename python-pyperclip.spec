# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_with	tests	# do perform "make test" (broken)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A cross-platform clipboard module for Python
Name:		python-pyperclip
Version:	1.5.27
Release:	7
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/7b/a5/48eaa1f2d77f900679e9759d2c9ab44895e66e9612f7f6b5333273b68f29/pyperclip-%{version}.zip
# Source0-md5:	18b86c2e6d10ed827cdd42aed80b4cbe
URL:		https://pypi.python.org/pypi/pyperclip
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cross-platform clipboard module for Python. (only handles plain text
for now)

%package -n python3-pyperclip
Summary:	A cross-platform clipboard module for Python
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-pyperclip
A cross-platform clipboard module for Python. (only handles plain text
for now)

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
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
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
%{py_sitescriptdir}/pyperclip
%{py_sitescriptdir}/pyperclip-%{version}-py*.egg-info
%if %{with doc}
%doc docs/_build/html/*
%endif
%endif

%if %{with python3}
%files -n python3-pyperclip
%defattr(644,root,root,755)
%{py3_sitescriptdir}/pyperclip
%{py3_sitescriptdir}/pyperclip-%{version}-py*.egg-info
%if %{with doc}
%doc docs/_build/html/*
%endif
%endif
